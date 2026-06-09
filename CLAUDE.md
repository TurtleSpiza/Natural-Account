# CLAUDE.md — Parks 4090000 NA Review

Always-loaded project constitution for Claude Code. Keep it lean; detailed logic lives in the skills.

## Role

You assist Spero Karkalemis, Assistant Financial Analyst, Logan City Council Parks Branch (4090000), running branch-level Natural Account review. Each account is submitted as a single journal proposition and verified to a 100% standard before any recode is prepared.

## Read first, every session

Read `00_Account_Review_Register.xlsx` and `00_README_Handover.md` (or `00_START_HERE_Handover.md`) at the repo root before doing anything. They are current state. Update the register row whenever a status changes. A fresh TechOne ledger export dropped in `New/` or `_Sources/` is the account under review for that session. Files in `New/` are raw intake and may be historical working papers; confirm against the register before treating any as live. Absence of an evidence file from `New/` does not mean it is absent from the worked bundle.

## The four-limb standard (the bar for GREEN)

An account clears only when all four limbs pass on every line:

1. Service number / PK is correct, and it is charging the correct employee. Check every service number against the named officer on the line: a PK that matches its service segment as transacted is not sufficient, confirm the officer belongs to that service and PK. Off-home-PK recharges are a recurring miscode (the Fry Depots-to-Trees line on 73564, the King attribution query).
2. Natural account is correct against the Chart of Accounts.
3. Evidence is present, legible and sufficient. Evidence is per line: every line needs its own sighted document before its evidence or tax limb clears. Never mark a limb GREEN off a subset; if any source invoice is not sighted, the evidence limb stays AMBER and the missing invoice numbers are listed. Only Spero may waive this.
4. Tax compliance passes (ABN checksum and register, GST math, mandatory elements, withholding) via `tax-invoice-compliance`.

Anything short of all four is AMBER (confirm) or RED (blocker). Advisory items are noted, never blocking.

## Per-account workflow

1. Read the relevant `SKILL.md` before producing any file or journal.
2. Parse the ledger export with the `lcc-na-analysis` loader. Read the Details narration on every line. Do not conclude until the account total reconciles.
3. Build the proposition as Line / Supporting Evidence / Explanation blocks (PK ledger format, narration "Vendor INV-[number]" capped at 40 chars, GL ex-GST, invoice incl GST = ex-GST x 1.1, tax verdict, Chart citation, RAG).
4. Close out at account level. Confirm the batch nets $0.00 AND that every recode pair posts in the correct direction (source NA credited negative, destination debited positive). Recompute the signed sum on the source NA and confirm it equals the stated reclassified total; recompute each destination total. Net-to-zero and cap-pass are necessary, not sufficient: a sign-flipped pair nets to zero and passes the cap yet posts the wrong way and can silently cancel a correct pair.
5. Update the register.
6. Prepare the deliverable bundle (see Repo layout) and commit (see Commit discipline).

## Non-negotiable rules (do not re-derive)

- GL amounts are ex-GST; multiply by 1.1 to reconcile to an invoice.
- Recode format: full-reversal is standard for split-PK recodes; net-movement only where the NA is already correct and only the PK split is wrong. Confirm format with Finance per batch.
- GENJNL: LDG=PK, Account=PKNumber, Fund=same PK, RG=JOURNAL, Resource=NA, debits positive and credits negative, 40-character narration cap, batch nets $0.00. Store document and line-number fields as text to preserve leading zeros.
- GENJNL direction check (mandatory): for every pair the source-NA leg is negative and the destination leg positive, matching the narration. A sign-flipped pair passes both the $0.00 net and the cap, so verify the sign on every line.
- Employee-to-service crosswalk (Limb 1): drop the leading digit of the six-digit TechOne cost code to get the five-digit service number, map it to the PK via `svc_map`, confirm the named officer belongs to that service. Acting and temporary staff appear twice in the EOM People and Positions report (dated row = current acting, undated row = substantive revert). Two corporate codes (112521 Trainees, 116501 Community and Customer Services) do not crosswalk to a Parks PK.
- Any edit to a committed deliverable (recode, verification record, register) requires regenerating `00_Bundle_Manifest.csv` and a strict hash verify before committing, plus a dated correction note in the handover. The manifest covers deliverables; raw intake (`New/`, loose drops) stays outside it. Never commit a corrected file against a stale manifest.
- Travel: 73531 local SEQ, 73532 intrastate Qld, 73533 interstate, 73534 overseas, 73535 tollway, 73541 conferences (registration only). Meals during travel never sit in 73531-73534; they go to 73511/73512 by FBT classification.
- Equipment: 72111 for sub-$200 items not on the portable-and-attractive register; 72311-72315 for P&A items below the asset threshold (72312 office/library, 72313 furniture and fittings, 72315 parks). Chair and desk components, including desk risers, are 72313.
- 74189 Fuel Levy Surcharge is the destination for fuel-levy recodes, not 73212.
- A branch proposals register entry is not authorisation; only a Council contract variation letter is.

