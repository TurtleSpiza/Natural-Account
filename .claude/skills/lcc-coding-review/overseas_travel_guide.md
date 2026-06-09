# LCC Travel & Accommodation Guide

Source: Chart of Accounts PDF, page 72 (Overseas Travel Guide) and PDF page 51-52 (travel account descriptions).
Authority: Local Government Regulation 2012 s.196.

The travel account taxonomy is location-driven. The destination of the travel decides the account, not the supplier or the trip purpose.

## Account taxonomy

| Account | Title | Scope | GST |
|---------|-------|-------|-----|
| **73531** | Local Travel (SEQ) Cabcharge / Parking | Local taxi fares and parking fees within South East Queensland. Excludes tolls (73535), interstate taxi (73533), overseas taxi (73534). | C |
| **73532** | Intrastate Travel and Accommodation | All travel and accommodation within Queensland. | C |
| **73533** | Interstate Travel and Accommodation | All travel and accommodation within Australia, excluding local travel in SEQ (73531) and travel/accommodation in Queensland (73532). | C |
| **73534** | Overseas Travel & Accommodation | All expenses related to overseas travel and accommodation. | C |
| **73535** | Tollway Charges | Toll charges incurred by Council (Motorway Qld invoices). | C |
| **73541** | Conferences & Seminar Fees | Conference registration fees only. **Travel and accommodation are separate** — coded to the 73531-73534 series above. | C |

## Decision rule

Where did the travel happen?

1. **In SEQ?** → 73531 if it's just cabcharge/parking; 73532 if it's overnight or includes accommodation in Queensland.
2. **In Queensland (outside SEQ)?** → 73532 (Intrastate).
3. **In Australia but outside Queensland?** → 73533 (Interstate).
4. **Outside Australia?** → 73534 (Overseas).
5. **A toll charge?** → 73535 regardless of where in Australia.

## Meals during travel — separate rule

> **Meals consumed while undertaking travel should be costed according to the Hospitality & Entertainment Guide and should not be costed to the accounts above.**

This is the trap most often missed. A breakfast in a Brisbane hotel during an interstate trip is not 73533. It is one of:

- 73512 Entertainment & Hospitality Non-FBT — if a working breakfast on a meeting day, Reason A or B.
- 73511 Entertainment & Hospitality FBT — if alcohol is involved or it's a social/elaborate meal, Reason C.
- Apply Reason H if borderline (see `fbt_reason_codes.md`).

Hotel **room** charges and the **flight/train/cab** to get there are 73531-73534 by destination. The food is 73511/73512 by FBT classification.

## Conference costs are split

A typical external conference incurs four cost streams. Each goes to a different account:

| Cost stream | Account |
|-------------|---------|
| Registration fee | 73541 (Conferences & Seminar Fees) |
| Travel to venue | 73532/73533/73534 by destination |
| Accommodation | 73532/73533/73534 by destination |
| Meals during the conference | 73511 or 73512 per Hospitality Guide |

Internal-government workshops are different — see `hospitality_scenarios.md` scenario 8 (73512/7B222) and scenario 9a (73544 for external training).

## Overseas travel — LGR 2012 s.196 reporting

For every overseas trip, Council must capture:

1. The **employee** who undertook the overseas travel.
2. The **position held** by that employee.
3. The **destination** of the overseas travel.
4. The **purpose** of the overseas travel.
5. The **cost** of the overseas travel.
6. **Any other detail** about the overseas travel the local government considers relevant in accordance with reporting procedures.

A cover slip or memo with this information must travel with every 73534 transaction. Without it, the line cannot be cleared.

## Common confusion pairs

| Confusable pair | Distinguish by |
|-----------------|----------------|
| 73531 vs 73533 | 73531 is SEQ taxi/parking only. Sydney taxi is 73533. |
| 73533 vs 73534 | 73533 = interstate within Australia. 73534 = overseas only. Don't combine. |
| 73531 vs 73535 | 73531 is taxi/parking. 73535 is toll charges (Motorway Qld). Even if the toll was incurred during a SEQ trip. |
| 73541 vs 73544 | 73541 is conference/seminar registration fees. 73544 is training & development (broader, includes courses, certifications, professional development that isn't a conference). |
| 73541 vs travel account | 73541 is registration only. The travel and accommodation portions never go to 73541. |
| Travel account vs 73511/73512 | Travel accounts cover transport and accommodation. Meals during travel are 73511/73512 per the Hospitality Guide. |

## Operational rules

1. **Destination decides the account**, not the supplier (Webjet, Flight Centre, Qantas, Uber).
2. **Meals are never 73531-73534**, ever. Always 73511/73512 with a reason code.
3. **Tollway charges are 73535**, separate from cab/parking.
4. **Conference registration is 73541** only; the travel portions split out.
5. **Overseas trips need s.196 documentation** on the cover slip.

## Cross-references

- `accts.json` and `full_chart_of_accounts.json` — full descriptions of 73531, 73532, 73533, 73534, 73535, 73541, 73544.
- `hospitality_scenarios.md` — for the meals-during-travel allocation.
- `fbt_reason_codes.md` — for Reason H assessment on meal-during-travel borderline cases.
- `evidence_tier_checklist.md` — Tier 1 sighting standard for cover slips on 73534.
