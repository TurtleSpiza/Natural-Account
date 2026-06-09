---
name: spero-writing-style
description: "Spero writing style, two registers. Prose: Australian English, no em-dashes, hedge-then-commit ('arguably... ought to'), prose-default not bullets, signature lexicon ('arguably', 'self-evidently', 'ought to'), magnitudes anchored to dollar amounts, decisive verdicts. Email: unnumbered text headers, bold lead-in bullets, sub-bullets (max two levels), italics for figures, identifiers, judgement words, methodological assumptions, Cambria font, standardised sign-off. Voice rules apply in email prose. Use when drafting in Spero's voice (emails, reports, essays, cover letters, dashboards, handovers), linting drafts, or drafting structured emails. Triggers: 'in my voice', 'spero style', 'write this for me', 'draft in my style', 'lint this prose', 'style check', 'em-dash check', 'arguably', 'spero email format', 'structured email', 'bold bullets email', 'email to section leader'. Distinct from finance-investigation-narrative and lcc-finance-batch-email."
---

# spero-writing-style

The skill that codifies Spero's writing voice and the structured email format he uses for management correspondence, with a Python linter that flags voice violations. The voice content is drawn from `Downloads/spero_writing_style.md`, derived from approximately 63,000 words of undergraduate coursework. The email format is derived from a Period 10 Parks Maintenance variance email exchange and the user's stated preferences.

The voice is analytical, confident, strongly declarative. Hedge-then-commit ("arguably... ought to"). Prose-default in long-form work. Australian English. No em-dash separators (commas, parens, or full stops instead). The structured email register deliberately departs from the prose-default rule and uses unnumbered text headers, bold lead-in bullets, indented sub-bullets, and judicious italics, all set in Cambria.

## Two registers

This skill covers two coexisting registers:

* **Prose register** (default). Long-form documents, essays, reports, cover letters, narrative sections of dashboards, handovers, investigation emails written as continuous prose. The eight-item drafting checklist and the full style guide apply.
* **Email register**. Structured emails to section leaders, managers, finance colleagues, and other internal stakeholders where the email's purpose is to convey multiple findings or recommendations efficiently. The email format guide applies. Voice rules still apply within the prose passages (opening paragraph, bullet text, closing paragraph), the structural defaults of the prose register (no bullets, long sentences) are deliberately overridden.

The two registers are not mutually exclusive. A narrative-style email to a non-finance recipient with a single ask is prose register. A multi-finding update to a section leader is email register. The user's intent and the deliverable's purpose determine which applies.

## When to apply

Apply this skill when:

* The user asks Claude to draft prose in their voice, prose register, including long-form work or narrative emails.
* The user asks Claude to draft an email in the structured email register, including phrases like "spero email format", "structured email", "bold bullets email", "email to a section leader", or any email to a named manager or section leader where the content is multi-point.
* The user pastes a draft and asks for a style check, em-dash hunt, hedging review, magnitude-adjective audit.
* Cross-cutting use, another skill is producing prose (a finance-investigation email, a forecast handover, a section of an HTML dashboard) and the prose should match Spero's voice. Apply the linter as a final check.

Do not apply this skill when:

