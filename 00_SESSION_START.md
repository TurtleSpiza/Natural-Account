# 00_SESSION_START.md, Parks 4090000 NA Review (Claude AI)

The Claude AI analogue of the old SETUP.md. The sandbox resets between tasks, so provision each fresh session before working.

## Read first, every session
Read `00_Account_Review_Register.xlsx` and `00_START_HERE_Handover.md` from the uploaded bundle archive, not from loose uploads. Update the register row whenever a status changes. A fresh TechOne export is the account under review; `New/` is raw intake and may be historical, so confirm against the register before treating any item as live.

## Skills (primary method, installed)
The `lcc-*` skills installed in this Claude AI project are the source of truth. Do not read reference data from any bundled skills copy. Read the relevant SKILL.md before producing any file or journal.

## Provisioning (one line)
```
pip install python-calamine py7zr --break-system-packages
```
pandas, openpyxl and pypdf are already present. LibreOffice 24.2.7 (`soffice`) is present for formula recalculation.

## TechOne exports
Parse with the `lcc-na-analysis` loader: `read_excel(engine='calamine')`; a parameter block sits above the data, headers at row index 5 (zero-based), data from row 6; detect the header dynamically by scanning for "Short Description".

## Formula recalc
`soffice --headless --calc --convert-to xlsx` then reload with openpyxl `data_only=True` to read computed values. Never hardcode a computed total.

## Integrity (single gate, no CI)
Before each re-zip: `python gen_manifest.py` then `python verify_manifest.py --strict`. Do not hand back on a mismatch. The manifest covers deliverables; `New/` raw intake stays outside it.

## Session log
Append a dated correction note to the handover per workstream. That is the Claude AI replacement for the old one-commit-per-workstream session log.

## Standing directive (recap)
No emails to anyone, Finance included. Decisions are Spero's and prepared recodes are journal-ready. Spero's commentary overrides journal holds; a missing source document is recorded as a manifest GAP for audit, never silently cleared. The only hard gate left is the 72111 TE005091 / Doc46-vs-AP dedup.

## Multi-part bundle intake (from 10-Jun-2026)
The bundle may arrive as split parts named `<bundle>.7z.part01`, `.part02`, ... (straight byte splits of one .7z). Reassemble and extract:
```
cat /mnt/user-data/uploads/*.7z.part* > /home/claude/bundle.7z
python3 -c "import py7zr; py7zr.SevenZipFile('/home/claude/bundle.7z').extractall('/home/claude/bundle')"
```
Verify each part's SHA-256 against the accompanying `*_PARTS.sha256` file before extracting; then run the normal `verify_manifest.py --strict` on the extracted tree. A plain `.zip` single-file bundle remains equally valid intake.
