# LCC Hospitality & Entertainment Scenarios

Source: Chart of Accounts PDF, page 68 (Hospitality & Entertainment Guide allocation table).
Authority: FBT Act and Local Government Regulation 2012 s.196.
Method: Council uses the 50/50 method for meal entertainment FBT.

The table below has been designed to cater for Fringe Benefits Taxation (FBT) and Local Government Regulation (LGR) 2012 section 196. Council has a legal obligation to comply with the FBT Act and the LGR. Refer any concerns to the Finance Branch (FinancialAccounting@logan.qld.gov.au).

## Allocation table

| # | Scenario | Account | Reason | GST | FBT? |
|---|----------|---------|--------|-----|------|
| 1 | Art Gallery Openings / Citizenship Ceremony / Open Day / Media Launches / Opening of Facilities, e.g. new library — Hospitality | 73512 / 7B222 | A | C | No |
| 2 | Author Visits — morning tea | 73512 | A or B | C | No |
| 3 | Children's Activities / Parties / Book Club — Snacks | 73512 | A | C | No |
| 4 | Honorary Park Rangers & Bush care group functions — BBQ | 73511 | C | P | Yes |
| 5a | Flowers / Cards / Gifts — Employee Reward and Recognition < $300 | 73513 / 7B222 | D | C | No |
| 5b | Flowers / Cards / Gifts — Employee Reward and Recognition ≥ $300 | 73513 / 7B221 | E | C | Yes |
| 5c | Flowers / Cards / Gifts — Non-Employee | 73553 | K | C | No |
| 6 | Staff Morning Tea / Afternoon Tea | 73512 | B | C | No |
| 7 | Christmas Party (All costs e.g. Karaoke) / Gala Dinners | 73511 | C | P | Yes |
| 8 | Workshop / Seminar / Course / Conference provided by the local government | 73512 / 7B222 | F | C | No |
| 9a | Workshop / Courses provided by an external organisation | 73544 | F | C | No |
| 9b | Seminars / Conferences provided by an external organisation | 73541 | F | C | No |
| 10 | Entertainers for Events e.g. Carols by Candlelight | 73515 | L | C | No |
| 11 | Conference Meals — Employees Only | 73512 | A | C | No |
| 12a | Staff retirement / farewell — Morning/Afternoon Tea & nibbles | 73512 / 7B222 | B | C | No |
| 12b | Staff retirement / farewell — Lunch / Dinner | 73511 / 7B221 | C | P | Yes |
| 13 | Lunches — customer meetings / consultants / formal off-site meetings / Working Lunches — ELT & special project groups | 73511 or 73512 (apply Reason H) | H | P | depends |
| 14 | Formal off-site and on-site meetings for external and internal attendees | 73511 or 73512 (apply Reason H) | H | P | depends |
| 15 | Refreshments / lunches etc. for visiting Dignitaries | 73512 | G | C | No |
| 16 | Refreshments — ELT — includes alcohol | 73511 | C | P | Yes |
| 17 | Annual ELT / Stream / Mgt Team lunches | 73511 or 73512 (apply Reason H) | H | P | depends |
| 18 | Business Breakfasts / Networking Events | 73511 or 73512 (apply Reason H) | H | C | depends |
| 19a | Employee Functions & Awards — Lunch or dinner | 73514 / 7B223 | D or E | C | Yes |
| 19b | Employee Functions & Awards — Year of Service Gift Cards | 73514 / 7B223 | I or J | NA | depends |

## Quick decision rules

Three signals push a transaction from 73512 (Non-FBT) to 73511 (FBT):

1. **Off-site venue.** Anything off Council premises trends 73511.
2. **Alcohol present in any form.** Wine, beer, spirits → 73511.
3. **Social/recreational element.** Christmas party, gala dinner, BBQ for community group, ELT social → 73511.

If none of those three apply, default to **73512** with the relevant Reason A, B, F, or G.

## Reason H 4-factor assessment

For ambiguous cases (scenarios 13, 14, 17, 18), apply Reason H:

| Factor | 73512 likely | 73511 likely |
|--------|--------------|--------------|
| Purpose | Refreshment (light lunch, teas) | Social |
| Type of food/drink | Tea / light / finger lunch | Elaborate meal / alcohol |
| When | During work / overtime | Outside work |
| Where | On business premises | Off-site / function room |

Single 73511 trigger across any factor pushes the whole event to 73511.

## Internal catering (LEC, Logan Metro InSports)

Where catering is provided by Council owned and operated facilities:

- **7B221** — catering that incurs FBT
- **7B222** — catering that does not incur FBT

The 7Bxxx pair shadows the 73511/73512 pair for internal sourcing.

## Cross-references

- `fbt_classification.json` — machine-readable form of this table.
- `fbt_reason_codes.md` — full Reason A-L definitions with 4-factor Reason H breakout.
- `fbt_data.json` — operational allocation lookup (24 keyed entries used by the AI tool).
- `fbt_5050_batch_identifiers.md` — Finance 50/50 batch detection (do not treat batch movements as miscodes).
- `confusion_pairs.json` — 73511 vs 73512 side-by-side examples.
