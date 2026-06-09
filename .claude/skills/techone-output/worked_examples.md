# Worked Examples — TechOne GENJNL Recode Journals

Twenty-five recode journals from the P10 FY2025-26 branch coding review, totalling $33,192.04 in confirmed quantum and $27,878.95 in Dr movements. Each example shows the input miscoding, the journal lines that recode it, and the validation that confirmed the recode.

## Column structure

The TechOne GENJNL upload format expects these columns. Order matters.

| Col | Header | Width | Notes |
|---|---|---|---|
| A | LDG | 3 | `PK` for Parks ledger, `SL` for Sales/SL ledger (cross-branch corrections) |
| B | Account number | varies | PKNumber for PK ledger (e.g. `PK000017`), or full account string for SL ledger (e.g. `1-18611-73564`) |
| C | Fund account | varies | Mirrors col B for PK ledger; same as col B for SL ledger |
| D | Resource Group Code | 7 | Always `JOURNAL` for recode journals |
| E | Resource Code | 5 | Natural account, e.g. `73126` |
| F | Amount | numeric | Dr positive, Cr negative. Sign convention matters. |
| G | Narrative1 | 40 | First narrative field |
| H | Narrative2 | 40 | Second narrative field |
| I | Narrative3 | 40 | Third narrative field |

For natural-account recodes (where the cost centre stays the same but the natural account changes), col B / col C / col E carry the recode mechanics. The PK ledger uses the PKNumber to identify the cost centre. The SL ledger uses the full account string.

## Example 1 — Cost centre correction within 7B411

**Issue:** Anita Moore laptop $1,699 posted to cost centre 20374 (Park Maintenance) but Anita is in cost centre 20001 (Parks Branch Management). 7B411 (Internal IT Equipment) is the correct natural account.

**Recode:** Move $1,699 from svc 20374 to svc 20001, both in 7B411.

```
LDG | Account num | Fund account | Resource Grp | Resource Code | Amount  | Narrative1                          | Narrative2                       | Narrative3
PK  | PK000035    | PK000035     | JOURNAL      | 7B411         | -1699.00| Anita Moore laptop reversal         | Reverses 7B411 svc 20374 incorrec | IT batch correction P10 FY26
PK  | PK000087    | PK000087     | JOURNAL      | 7B411         |  1699.00| Anita Moore laptop                  | Correct svc 20001 Parks Branch Mg | IT batch correction P10 FY26
```

(PK000035 = Park Maintenance per service map; PK000087 = Parks Branch Management.)

## Example 2 — Cross-branch correction (SL ledger)

**Issue:** Naomi English laptop $1,699 posted to Parks branch 4090000 svc 20191. English is an LCI employee, not Parks. The cost belongs in LCI branch 18611.

**Recode:** Reverse from Parks PK ledger, post to LCI SL ledger using full account string.

```
LDG | Account num         | Fund account        | Resource Grp | Resource Code | Amount   | Narrative1                          | Narrative2                       | Narrative3
PK  | PK000082            | PK000082            | JOURNAL      | 7B411         | -1699.00 | Naomi English laptop reversal       | LCI employee posted to Parks      | Cross-branch correction
SL  | 1-18611-73564       | 1-18611-73564       |              |               |  1699.00 | Naomi English laptop                | Correct LCI branch 18611 73564    | Cross-branch correction
```

Note SL ledger entries don't carry Resource Group Code or Resource Code — the natural account is encoded in the full account string `1-18611-73564`. This matches the canonical SL ledger format.

## Example 3 — Natural account recode within same cost centre

**Issue:** Blue card fee $80 posted to 73544 (Training & Development). Blue cards are fees, not training, so belong in 73433 (Other Fees & Charges).

**Recode:** Move $80 from 73544 to 73433, same cost centre.

```
LDG | Account num | Fund account | Resource Grp | Resource Code | Amount  | Narrative1                          | Narrative2                       | Narrative3
PK  | PK000084    | PK000084     | JOURNAL      | 73544         | -80.00  | Blue card fee reversal              | Misc to 73544; belongs in 73433   | Branch coding review P10
PK  | PK000084    | PK000084     | JOURNAL      | 73433         |  80.00  | Blue card fee Other Fees & Charges  | Recode from 73544 Training        | Branch coding review P10
```

## Example 4 — Software licence recode

**Issue:** Canva Pro $18.18 and VisitUs Reception SaaS $1,249 posted to 73543 (Reference Materials and Subscriptions). LCC chart definition restricts 73543 to magazines/newspapers/books/electronic information. Software licences belong in 73566 (IT Software Licence Fees).

**Recode:** Two pairs of journal lines, one per item.

