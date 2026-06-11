# NA73128 Other services, Verification Record
Account 1-20151-73128 | Branch 4090000 Parks | Section 4090210 | Svc 20151 Parks Leadership and Administration | PK000001 Depots | FY2026 P1 to P12 | Prepared 10-Jun-2026

## Verdict
AMBER, journal-ready. Natural account miscode confirmed on the full milk spend. Recode 73128 to 73512 instructed by Spero Karkalemis on 10-Jun-2026 and prepared journal-ready per the standing directive. Evidence limb GREEN as at the second intake of 10-Jun-2026, all 50 invoices and the bond refund documents sighted. Sixteen GST errors confirmed, $61.11 total ITC overclaimed, plus one net-nil bond GST note, staged for the GST Errors Register. Account remains AMBER pending journal upload and register writes only.

## Account reconciliation
TCB Distributors weekly milk, 57 PUR lines incl 7 variance lines: $2,026.90.
GJ075544 EOY 2024/25 AP accrual reversal, 4 lines at -$43.05: -$172.20.
Raj Aggarwal bond refund pair, Cred inv 12022026 +$2,727.27 and AP003810 -$2,727.27: $0.00.
Account net: $1,854.70. Reconciled to the ledger export, no residual.

## Four-limb result
Limb 1 Service and PK: PASS. Svc 20151 maps to PK000001 section Depots per the installed svc_map. All 25 sighted invoices addressed to 117 Chambers Flat Rd Marsden, standing order PO 709655, customer 643. No employee attribution arises on consumables. Advisory: the Raj Aggarwal Access to Parks bond refund sits on the Depots service, nets $0.00, no recode dollar.

Limb 2 Natural account: FAIL, recoded. 73128 is a last resort services account per the Chart of Accounts. Milk is a goods purchase. Destination 73512 Entertainment and Hospitality Non-FBT, on-site staff refreshments, no FBT, per the FBT ruleset in lcc-coding-review. Instructed by Spero 10-Jun-2026. Advisory: the bond refund pair also does not belong on 73128 (72233 or balance sheet is the conventional home) but nets $0.00 and is excluded from the recode.

Limb 3 Evidence: AMBER. 25 of 50 unique invoices sighted and reconciled line by line. 25 invoices unsighted, GL value $1,175.46, listed as GAP rows in NA73128_Evidence_Manifest.csv with TechOne Document File IDs. Raj Aggarwal Document Files 1209387 and 1214571 also unsighted, GAP rows. No evidence waiver granted as at 10-Jun-2026.

Limb 4 Tax: AMBER. All sighted invoices are GST-free fresh milk, GST $0.00 stated. Six invoices Jul-2025 to mid-Sep-2025 had 1/11th GST wrongly extracted at AP, input tax credits overclaimed $18.11 in total: INV-397213 $3.68, INV-398029 $2.45, INV-398653 $1.84, INV-398878 $1.90, INV-399080 $4.45, INV-399291 $3.79. Corrected at source from INV-399504 (21-Sep-2025) onward, all later sighted invoices post 1 to 1. INV-399291 additionally keyed off the $41.90 delivery docket figure rather than the $41.88 invoice, 2 cents. Suspected same extraction error on the ten unsighted $43.05 lines Jun-2025 to Aug-2025, up to $43.05 further ITC, unconfirmed pending sighting. ABN 65 654 974 633 passes the checksum, ABR live lookup not completed this session (fetch returned a cached unrelated record), registration status checksum-valid register-unconfirmed. All invoices under $82.50 so formal tax invoice requirements are light, the ITC finding rests on the invoices' own GST 0.00 declarations. Six errors staged for 00_GST_Errors_Register.xlsx, bundle not available this session.

## Recode journal
NA73128_GENJNL_Recode.txt. PK ledger format, 122 lines, 61 full-reversal pairs covering every milk GL line as transacted (57 PUR incl variance lines, 4 GJ075544 reversal lines). Source leg 73128 posts opposite to the original line sign, destination leg 73512 posts the original sign. Direction verified per pair. Signed sum on 73128 legs -$1,854.70 equals the reclassified total, 73512 legs +$1,854.70, batch nets $0.00. Narrations within the 40-character cap, validated. PK000001 preserved as transacted. 73512 passes the restriction check. Raj Aggarwal pair excluded.

## Data quality notes
GL Reference 643 (08-Mar-2026) is the TCB customer number keyed as the reference, actual invoice 404203, sighted. Reference 4053884 carries an extra digit, actual invoice 405388, sighted. Reference 40581 is truncated, actual invoice 405812, sighted. C00275278.pdf and C00275278 (1).pdf in the intake are byte-identical, one document retained.

## Open items
1. 25 unsighted invoices, GAP, no waiver granted.
2. Ten suspected GST extractions Jun-Aug 2025, unconfirmed.
3. GST Errors Register entries staged, bundle required.
4. Register row staged, bundle required.
5. Raj Aggarwal Document Files 1209387 and 1214571 unsighted, advisory.

## Correction note, 10-Jun-2026, second intake (C00216123.zip)
Twenty five further TCB invoices and the Raj Aggarwal bond refund documents received and sighted. All evidence GAPs cleared, manifest regenerated, no GAP rows remain.

