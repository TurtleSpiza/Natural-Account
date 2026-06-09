# NA 72111 Minor Equipment & Supplies, Reconciliation Note (account held)

Reviewed 9-Jun-2026. Section 4090000, FY26 (26SLACT). Account balance $67,055.47 ex-GST (SE2).

Verdict: AMBER, not closeable. Two separate review passes exist for this account and they overlap, so they cannot be summed. One RED blocker (TE005091) remains open. The account stays held in CN-23167 and reconciliation to 100% is not yet achievable.

## Two populations, partially overlapping

- Pass 1, AP-invoice review (8-Jun register row). $3,433.91 across five AP creditor and stock lines, $2,260.36 miscoded. Tennyson vehicle stickers $335.00 to 72222, Ultimate PPE trousers and pants $694.68 to 72113, serial-numbered STIHL GTA 40 $439.68 to 72315, INITIATOR insecticide and fertiliser $791.00 to 72112.
- Pass 2, Doc46 journal-document audit (3-Jun, carried in `_CarryForward/72111_Doc46_Audit_source.xlsx`). 93 lines recoding $22,391.77 off 72111 (or $22,028.13 net of the held J12 riser line) across eleven destinations: 72113 $5,149.09, 72311 $4,286.05, 72249 $2,942.24, 73211 $1,707.25, 72112 $1,613.37, 72231 $1,409.84, 73220 $1,383.29, 72248 $1,360.00, 72315 $1,250.00 (Petersen Castings cemetery monument material), 72222 $927.00, 72313 $363.64 (the J12 risers, held).

## The overlap

The two passes are not disjoint. Tennyson Group reference 27577, $335.00, svc 20241 PK000055, recode 72111 to 72222, appears in both the 8-Jun AP review (line L02) and Doc46 (line J22). Posting both would double-count the relocation. Any merged 72111 recode must dedupe the overlapping transactions before posting; Tennyson 27577 is the confirmed overlap and the full line-by-line dedupe across the 93 Doc46 lines and the five AP lines has not been completed.

## The RED blocker (TE005091)

Doc46 line J12 recodes twenty desk risers $363.64 from 72111 to 72313. The same risers are already split in the PCard batch recode of Officeworks invoice 626529478. Booking both double-counts the riser relocation, so J12 was removed from the consolidated journal and stays removed unless TE005091 proves to be a separate purchase. Confirm with Finance whether TE005091 is the riser line of invoice 626529478.

## Why the account does not close

The standing standard verifies each account to 100% before close. The two passes together touch roughly $25,825 of the $67,055 balance; the remainder (ecology fuel-reduction already reversed by GJ078960, stores issues, standing orders, over-threshold one-offs) is untested. Closing 72111 requires: the population dedupe, the TE005091 resolution, and the open Finance confirmations carried on the 8-Jun register (PPE 72113 versus 72114, STIHL asset threshold and P&A register, 72222 for printed decals, INITIATOR stores item).

## Open actions

1. Resolve TE005091 (riser line of inv 626529478, or separate purchase). Sets whether J12 re-enters the batch.
2. Dedupe the Doc46 and AP-invoice populations before any 72111 recode posts. Tennyson 27577 confirmed in both; complete the full line match.
3. Carry the 8-Jun Finance confirmations (PPE destination, STIHL threshold, decal account, INITIATOR) into the consolidated Finance email.

---

## Addendum, 9-Jun-2026 (full ledger received; gate resolved; line-level review opened)

The full 72111 ledger export is now in hand: 364 transaction lines reconciling to $67,055.47 ex-GST (the export carried one total row, excluded). The line-level review across all four limbs is tracked in `00_Running_Transaction_Listing.xlsx` (sheet 72111), and sighted support is filed in `NA72111_Evidence/`. Three results this pass:

