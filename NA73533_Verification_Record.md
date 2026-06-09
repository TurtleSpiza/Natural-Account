# NA 73533 Interstate Travel & Accommodation, Verification Record

Batch CN-23167. Reviewed 9-Jun-2026. Section 4090000, FY26 (26SLACT), Period 1-12.
Ledger export reconciles to 8 lines, total $1,021.70 ex-GST (footer $1,021.70, matched).
Single traveller, single trip: Kirsty Quinn, Brisbane to Melbourne and return, svc 20151 PK000001.

Verdict: GREEN (revised 9-Jun-2026, see final addendum). $1,015.15 (99.4%) confirmed correctly coded to 73533. The $6.55 7-Eleven line is now sighted as a meal during travel and recoded to 73512 (posted). The hotel GST substantiation is waived by Spero. The body below records the AMBER pass; the closing addendum carries the current GREEN state.

## Account composition

Eight lines, all on 1-20151-73533, all the one Quinn BNE-MEL-BNE trip in Jan-2026.

| Line | Reference | Detail | Ex-GST |
|---|---|---|---|
| Airfare | TE005128 | Qantas BNE-MEL-BNE | $509.93 |
| Accommodation | TE005080 | Booking.com Melbourne hotel | $288.18 |
| Ride | 21012026 | Uber to Qantas lounge (Melbourne) | $137.85 |
| Taxi | INV0000315295 | Cabcharge Melbourne hotel-to-hotel (two legs $3.76 + $57.06) | $60.82 |
| Booking fees | TE005128 | CTM booking + segment fees ($9.09 + $9.28) | $18.37 |
| Sundry | TE005080 | 7-Eleven general expenses | $6.55 |

73533 test: interstate travel and accommodation, the destination being interstate (not SEQ, not intrastate Queensland). Brisbane to Melbourne is interstate, so the airfare, the Melbourne accommodation, the Melbourne taxi and the booking fees all sit correctly in 73533. The non-negotiable travel destination rule places meals during travel in 73511 or 73512 by FBT classification, never in the 73531-73534 series, which is the only question the $6.55 raises.

## Four limbs (account level)

- L1 PK GREEN. PK000001 svc 20151 Parks Leadership and Administration. pk_validator VALID. All eight lines.
- L2 NA GREEN for $1,015.15. The five travel components are interstate travel and accommodation and sit correctly in 73533. AMBER for the $6.55 7-Eleven sundry: if the receipt shows food or drink it is a meal during travel and recodes to 73511 or 73512 by FBT classification; if a non-meal sundry it stays in 73533.
- L3 Evidence GREEN for $1,015.15, AMBER for $6.55. Airfare and segment fees on the CTM tax invoice (I0022860955). Accommodation and approvals in the travel support pack. Melbourne taxi on the Cabcharge tax invoice INV0000315295. The Uber $137.85, which previously carried no valid receipt, is now substantiated by the Uber ride-detail and activity screenshots and the Quinn Bankwest statement header showing the matching debit, which closes the one item that was open on this account. The 7-Eleven receipt behind the $6.55 is still outstanding.
- L4 Tax GREEN. All lines under the $1,000 tier. Airfare, accommodation and taxi are standard GST-registered travel suppliers (Qantas, Booking.com, Cabcharge); the Uber is an AP reimbursement to the traveller substantiated by the bank debit. No ABN or GST-math exception arises at this materiality. The $6.55 7-Eleven tax position is moot until the receipt is sighted.

## Account reconciliation

Ledger total $1,021.70 ex-GST = footer $1,021.70. Confirmed correct in 73533: $1,015.15 (five components). Held pending receipt: $6.55. Nothing recodes out of 73533 on the confirmed lines.

## Recode (none posted)

No recode is required for the confirmed $1,015.15. A contingent two-line pair for the $6.55 7-Eleven is drafted but not posted, pending the receipt and FBT classification. See NA73533_GENJNL_Recode.txt.

## Overall RAG

GREEN (revised 9-Jun-2026, see final addendum). At the original pass this was AMBER pending the 7-Eleven receipt. The receipt is now sighted (valid tax invoice, a meal), the $6.55 is recoded to 73512 (posted), and the hotel GST is waived by Spero, so all four limbs clear.

## Open actions

1. Sight the 7-Eleven receipt behind TE005080 $6.55. If food or drink, post the contingent recode to 73511/73512 by FBT classification; if a non-meal sundry, close in 73533.

## Method notes

- 73533-versus-73531/73532 call made on the non-negotiable travel destination rule (73531 local SEQ, 73532 intrastate Qld, 73533 interstate) and the lcc-coding-review overseas_travel_guide. Brisbane to Melbourne is interstate.
- Meals-during-travel exception applied to the $6.55 only: the travel series never carries meals; they go to 73511/73512 by FBT classification.
- Separate travel streams touching 73531/73532 (the Cabcharge multi-traveller airport legs, the Gold Coast parking) are not part of this account and are tracked separately; they need per-traveller PK and home-PK data before any recode.

---

