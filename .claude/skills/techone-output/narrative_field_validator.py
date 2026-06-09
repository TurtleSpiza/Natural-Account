"""
Narrative field validator for TechOne GENJNL upload.

TechOne caps narrative fields at 40 characters per field. The journal upload
layout has THREE narrative columns (Narrative1, Narrative2, Narrative3) so a
journal line can carry 120 characters of context across three fields.

Validation:
  - Each narrative field <= 40 characters
  - At least one narrative field populated
  - No tab characters or line breaks (TechOne strips them silently)
  - No leading/trailing whitespace (silently trimmed)

Usage:
    from narrative_field_validator import validate_narrative, split_narrative

    issues = validate_narrative("My narrative", "", "")
    # returns list of issue strings; empty list = ok

    parts = split_narrative("Long narrative text that exceeds the 40 character cap clearly")
    # returns ("Long narrative text that exceeds the 40", "character cap clearly", "")

CLI usage:
    python narrative_field_validator.py "narrative1" "narrative2" "narrative3"
"""

import sys
from typing import Tuple


MAX_LEN = 40


def validate_narrative(n1: str, n2: str = "", n3: str = "") -> list[str]:
    """Return a list of issues. Empty list = valid."""
    issues = []
    fields = [(1, n1), (2, n2), (3, n3)]
    populated = sum(1 for _, v in fields if v.strip())
    if populated == 0:
        issues.append("All three narrative fields are empty (at least one required)")
    for i, v in fields:
        if v != v.strip():
            issues.append(f"Narrative{i} has leading/trailing whitespace (will be silently trimmed)")
        if "\t" in v:
            issues.append(f"Narrative{i} contains tab character (will be silently stripped)")
        if "\n" in v or "\r" in v:
            issues.append(f"Narrative{i} contains line break (will be silently stripped)")
        if len(v) > MAX_LEN:
            issues.append(
                f"Narrative{i} is {len(v)} characters, exceeds {MAX_LEN}-character cap "
                f"(truncated to '{v[:MAX_LEN]}')"
            )
    return issues


def split_narrative(text: str) -> Tuple[str, str, str]:
    """Split a long narrative across three 40-char fields, breaking on word boundaries.

    Returns a tuple (narrative1, narrative2, narrative3).
    If the text fits in one field, narrative2 and narrative3 are empty.
    If the text exceeds 120 characters total, the overflow is silently dropped
    (caller is responsible for shortening before calling).

    Strategy: greedy fit — pack as much as fits up to the last word boundary
    within MAX_LEN, then move to the next field. Single words longer than
    MAX_LEN are hard-truncated.
    """
    text = text.strip()
    if len(text) <= MAX_LEN:
        return (text, "", "")

    parts = []
    remaining = text
    for _ in range(3):
        if not remaining:
            parts.append("")
            continue
        if len(remaining) <= MAX_LEN:
            parts.append(remaining)
            remaining = ""
            continue
        # Find last space within MAX_LEN
        chunk = remaining[:MAX_LEN]
        last_space = chunk.rfind(" ")
        if last_space == -1 or last_space < MAX_LEN // 2:
            # No good word break; hard split at MAX_LEN
            parts.append(chunk)
            remaining = remaining[MAX_LEN:].lstrip()
        else:
            parts.append(remaining[:last_space])
            remaining = remaining[last_space:].lstrip()

    return tuple(parts) if len(parts) == 3 else (parts[0], parts[1] if len(parts) > 1 else "", parts[2] if len(parts) > 2 else "")


def main():
    if len(sys.argv) < 2:
        print("Usage: python narrative_field_validator.py <narrative1> [narrative2] [narrative3]")
        print("       python narrative_field_validator.py --split <long-narrative>")
        sys.exit(1)

    if sys.argv[1] == "--split":
        text = " ".join(sys.argv[2:])
        n1, n2, n3 = split_narrative(text)
        print(f"Narrative1: '{n1}' ({len(n1)} chars)")
        print(f"Narrative2: '{n2}' ({len(n2)} chars)")
        print(f"Narrative3: '{n3}' ({len(n3)} chars)")
        issues = validate_narrative(n1, n2, n3)
        if issues:
            print("\nIssues:")
            for i in issues:
                print(f"  ! {i}")
        return

    n1 = sys.argv[1]
    n2 = sys.argv[2] if len(sys.argv) > 2 else ""
    n3 = sys.argv[3] if len(sys.argv) > 3 else ""
    issues = validate_narrative(n1, n2, n3)
    if not issues:
        print("OK")
        sys.exit(0)
    for i in issues:
        print(f"FAIL: {i}")
    sys.exit(1)


if __name__ == "__main__":
    main()
