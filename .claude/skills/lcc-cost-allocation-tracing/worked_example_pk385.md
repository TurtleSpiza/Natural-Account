# Worked Example — PK385 Urban Bushland Allocation Trace

The canonical case study for cost allocation tracing. PK385 is a passthrough PK that receives zero direct vendor invoices but carries an annualised $263,000 of operational spend, all delivered via journal splits from holding account 1-20276-73126.

This document is the full investigation trail from "$10,808 reported overspend" to "$140,246 annualised overcharge with no vendor basis." Use it as the template for any future passthrough investigation.

## Source data

- Service code: 20681 Urban Bushland Maintenance
- Work order: PK000385
- Section: Natural Areas (4090220)
- Annual budget: $164,950
- YTD P1-9 actual: $98,699
- YTD actual P1-10: $175,758
- Year-end projection (uncorrected): $263,000
- Year-end projection (corrected): $145,780

## The cost flow — five steps

### Step 1: Vendor invoices LZ6

Austspray and Glascott bill Council monthly for whole-zone landscape maintenance under contracts PAR/338A/2025 (Austspray LZ6), PAR/338B/2025 (Glascott LZ3), PAR/338C/2025 (Glascott LZ5). Each invoice is a single lump sum per zone.

**No vendor invoice has an Urban Bushland line. No vendor invoice references PK000385.**

The Austspray LZ6 invoice (e.g. INV-157860) reads: "PK000473 Parks/Roads $73,432.77 plus gst" — Austspray considers the entire amount a Parks/Roads cost.

### Step 2: Lump sum lands in holding account

At receipt, the full invoice posts to Parks Maintenance holding account `1-20276-73126` as a single lump sum.

### Step 3: Parks Maintenance posts split journal

