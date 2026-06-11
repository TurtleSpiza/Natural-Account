# NA 73563 Printing & Stationery, Verification Record

Batch CN-23167 (held). Reviewed 9-Jun-2026 (extends the prior WINC audit). Section 4090000, FY26 (26SLACT), Period 1-12.
Ledger export reconciles to 39 lines, total $9,495.37 ex-GST (footer $9,495.37, matched).
Services 20151 (PK000001 Depot Stationery), 20141 (PK000086 Planning), 20191 (PK000082 Design).

Verdict: AMBER. $6,354.47 (66.9%) miscoded out of 73563. The standing WINC stationery order is being used as a catch-all for tearoom refreshments, IT peripherals, cleaning and kitchen consumables, batteries, chemical and PPE. The two documents that were missing at the prior pass, the February WINC invoice and the Officeworks TE005250 receipt, are now sighted, so the account reconciles in full and the recode is complete. Held pending Finance acceptance of the systemic recode and one destination confirmation.

## Account composition and reconciliation

| Component | Reference | Ex-GST | Disposition |
|---|---|---|---|
| WINC creditor invoices P1-P10 (9 invoices) | 9901690129 ... 9901773647 | $6,261.48 | $3,852.64 miscoded, $2,408.84 stationery |
| WINC April | 9901782965 | $1,676.26 | $1,187.61 miscoded, $488.65 stationery |
| WINC February (now sighted) | 9901763737 | $1,240.45 | $961.49 miscoded, $278.96 stationery |
| Officeworks PCard (now sighted) | TE005250 / inv 628185694 | $352.73 | $352.73 miscoded (entirely) |
| Tom Kibble plan printing | TE004125 + TE005154 | $303.20 | Correct in 73563 |
| Marsden envelope stock issues | 094908 + 096380 | $109.47 | Correct in 73563 |
| GJ075544 EOY 2024-25 accrual reversal | GJ075544 | -$448.22 | Normal accrual, untouched |
| TOTAL | | $9,495.37 | $6,354.47 out, $3,140.90 retained |

The WINC GL ties to the WINC tax-invoice summaries line by line at $0.00 variance per the reconciliation workbook. The Marsden Library WINC charges ($3,049.21 across the nine invoices) hit branch 1-19101-73563 LCI, not Parks; no leakage observed.

## Four limbs (account level)

- L1 PK GREEN. PK000001 svc 20151, PK000086 svc 20141, PK000082 svc 20191. All valid, pk_validator VALID, preserved as transacted.
- L2 NA RED on $6,354.47, GREEN on the $3,140.90 retained. Per Chart of Accounts p23, 73563 covers printing and stationery costs only. Coffee, Milo, sugar, ice blocks, confectionery, USB cables, mice, keyboards, monitor risers, cleaning detergent, batteries, disinfectant aerosol, first-aid vest and desk risers are out of scope and recode to 73512 (hospitality, Reason B), 73564 (IT), 72111 (minor cleaning/kitchen/batteries), 72112 (chemical), 72113 (PPE) and 72313 (desk risers, furniture and fittings). Plan printing and the envelope stock issues are in scope and stay.
- L3 Evidence GREEN (closed 9-Jun-2026, see closure addendum). All eleven WINC line-detail invoices are now sighted: the nine P1-P10 invoices (9901690129, 9901699602, 9901709054, 9901718415, 9901727996, 9901737473, 9901746332, 9901754676, 9901773647) recovered from the archive, plus the February (9901763737) and April (9901782965) already held, the Officeworks invoice 628185694 behind TE005250, and the Marsden stock-issue document reconstruction. The 249 Parks lines across the nine reconcile to $6,261.48 ex-GST to the cent, both against the GL and against the support-pack rollup; every line maps to a tax-invoice line by item code and cost centre.
- L4 Tax GREEN (closed 9-Jun-2026). WINC ABN 94 000 728 398 checksum PASS (single ABN on all nine), GST-registered. Officeworks ABN 36 004 763 526 checksum PASS; the TE005250 receipt is under the $1,000 tier. Per-line GST reconciles on every sighted invoice.
- **GST status (Limb 4, per-line) GREEN.** The per-line food check is now complete against the sighted invoices. Of the 249 Parks lines, 34 ($1,195.79 ex) carry $0 GST on the WINC source invoices: these are the GST-free basic-food refreshments (coffee, Milo, hot chocolate, sugar, ice blocks and similar), correctly charged GST-free by the supplier, so no input tax credit is claimed and no phantom ITC arises. The remaining $5,065.69 is taxable and carries $506.56 GST (exactly 10%), which reconciles to the invoice totals. The earlier risk that a GST-free item might be grossed to 1/11 is closed: the GL books the per-line ex-GST and the source invoices supply the per-line GST.