## Addendum, 9-Jun-2026 (TE005080 backup sighted; tax limb reopened)

The TE005080 backup has been sighted. Two clarifications and one downgrade follow.

- **TE005080 is one PCard reference over two ledger lines, not one.** Line L07 is the Booking.com accommodation $288.18 ex-GST (14-Jan-2026); line L02 is the 7-Eleven sundry $6.55 (20-Jan-2026). The "7-Eleven" identity comes from the booked Details narration on L02 ("7-ELEVEN 1130-General Expenses-Purchase Card Reconciliations"), not from any receipt.
- **The hotel backup is now filed** (NA73533_L07_BookingCom_ibis_TE005080.pdf): Booking.com confirmation and receipt, ibis Melbourne Central, K Quinn, 20 to 21-Jan-2026, $317 incl ($288.18 + $28.82 at 10%).
- **Tax limb downgraded GREEN to AMBER.** The Booking.com document carries no ABN and states in terms that it is not a tax invoice and cannot be used to claim GST. At $317 incl the council needs a valid tax invoice to claim the $28.82 credit. The supplier of record is the property (ibis Melbourne, Accor), which must issue it. The coding (interstate, svc 20151 / PK000001) is unaffected; this is purely substantiation.
- **The 7-Eleven $6.55 receipt remains outstanding.** Confirmed not present in the TE005080 backup.

Revised open actions: (1) obtain the ibis Melbourne (Accor) tax invoice for the $288.18 accommodation, or treat the $28.82 GST as non-claimable; (2) sight the 7-Eleven $6.55 receipt (a travel-day 7-Eleven buy is most likely a meal and would recode to 73511/73512), or close on de minimis at $6.55 (0.6%). Overall remains AMBER.

**GST status (Limb 4, per-line).** The ibis accommodation books at $288.18 ex, asserting a $28.82 input tax credit, but the Booking.com document carries no ABN and states it is not a tax invoice; as an offshore booking-agent supply the credit is unsubstantiated and likely non-claimable until an Accor/ibis Australian tax invoice is sighted. The 7-Eleven $6.55 is unsighted and is a probable mixed supply carrying GST-free food, so its booked GST is unconfirmed. Qantas (TE005128), Cabcharge (INV0000315295) and the CTM fees are standard-rated and reconcile; the Uber is an AP reimbursement substantiated by the bank debit. GST status AMBER on the two PCard lines, GREEN on the rest.

---

## Addendum, 9-Jun-2026 (7-Eleven receipt sighted; recode posted; hotel GST waived by Spero)

Both open items on TE005080 are now closed and the account clears to GREEN.

- **7-Eleven receipt sighted and is a valid tax invoice.** NA73533_L02_7Eleven_TE005080.pdf: 7-Eleven 1130 Melb Queen St, ABN 86 960 363 023 (checksum PASS), the document is headed TAX INVOICE, dated 20-Jan-2026 19:07 during the Quinn Melbourne trip, one HAM PESTO SANDWICH $7.20 incl, GST $0.65, ex-GST $6.55. The cover slip (K Quinn, cardholder Kirsty Quinn) describes it as "Dinner/Breakfast". GST reconciles to the cent ($6.55 x 1.1 = $7.205, booked $6.55 ex, GST $0.65). Evidence and tax limbs on L02 GREEN.
- **The $6.55 is a meal during travel and recodes to 73512, posted.** A meal never sits in the 73531-73534 series. A sole-traveller sandwich with no alcohol, no social function, consumed during the work trip, is light refreshment, Reason B, so it moves to 73512 Entertainment & Hospitality Non-FBT (not 73511: no FBT trigger on the four-factor test). The contingent pair is now posted in NA73533_GENJNL_Recode.txt: 73533 -6.55 credit, 73512 +6.55 debit, nets $0.00, direction verified. Limb 2 on L02 was a confirmed miscode, now resolved by the recode.
- **Hotel GST substantiation waived by Spero (directive 9-Jun-2026).** The Booking.com accommodation ($288.18 ex, $28.82 GST) carries no ABN and states it is not a tax invoice. Spero has directed the line be accepted on the Booking.com confirmation as-is rather than holding for an ibis/Accor Australian tax invoice. Recorded as an explicit waiver under the four-limb standard (only Spero may waive evidence). Residual exposure noted: the $28.82 input tax credit is claimed without a compliant tax invoice, which is an ATO substantiation risk if the credit is ever reviewed; the room coding (interstate, 73533) is unaffected and correct. Tax limb on L07 cleared GREEN on the waiver.

**Revised limbs.** L1 PK GREEN. L2 NA GREEN ($1,015.15 correct in 73533; the $6.55 7-Eleven miscode resolved by the posted 73512 recode). L3 Evidence GREEN (all lines sighted). L4 Tax GREEN (7-Eleven valid tax invoice; hotel GST accepted on Spero's waiver; remainder standard-rated). **Overall RAG: GREEN.**

**Revised open actions:** none gating the account. Advisory only: if convenient, obtain the ibis Melbourne (Accor) tax invoice to retire the $28.82 ITC exposure noted above.