Each month a Parks Maintenance officer posts a GJ that splits the invoice across destination services using fixed dollar values from the Green Maintenance Budget Tracker (DM# 17767639).

**Confirmed via journal GJ078805 (07-Apr-26)** tracing Austspray invoice INV-157860 ($73,432.77 ex GST):

```
Credit  1-20276-73126 holding:        -$73,432.77
Debit   1-20376-73126 LZ6 works:       $59,439.74  (81%)
Debit   1-20681-73126 Urban Bushland:  $13,993.03  (19%)
```

Same pattern confirmed for LZ1 invoice INV-157858 ($57,284.53 ex GST):

```
Credit  1-20276-73126 holding:        -$57,284.53
Debit   1-20374-73126 LZ1 works:       $42,256.88  (74%)
Debit   1-20276-73126 Main Roads:      $11,870.44  (21%)
Debit   1-20681-73126 Urban Bushland:   $3,157.21   (5.5%)
```

### Step 4: EOM accruals mirror the same fixed values

End-of-month accruals (RJ-prefix journals) book the same fixed values BEFORE the vendor invoice arrives. $13,993 accrued for LZ6 Urban Bushland every month regardless of invoice content.

This confirms the split is pre-set and not responsive to invoice content. The journal entries are a fixed allocation, not a calculated one.

### Step 5: PK385 carries the accumulated splits

Across all six zones, PK385 receives the aggregated split values:

| Zone | Tracker $/month | Annual |
|---|---|---|
| LZ1 | $3,157.21 | ~$37,887 |
| LZ2 | $3,454.08 | ~$41,449 |
| LZ3 | $0 | $0 |
| LZ4 | $213.25 | ~$2,559 |
| LZ5 | $1,104.66 | ~$13,256 |
| LZ6 | $13,993.03 | ~$167,916 |
| **Total** | **$21,922.23** | **~$263,067** |

## Two governance documents that don't reconcile

The investigation surfaced a fundamental disconnect.

### Urban Bushland Checklist (DM# 14719249)

Defines approved scope as 33 sites across 6 zones at **$12,148.36 per round ex GST**. Approved via a formal process: funding confirmed, email to Natural Areas, mapping layer updated, approval email saved. Excludes ovals, roadsides, landscaped garden beds (item 1.1).

### Green Maintenance Budget Tracker (DM# 17767639)

Allocates **$21,922.24 per month ex GST** to PK000385. Does not reference Checklist sites. Values are static month-to-month. This is what actually drives the GL posting.

### Reconciliation gap

| Metric | Checklist | Tracker | Gap |
|---|---|---|---|
| Per period | $12,148.36 / round | $21,922.24 / month | +$9,774 |
| Annualised | (depends on rounds/year) | $263,067 | +$117,288 |

**Nobody has reconciled these two documents.**

## Zone-by-zone reconciliation

| Zone | Sites | Checklist $/round | Tracker $/month | Variance | Annual variance |
|---|---|---|---|---|---|
| LZ1 | 13 | $4,717.96 | $3,157.21 | -$1,560.75 | -$18,729 (under) |
| LZ2 | 4 | $2,666.99 | $3,454.08 | +$787.09 | +$9,445 (over) |
| LZ3 | 2 | $770.44 | $0 | -$770.44 | -$9,245 (zero alloc) |
| LZ4 | minor | $349.28 | $213.25 | -$136.03 | -$1,632 (under) |
| LZ5 | minor | $1,337.83 | $1,104.66 | -$233.17 | -$2,798 (under) |
| LZ6 | 7 | $2,305.86 | $13,993.03 | +$11,687.17 | +$140,246 (over 6×) |
| **Total** | 33 | **$12,148.36** | **$21,922.24** | **+$9,773.88** | **+$117,288** |

LZ6 alone drives 94% of the overcharge. The other zones partially offset.

## The LZ6 problem in detail

Austspray invoices LZ6 at ~$72,000-$73,000/month under PAR/338A/2025. The invoice intends the full amount to hit PK000473. Parks Maintenance splits 81/19, so $13,993/month lands on PK385.

Approved Urban Bushland scope for LZ6 is $2,306/round across 7 Yarrabilba-area parks (Myrtle, Elwyn, Darlington, Tallwoods Corridor, Daybreak, Autumnfield, Sandstone — first two are in Veresdale Scrub and Jimboomba; the rest in Yarrabilba).

The 19% allocation implies 6× the approved scope every month with **no governance basis**. Applying the correct bushland scope ($2,306) as a percentage of the monthly LZ6 invoice ($72,194) would give 3.2%, not 19%.

### Three candidate explanations

1. **Scope expanded, Checklist not updated.** LZ6 Urban Bushland scope grew beyond 7 sites without the governance process being followed. If additional sites were approved via DM# 1144082-1, the Checklist is out of date. Approvals must exist in writing before sites are added.

2. **Non-bushland work coded as bushland.** Checklist item 1.1 explicitly excludes ovals, roadsides, landscaped garden beds. If LZ6 general landscape work is being allocated to PK385 in error, this is a mis-coding issue. The LZ6 zone includes significant non-bushland area.

3. **Green Tracker allocation percentage is wrong.** If the 19% was set in error (e.g. by applying a percentage of the total zone works invoice rather than the bushland-specific sites), the fix is a Tracker correction and YTD reversal.

Option three is most consistent with the data. The 19% does not correspond to any documented allocation basis.

## PK473 budget mask

PK000473 LZ6 zone works is already over budget. At P1-10 it was tracking at 102-114% of annual budget. The $13,993/month carve-out to PK385 reduces the visible overspend on PK000473.

Over 9-10 months that is approximately $105,000-$126,000 shifted from PK473 to PK385. **Corrected PK000473 position** (if LZ6 excess reversed back): approximately $581,654 YTD against $467,090 annual budget — **124% of budget**. That is the real LZ6 Parks Maintenance position being masked by the Green Tracker split.

The Tracker is reducing reported overspend on PK473 by inflating reported spend on PK385.

## Corrected YTD position

| Metric | Current | Corrected |
|---|---|---|
| PK385 YTD P1-10 | $175,758 | $109,335 |
| PK385 year-end | $263,000 | $145,780 |
| PK385 vs $164,950 budget | +$98,050 over | -$19,170 under |

The $19,170-under figure is consistent with the Checklist note "Remaining funds $11,690 ex GST" within timing and GST variance.

## Open questions not yet resolved

These are documented in the LZ Findings file as outstanding queries for Parks Maintenance:

1. **Why is 19% applied to LZ6?** No document explains the origin of this figure. PM must answer: how was the LZ6 PK385 split set, and when was it last reviewed?
2. **LZ3 zero allocation.** Are Sturdee Park Loganlea (LZ3-310) and Lake Breeze Park Loganholme (LZ3-333) being maintained? If yes, who is paying for it?
3. **LZ5 double-billing April.** GJ078805 (07-Apr-26) and GJ078959 (16-Apr-26) both contain $1,104.66 Glascott LZ5 entries. Two invoices in one month (INV-9709 and INV-010266). Verify both are legitimate or one is a catch-up.
4. **LZ6 scope audit.** Checklist lists 7 approved sites. If sites have been added via DM# 1144082-1, the Checklist must be updated.
5. **Green Tracker amendment and YTD reversal.** Two-step fix: (a) PM amends Tracker LZ6 PK385 line from $13,993 to $2,306; (b) GJ reclassifying YTD excess from `1-20681-73126` back to `1-20376-73126`.

## What this case study teaches

The pattern that recurs across passthrough investigations:

1. **Identify whether the PK has direct invoices.** If no, it's a passthrough.
2. **Trace one transaction back to its source.** Pick a recent GJ on the PK, follow the credit side to the holding account, follow the holding account back to the AP invoice.
3. **Compare the split basis to the governance document.** The holding account split is driven by ONE document (often a Tracker). The governance document (Checklist, rate card, contract schedule) is what SHOULD drive the split. If they don't match, that's the finding.
4. **Reconcile by zone / by site.** The aggregate gap doesn't tell you which zone is the problem. Per-zone reconciliation surfaces the outlier.
5. **Check whether the gap masks another budget.** A passthrough that overcharges Account A may be relieving Account B. Always check the upstream cost centre's budget position.

## Reusing this template

For a new passthrough investigation:

1. Copy this document structure
2. Replace PK385 / 1-20276-73126 / Tracker DM / Checklist DM with the new identifiers
3. Run the five-step trace
4. Build the zone-by-zone reconciliation table
5. Document the governance gap and the masked-budget effect

The structure transfers directly. The numbers don't.
