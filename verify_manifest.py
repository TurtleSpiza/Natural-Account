#!/usr/bin/env python3
"""Strict integrity check of 00_Bundle_Manifest.csv against the working tree.

Cloud replacement for the local pre-commit hook (see SETUP.md section 5 and
CLAUDE.md "Commit and integrity discipline"). The GitHub Actions workflow
.github/workflows/verify-manifest.yml runs `python verify_manifest.py --strict`
on every push and PR.

Three failure classes are reported:
  - drift   : a manifested file's SHA-256 or byte size no longer matches.
  - missing : a manifested file is absent from the tree.
  - orphan  : a deliverable file is present but not listed in the manifest.

The deliverable scope is defined in gen_manifest.py and shared here, so the two
scripts can never disagree about what counts as a deliverable. Under --strict
any of the three classes exits non-zero; without it, orphans are reported as a
warning only (drift and missing still fail). The workflow always passes
--strict, so any hash drift fails the check.
"""
from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

from gen_manifest import MANIFEST_NAME, deliverable_files, sha256


def load_manifest(path: Path) -> dict[str, tuple[str, int]]:
    rows: dict[str, tuple[str, int]] = {}
    with path.open(newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        expected = {"file", "sha256", "bytes"}
        if set(reader.fieldnames or []) != expected:
            raise SystemExit(
                f"{MANIFEST_NAME}: unexpected header {reader.fieldnames!r}, "
                f"expected {sorted(expected)}"
            )
        for row in reader:
            rows[row["file"]] = (row["sha256"], int(row["bytes"]))
    return rows


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="Verify the bundle manifest.")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Treat orphan deliverables (present but unlisted) as a failure.",
    )
    parser.add_argument("root", nargs="?", default=None, help="Repo root (default: script dir).")
    args = parser.parse_args(argv[1:])

    root = Path(args.root).resolve() if args.root else Path(__file__).resolve().parent
    manifest_path = root / MANIFEST_NAME
    if not manifest_path.is_file():
        print(f"FAIL: {MANIFEST_NAME} not found at {root}", file=sys.stderr)
        return 2

    manifest = load_manifest(manifest_path)
    on_disk = {p.as_posix() for p in deliverable_files(root)}

    drift: list[str] = []
    missing: list[str] = []
    for rel, (want_hash, want_bytes) in sorted(manifest.items()):
        abs_path = root / rel
        if not abs_path.is_file():
            missing.append(rel)
            continue
        got_bytes = abs_path.stat().st_size
        got_hash = sha256(abs_path)
        if got_hash != want_hash or got_bytes != want_bytes:
            drift.append(
                f"{rel}: manifest {want_hash[:12]}…/{want_bytes}B "
                f"vs disk {got_hash[:12]}…/{got_bytes}B"
            )

    orphan = sorted(on_disk - set(manifest))

    for rel in missing:
        print(f"MISSING: {rel}", file=sys.stderr)
    for line in drift:
        print(f"DRIFT:   {line}", file=sys.stderr)
    for rel in orphan:
        label = "ORPHAN" if args.strict else "WARN-ORPHAN"
        print(f"{label}: {rel} present but not in manifest", file=sys.stderr)

    failed = bool(drift or missing or (orphan and args.strict))
    verified = len(manifest) - len(missing) - len(drift)
    print(
        f"Manifest verify: {len(manifest)} rows, {verified} ok, "
        f"{len(drift)} drift, {len(missing)} missing, {len(orphan)} orphan."
    )
    if failed:
        print("RESULT: FAIL", file=sys.stderr)
        return 1
    print("RESULT: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
