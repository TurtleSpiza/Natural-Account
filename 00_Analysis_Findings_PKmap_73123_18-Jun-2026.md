# Analysis findings, 18-Jun-2026 — PK-map crosswalk and 73123 reconciliation

Two of the remaining items were analysis tasks (not document requests). Both were advanced from data already in the bundle.

## 1. PK-map crosswalk (Limb 1) — 3 of 4 PKs resolved

The audit flagged 12 journal lines on PKs absent from every installed service map. The 18-Jun 72111 ledger carries these PKs against their cost codes, which extends the map from canonical TechOne data:

| PK | Cost code (from ledger) | Context |
|---|---|---|
| PK000083 | 1-20451-72111 | Despatch stock requisition 092853 (Allstore/Chambers) |
| PK000445 | 1-20451-72111 | Blue Pearl Sloper desk (72313 furniture candidate) |
| PK000493 | 1-20392-72111 | Standing order 24/25, EOY AP reversal |

PK000083 and PK000445 map to service cost code **20451**; PK000493 to **20392**. The crosswalk for these lines is now evidenced from the ledger rather than unconfirmed. **PK000510/PK000511** (carried lines) are not in any held ledger and remain the only unmapped PKs — they still need the canonical PK record.

## 2. 73123 export-vs-SE2 reconciliation — materially narrowed, not closed

The blocker: export $3,951,109.43 vs SE2 actual $3,900,770.79, gap **$50,338.64** (export higher), blocking all 73123 line work.

Findings from the full ledger (3,776 lines, total confirmed $3,951,109.43 exact):

- **$18,342.92 of genuine duplicate inflation** — 333 excess lines where an identical (reference + amount + date + details) row appears two or more times. This is real export-side double-counting and is the largest identified component of the gap.
- **A probable duplicate journal posting:** RJ013539 and RJ013556 are two structurally identical 64-line journals, both dated 4-Mar-2026, each netting $0.00. Net-zero so they do not move the total, but two identical balanced journals on one date is a data-quality flag worth the GL team's eye.
- **P12 timing:** period 12 nets -$23,785.70; a timing difference between the export cut and the SE2 snapshot is a candidate for part of the residual.
- **Residual ~$31,995.72** ($50,338.64 less the duplicate inflation) is unexplained from the export alone.

**Why it cannot be fully closed here:** the SE2 is a budget-vs-actual summary (one row per account), not line-level, so the export cannot be matched line-for-line against it. Closing the residual needs the GL team to confirm which entries the SE2 actual excludes (most likely the duplicate set above plus a P12/P13 timing slice). The duplicate inflation is now quantified, which is the actionable half.
