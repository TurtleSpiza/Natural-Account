#!/usr/bin/env python3
"""Regenerate 00_Bundle_Manifest.csv.

The manifest is the SHA-256 fingerprint of every *deliverable* file in the
review bundle. It is the cloud replacement for the local pre-commit hook: run
this before any commit that touches a deliverable, then run verify_manifest.py
(strict) and do not commit on a mismatch.

Scope (see CLAUDE.md "Repo layout" and "Commit and integrity discipline"):
  - Deliverables ARE manifested: the 00_* current-state files, every NA<acct>_*
    file and NA<acct>_Evidence/ tree, plus _CarryForward/ and _Sources_*/.
  - NOT manifested: raw intake (New/), repo tooling and project constitution
    (CLAUDE.md, SETUP.md, requirements.txt, README.md, the manifest scripts),
    agent config (.claude/), CI config (.github/), git internals (.git/), and
    the manifest file itself.

Output columns: file,sha256,bytes  (POSIX relative paths, sorted ascending).
"""
from __future__ import annotations

import csv
import hashlib
import sys
from pathlib import Path

MANIFEST_NAME = "00_Bundle_Manifest.csv"

# Directories excluded wherever they appear in the tree.
EXCLUDE_DIRS = {".git", ".github", ".claude", "New", "__pycache__"}

# Individual repo-tooling / project files excluded by repo-relative path.
EXCLUDE_FILES = {
    MANIFEST_NAME,
    "requirements.txt",
    "00_SESSION_START.md",
    "gen_manifest.py",
    "verify_manifest.py",
    "build_listing.py",
    "build_master.py",
    "build_live_journal.py",
    "CLAUDE.md",
    "SETUP.md",
    "README.md",
    "setup.sh",
    ".gitignore",
}


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def deliverable_files(root: Path) -> list[Path]:
    """Every manifested deliverable under root, as repo-relative Paths."""
    out: list[Path] = []
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        rel = path.relative_to(root)
        if any(part in EXCLUDE_DIRS for part in rel.parts):
            continue
        if rel.as_posix() in EXCLUDE_FILES:
            continue
        out.append(rel)
    return sorted(out, key=lambda p: p.as_posix())


def build_rows(root: Path) -> list[tuple[str, str, int]]:
    rows = []
    for rel in deliverable_files(root):
        abs_path = root / rel
        rows.append((rel.as_posix(), sha256(abs_path), abs_path.stat().st_size))
    return rows


def main(argv: list[str]) -> int:
    root = Path(argv[1]).resolve() if len(argv) > 1 else Path(__file__).resolve().parent
    rows = build_rows(root)
    manifest = root / MANIFEST_NAME
    # CRLF matches the authoritative bundle manifest byte-for-byte, so a
    # re-run on an unchanged tree is a no-op rather than a line-ending churn.
    with manifest.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.writer(fh, lineterminator="\r\n")
        writer.writerow(["file", "sha256", "bytes"])
        writer.writerows(rows)
    print(f"Wrote {manifest.name}: {len(rows)} deliverable rows.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
