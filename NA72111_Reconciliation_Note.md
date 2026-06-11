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

---

## Addendum, 9-Jun-2026 (Posca markers to 73563; Spero standing directive recorded)

**Standing directive (Spero, 9-Jun-2026).** Anything Spero gives commentary or instruction on overrides the review criteria and is prepared for journal (upload-ready), applied retroactively. A missing source document is recorded for audit but no longer holds a directed line. This is now the operating rule for this batch; the recode files carry the disposition and the directed sets are upload-ready rather than held on evidence sighting.

**Set 4 - Posca paint markers (sighted).** TE004824 Officeworks invoice 624206983 (ABN 36 004 763 526 PASS, Kirsty Quinn, 2-Oct-2025) and the Celeste Fry cover slip are sighted. A partial recode off the $95.57 ex line: the PK8 POSCA PC5M marker pack ($45.16 inc / $41.05 ex) is stationery and moves to 73563 Printing & Stationery; the 3 OTTO acrylic desk risers ($59.97 inc / $54.52 ex) stay in 72111 for now. Set 4 is $41.05 ex to 73563.

The combined 72111 recode is now 14 lines, net 72111 movement -$1,790.85, batch nets $0.00, destinations 72113 +$1,758.12, 72315 +$439.68, 73563 +$41.05, 64411 -$448.00.

**Advisory (not journalled, awaiting instruction).** The 3 OTTO desk risers ($54.52 ex) on this invoice are stands for monitors/laptops; per the desk-component rule (chair and desk components, including desk risers, are 72313) they belong in 72313 Furniture & Fittings, not 72111. Left in place pending Spero's instruction, consistent with the directive that only instructed lines are journalled.


## Addendum, 10-Jun-2026 (TE004478 reconstruction sighted; cardholder ...0429 identified)

The Document Reconstruction for doc 202509081027550000000031 is sighted (filed `NA72111_Evidence/NA72111_TE004478_Oasis_DocReconstruction.pdf`): Oasis Landscaping & Building, $27.55 ex + $2.75 GST on 1-20151-72111, PCard 5550-XXXX-XX86-0429 named **DANIEL HARMAN**. The employee map confirms Daniel Harman (emp 16963), Urban Parks Team Leader, Park Maintenance, home svc 20440 / PK000003.

- **Cardholder identity pending closed.** The card ...0429 identity behind the TE004476 lines ($32.66 and $126.46 on 20392; $40.38 and $259.89 on 20151) and TE004478 ($27.55) is resolved to Harman. Those five listing lines now carry the cardholder.
- **Observation, not a recode basis.** Harman homes off the charged services (20392 Park Services, 20151 Depots). A PCard charge follows the purpose of spend, not the cardholder's home PK (PCard convention differs from the IT-recharge officer-home convention), so this is recorded as a candidate observation only — no PK move is proposed.
- **Evidence status.** The reconstruction proves the posting; the underlying Oasis merchant receipt remains unsighted (GAP), so TE004478's evidence limb does not clear.


## Addendum, 10-Jun-2026 (Doc46-vs-AP dedup closed; Tennyson stood down; gate lifted)

The last hard gate on this account's journal is closed. Every one of the 41 carried Doc46 items was matched to its underlying line in the full 364-line ledger (37 full-line, 4 within-line partials), every credit is contained within its line, and the ledger-line sets across all twelve journal streams intersect to nothing. TE005091 is settled on the evidence: the $473.64 Officeworks line is covered once, by the Doc45 split, and Doc46 J12 is confirmed absent from the live journal. Full record: `00_Doc46_AP_Dedup_10-Jun-2026.md`.

- **Tennyson 27577 stood down.** The $335.00 to 72222 recode is already carried as Doc46 J22; the separately prepared pair held since 9-Jun is permanently stood down, since staging it would double-count, the J12 pattern over again. The invoice is sighted (ABN PASS, GST exact), so the listing line moves L3/L4 GREEN and stays J via J22.
- **Three un-annotated Doc46 partials surfaced.** J10 ($33.20 of Pac Fire 188738 stays), J11 ($13.20 of Pac Fire 183802 stays) and J18 ($16.23 of Bunnings 8171/01259462 stays) are within-line partials with no remainder note in the source; the $62.63 joins the untested remainder, source invoices unsighted.
- **TE004478 is dual-merchant.** The reference resolves to the recoded Oasis $27.55 and an untouched KOMPAN $121.00 line; not a duplicate.
- **Consequence.** No hard gate remains on the 72111 batch or anywhere on CN-23167; confirmed recodes are upload-ready, with directive-staged evidence gaps still recorded for audit.

## Addendum, 10-Jun-2026 (the three outstanding receipt sets sighted)

All three remaining 72111 evidence GAPs are closed on documents received this session, each reconciling to the GL to the cent.

- **Oasis TE004478, $27.55.** Merchant receipt sighted (docket S7165, Oasis Landscaping & Building Supplies, ABN 83 827 343 713 checksum PASS): crusher dust 1/3 m3 $30.00 incl GST $2.73, plus a $0.30 EFTPOS surcharge, card ...0429 (Daniel Harman, matching the Document Reconstruction). GL $27.55 equals $30.30 divided by 1.1 exactly; the surcharge takes the taxable character of the underlying supply (GSTR 2014/2), so the booked base and the implied $2.75 ITC are correct within a cent of the receipt's $2.73 plus surcharge GST. Verdict COMPLIANT_WITH_NOTE. Advisory: the receipt is dated 18-Jun-2024 against a P3 FY26 posting, a roughly fifteen-month-late PCard reconciliation, noted for completeness.
- **Pac Fire 183802, $327.90 (P4).** Tax invoice sighted (ABN 60 088 233 783 PASS, 09-Oct-2025): BR9 fire helmet $299.70, name sticker (Van Werkhoven) $13.20, freight $15.00; GST $32.79 exact. COMPLIANT. The content is PPE; this is a Doc46 partial-recode source and the un-instructed remainder is a 72113 candidate.
- **Pac Fire 188738, $340.55 (P9).** Tax invoice sighted (same ABN, 27-Mar-2026): Apollo Wildland boot $307.35 and two torch holders $33.20; GST $34.06 exact. COMPLIANT. Footwear PPE; the remainder joins the standing 72113-versus-72114 footwear class ruling.
- **Bunnings 8171/01259462, $219.80 (P3).** Tax invoice sighted (ABN 26 008 672 179 PASS, 03-Sep-2025): six artificial plants and one pair of garden gloves; GST $21.96 by line-level rounding (compliant against $21.98 at a flat 10%). COMPLIANT. Gloves are a PPE candidate; the plants are decor for which 72111 is plausible.

The evidence manifest is updated (Oasis GAP text closed, four SIGHTED rows added) and the four canonical PDFs are filed in NA72111_Evidence/ with raw copies archived to _Sources_10-Jun-2026/. The Doc46 un-annotated remainders ($62.63) remain in the untested balance; the new sightings classify their content but no recode is staged without instruction.
