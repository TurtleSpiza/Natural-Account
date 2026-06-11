# Doc46-vs-AP population dedup, 10-Jun-2026 (the last hard gate, closed)

This record settles the one remaining hard gate on the CN-23167 journal: whether the 3-Jun Doc46 audit recodes carried into `00_Live_Recode_Journal.xlsx` overlap the AP and PCard populations worked since, anywhere beyond the two collisions already known (J12, J30). The verdict is that they do not. Every carried Doc46 item was matched to its underlying line in the full 364-line 72111 ledger, every match was containment-tested against the journalled credit, and the resulting ledger-line sets were intersected across all twelve journal streams. Zero collisions arise, the journal stands as built, and the gate is closed. Nothing in this pass changes a journal line or a register dollar.

## Method

The carried Doc46 stream (41 journal items, 88 GENJNL lines) was rebuilt from `_CarryForward/72111_Doc46_Audit_source.xlsx` and each item's invoice reference, service code and 72111 credit were matched against `NA72111_Evidence/NA72111_Ledger_Full_9-Jun-2026.xlsx` (the full FY26 export, 364 lines, $67,055.47 ex-GST, criteria Branch 4090000, O110-O115, Periods 1-12). A match required the reference to resolve to a real ledger line on the stated service, and the journalled credit to be contained within (equal to or less than) that line's ex-GST amount. The same mapping was then built for every other stream that credits or debits 72111: the Doc45 PCard residual (from `_CarryForward/72111_PCard_Doc45_source.xlsx` as carried), NA72111 Sets 1 to 4, and the adjacent streams (NA73563 WINC, NA73513 Flair, NA72114 Reali) for completeness. The ledger-line index sets were intersected pairwise. The live journal itself was independently re-verified: 200 lines, batch net $0.00, every one of the twelve streams nets $0.00 individually, gross $38,894.06, no narrative field over 40 characters, no positive 72111 leg anywhere in the carried block and no negative destination leg either, so the per-pair direction holds throughout.

## Doc46 match table (41 carried items)

Every item resolves. 37 are full-line recodes where the credit equals the ledger line to the cent; 4 are within-line partials where a remainder stays in 72111.

