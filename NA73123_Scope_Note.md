# NA73123 Scope Note - Maintenance Services - OPENED, NOT RECONCILED
Prepared 11-Jun-2026 | Spero Karkalemis | Ledger 26SLACT, Branch 4090000, O110-O115, P1-12

Verdict: OPENED only. The full-branch export (3,776 data lines) sums to $3,951,109.43 ex-GST against SE2 (8-Jun-2026) accumulated actuals of $3,900,770.79, a gap of $50,338.64. Under the session rule, no account-level conclusion is drawn until the total reconciles. No limb is rated.

## The reconciliation gap, $50,338.64
Two candidate explanations, unresolved:
1. Export row duplication. 2,062 rows share a Document Unique ID across 717 IDs, which is normal for multi-line documents, but 365 rows are exact duplicates on ID + amount + period + account ($20,201.46), and several RJ013539/RJ013556 accrual legs at $363,737.42 appear three times each in the raw export. That pattern arguably points to a TechOne extract artefact rather than triple postings.
2. Timing. SE2 is dated 8-Jun-2026 and the export 11-Jun-2026; three days of P12 postings could carry part of the gap.
Resolution path: re-pull the export (or pull P12 only) and diff, or tie the per-period totals to an SE2 refresh. Do not work lines until this closes.

## Profile (indicative only, pre-reconciliation)
- Sources: AP $3,971,119.30 (3,339 rows), GL net -$23,019.35 (433 rows, dominated by self-reversing EOM Natural Area and Park Services accruals plus two Pool Shop recodes out, -$33,717.41 and -$26,224.15), IN $2,883.33, TE $126.15.
- Largest service codes: 20392 Parks Asset Maint and Repairs $1,304,200.29 (1,894 rows); 20481 $1,273,366.36 (1,036 rows); 20454 $184,461.88; 20551 $171,655.34; 20431 $144,436.26; 20821 Parks Disaster Management $138,508.44; 20802 Water Parks $137,334.50.
- Attachment coverage: 12 rows $321,060.51 carry no attachment; 3,749 rows attach.
- GJ079210 sits inside this account too: the -$79,418.00 condition assessment leg off 1-20261 (PK000035) and its +$79,418.00 destination on PK000022, netting zero within 73123 (backup sighted 11-Jun-2026, see NA73212 addendum).
- Known trap applies: 73123 and 73212 are a reclassification pair and must be read combined, never in isolation.
- Sub-extracts on hand: s4090210 (14 lines, $2,985.97, all small Depots preventative maintenance, plausibly correctly coded) and s4090230 (22 lines, $31,995.72 incl the GJ079210 leg and the RJ013706 accrual pair netting zero).

## Open actions
1. Resolve the $50,338.64 export-vs-SE2 gap (re-pull or P12 diff) before any line work.
2. Read 73123 jointly with 73212 (the GJ076924 95-line redistribution touches both, plus 73126 and 73121; backup sighted 11-Jun-2026).
3. Plan the line review by service code, 20392 and 20481 first (65% of dollars).