Limb 3 Evidence: now PASS. 50 of 50 unique invoices sighted and reconciled to the GL line by line. Bond refund evidence sighted: Parks Events Bookings email chain (Raj.pdf and the .msg original), Queensland Country Bank statement Nov-2025 showing the $3,150.00 transfer to Logan City Council City Account 138001223 on 21-Nov-2025 ($3,000 bond plus $150 event fee, Mundoolun Park event), and ABN Lookup records for Mundoolun Estate Community and Environmental Group INC, ABN 72 940 549 625, active, not registered for GST.

Limb 4 Tax: the ten suspected extractions are CONFIRMED. Each Jun-2025 to Aug-2025 invoice totals $47.35 GST-free and the GL keyed $43.05, being $47.35 divided by 1.1. ITC overclaimed $4.30 per invoice, $43.00 in total. Confirmed GST errors now sixteen, $61.11: INV-396217, 396428, 396633, 396827, 397026, 397411, 397642, 397820, 398238, 398437 at $4.30 each, INV-397213 $3.68, INV-398029 $2.45, INV-398653 $1.84, INV-398878 $1.90, INV-399080 $4.45, INV-399291 $3.79. The error window is Jun-2025 to mid-Sep-2025 inclusive, corrected at source from INV-399504 (21-Sep-2025).

Bond refund GST note, net nil: the $3,000 bond refund to a non-GST-registered incorporated association was booked at $2,727.27 ex-GST on Cred inv 12022026 (12-Feb-2026), implying $272.73 ITC claimed on a payment that is not a creditable acquisition. AP003810 (10-Mar-2026) reversed the full amount at the same ex-GST figure, R/N 19355382, so the net GST effect is nil with a Feb-2026 to Mar-2026 cross-period misstatement of $272.73. Recorded for the GST Errors Register as net-nil, timing only.

Vendor rounding pattern, data quality: TCB printed invoice totals are rounded to the nearest five cents (47.355 to 47.35, 55.22 to 55.20, 50.99 to 51.00, 41.88 to 41.90). AP keying alternated between the item sum and the rounded printed total: INV-401989 keyed $55.20 against a $55.22 item sum (2 cents under, no variance line), INV-404405 keyed $55.22 against a $55.20 printed total, INV-406431, 406649 and 406866 keyed $51.00 with -$0.01 variance lines squaring back to the $50.99 item sums, INV-399291 GST-extracted from the rounded $41.90. Immaterial, noted for completeness.

The four GJ075544 EOY reversal lines at -$43.05 correspond to FY25 accruals raised at the wrongly extracted base for the June 2025 weeks. The FY25 side is outside this review's scope, advisory only.

The recode journal NA73128_GENJNL_Recode.txt is unchanged by this intake. Amounts recode as transacted, the GST corrections are a separate BAS adjustment, not a GENJNL movement.

Open items after this correction: 1. GST Errors Register, sixteen entries plus the bond net-nil note, staged, bundle workbook required. 2. Register row, staged, bundle required. 3. Journal upload. No evidence items remain open.

## Correction note, 10-Jun-2026, bundle integration session

The account is integrated into the master bundle this session. Three closures and one packaging gap.

Limb 4 Tax, ABR item closed: the ABR live lookup completed 10-Jun-2026. TCB Distributors Pty Ltd, ABN 65 654 974 633, Australian Private Company, active from 1-Nov-2021, GST registered from 1-Nov-2021, main business location QLD 4129. Registration status moves from checksum-valid register-unconfirmed to register-confirmed. Record filed as NA73128_Evidence/NA73128_ABR_TCB_65654974633_10-Jun-2026.pdf. A GST-registered supplier issuing GST-free invoices is consistent with fresh milk as GST-free basic food. Limb 4 carries no remaining verification items; the sixteen confirmed errors are recorded on the GST Errors Register as corrective actions, not open verifications.

GST Errors Register written: GSTE-07 to GSTE-22 (sixteen TCB extractions, $61.11 ITC over-claimed, OPEN, BAS adjustment) and GSTE-23 (bond refund net-nil timing note, $272.73, NOTE). Register OPEN total recalculates to $130.61 across all accounts. Open item 1 of the prior note is closed.

Account Review Register written: 73128 row added (AMBER, journal-ready), register total now $71,807.68 ex-GST across nine accounts. Open item 2 of the prior note is closed. The live consolidated recode journal is regenerated with the NA73128 stream (122 lines), still netting $0.00.

Packaging gap, recorded not cleared: the 56 per-line evidence PDFs behind this account's manifest hashes were produced and sighted in the prior session but only the compressed second-intake binder (25 TCB invoices, the QCB statement, ABN Lookup records and the bond email chain) travelled into this bundle, filed as NA73128_Evidence/NA73128_SecondIntake_Binder_C00216123.pdf. The first-intake split files are not physically present in this bundle. The sighting itself stands (all 50 invoices reconciled line by line, hashes fingerprinted at sighting in NA73128_Workstream_Manifest_10-Jun-2026.csv, carried in the bundle); the evidence limb remains PASS on sighting, and the per-line packaging is an open artefact action, listed in the register row and 00_Outstanding_Evidence_and_Actions.md.

Open items after this note: 1. Journal upload (NA73128_GENJNL_Recode.txt, journal-ready). 2. BAS adjustment $61.11. 3. Per-line evidence packaging into NA73128_Evidence/.