| J | Vendor | Ref | Svc | Ledger ex-GST | Credit | Match |
|---|---|---|---|---|---|---|
| J1 | Pac Fire | 188512 | 20401 | 2,377.35 | 2,377.35 | FULL |
| J2 | Altus Traffic | 410015740 | 20401 | 1,383.29 | 1,383.29 | FULL |
| J3 | Industrial Decontamination | INV-19260 | 20401 | 696.10 | 696.10 | FULL |
| J4 | Industrial Decontamination | INV-18994 | 20401 | 560.85 | 560.85 | FULL |
| J5 | Industrial Decontamination | INV-19437 | 20401 | 450.30 | 450.30 | FULL |
| J8 | Reptile Awareness Displays | 003-2026 | 20411 | 200.00 | 200.00 | FULL |
| J9 | Alpha First Aid | 8168559 | 20662 | 369.00 | 369.00 | FULL |
| J10 | Pac Fire | 188738 | 20401 | 340.55 | 307.35 | PARTIAL, $33.20 stays |
| J11 | Pac Fire | 183802 | 20401 | 327.90 | 314.70 | PARTIAL, $13.20 stays |
| J13 | Bunnings | 8210/02030503 | 20181 | 397.26 | 397.26 | FULL ($0.04 invoice variance noted in Doc46) |
| J14 | Bunnings | 8171/01438782 | 20181 | 324.13 | 324.13 | FULL |
| J15 | Bunnings | 8210/01369423 | 20181 | 309.60 | 309.60 | FULL ($0.01 rounding noted in Doc46) |
| J16 | Bunnings | 8210/01349884 | 20181 | 240.23 | 240.23 | FULL |
| J17 | Bunnings | 8171/01240231 | 20181 | 226.78 | 226.78 | FULL |
| J18 | Bunnings | 8171/01259462 | 20181 | 219.80 | 203.57 | PARTIAL, $16.23 stays (previously un-annotated) |
| J19 | Bunnings | 8171/01228418 | 20181 | 210.29 | 210.29 | FULL |
| J20 | Spill Station | 109368 | 20181 | 203.79 | 203.79 | FULL |
| J21 | Big Red Truck Fire Rescue | S206895 | 20401 | 388.50 | 388.50 | FULL |
| J22 | Tennyson Group | 27577 | 20241 | 335.00 | 335.00 | FULL (see Tennyson, below) |
| J23 | Traffic Control Supplies | 178176 | 20401 | 285.00 | 285.00 | FULL |
| J24 | Tennyson Group | 25804 | 20412 | 307.00 | 307.00 | FULL |
| J25 | Legacy Monuments | 2591 | 20451 | 1,360.00 | 1,360.00 | FULL |
| J26 | Fulton Hogan | 20587563 | 20451 | 1,308.58 | 1,308.58 | FULL |
| J27 | Fulton Hogan | 20672646 | 20451 | 841.16 | 841.16 | FULL |
| J28 | Fulton Hogan | 20736903 | 20451 | 792.50 | 792.50 | FULL |
| J29 | Petersen Foundry | 1215 | 20392 | 1,250.00 | 1,250.00 | FULL |
| J33 | Stihl Shop Jimboomba | 283346 | 20181 | 913.09 | 913.09 | FULL |
| J34 | STKISS INITIATOR RB43 | 096371 | 20381 | 791.00 | 791.00 | FULL (a second 096371 line $44.06 is untouched) |
| J35a | STKISS LITTER PIC JF51 | 092580 | 20662 | 418.22 | 418.22 | FULL |
| J35b | STKISS LCC AWARE RB22 | 093813 | 20151 | 331.18 | 331.18 | FULL (same-docket lines $36.95, $80.79 untouched) |
| J35c | STKISS SITE BARRI XI11 | 095340 | 20392 | 562.79 | 562.79 | FULL (same-docket lines $57.06, $73.40, $143.21 untouched) |
| J35d | STKISS TRIMMER CO RC42 | 095736 | 20440 | 227.09 | 227.09 | FULL (same-docket line $64.00 untouched) |
| J35e | STKISS ELECTROLYT RE21 | 095893 | 20301 | 343.46 | 343.46 | FULL |
| J35f | STKISS LITTER PIC LF21 | 096300 | 20662 | 285.49 | 285.49 | FULL |
| J35g | STKISS LITTER PIC LF21 | 096601 | 20151 | 286.06 | 286.06 | FULL |
| J35h | STKISS TRAFFIC CO XF11 | 096664 | 20362 | 241.43 | 241.43 | FULL (same-docket lines $11.45, $34.35, $73.80, $187.60 untouched) |
| J35i | STKISS TRIMMER CO RC42 | 097341 | 20440 | 229.11 | 229.11 | FULL |
| J35j | STKISS TRIMMER CO RC42 | 097673 | 20181 | 229.11 | 229.11 | FULL |
| J35k | STKISS STAR PICKE WD26 | 097868 | 20181 | 334.16 | 334.16 | FULL (same-docket lines $8.50, $31.62 untouched) |
| J36 | Bunnings Underwood | 8210/00230575 | 20181 | 314.97 | 303.46 | PARTIAL, $11.51 watering can stays (annotated in Doc46) |
| J37 | Bunnings Underwood | 8210/02056322 | 20181 | 264.75 | 264.75 | FULL |

Carried Doc46 total credit out of 72111: $21,402.73 over 41 items. With the PCard residual ($473.64 + $54.52 + $27.55 = $555.71) the carried stream credits 72111 by $21,958.44 over 44 legs, which reconciles exactly to the live journal. Across all streams the journal credits 72111 by $24,197.29 (carried $21,958.44 plus NA72111 Sets 1-4 $2,238.85), debits it by $1,639.97 (Set 3 income lift $448.00 plus the WINC non-stationery $1,191.97 coming in from 73563), net 72111 movement -$22,557.32.

## AP and PCard side of the match

