# _CarryForward triage, 9-Jun-2026

Review of the two archive drops (`04_Original_Archives.zip`, `01_Consolidated_Recode_Journal.zip`) against `_CarryForward/` and the live bundle, to decide what is integrated, what is marked for review, and what is a duplicate or superseded.

## Method

Every file in both archives was SHA-256 hashed and matched against every file currently in the repo (183 files). Byte-identical matches are duplicates of already-integrated material (the archives are the provenance of the current bundle: 22 of 56 files in the consolidated-journal zip and 9 of 29 in the original-archives zip are already present). Nested zips were opened and their indexes read. Only genuinely new content is actioned below.

## Verdict summary

| Cluster | Verdict | Action |
|---|---|---|
| Consolidated journal + build script + april_classified.csv | INTEGRATE | build_consol.py, april_classified.csv added to _CarryForward as the carried journal's provenance |
| 3-Jun original handover (HANDOVER.md) | INTEGRATE | added as _CarryForward/Handover_3-Jun-2026.md |
| **Nine unsighted WINC invoices (files (4).zip)** | **FOR REVIEW (high value)** | extracted to New/CarryForward_9-Jun-2026/WINC_invoices_73563/ — closes the 73563 evidence gap |
| 73563 coding-review support pack (Coding_Review_Support.zip) | FOR REVIEW | extracted to New/CarryForward_9-Jun-2026/73563_support/ — the line-item audit behind the recode |
| WINC 9901782965 April PDF + line-item audit xlsx | FOR REVIEW | staged to New/; firms the one already-sighted WINC line |
| Flair Floral invoice + ABN | FOR REVIEW (new vendor) | staged to New/; not yet attached to any account |
| C00281989 PDF | FOR REVIEW | staged to New/; unassigned PO/invoice |
| Document Reconstruction (12) + 096380 GJ | FOR REVIEW | staged to New/ and New/73563_support/; GJ source, likely 73563 |
| 72312 / 73533 / 73563 ledger exports (02_Ledger_Exports) | DUPLICATE / dedupe | same accounts already carry ledger extracts in their NA*_Evidence/; one 73533 file is named "_duplicate" |
| 73533 + 72312 evidence (Cabcharge, CTM, Uber, IKEA, Empire) | DUPLICATE | byte-identical to NA73533_Evidence/ and NA72312_Evidence/ already in the bundle |
| .msg source emails (WINC, Uber, Quinn Bankwest) | RAW PROVENANCE | left in the archive; the sighted jpg/png/pdf derivatives are already in the bundle |
| Abu_Journal.zip (8.4MB) | SUPERSET | a master archive containing all of the Random/ items above; nothing new beyond what is actioned |
| Old 00_Account_Review_Register.xlsx, 00_MANIFEST.csv, 00_START_HERE_Handover.md | SUPERSEDED | older snapshots; do NOT integrate, the live root files supersede them |

## Integrated this pass (into _CarryForward, manifested)

- `build_consol.py` and `april_classified.csv` — the build script and its classified input for `Parks_4090000_Consolidated_Recode_Journal_3-Jun-2026.xlsx` already carried here. They make the carried journal reproducible.
- `Handover_3-Jun-2026.md` — the original 3-Jun handover, the provenance for the carried journal and the starting point of the current programme.

## Marked for review (staged to New/CarryForward_9-Jun-2026/, raw intake, un-manifested)

The headline item is the **73563 evidence gap**. The 9-Jun handover recorded 73563 evidence as AMBER because only two of eleven WINC line-detail invoices were sighted (9901763737, 9901782965) and nine were not. All nine are in this archive and are now staged:

- `WINC_invoices_73563/` — the nine unsighted WINC invoices: 9901690129 (Jun-25), 9901699602 (Jul-25), 9901709054 (Aug-25), 9901718415 (Sep-25), 9901727996 (Oct-25), 9901737473 (Nov-25), 9901746332 (Dec-25), 9901754676 (Jan-26), 9901773647 (Mar-26).
- `73563_support/` — the 14-file coding-review pack: parks line-items raw/classified/miscoded, WINC parks summary, findings, GL listing source, Document Reconstruction 096380 (xlsx + pdf), recode-by-PK and recode-by-invoice summaries, distinct miscoded and OK-stationery item lists. This is the derived analysis behind the 73563 recode the handover called "derived analysis, not primary evidence".
- `WINC_9901782965_April2026.pdf` and the April line-item audit — firm up the already-sighted April line.
- `FlairFloral_invoice.pdf`, `FlairFloral_ABN.pdf` — a new vendor not attached to any account; needs an account and a four-limb check.
- `C00281989.pdf` — an unassigned PO/invoice.
- `DocumentReconstruction_12.pdf` — a GJ reconstruction source, likely 73563.

## Recommended next actions, in priority order

1. **Reopen 73563 evidence.** Verify the nine staged WINC invoices line by line against the recode; on a clean pass the evidence limb moves AMBER to GREEN and the 73563 verification record and register update. This is the single largest gap-closer in the bundle.
2. **Place Flair Floral.** Identify the account (floral supply is typically promotional, hospitality or an event line), run the four-limb and tax check, and confirm the ABN.
3. **Dedupe the 02_Ledger_Exports** against the per-account ledger extracts before treating any as a fresh export.
4. **Leave the superseded 00_* snapshots and the Abu_Journal superset where they are.** They are historical and would conflict with live state if integrated.

Nothing in this triage posts to the ledger or changes a register figure; the register total holds at $64,568.41 ex-GST. The staged New/ material is raw intake and stays outside the bundle manifest until reviewed.