- **TE005091 resolved, the RED gate clears.** TE005091 is Officeworks invoice 626529478 (13-Jan-2026, Kirsty Quinn, $473.64 ex), date and amount matched to the ledger and to the sighted invoice and cover slip. The Doc45 PCard batch already splits it correctly off 72111 (risers $398.18 to 72313, diary $43.64 to 73563, adapter $31.82 to 73564, nets $0.00). Doc46 line J12 recodes the same 20 acrylic risers a second time, so it is a duplicate and stays dropped. Keep the Doc45 split, drop J12; the hard gate on the consolidated upload is cleared.
- **GST error on the Coles milk (TE005080), Limb 4 RED.** $12.50 GST-free (plain milk, receipt shows GST $0.00) booked at $11.36, that is incl / 1.1, claiming a $1.14 input tax credit that does not exist. Gross the GL to $12.50 and reverse the ITC. The Woolworths (TE005250) and the other Coles (TE005531) milk lines are booked at full value and are correct, so the defect is per line, not systemic. All three milk buys are depot amenity, not minor equipment (advisory, immaterial).
- **TE004477 (Bunnings, Steel Post & Rail, Play Safety), two findings.** Limb 1 RED: all three are operational park materials sitting on Depots admin svc 20151 / PK000001 and belong in Parks Services svc 20392 / PK000022; recode the PK on all three. Limb 4 RED on Steel Post & Rail: the document is a payment receipt, not the tax invoice (invoice 11925 is needed), and it carries a $2.02 input-taxed finance charge inside a fully grossed $93.63, so GST is over-claimed on the finance charge. Bunnings is a clean tax invoice with correct GST. Play Safety ($681.82) is not yet sighted.

Support filed in `NA72111_Evidence/`: Officeworks 626529478 invoice and cover slip, Coles and Woolworths milk receipts and slips, Bunnings tax invoice, Steel Post & Rail payment receipt 621. The remaining lines are PENDING in the listing until their receipts are sighted; the untested remainder is now a line-level review, not a held scope item.

Further lines worked (same pass): TE005080 Choice storage tubs $73.35 clears all four limbs (ABN 45 647 301 764 valid, GST $7.34, booked correct), the first 72111 line to clear fully. TE004476 (Bunnings, card ...0429) is correctly split across services: $32.66 and $126.46 already sit on Parks Services svc 20392/PK000022, while the two sighted lines ($259.89 tool trolley and bolts, $40.38 cleaning and cable ties) sit on Depots svc 20151; both have correct GST (ABN 26 008 672 179, $26.00 and $4.04). TE004476 is the contrast that supports the TE004477 recode: the same card and vendor were split to Parks Services here. Open: confirm the two Depots lines are not also Parks Services, and a P&A-register check on the $226 tool trolley. 13 of 364 lines now carry a verdict in the listing.

---

## Addendum, 9-Jun-2026 (Ultimate Motorbikes set sighted; three Trees-PK recodes staged)

The Ultimate Motorbikes / Woodmans / Tennyson evidence set (C00267478) is now sighted, closing two of the standing GAP rows on the evidence manifest (STIHL, and the PPE/decal source invoices). All five invoices reconcile to the ledger and all four ABNs checksum PASS (Ultimate 91 104 115 095, Woodmans 88 105 899 689, Tennyson 31 110 400 809). Three Trees-section lines (all svc 20241 / PK000055) are confirmed by Spero and staged in the new `NA72111_GENJNL_Recode.txt` as NA-only recodes (PK preserved):

- **ADVANCE X-Light trousers (PIK2270125) $292.09 ex -> 72113 PPE.** A partial recode off a $409.62 mixed invoice; the trousers portion ($321.30 incl) is protective clothing, the STIHL files, wrenches and mixing bottle ($80.29 ex) stay correctly in 72111.
- **Protective Pants G&U Navy (PIK2267644) $402.59 ex -> 72113 PPE.** A partial recode off a $776.72 mixed invoice; the pants portion ($442.85 incl) is protective clothing, the AS-system charger, battery and Scepter fuel/oil ($303.52 ex) stay in 72111 (advisory only whether the $286 incl battery/charger is P&A).
- **STIHL GTA 40.0 SET (PIK2267816) $439.68 ex -> 72315 parks P&A.** The whole line; a serialised parks power tool (SN451265196) below the asset threshold, so portable-and-attractive parks equipment.

The recode batch nets $0.00, all narrations within the 40-character cap, direction verified per pair (72111 source credited, destinations debited): $1,134.36 out of 72111, $694.68 to 72113, $439.68 to 72315. PPE destination set to 72113 by Spero (resolves the 72113-vs-72114 question on these lines). The batch stays HELD with the rest of CN-23167.