* The user is drafting prose for a different voice (Sevilay's cover letter uses a calmer applicant register, an LCC Finance batch email uses the Finance-Batch register, a vendor email uses an operational register). These are not Spero's authorial voice.
* The deliverable is not prose (a CSV, a JSON config, a Python module, a spreadsheet). The linter has nothing to lint.
* The user asks for "neutral" or "balanced" prose. Spero's voice is not neutral, that is a different register and out of scope here.
* The email is a one-line acknowledgement, scheduling reply, or other transactional message. The structured format is overkill for short transactional content.

## File index

```
SKILL.md                          This playbook.
style_guide.md                    Full prose style guide (canonical reference).
                                  Voice, sentence construction, signature
                                  lexicon, argument structure, document
                                  architecture, mechanics, marker frequencies.
checklist_for_drafting.md         Eight-item pre-flight checklist for prose.
                                  Open with thesis, hedge-then-commit, prose-
                                  default, Australian English, signature
                                  lexicon, no em-dashes, mechanical argument
                                  chains, decisive close.
worked_example_paragraph.md       The canonical prose demonstration paragraph,
                                  annotated.
email_format_guide.md             The structured email format spec. When to
                                  use, the four format elements (headers,
                                  bold lead-in bullets, sub-bullets,
                                  italics), typography, salutation and sign-
                                  off, the email skeleton, voice rules that
                                  still apply, linting.
email_template.html               Reusable HTML template for the email
                                  format, with Cambria fallback chain,
                                  ready to fill and paste into Outlook.
worked_example_email.md           The canonical email demonstration, the
                                  Period 10 Parks Maintenance variance
                                  email, in Markdown and HTML, annotated.
style_lint.py                     Python linter. Flags em-dash separators,
                                  American spelling, "However," sentence-
                                  openers, banned hedges, magnitude
                                  adjectives without dollars, low arguably
                                  density, short-sentence runs, bullet-
                                  heaviness, weak closes. Importable as a
                                  module or CLI. Supports a register='email'
                                  mode (or --email CLI flag) that skips
                                  bullet_heavy and short_sentence_run
                                  checks, since the email format relies on
                                  bullets and short bullet text.
```

## Workflow — drafting in the prose register

Step 1. Read `checklist_for_drafting.md`. Eight items.

Step 2. Draft the prose. Apply the checklist while drafting, not after.

Step 3. Run `style_lint.py` on the draft. Address every flagged violation:

```bash
python style_lint.py path/to/draft.md
```

Step 4. Re-read aloud. Check that "arguably" appears at least once per ~500 words for prose that aims to match the corpus density. Check that the close is a verdict, not a summary.

Step 5. Deliver.

## Workflow — drafting in the email register

Step 1. Read `email_format_guide.md`. The format spec, the italic-placement rules, the typography, the email skeleton.

Step 2. Read `worked_example_email.md`. The annotated reference email shows every element in operation.

Step 3. Draft the email. Use the skeleton from the format guide. Apply the four elements (headers, bold lead-in bullets, sub-bullets, italics) deliberately, not by default. Voice rules apply to the prose passages (opening paragraph, bullet text, closing paragraph).

Step 4. Run `style_lint.py` with the `--email` flag on the draft:

```bash
python style_lint.py path/to/email.md --email
```

The `--email` flag skips `bullet_heavy` and `short_sentence_run` checks. All other voice rules (em-dash, American spelling, however opener, banned hedges, magnitude without quantity, arguably density, decisive close) still apply.

Step 5. If the email is being delivered as HTML for direct paste into Outlook, populate `email_template.html` with the drafted content. The Cambria fallback chain (`Cambria, Georgia, 'Times New Roman', serif`) ensures graceful degradation if Cambria is unavailable on the recipient's machine.

Step 6. Deliver.

## Workflow — linting external prose

When the user pastes a draft and asks for a style check, apply the linter and report findings.

```python
from style_lint import lint_text

violations = lint_text(text)                       # Prose register, default
violations = lint_text(text, register="email")     # Email register
for v in violations:
    print(f"[{v['severity']}] {v['line']}: {v['rule']} — {v['snippet']}")
```

Output is a list of `{severity, line, rule, snippet, suggestion}` records. Severity is `error` (must fix), `warning` (review), or `info` (style hint).

## The hard rules (must enforce in both registers)

These are non-negotiable per the style guide:

1. **No em-dashes (`—`) or en-dashes (`–`) as separators.** Use commas, parentheses, or a full stop and a new sentence. The writer reaches for one of those three, em-dashes do not appear in the corpus.

2. **No American spelling.** "optimise", not "optimize". "favourable", not "favorable". "behaviour", not "behavior". Linter flags ize/yze/our→or drift.

3. **No mid-paragraph "However."** "However" appears mid-sentence, comma-introduced. "However, X" as sentence opener is a Claude tic that does not appear in the corpus.

4. **No "Perhaps", "it could be argued", "some might say".** These are conspicuously absent from the corpus. The writer hedges with "arguably" or "upon further research" and then commits.

5. **No bullet-heavy responses in the prose register.** Prose paragraphs that chain through reasoning are the default. Bullets only when content is genuinely enumerable (recommendation lists, risk profiles). This rule is deliberately overridden in the email register, which uses bullets as the load-bearing structure.

## The soft rules (warnings)

These the linter flags but does not reject:

1. **Magnitude adjectives without dollar amounts.** "significant", "substantial", "considerable", "material" — flag if no `$X` figure attached within the same sentence or the next.

2. **"arguably" density too low.** If the prose runs >500 words and no "arguably", flag. The corpus has 32 instances across 63k words, roughly 1 per ~2k words, but appearance density should be visible.

3. **Sentence too short.** The corpus is dominated by long, comma-chained sentences. Three sentences in a row under 12 words is a register drift toward terse-Claude. **Skipped in email register**, sub-bullets are intentionally short.

4. **Bullet ratio too high.** If >30% of the response is bulleted and the section is supposed to be prose, flag. **Skipped in email register**, bullets are the format.

5. **Missing decisive close.** The last paragraph that summarises rather than verdicts. Closing with "in summary, X, Y, Z were discussed" is wrong, closing with "intervention is dangerous, decisively so" matches the corpus. Applies to both registers, the email's closing prose should still carry a verdict or a call-to-action, not a recap.

## The style fingerprints (info)

Things the linter notes for tuning:

* "arguably" count
* "ought to" count
* "self-evidently" count
* Average sentence length (corpus norm, long, ~25-35 words for prose register, lower acceptable for email register)
* Bullet ratio
* "i.e." inline glosses count

## Anti-patterns

* **Linting a non-prose deliverable.** A CSV file or a Python module has no prose to lint. Refuse the lint, suggest the user is asking the wrong question.
* **Auto-correcting flagged violations.** The linter flags, the user (or a follow-up turn) decides whether to rewrite. Do not silently change the draft.
* **Treating warnings as errors.** Magnitude adjective without $ figure is a soft warning, not a blocker. The user may have legitimate reasons (e.g. the magnitude is not yet quantified).
* **Applying the voice to other writers.** Sevilay's cover letter is not in Spero's voice, running this linter on it would produce false positives. Different register, different rules.
* **Forgetting the `--email` flag.** Linting an email-register draft without `--email` will produce false-positive `bullet_heavy` warnings, since the format relies on bullets by design.
* **Doubling bold and italic on the same fragment.** The bullet lead-in is bold, the italic emphasis lands inside the explanatory clause, not on the lead-in itself. The two emphasis types must not collide.
* **Numbering email headers.** The email register uses unnumbered text headers. The 1.0/2.0 decimal Harvard format is reserved for the prose register (documents, reports, essays).
* **Three or more nesting levels in an email.** The format caps at two levels (primary bullet, one indented sub-bullet). Deeper nesting fragments the email across most email clients.

## Cross-skill flow

```
Other skill produces a prose or email draft (any of):
  - finance-investigation-narrative (Marisa email)
  - lcc-html-dashboard-design (narrative section in a dashboard)
  - lcc-parks-forecast (handover commentary)
  - exam-question-generator (question prose, sometimes)
       │
       ▼
spero-writing-style [THIS SKILL — apply as final lint]
  → flags em-dash separators (both registers)
  → flags American spelling (both registers)
  → flags hedging without commit (both registers)
  → flags magnitude adjectives without dollars (both registers)
  → flags bullet-heaviness (prose register only)
  → flags short sentence runs (prose register only)
       │
       ▼
Drafting skill addresses violations, re-lints, delivers.
```

The linter is a cross-cutting utility. It runs as the last step before any prose or email deliverable is signed off.

## Reference artefacts

* `Downloads/spero_writing_style.md` — the canonical prose style guide. Lifted into this skill at `style_guide.md`.
* `Downloads/All_Uni.pdf` — the source corpus (~63,000 words of coursework). Not stored here, original lives in the user's archive.
* `worked_example_paragraph.md` — the canonical prose demonstration paragraph.
* `worked_example_email.md` — the canonical structured email demonstration.