- **TE005091 / Officeworks 626529478** ($473.64, svc 20151). One ledger line, covered once, by the Doc45 split only (diary $43.64 to 73563, twenty risers $398.18 to 72313, adapter $31.82 to 73564, netting the $473.64 credit). Doc46 J12 ($363.64 riser duplicate) is confirmed absent from the live journal, zero J12-narrated lines. The historical RED gate is settled on the evidence, not just removed by assertion.
- **TE004824 / Officeworks 624206983** ($95.57, svc 20151). The one deliberately two-stream line: Set 4 credits $41.05 (Posca to 73563) and the carried PCard leg credits $54.52 (risers to 72313). The two credits sum to the ledger line exactly, complementary, no overlap.
- **TE004478** resolves to two ledger lines sharing the reference: Oasis Landscaping $27.55 (recoded to 72248, carried) and KOMPAN Australia $121.00 (untouched, still PENDING in the listing). The shared reference is a dual-merchant PCard batch, not a duplicate.
- **NA72111 Sets 1 and 2 containment**: PIK2270125 credit $292.09 within the $372.38 line, PIK2267644 $402.59 within $706.11, PIK2267816 $439.68 full line, doc 10286878 $883.49 within $1,169.62, doc 10287279 $179.95 full line. Set 3 lifts the full -$448.00 SC10906 credit. All contained.

## Collision result

The intersection of the Doc46 ledger-line set with every other stream's ledger-line set is empty, and no ledger line is hit twice within Doc46 itself. The only line touched by two streams anywhere in the journal is TE004824, by design, and its credits are complementary. J30 (Motorcycles R Us) remains dropped and its underlying line (10286878) is covered solely by Set 2.

## Tennyson 27577, the dependent line, closed

Doc46 J22 already carries the Tennyson 27577 recode, $335.00 from 72111 to 72222 on svc 20241 / PK000055, and it sits in the live journal, direction verified. The separately prepared NA72111 Tennyson pair, held since 9-Jun precisely for this question, is therefore permanently stood down: staging it would double-count the relocation, the J12 pattern over again. The line's evidence position is unaffected and is in fact complete, the invoice is sighted and filed (`NA72111_Evidence/NA72111_27577_Tennyson_VehicleStickers.pdf`, ABN 31 110 400 809 PASS, GST $33.50 exact), so the listing row's evidence and tax limbs move to GREEN with the line reading J (in journal, via J22).

## New observations from the match (recorded, not journalled)

1. **Three previously un-annotated partials.** J10, J11 and J18 are within-line partial recodes whose remainders ($33.20, $13.20, $16.23, together $62.63) stay in 72111 without a remainder note in the Doc46 source. The amounts are contained, so no double-count arises, but the three remainders join the untested 72111 balance and their source invoices (Pac Fire 188738, 183802; Bunnings 8171/01259462) are unsighted, consistent with the Doc46 stream's carried evidence basis.
2. **Same-docket residuals.** Six STKISS dockets and one INITIATOR docket carry smaller sibling lines (eleven lines, $689.18 in total) that no stream touches. They are part of the untested remainder, listed in the match table above.
3. **TE004478 dual-merchant.** The KOMPAN $121.00 line shares the TE004478 reference with the recoded Oasis line and is otherwise unworked.

## The 3-Jun outstanding flags, reconciled

The carried journal's own Verification & Findings sheet raised one RED and four AMBER flags plus one carry-forward item. All six now reconcile: the J12/TE005091 RED is resolved above; the Flair $77.27 AMBER resolved on 9-Jun exactly as the flag required (the Doc45 reversal source was wrong, the cover slip wrote to 71111, and the superseding NA73513 recode codes the actual $85.00 from 71111); the Reali format AMBER (net-movement versus full-reversal) remains a live Spero decision already on the outstanding register; the WINC 9901763737 carry-forward closed on 9-Jun when the invoice was sighted. The two travel AMBERs flagged "not in this batch", the Gold Coast parking TE004218 ($6.05, 73541 to 73531, Craig Logan PCard 16-Jun-2025) and the Cabcharge Jan-2026 statement split ($787.74, mixed local SEQ and Melbourne/Geelong interstate legs needing a per-traveller split), had been described as tracked separately but sat on no register; both are restored to `00_Outstanding_Evidence_and_Actions.md` as candidates for the 73531/73541 programme accounts.

## Verdict and consequences

The Doc46-vs-AP dedup is CLOSED and TE005091 with it. No hard gate remains anywhere on the CN-23167 journal; the 200-line live journal is upload-ready on the dedup standpoint, with the evidence gaps that ride on directive-staged lines still recorded for audit exactly as before. `_CarryForward/` is now fully worked: the consolidated journal and the Doc45/Doc46 sources are reconciled line-for-line into the live journal, and the folder stands as provenance only.