Two further lines in the same set are sighted but not recoded here: the Tennyson PFS Vehicle Stickers ($335.00 -> 72222) evidence is now in hand but its recode stays held pending the Doc46-vs-AP double-count dedup (Tennyson 27577 is the confirmed overlap), and the Woodmans mulch fork and flexi tub ($54.41) are sub-$200 minor equipment, correct in 72111. The account remains AMBER: NA RED stands at account level on the untested remainder, and the population dedupe is still open.

---

## Addendum, 9-Jun-2026 (Motorcycles R Us PPE staged on directive; Set 2 of the recode)

Two further 72111 lines on svc 20301 / PK000084 (Parks and Bushland Rangers, Park Services) are confirmed by Spero as motorcycle PPE and staged in Set 2 of `NA72111_GENJNL_Recode.txt`, all to 72113:

- **Doc 10286878 (9-Sep-2025), partial $883.49 ex of $1,169.62.** Four PPE items: LS2 MX701 helmet 2XL $390.90, Tourmax 2 pants 3XL $179.95, Alpinestars Tech 3 boots $234.50, Five Stunt Evo 2 gloves $78.14. The remaining $286.13 ex stays in 72111 (confirmed by Spero, non-PPE).
- **Doc 10287279 (17-Sep-2025), full line $179.95 ex.** Tourmax 2 motorcycle pants XXL, armoured riding pants. The two Tourmax pants (3XL on 10286878, XXL on 10287279) are distinct sizes on different dates, not a duplicate.

Set 2 totals $1,063.44 ex to 72113; the combined 72111 recode (Set 1 Ultimate + Set 2 Motorcycles R Us) is $2,197.80 out of 72111 ($1,758.12 to 72113, $439.68 to 72315), nets $0.00, narrations within the cap, direction verified.

Evidence basis differs from Set 1: the Motorcycles R Us invoices (Doc 10286878, Doc 10287279) are NOT packaged. Set 2 is staged on Spero's line-level directive, with the source invoices carried as GAP rows on the evidence manifest and the evidence and tax limbs unverified (ABN and GST not sighted) until the PDFs are provided. The recode dollars are populated on the directive; per the standing standard they are not evidence-cleared until the source invoices are sighted. The account stays AMBER.

---

## Addendum, 9-Jun-2026 (scrap-plaque sale income reclassified out of 72111; Set 3)

A negative $448.00 ex line ("returned plaques for scrap", doc SC10906, 15-Jan-2026) sits as a CREDIT in 72111 on Depots svc 20151 / PK000001. It is sale income wrongly offsetting Parks minor-equipment expense, and it belongs to Cemeteries. Confirmed by Spero and staged in Set 3 of `NA72111_GENJNL_Recode.txt`:

- **Reclass to 64411 Sale of materials (revenue, grp 6, unrestricted) on Cemeteries svc 20451 / PK000402.** Scrap metal is recycled goods, which is what 64411 covers; there is no dedicated scrap account. This is both a natural-account change (72111 expense to 64411 revenue) and a section/PK change (Depots PK000001 to Cemeteries PK000402).
- **Sign treatment.** The amount moved is a credit (-448.00 income), so the usual expense-recode direction inverts: 72111 is DEBITED +448.00 (lifting the income back out of the expense account, which restores Parks minor-equipment expense by $448), and 64411 is CREDITED -448.00 (booking the revenue in Cemeteries). This is correct double-entry, not a sign-flip; the recode flags it explicitly so it is not mis-read at upload.
- **Effect.** Net 72111 movement across all three sets is now -$1,749.80 ($2,197.80 expense out to 72113/72315, less the $448.00 income reversed back in as a debit). The $448.00 income leaves Parks 4090000 for the Cemeteries revenue line.

Evidence basis: the scrap-sale source document SC10906 is not packaged, so this is staged on Spero's directive plus the intrinsic ledger evidence (a credit balance in an expense account with a scrap-sale narration). Carried as a GAP row on the evidence manifest until SC10906 is sighted. The -492.80 inc / -448.00 ex / -44.80 GST is a taxable scrap supply; GST treatment follows the original booking. The account stays AMBER.
