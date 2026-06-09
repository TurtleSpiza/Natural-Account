#!/usr/bin/env python3
"""
style_lint.py — Spero writing-style linter.

Flags violations of the Spero writing style guide. Hard-fails (errors) on
em-dash separators, American spelling, "However," sentence-openers, and
banned hedging phrases. Warns on magnitude adjectives without dollar
amounts, low "arguably" density, sentence-length drift, bullet-heaviness,
and missing decisive close.

Two registers are supported:

* prose (default) — long-form documents, essays, reports, narrative emails.
  Every check applies.
* email — structured emails using bold lead-in bullets, sub-bullets, and
  unnumbered headers. The bullet_heavy and short_sentence_run checks are
  skipped, since the email format relies on bullets and short bullet text.
  All other voice rules apply.

CLI usage:
    python style_lint.py <file>
    python style_lint.py <file> --email          # email register
    python style_lint.py - < stdin
    python style_lint.py <file> --json
    python style_lint.py <file> --info           # include info-level findings
    python style_lint.py <file> --no-soft        # only error-level

Library usage:
    from style_lint import lint_text
    findings = lint_text(text)                       # prose register (default)
    findings = lint_text(text, register="email")     # email register

Each finding is a dict:
    {
        "severity": "error" | "warning" | "info",
        "rule":     "no_em_dash_separator" | ...,
        "line":     int,
        "snippet":  str,
        "suggestion": str,
    }
"""

import sys
import re
import json
import argparse
from pathlib import Path


# ─── Rule definitions ────────────────────────────────────────────────────────

# Hard errors — banned patterns

EM_DASH_PATTERN = re.compile(r"[—–]")
# American spelling drift — common ize/yze and our→or violations
US_SPELLING_PATTERNS = [
    (re.compile(r"\b(\w+)ize\b", re.IGNORECASE), "{}ise (Australian)"),
    (re.compile(r"\b(\w+)yze\b", re.IGNORECASE), "{}yse (Australian)"),
    (re.compile(r"\b(behavior|behaviors)\b", re.IGNORECASE), "behaviour/behaviours"),
    (re.compile(r"\b(favor|favors|favorable|favorably)\b", re.IGNORECASE), "favour/favourable"),
    (re.compile(r"\b(labor|labors)\b", re.IGNORECASE), "labour"),
    (re.compile(r"\b(color|colors|colored|coloring)\b", re.IGNORECASE), "colour/coloured"),
    (re.compile(r"\b(neighbor|neighbors|neighborhood)\b", re.IGNORECASE), "neighbour/neighbourhood"),
    (re.compile(r"\b(center|centers|centered)\b", re.IGNORECASE), "centre/centred"),
    (re.compile(r"\b(theater|theaters)\b", re.IGNORECASE), "theatre"),
    (re.compile(r"\b(meter|meters)\b", re.IGNORECASE), "metre/metres"),
    (re.compile(r"\b(traveling|traveled|traveler)\b", re.IGNORECASE), "travelling/travelled/traveller"),
    (re.compile(r"\b(modeling|modeled)\b", re.IGNORECASE), "modelling/modelled"),
]
# Whitelist — words that legitimately end -ize/-yze even in Australian English
US_SPELLING_WHITELIST = {
    "size", "prize", "seize", "capsize",
    "analyze",  # NOTE: this is American; corpus uses "analyse" — keep listed
    # Some words are unambiguous; do not flag:
    "isenze", "matrize",  # Sanity-only; these aren't real English words
}

# "However," at start of paragraph or sentence is a Claude tic
HOWEVER_AS_OPENER = re.compile(
    r"(?:^|[\.\!\?]\s+|\n\s*)However,",
    re.MULTILINE,
)

# Banned hedging phrases — corpus does not contain these
BANNED_HEDGES = [
    re.compile(r"\b[Pp]erhaps\b"),
    re.compile(r"\bit could be argued\b", re.IGNORECASE),
    re.compile(r"\bsome might say\b", re.IGNORECASE),
    re.compile(r"\bsome could argue\b", re.IGNORECASE),
    re.compile(r"\bin certain circumstances\b", re.IGNORECASE),
    re.compile(r"\bone might think\b", re.IGNORECASE),
    re.compile(r"\bit might be the case\b", re.IGNORECASE),
    re.compile(r"\bone could potentially\b", re.IGNORECASE),
]