## February WINC 9901763737 line audit (now sighted, 45 Parks lines, $1,240.45)

The February invoice was open at the prior pass for want of the PDF. Sighted now, the 45 Parks lines follow the same catch-all pattern: $961.49 (77.5%) is not stationery. Tearoom refreshments (coffee, Milo, hot chocolate, ice blocks, confectionery) $405.56 to 73512; IT peripherals (Apple lightning cable, monitor stand and riser, keyboard and mouse) $245.46 to 73564; cleaning, kitchen, batteries and storage $280.25 to 72111; Glen 20 disinfectant $6.65 to 72112; first-aid vest $23.57 to 72113. Stationery retained $278.96.

## Officeworks TE005250 / invoice 628185694 (now sighted, $352.73)

Three lines, all out of 73563. JB 2-in-1 active stylus pen $62.73 ex to 73564 IT Equipment. Otto desk riser large acrylic (15) plus mesh desk riser with drawer (1) $290.00 ex to 72313 Furniture & Fittings, mirroring the PCard-batch treatment of the separate Officeworks riser invoice 626529478. Total $352.73 is entirely outside printing and stationery.

## Recode (held, batch CN-23167)

58 lines, each miscoded item credited out of 73563 and debited to its destination, PK preserved. Batch nets $0.00. Total reclassified $6,354.47. See NA73563_GENJNL_Recode.txt. The WINC P1-P10 and April lines are carried unchanged from the prior balanced consolidated journal; the February and TE005250 lines are added this pass.

**Correction 9-Jun-2026.** The P1-P10 PK000001 PPE pair ($23.57, first aid vest and nitrile gloves) carried reversed signs, debiting 73563 and crediting 72113, which cancelled the correct Feb PK000001 PPE pair. Signs were flipped to credit 73563 and debit 72113, matching the narration and the PK000086 analogue. Reclass out of 73563 rises $47.14 to $6,354.47, the 72113 destination rises to $54.89, and the batch still nets $0.00.

## Overall RAG

AMBER. The account reconciles in full and the coding findings are firm. Held only on Finance acceptance of the systemic WINC recode, the 72313-versus-72111 destination for sub-$200 desk risers, and the Reason B assumption on the 73512 movements (filter any Finance 50/50 batch before posting).

## Open actions

1. Confirm Finance accepts the WINC systemic recode out of 73563 (catch-all stationery order). The pattern is consistent across P1-P10, April and February.
2. Confirm 72313 versus 72111 for the TE005250 desk risers ($290.00). 72313 mirrors the inv 626529478 riser treatment; lcc-asset-accounting not installed.
3. Confirm the 73512 movements are Reason B (staff morning/afternoon tea on-site, Non-FBT) and not already in a Finance 50/50 batch.
4. On confirmations, release the held recode in CN-23167.

## Method notes

- WINC line-level classification follows the prior P1-P10 audit precedents (cleaning and kitchen to 72111, refreshments to 73512 Reason B, IT peripherals to 73564, chemical to 72112, PPE to 72113), applied to the now-sighted February lines.
- Desk risers to 72313 follow the non-negotiable rule that desk components are 72313 and the established PCard-batch treatment; flagged for the 72313-versus-72111 sub-$200 question because lcc-asset-accounting is not installed.
- The $448.22 GJ075544 EOY reversal is a normal accrual treatment for the June 2025 invoice and is left untouched.