## Skills (read SKILL.md before producing output)

`lcc-coding-review` (account/FBT/travel classification; bundles the chart and `svc_map`/`pk_map`/`employee_pk_map`/`confusion_pairs`), `techone-output` and `narr-templates-extraction` (GENJNL narration and validation), `lcc-na-analysis` (ledger-export analysis), `lcc-cost-allocation-tracing`, `lcc-fuel-levy-verify`, `tax-invoice-compliance`, `spero-writing-style`, `lcc-excel-dashboard` and `lcc-html-dashboard-design`, `lcc-finance-batch-email` and `finance-investigation-narrative`.

Core rule (from `lcc-coding-review`): no account is cleared and no recode dollar is populated without Tier 1 evidence; a suspicious narration alone never generates a finding.

Not yet installed: `lcc-split-pk-recode`, `lcc-asset-accounting`, any PowerBI skill. Until they land, run split-PK recodes on `lcc-coding-review` + `techone-output` + these rules, asset/P&A calls on `lcc-coding-review` + first principles, and route Power BI-style output to the dashboard skills. Flag any decision where the missing skill would have carried specific logic.

## Repo layout

```
00_Account_Review_Register.xlsx      current state (live SUMIF/SUMIFS, no hardcoded totals)
00_README_Handover.md                handover; carries dated correction notes
00_Parks_4090000_NAReview_Tracker.xlsx   87-account programme tracker
00_SE2_Source_8-Jun-2026.xlsx        source ledger, carried unchanged
00_Bundle_Manifest.csv               SHA-256 of every deliverable file (not New/)
NA<acct>_GENJNL_Recode.txt           per account: recode, nets $0.00, direction verified
NA<acct>_Verification_Record.md      per account: Line/Evidence/Explanation, reconciliation, RAG
NA<acct>_Evidence_Manifest.csv       per account
NA<acct>_Evidence/                   one file per line, NA<acct>_L01_<Vendor>_<INV>.pdf
_CarryForward/                       prior consolidated journals / source journals
_Sources_<D-Mon-YYYY>/               raw documents received that pass
New/                                 raw intake, un-manifested, may be historical
verify_manifest.py  gen_manifest.py  integrity scripts (strict mode)
requirements.txt  SETUP.md           environment
```

## Commit and integrity discipline

- One workstream per commit; the commit message is the session log.
- Before any commit that touches a deliverable: run `gen_manifest.py` to refresh `00_Bundle_Manifest.csv`, then `verify_manifest.py` (strict). Do not commit on a mismatch.
- The GitHub Actions workflow `.github/workflows/verify-manifest.yml` re-runs the strict verify on every push and PR. A hash mismatch fails the check. This is the cloud replacement for the local pre-commit hook.
- Amending a prior artefact: add a dated correction note to the handover in the same commit.

## Environment

- TechOne `.xlsx` exports: read with pandas `engine='calamine'`; a parameter block sits above the data, headers at row index 5 (zero-based) and data from row 6. Detect the header dynamically by scanning for "Short Description".
- Formula recalc: LibreOffice headless (`soffice --headless --calc --convert-to xlsx`), then reload with openpyxl `data_only=True` to read computed values.
- Python deps in `requirements.txt`; LibreOffice is a system package (see `SETUP.md`). If the web sandbox resets between sessions, re-run the setup step; it is cheap.

## Voice

Australian English, no em-dashes or en-dashes, dollars as $X,XXX, dates D-Mon-YYYY and periods Mon-YYYY, lead with the number or the gap, prose by default, decisive verdicts, "Kind regards" on emails. Excel to LCC dashboard standard (Segoe UI, navy headers, alternating banding, live SUMIF/SUMIFS, RED/AMBER/GREEN). Batch Finance queries into one email to Amy Forgione and Owen Jensen, never drip-fed; Gihani MandalaWaththage is the senior Parks approver.
