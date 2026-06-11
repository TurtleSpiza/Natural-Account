# NA73433 Verification Record - Other Fees & Charges
Prepared 10-Jun-2026 | Spero Karkalemis | Ledger 26SLACT, Branch 4090000, O110-O115, P1-12

Verdict: AMBER. Two lines, $139.25 ex-GST, account reconciles. One miscode found and recoded on instruction (QUT parking to 73531, journal prepared). One evidence GAP (TE004496 blue card receipt).

## Line 1. TE005281, QUT Parking, $34.55 ex-GST, P12, PK000087 (svc 20001 Parks Branch Management)
- Limb 1 (PK/officer): AMBER. Cardholder on TE005281 not yet confirmed.
- Limb 2 (NA): FAIL as posted. Receipt is 1hr 23min visitor parking; Chart places SEQ parking in 73531 Local Travel (SEQ) Cabcharge/Parking. Recode 73433 to 73531 instructed by Spero 10-Jun-2026 and prepared (NA73433_GENJNL_Recode.txt, nets $0.00, direction verified). Precedent: GJ078933 recoded Cabcharge $199.32 (73532) and GC parking $6.05 (73541) to 73531.
- Limb 3 (Evidence): PASS. Receipt 1795/0602/602 sighted, 18-Mar-2026, $38.00 incl GST.
- Limb 4 (Tax): PASS. ABN 83 791 724 622 checksum VALID, GST $3.45 = $38.00/11 exact, $34.55 x 1.1 = $38.01 (1c rounding). Under $82.50 tier, receipt sufficient.

## Line 2. GJ078933, Blue Card Services recode in from 73544, $104.70, P10, PK000075 (svc 20411 Bushcare)
- Limb 1: PASS on journal face (officer on original TE004496 to confirm).
- Limb 2 (NA): PASS. Chart 73433 description names blue cards explicitly. Pair direction verified via Document Reconstruction 75: 73544 leg -$104.70, 73433 leg +$104.70.
- Limb 3 (Evidence): GAP. Original TE004496 Blue Card Services receipt unsighted. Recorded as manifest GAP; not silently cleared.
- Limb 4 (Tax): AMBER pending the receipt.

## Reconciliation
$34.55 + $104.70 = $139.25 = export total. Exact.

## Open
1. TE004496 receipt (GAP). 2. TE005281 cardholder name.

## Addendum, 11-Jun-2026: TE004496 blue card receipt SIGHTED, evidence gap closed

The original receipt behind the GJ078933 recode-in is sighted (TE004496.pdf, 2 pages): Blue Card Services payment receipt 56213618922, 19-Aug-2025, $104.70, applicant Todd Preussner, with the PCard cover slip (cardholder Marissa Dyba, requesting officer Preussner, cost account PK000075-73544, "Blue Card Renewal"). The receipt states the fee is GST exempt under Division 81, and the $104.70 was booked gross with no ITC claimed, so the tax limb holds clean on this line. Distinct from the Barter blue card as recorded (same $104.70 standard fee, different officer and payment channel; Blue Card Services ABN 13 846 673 994 checksum PASS).

Evidence limb on the blue card line clears; the account's remaining open is the TE005281 cardholder confirmation on the QUT line. Evidence filed: NA73433_Evidence/NA73433_L02_BlueCard_TE004496_Preussner.pdf.
