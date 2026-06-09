# SETUP.md — Parks 4090000 NA Review (Claude Code on the web, GitHub repo)

This repo runs the branch-level NA review under Claude Code, working against GitHub. The session executes in a managed sandbox, so the environment must be provisioned each time it is fresh. Keep this file accurate against what the work actually invokes; a stale SETUP.md is the most common reason a clean clone fails.

## 1. Environment provisioning

`setup.sh` at the repo root is the single source of truth. It installs LibreOffice headless and the Python dependencies, is idempotent (safe to re-run), and self-heals the two snags this sandbox image throws: the Debian-managed `pip` cannot self-upgrade (so the script does not try), and `cffi`'s `_cffi_backend` occasionally ships broken (so the script detects a failed `pypdf` import and force-reinstalls `cffi`).

```bash
bash setup.sh
```

**Automatic on Claude Code web.** `.claude/hooks/session-start.sh` is a `SessionStart` hook (registered in `.claude/settings.json`) that runs `setup.sh` on every fresh web session, guarded to remote sessions only via `$CLAUDE_CODE_REMOTE`. It runs synchronously, so dependencies are guaranteed ready before the session starts. The hook activates for all future sessions once `.claude/settings.json` is merged to the default branch.

Confirm the toolchain before working:

```bash
python3 -c "import pandas, openpyxl, py7zr, pypdf; import python_calamine; print('python OK')"
soffice --headless --version
```

If `python-calamine` is missing, TechOne exports will not parse. If LibreOffice is missing, the register and tracker totals cannot be recalculated and verified.

## 2. Skills

The `lcc-*` skills are the primary method and must be discoverable by Claude Code (project `.claude/skills/` or the user-level skills directory). They are self-contained: `lcc-coding-review` bundles the chart of accounts and the `svc_map` / `pk_map` / `employee_pk_map` / `confusion_pairs` reference data, so no separate provision of reference files is needed. Read the relevant `SKILL.md` before producing any file or journal. See https://docs.claude.com/en/docs/claude-code/overview for the install path on this platform.

## 3. Repo layout

Root holds current state and per-account deliverables; see `CLAUDE.md` for the full tree. The load-bearing files:

- `00_Account_Review_Register.xlsx`, `00_README_Handover.md` — read first, every session.
- `00_Parks_4090000_NAReview_Tracker.xlsx`, `00_SE2_Source_8-Jun-2026.xlsx` — programme tracker and source ledger.
- `00_Bundle_Manifest.csv` — SHA-256 of every deliverable file. Excludes `New/`.
- `NA<acct>_*` — per-account recode, verification record, evidence manifest and `NA<acct>_Evidence/`.
- `_CarryForward/`, `_Sources_<D-Mon-YYYY>/` — prior journals and raw documents received.
- `New/` — raw intake, un-manifested, may be historical; confirm against the register before treating as live.
- `verify_manifest.py`, `gen_manifest.py` — strict-mode integrity scripts.

## 4. Per-session protocol

1. Read the register and handover at the repo root.
2. A fresh TechOne export in `New/` or `_Sources/` is the account under review. Parse it with the `lcc-na-analysis` loader (`engine='calamine'`; header at row index 5; detect by scanning for "Short Description"), and reconcile the account total before concluding.
3. Work the four limbs (see `CLAUDE.md`). For Limb 1, run the employee-to-service crosswalk on every line.
4. Close out: batch nets $0.00, per-pair direction verified, source-NA signed sum equals the stated reclass, destinations reconcile.
5. Update the register; recalc its formulas via LibreOffice and read back with openpyxl `data_only=True`.
6. Regenerate the manifest, strict-verify, commit.

## 5. Integrity enforcement (replaces the local pre-commit hook)

In a web/cloud environment a local git pre-commit hook will not reliably fire, so integrity is enforced two ways:

- **In-session, before each commit:** run `python gen_manifest.py` then `python verify_manifest.py` (strict). Do not commit on a mismatch.
- **Server-side, on every push and PR:** `.github/workflows/verify-manifest.yml` re-runs the strict verify in GitHub Actions and fails the check on any hash drift. This is the durable backstop.

One workstream per commit; the commit message is the session log. When you amend a prior artefact, regenerate the manifest and add a dated correction note to the handover in the same commit.

## 6. Note

`verify_manifest.py` and `gen_manifest.py` are assumed to exist from the prior repo and to exit non-zero on a mismatch under strict mode. If their invocation differs, align the commands in section 5 and in the Actions workflow accordingly.
