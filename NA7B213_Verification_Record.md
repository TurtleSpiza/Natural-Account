# NA7B213 Verification Record — Internal Medical Services (Immunisation)

**Register row**

| Field | Value |
|---|---|
| Account | 7B213 Internal - Medical Services |
| Workstream | NA7B213 Immunisation svc-PK split, FY26 26SLACT |
| Period in scope | P2 to P12 FY26 (13-Aug-2025 to 12-Jun-2026) |
| Dollars in scope (ex-GST) | $4,861.70 over 70 lines |
| Overall RAG | AMBER |
| Recode staged | $3,799.50 reallocated, 17 pairs, net $0.00 |
| Evidence location | This record; NA7B213_GENJNL_Recode.txt |
| Prepared | 16-Jun-2026 |

## 1. What this account is

7B213 is the internal recharge for immunisation, vaccination and pathology services provided to staff. Each export line is a per-employee charge raised on an internal journal (IJ072836 to IJ074855). The natural account (7B213) and the per-line amounts are not in dispute. The defect is the PK the cost lands on.

## 2. Reconciliation

Export sums to $4,861.70 ex-GST across 70 lines. Not yet tied to SE2 to the cent in this session. No account-level GREEN until SE2 agreement is confirmed.

Split of the $4,861.70:

| Bucket | Lines | Amount |
|---|---|---|
| Parks employees, reallocated to home PK | 56 | $3,799.50 |
| Parks Natural Areas, already on correct PK000432 (James Lloyd-Jones, Renee Hoyle) | 5 | $420.30 |
| Parks, held pending section (Arno Schneider) | 2 | $121.00 |
| Off-branch employees (not Parks) | 4 | $520.90 |
| Total | 70 | $4,861.70 |

## 3. Root cause (Limb 1, PK attribution)

The immunisation working paper Internal_Medical.XLSM, sheet "Lookup Values" row 23, maps the entire 4090000 Parks branch to a single ledger line PK000432-7B213. PK000432 is service 20318, Natural Areas Environment Levy Coord & Admin. Every Parks employee's immunisation charge is therefore posted to Natural Areas regardless of the employee's actual section. Every other directorate in that lookup carries its own distinct code; Parks is the only branch collapsed onto one section PK.

Confirmed against the export: every line carries Service No 20318, Section 4090220, Account 1-20318-7B213. Three named employees (Isabel Howard, James Lloyd-Jones, Renee Hoyle) are genuinely Natural Areas; the remaining Parks staff are not.

## 4. Recode (staged, held, not posted)

Format is a PK ledger split-PK recode. Natural account 7B213 is unchanged on every line; only the PK moves. For each employee the source leg credits PK000432 (negative) and the destination leg debits the home PK (positive). Batch nets $0.00. Source PK000432 signed sum in the journal is -$3,799.50, matching the stated reclassified total. Every line passed pk_validator (PK exists, service matches, 7B213 valid and unrestricted) and the 40-character narration cap.

| Employee | Move | Home PK | Section | Amount |
|---|---|---|---|---|
| Dale Mckenzie | 432 to PK000003 | PK000003 | Park Maintenance | $261.00 |
| Guy Carkeet | 432 to PK000003 | PK000003 | Park Maintenance | $313.00 |
| Henry Fusi | 432 to PK000003 | PK000003 | Park Maintenance | $82.00 |
| Jason Fourmile | 432 to PK000003 | PK000003 | Park Maintenance | $443.30 |
| Adam Goodsir | 432 to PK000012 | PK000012 | Park Maintenance | $26.00 |
| Benjamin Tabuwaitui | 432 to PK000012 | PK000012 | Park Maintenance | $58.00 |
| Graeme Gray | 432 to PK000012 | PK000012 | Park Maintenance | $84.00 |
| Gregory Cavell (Spero) | 432 to PK000012 | PK000012 | Park Maintenance | $82.00 |
| Mario Fuentes | 432 to PK000012 | PK000012 | Park Maintenance | $230.30 |
| Oliver Mueller | 432 to PK000012 | PK000012 | Park Maintenance | $432.30 |
| Sonya Karlsson (Spero) | 432 to PK000012 | PK000012 | Park Maintenance | $82.00 |
| Christian De Leon (Spero) | 432 to PK000084 | PK000084 | Park Services, Rangers | $82.00 |
| Isabel Howard | 432 to PK000431 | PK000431 | Natural Areas | $192.00 |
| Shane Morris | 432 to PK000433 | PK000433 | Trees | $315.00 |
| Dominic Unwin | 432 to PK000435 | PK000435 | Park Services | $371.00 |
| Darren Bester | 432 to PK000439 | PK000439 | Cemeteries | $459.30 |
| Lachlan Peebles | 432 to PK000439 | PK000439 | Cemeteries | $286.30 |
| Total reallocated | | | | $3,799.50 |

After posting, PK000432 retains $541.30: James Lloyd-Jones $338.30 and Renee Hoyle $82.00 (correctly Natural Areas) plus Arno Schneider $121.00 (held).

Spero-instructed placements (Sonya Karlsson PK000012, Christian De Leon PK000084, Gregory Cavell PK000012) are prepared journal-ready per the standing directive. Sonya and Gregory are not on the EOM People and Positions extract (ingest_anchor 05-Jun-2026); Christian is resolved to PK000084 Parks and Bushland Rangers. These three carry no roster line, so the placement rests on Spero's instruction, not the crosswalk.

## 5. Held and outstanding (not in this recode)

1. Arno Schneider, $121.00, IJ074595 (DTPa and Blood Test). Not on the roster, section not advised. Stays on PK000432 until the section is confirmed. Flagged, not journalled.
2. Off-branch employees, $520.90, do not belong on Parks 7B213 at all. Jennifer Harley (Plant Fleet 2070000) $82.00; Zhi Cai (Water 6110000) $146.30; Anna-Marie Higgins (City Standards 4020000) $146.30 x2. These are cross-branch corrections (SL ledger, full account string), not Parks-to-Parks moves, so they sit outside this PK recode and need Finance to action the cross-branch leg.
3. Duplicate inside item 2: Anna-Marie Higgins, Q Fever Initial, 23-Jul-2025, $146.30, posted twice on IJ073052. One line is a duplicate to be reversed.

## 6. Source fix (or the defect recurs monthly)

The recode corrects FY26 to date. The recurring cause is the single PK000432-7B213 Parks line in Internal_Medical.XLSM "Lookup Values" row 23. Replace it with a per-section Parks lookup (Park Maintenance PK000012 / PK000003, Cemeteries PK000439, Park Services PK000435, Trees PK000433, Natural Areas PK000431 / PK000432, Rangers PK000084) keyed on the employee, or every future immunisation IJ repeats this miscode.

## 7. Four-limb status

- Limb 1 PK/service: corrected by this recode for 56 lines; 2 lines held (Arno); 4 lines off-branch. AMBER until Arno and the off-branch leg clear.
- Limb 2 natural account: 7B213 confirmed correct for all Parks lines. GREEN.
- Limb 3 evidence: no immunisation IJ source documents sighted. Recorded as a GAP. Limb stays AMBER. Unsighted sources: IJ072836, IJ073052, IJ073262, IJ073453, IJ073639, IJ073756, IJ073940, IJ074226, IJ074372, IJ074595, IJ074855.
- Limb 4 tax: not assessed; internal recharge, no external tax invoice in scope this session. AMBER.

Overall AMBER. The split-PK recode is staged and arithmetically clean; the account does not clear to GREEN while evidence is unsighted, Arno is unplaced, and the off-branch and duplicate items are open.