```
LDG | Account num | Fund account | Resource Grp | Resource Code | Amount    | Narrative1                          | Narrative2                       | Narrative3
PK  | PK000087    | PK000087     | JOURNAL      | 73543         |   -18.18  | Canva Pro reversal                  | SaaS not 73543 Reference Material | Recode to 73566
PK  | PK000087    | PK000087     | JOURNAL      | 73566         |    18.18  | Canva Pro IT Software Licence       | Recode from 73543                 | Branch coding review P10
PK  | PK000087    | PK000087     | JOURNAL      | 73543         | -1249.00  | VisitUs Reception SaaS reversal     | SaaS not 73543 Reference Material | Recode to 73566
PK  | PK000087    | PK000087     | JOURNAL      | 73566         |  1249.00  | VisitUs Reception IT Software Lic   | Recode from 73543                 | Branch coding review P10
```

## Example 5 — Cemetery refund recode

**Issue:** Iakopo $3,199.09 cemetery deposit refund posted to 73421 (Rates & Charges Paid). 73421 is for payments to external authorities (rates, fire levy). Customer deposit refunds belong in 73412 (Refund of Operational Contributions).

**Recode:**

```
LDG | Account num | Fund account | Resource Grp | Resource Code | Amount   | Narrative1                          | Narrative2                       | Narrative3
PK  | PK000402    | PK000402     | JOURNAL      | 73421         | -3199.09 | Iakopo cemetery deposit refund rev  | Customer refund not auth payment  | Recode to 73412
PK  | PK000402    | PK000402     | JOURNAL      | 73412         |  3199.09 | Iakopo cemetery deposit refund      | Refund of operational contribution| Recode from 73421
```

## Example 6 — Travel account split

**Issue:** Quinn Cabcharge Ormiston→Brisbane Airport $199.32 posted to 73532 (Intrastate Travel). Brisbane Airport is in SEQ, so this is local travel — belongs in 73531 (Local Travel SEQ).

**Recode:**

```
LDG | Account num | Fund account | Resource Grp | Resource Code | Amount  | Narrative1                          | Narrative2                       | Narrative3
PK  | PK000002    | PK000002     | JOURNAL      | 73532         | -199.32 | Quinn Cabcharge SEQ travel reversal | Brisbane Airport is SEQ local     | Recode to 73531
PK  | PK000002    | PK000002     | JOURNAL      | 73531         |  199.32 | Quinn Cabcharge Ormiston-BNE Airpt  | Recode from 73532 Intrastate      | Branch coding review P10
```

## Patterns across the 25 recodes

### Pattern A: cost centre correction (same NA)
- Anita Moore $1,699 — 20374 → 20001 (7B411)
- A-M King laptop 1 $1,699 — 20191 → 20151 (7B411)
- A-M King Adobe CC $1,464 — 20191 → 20151 (7B411)
- A-M King laptop 2 $1,699 — 20001 → 20151 (7B411)
- Fiona Perry $460 — 20151 → 20141 (7B411)
- Jill Provins $320 — 20001 → 20141 (7B411)

Six examples. Same NA throughout. Two journal lines per recode (reverse and re-post).

### Pattern B: cross-branch SL ledger correction
- Naomi English $1,699 — Parks PK000082 → LCI SL `1-18611-73564`

One example. PK ledger reversal + SL ledger post.

### Pattern C: natural-account recode (same cost centre)
- Blue card fee 73544 → 73433
- ACDC electrical licence 73544 → 73433
- Preussner ENVR1001/CHEM1001/STAT1002 73544 → 73545
- Empire chair 73544 → 72313
- Canva Pro 73543 → 73566
- VisitUs SaaS 73543 → 73566
- Bushcare water cart 72411 → 74114
- Iakopo cemetery refund 73421 → 73412
- Tankei cemetery refund 73421 → 73412
- Hospitality items 73513 → 73511 or 73512 (multiple lines)

Most common pattern. Reverse from wrong NA, post to correct NA.

### Pattern D: travel account split
- Quinn Cabcharge $199.32 — 73532 → 73531
- Gold Coast parking $6.05 — 73541 → 73531

Two examples.

## Validation steps before submission

1. Run `narrative_field_validator.py` on every narrative field — confirm 40-char cap not exceeded
2. Run `pk_validator.py` on every line — confirm PK exists, PK matches service code, NA is valid and not restricted
3. Confirm Dr/Cr signs balance — sum of all amounts in a journal batch must equal zero
4. Confirm each recode has both halves (reversal AND re-post)
5. Cross-check destination NA against `full_chart_of_accounts.json` (also at `_shared/lcc_chart_of_accounts.json`) for restrictions
6. Stage all journals on a single workbook sheet ready for Finance upload — never drip-feed