# Soft warnings — magnitude adjectives without dollar amounts
MAGNITUDE_ADJECTIVES = re.compile(
    r"\b(significant|substantial|considerable|material|major|sizeable|sizable|notable|meaningful)\b",
    re.IGNORECASE,
)
DOLLAR_FIGURE = re.compile(r"\$[\d,]+(?:\.\d+)?[kKmMbB]?|\b\d+(?:,\d{3})+\b|\b\d+\s*(?:per\s*cent|%)")

# Listy paragraphs — count bullet vs prose lines
BULLET_LINE = re.compile(r"^\s*[\-\*\+•]\s+|\s*\d+\.\s+")

# Decisive close — heuristic: last paragraph contains intensifier
DECISIVE_INTENSIFIERS = re.compile(
    r"\b(decisively|self-evidently|without doubt|without question|indisputably|"
    r"ought to|the only|categorically|emphatically|unequivocally)\b",
    re.IGNORECASE,
)


# ─── Lint functions ──────────────────────────────────────────────────────────

def _line_of(text: str, idx: int) -> int:
    """1-indexed line number of position idx in text."""
    return text.count("\n", 0, idx) + 1


def _snippet(text: str, idx: int, span: int = 60) -> str:
    """Snippet around idx, truncated to span chars."""
    start = max(0, idx - span // 2)
    end = min(len(text), idx + span // 2)
    s = text[start:end].replace("\n", " ")
    return s.strip()


def check_em_dashes(text: str) -> list:
    findings = []
    for m in EM_DASH_PATTERN.finditer(text):
        findings.append({
            "severity": "error",
            "rule": "no_em_dash_separator",
            "line": _line_of(text, m.start()),
            "snippet": _snippet(text, m.start()),
            "suggestion": "Replace with comma, parentheses, or a full stop and new sentence.",
        })
    return findings


def check_american_spelling(text: str) -> list:
    findings = []
    # Generic ize/yze with whitelist
    for m in re.finditer(r"\b(\w+ize|\w+yze)\b", text):
        word = m.group(1).lower()
        # Allowed words
        if word in {"size", "prize", "seize", "capsize", "wise", "rise", "exercise", "advertise",
                    "compromise", "demise", "despise", "disguise", "enterprise", "franchise",
                    "improvise", "premise", "supervise", "surprise", "televise", "merchandise",
                    "revise", "advise", "arise", "comprise", "devise", "praise", "raise",
                    "appraise", "chastise", "exorcise"}:
            continue
        findings.append({
            "severity": "error",
            "rule": "american_spelling_ize_yze",
            "line": _line_of(text, m.start()),
            "snippet": _snippet(text, m.start()),
            "suggestion": f"{word} → {word[:-3] + 'ise' if word.endswith('ize') else word[:-3] + 'yse'} (Australian)",
        })
    # Specific common drifts
    for pattern, suggestion in US_SPELLING_PATTERNS[2:]:  # Skip the first two ize/yze patterns; handled above
        for m in pattern.finditer(text):
            findings.append({
                "severity": "error",
                "rule": "american_spelling",
                "line": _line_of(text, m.start()),
                "snippet": _snippet(text, m.start()),
                "suggestion": suggestion,
            })
    return findings


def check_however_opener(text: str) -> list:
    findings = []
    for m in HOWEVER_AS_OPENER.finditer(text):
        findings.append({
            "severity": "error",
            "rule": "however_as_sentence_opener",
            "line": _line_of(text, m.end() - len("However,")),
            "snippet": _snippet(text, m.end() - len("However,")),
            "suggestion": "Use 'However' mid-sentence preceded by a comma, or rewrite to bury the contrast.",
        })
    return findings


def check_banned_hedges(text: str) -> list:
    findings = []
    for pattern in BANNED_HEDGES:
        for m in pattern.finditer(text):
            findings.append({
                "severity": "error",
                "rule": "banned_hedge",
                "line": _line_of(text, m.start()),
                "snippet": _snippet(text, m.start()),
                "suggestion": "Replace with 'arguably' or 'upon further research', then commit to a verdict.",
            })
    return findings


def check_magnitude_without_dollar(text: str) -> list:
    """Flag 'significant' / 'substantial' etc. without a $ figure within ~100 chars."""
    findings = []
    for m in MAGNITUDE_ADJECTIVES.finditer(text):
        # Look for a dollar figure or % within 200 chars before or after
        window_start = max(0, m.start() - 200)
        window_end = min(len(text), m.end() + 200)
        window = text[window_start:window_end]
        if not DOLLAR_FIGURE.search(window):
            findings.append({
                "severity": "warning",
                "rule": "magnitude_without_quantity",
                "line": _line_of(text, m.start()),
                "snippet": _snippet(text, m.start()),
                "suggestion": "Attach a dollar amount or percentage to anchor the magnitude claim.",
            })
    return findings


def check_arguably_density(text: str) -> list:
    word_count = len(text.split())
    if word_count < 500:
        return []
    arguably_count = len(re.findall(r"\barguably\b", text, re.IGNORECASE))
    if arguably_count == 0:
        return [{
            "severity": "warning",
            "rule": "missing_arguably_signature",
            "line": 1,
            "snippet": f"Document is {word_count} words, no instances of 'arguably'.",
            "suggestion": "The corpus uses 'arguably' as the dominant hedge-then-commit marker. Consider adding one.",
        }]
    return []


def check_bullet_heavy(text: str) -> list:
    lines = [ln for ln in text.split("\n") if ln.strip()]
    if not lines:
        return []
    bullet_lines = sum(1 for ln in lines if BULLET_LINE.match(ln))
    if bullet_lines / len(lines) > 0.3 and len(lines) > 6:
        return [{
            "severity": "warning",
            "rule": "bullet_heavy",
            "line": 1,
            "snippet": f"{bullet_lines}/{len(lines)} lines are bullets ({100*bullet_lines/len(lines):.0f}%).",
            "suggestion": "Voice prefers prose paragraphs that chain reasoning. Convert bullets to prose where the content can flow. (Pass --email or register='email' if this is a structured email.)",
        }]
    return []


def check_short_sentence_run(text: str) -> list:
    """Three or more consecutive sentences under 12 words is a register drift."""
    sentences = re.split(r"(?<=[\.!?])\s+", text)
    findings = []
    run = 0
    run_start = None
    for i, s in enumerate(sentences):
        words = len(s.split())
        if 0 < words < 12:
            if run == 0:
                run_start = i
            run += 1
            if run >= 3:
                findings.append({
                    "severity": "warning",
                    "rule": "short_sentence_run",
                    "line": _line_of(text, text.find(sentences[run_start])) if run_start is not None else 1,
                    "snippet": " ".join(sentences[run_start:run_start+3])[:120],
                    "suggestion": "Three short sentences in a row drift toward terse-Claude. Voice prefers long comma-chained sentences. (Pass --email or register='email' if this is a structured email.)",
                })
                # Reset to avoid flagging the same run repeatedly
                run = 0
                run_start = None
        else:
            run = 0
            run_start = None
    return findings


def check_decisive_close(text: str) -> list:
    """Last paragraph should carry a decisive intensifier or strong verdict."""
    paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]
    if not paragraphs or len(text.split()) < 200:
        return []
    last = paragraphs[-1]
    # For email register, the actual close may be a single-line sign-off ("Kind regards,\nSpero").
    # Walk backwards past sign-off-like paragraphs to find the substantive close.
    SIGNOFF_PATTERN = re.compile(r"^(kind regards|best regards|cheers|regards|sincerely|spero)\b", re.IGNORECASE)
    close_idx = len(paragraphs) - 1
    while close_idx >= 0 and SIGNOFF_PATTERN.match(paragraphs[close_idx]):
        close_idx -= 1
    if close_idx < 0:
        return []
    last = paragraphs[close_idx]
    if not DECISIVE_INTENSIFIERS.search(last):
        return [{
            "severity": "info",
            "rule": "weak_close",
            "line": _line_of(text, text.rfind(last)),
            "snippet": last[:120],
            "suggestion": "Voice prefers a decisive close (verdict, intensifier, 'ought to' obligation, or clear call-to-action), not a summary.",
        }]
    return []


def lint_text(
    text: str,
    include_info: bool = True,
    include_warnings: bool = True,
    register: str = "prose",
) -> list:
    """Lint text against the Spero writing style.

    Parameters:
        text: the prose to lint.
        include_info: include info-level findings (e.g. weak close).
        include_warnings: include warning-level findings.
        register: 'prose' (default) or 'email'. The 'email' register
            skips bullet_heavy and short_sentence_run checks, since the
            structured email format relies on bullets and short bullet text.
            All other voice rules apply.
    """
    if register not in {"prose", "email"}:
        raise ValueError(f"register must be 'prose' or 'email', got {register!r}")

    findings = []
    findings.extend(check_em_dashes(text))
    findings.extend(check_american_spelling(text))
    findings.extend(check_however_opener(text))
    findings.extend(check_banned_hedges(text))
    if include_warnings:
        findings.extend(check_magnitude_without_dollar(text))
        findings.extend(check_arguably_density(text))
        if register == "prose":
            # Skip bullet-heaviness and short-sentence-run in the email
            # register, the structured email format relies on bullets and
            # intentionally short sub-bullet text.
            findings.extend(check_bullet_heavy(text))
            findings.extend(check_short_sentence_run(text))
    if include_info:
        findings.extend(check_decisive_close(text))
    findings.sort(key=lambda f: (f["line"], {"error": 0, "warning": 1, "info": 2}[f["severity"]]))
    return findings


def fingerprint_summary(text: str) -> dict:
    """Return signature-marker frequencies for the input."""
    counts = {
        "arguably": len(re.findall(r"\barguably\b", text, re.IGNORECASE)),
        "ought_to": len(re.findall(r"\bought to\b", text, re.IGNORECASE)),
        "self_evidently": len(re.findall(r"\bself-evidently\b", text, re.IGNORECASE)),
        "cumulatively": len(re.findall(r"\bcumulatively\b", text, re.IGNORECASE)),
        "so_to_speak": len(re.findall(r"\bso to speak\b", text, re.IGNORECASE)),
        "ie_inline": len(re.findall(r"\bi\.e\.\b", text)),
        "however_inline": len(re.findall(r"[a-z],\s*however,?\s*[a-z]", text)),
        "thus": len(re.findall(r"\bthus\b", text, re.IGNORECASE)),
        "consequently": len(re.findall(r"\bconsequently\b", text, re.IGNORECASE)),
        "in_turn": len(re.findall(r"\bin turn\b", text, re.IGNORECASE)),
    }
    sentences = [s for s in re.split(r"(?<=[\.!?])\s+", text) if s.strip()]
    if sentences:
        avg_sentence_len = sum(len(s.split()) for s in sentences) / len(sentences)
    else:
        avg_sentence_len = 0
    word_count = len(text.split())
    return {
        "word_count": word_count,
        "sentence_count": len(sentences),
        "avg_sentence_length_words": round(avg_sentence_len, 1),
        "marker_counts": counts,
    }


def main():
    ap = argparse.ArgumentParser(description="Lint prose against Spero's writing style.")
    ap.add_argument("input", nargs="?", default="-", help="File path or - for stdin")
    ap.add_argument("--json", action="store_true", help="JSON output")
    ap.add_argument("--no-soft", action="store_true", help="Only error-level findings")
    ap.add_argument("--info", action="store_true", help="Include info-level findings")
    ap.add_argument("--fingerprint", action="store_true", help="Output marker fingerprint")
    ap.add_argument("--email", action="store_true",
                    help="Email register: skip bullet_heavy and short_sentence_run checks. "
                         "Use for structured emails that rely on bullets by design.")
    args = ap.parse_args()

    if args.input == "-":
        text = sys.stdin.read()
    else:
        text = Path(args.input).read_text(encoding="utf-8")

    if args.fingerprint:
        fp = fingerprint_summary(text)
        if args.json:
            print(json.dumps(fp, indent=2))
        else:
            print(f"Words: {fp['word_count']}, Sentences: {fp['sentence_count']}, "
                  f"Avg sentence length: {fp['avg_sentence_length_words']} words")
            print("Marker counts:")
            for k, v in fp["marker_counts"].items():
                print(f"  {k:<18} {v}")
        return

    register = "email" if args.email else "prose"
    findings = lint_text(
        text,
        include_warnings=not args.no_soft,
        include_info=args.info,
        register=register,
    )

    if args.json:
        print(json.dumps(findings, indent=2))
        return

    if not findings:
        print(f"OK — no style violations. (register: {register})")
        return

    sev_count = {"error": 0, "warning": 0, "info": 0}
    for f in findings:
        sev_count[f["severity"]] += 1
        marker = {"error": "[X]", "warning": "[!]", "info": "[i]"}[f["severity"]]
        print(f"{marker} L{f['line']:<4} {f['severity'].upper():<7} {f['rule']:<35} {f['snippet']}")
        print(f"           -> {f['suggestion']}")
        print()
    print(f"Summary: {sev_count['error']} errors, {sev_count['warning']} warnings, {sev_count['info']} info  (register: {register})")
    if sev_count["error"] > 0:
        sys.exit(1)


if __name__ == "__main__":
    main()