---

## Correction, 9-Jun-2026 (evidence limb incomplete) — SUPERSEDED by the closure below

A prior statement that 73563 had no outstanding invoices was wrong. The WINC reconciliation and the P1-P10 line-item audit reference eleven WINC invoices. The evidence pack held only two WINC line-detail invoices, 9901763737 (Feb) and 9901782965 (April); the audit workbook is derived analysis, not primary evidence. Nine WINC source invoices were not sighted: 9901690129, 9901699602, 9901709054, 9901718415, 9901727996, 9901737473, 9901746332, 9901754676 and 9901773647. The evidence limb reverted to AMBER. This gap is now closed, see below.

---

## Closure, 9-Jun-2026 (nine WINC invoices recovered and verified; evidence and tax limbs GREEN)

The nine unsighted WINC invoices were recovered from the `_CarryForward` archive (`files (4).zip`) and verified line by line. Result: a clean pass.

- **Reconciliation exact.** The 249 Parks lines (ACCOUNT 10179376 / PK000001 Depot Stationery and 10428958 / PK000086 Planning) across the nine invoices sum to **$6,261.48 ex-GST**, matching the WINC P1-P10 figure in this record and the GL to the cent (+$0.00). Each invoice also ties to the support-pack rollup `04_winc_parks_summary.csv` to the cent: P1 $448.22, P2 $458.49, P3 $357.50, P4 $1,092.86, P5 $776.44, P6 $629.66, P7 $597.86, P8 $949.99, P10 $950.46.
- **Tax clean.** WINC ABN 94 000 728 398 checksum PASS on all nine. Per-line GST reconciles: $506.56 on $5,065.69 taxable (10%), and 34 lines ($1,195.79) are GST-free basic food carrying $0 GST, so no input tax credit is claimed on food. The per-line food check the prior correction required is complete.
- **Limbs.** L3 Evidence AMBER to GREEN; L4 Tax (incl per-line GST status) to GREEN. L1 PK GREEN unchanged. L2 NA remains RED on the $6,354.47 systemic miscode: the finding is firm and the recode is prepared, but it is held on Finance acceptance of the reclass out of 73563 (an external decision), so the overall RAG stays AMBER on that and the two destination confirmations (72313-vs-72111 risers; Reason B / 50/50 filter), not on evidence or tax.

The nine invoices are filed in `NA73563_Evidence/` and listed SIGHTED on the evidence manifest. Overall RAG stays AMBER, now gated solely on the Finance-acceptance items, not on the evidence or tax gap.


## Addendum, 10-Jun-2026 (stores lines closed under the Marsden convention; code collision documented)

The two Despatch Stock Requisition lines (094908 $37.93, 096380 $71.54, both 1-20151-73563) are closed.

- **Evidence.** Both lines narrate item **207144**, and the Document Reconstruction for 096380 is sighted (filed `NA73563_Evidence/NA73563_096380_DocReconstruction.pdf`), confirming the posting. Under the Marsden stores convention (Spero, 10-Jun-2026) the 6-digit item match satisfies the evidence limb.
- **Code collision documented.** The Marsden inventory carries 207141-207144 twice: once as ENVELOPES (207144 = ENVELOPE DLX BARCODE WINDOW FACE SELF SEAL, BOX 500) and once as Steel Blue footwear flagged in-catalogue as a typo (should be 208141-44). The true item on these lines is the envelope — consistent with the QE11/ENVELOPE D narration — so the natural account 73563 is **correct** and no recode arises. Recorded so future reviewers do not read the boots entry.
- **Tax.** An internal stores issue is no GST event (the GST sat on the original stores purchase), per the 72114 stores precedent; tax limb GREEN on both lines.
- **April invoice firmed.** A PDF summary copy of WINC 9901782965 (April) is filed (`NA73563_WINC_April_9901782965_SummaryPDF.pdf`); it duplicates the already-sighted xlsx invoice and adds no new value.

Account RAG unchanged (AMBER on the held WINC systemic recode); the two stores lines move to GREEN in the running listing.
