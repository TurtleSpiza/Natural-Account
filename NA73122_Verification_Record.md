# NA73122 Garbage Collection - Verification Record

Reviewed 17-Jun-2026. Branch 4090000, Ledger 26SLACT, FY25/26, periods 1 to 12.

## Register-row header

- Account: 73122 Garbage Collection
- Dollars in scope: $21,876.60 (accumulated actual p1-12)
- Reconciliation: CLEARS to SE2 to the cent. Export $21,876.60 = SE2 $21,876.60, gap $0.00.
- Overall RAG: AMBER (confirm). Coding verified correct, no recode. Held on evidence completeness only.
- Findings: F1 evidence gap (5 of 9 months unsighted), F2 no Parks tax invoice exists by design, F3 EOM accrual noise nets to zero, F4 ABN not sighted in Parks set.
- Open actions: 4 (see Outstanding actions).
- Evidence location: NA73122_Evidence/ plus four council-wide Cleanaway statements fingerprinted in the Evidence Manifest.

## Verdict

Account 73122 is correctly coded and reconciles to SE2 to the cent. No recode is required. The account is held AMBER, not GREEN, on the evidence limb alone: only 4 of the 9 charge-months have a sighted source document, and no single month has the full Tier 1 chain. There is no blocker and no recode dollar.

## Reconciliation

SE2 accumulated actual for 73122 is $21,876.60. The headline export supplied first (file ...103919.445) was filtered to Section 4090210 only and returned $3,578.94. The unfiltered branch export (file ...104128.223) returns the full $21,876.60 across four sections and reconciles to SE2 at $0.00 gap.

| Section | Lines | Sum | Nature |
| --- | --- | --- | --- |
| 4090210 Parks Leadership | 27 | $3,578.94 | Cleanaway, PK000001 |
| 4090220 | 2 | $0.00 | RJ accrual + reversal, nets zero |
| 4090240 Park Services | 33 | $18,297.66 | Cleanaway, PK000022 |
| 4090250 | 8 | $0.00 | RJ accrual + reversal, nets zero |
| Total | 70 | $21,876.60 | = SE2 |

Real spend is the 36 GENERAL JOURNAL lines ($21,876.60). The 34 RJ accrual lines net to exactly $0.00.

## Account composition

73122 is Parks' allocated share of the council-wide monthly Cleanaway claim. Each month the council-wide Cleanaway bill is split across all cost centres by a council-wide allocation journal. Parks receives two slices:

- PK000001 Parks Leadership (svc 20151): a flat $397.66 every month, three fixed standing lines of $69.19, $131.39, $197.08. These are fixed public-place-bin standing charges.
- PK000022 Parks Asset Maint and Repairs (svc 20392): a variable amount, $1,808.68 to $2,411.57 per month, volume-based public-place-bin servicing.

| Charge month | Posting | PK000001 | PK000022 | Total ex-GST | Source doc held |
| --- | --- | --- | --- | --- | --- |
| Jul-2025 | GJ076954 | $397.66 | $1,808.68 | $2,206.34 | none (doc 25130428 not sighted) |
| Aug-2025 | GJ076960 | $397.66 | $1,811.98 | $2,209.64 | Statement sighted |
| Sep-2025 | GJ077308 | $397.66 | $2,296.27 | $2,693.93 | none, and GL attachment flag = N |
| Oct-2025 | GJ077648 | $397.66 | $1,877.87 | $2,275.53 | Statement sighted |
| Nov-2025 | GJ077967 | $397.66 | $1,884.45 | $2,282.11 | Statement sighted |
| Dec-2025 | GJ078369 | $397.66 | $2,355.57 | $2,753.23 | none |
| Jan-2026 | GJ078765 | $397.66 | $1,900.93 | $2,298.59 | allocation journal only |
| Feb-2026 | GJ078765 | $397.66 | $1,950.34 | $2,348.00 | allocation journal only |
| Mar-2026 | GJ079127 | $397.66 | $2,411.57 | $2,809.23 | Statement sighted |
| Total | | $3,578.94 | $18,297.66 | $21,876.60 | |

## Four-limb assessment

Limb 1, service and PK correctness: GREEN. Both real-spend streams crosswalk correctly. svc 20151 maps to PK000001 Parks Leadership and Administration. svc 20392 maps to PK000022 Parks Asset Maint and Repairs. No named officer applies, these are journalled supplier costs not person-attributable. The off-map svc/PK combinations on the accrual lines (svc 20241 to PK000474/477, svc 20381 to PK000479/482) sit only on RJ lines that net to $0.00 and do not affect the balance.

Limb 2, natural account correctness: GREEN. External Cleanaway garbage collection belongs in 73122 Garbage Collection. It is correctly distinguished from 73121 Cleaning and Sanitary, from 7B115 Internal Garbage Charges, and from 7B122 Internal Tip Fees. No miscode.

Limb 3, evidence sufficiency: AMBER. Per the mandatory per-line evidence rule, this limb cannot go GREEN. The evidence chain for any Parks line is Cleanaway Statement of Services (council-wide tax invoice) then council-wide allocation journal (derives the Parks split) then GL line. What is held does not complete that chain for any single month:
- Statements sighted: Aug, Oct, Nov 2025, Mar 2026 (4 of 9). These confirm the council-wide claim and GST but do not show the Parks slice.
- Allocation journal sighted: Jan and Feb 2026 only. This shows the Parks PK000001/PK000022 split but lacks the underlying Statement.
- No month holds both. Three months (Jul, Sep, Dec 2025) hold neither.
Missing source documents listed explicitly: Cleanaway Statements for Jul-2025 (doc 25130428), Sep-2025 (doc 25172924), Dec-2025; and per-month allocation journals for Jul, Aug, Sep, Oct, Nov, Dec 2025 and Mar 2026.

Limb 4, tax compliance: AMBER. GST is correct, the sighted council-wide claims book GST at exactly 10% (collection cost times 0.1). The ABN element cannot be cleared: no Cleanaway tax invoice carrying an ABN sits in the Parks evidence set. Cleanaway is vendor CLE057, GST booked at council level on the council-wide AP document held centrally, not at the Parks line. ABN not sighted, not validated.

## Findings

F1. Evidence gap. 5 of 9 charge-months have no sighted Cleanaway Statement (Jul, Sep, Dec 2025, Jan, Feb 2026). Per-month allocation journals are held for Jan and Feb only.

F2. No standalone Parks tax invoice exists by design. 73122 is an allocated slice of a council-wide claim. Per-line evidence at Parks level requires both the monthly Statement and the monthly allocation journal. This is structural, not an error.

F3. EOM accrual noise. RJ013015, RJ013048, RJ013123, RJ013158, RJ013222, RJ013283, RJ013485, RJ013539, RJ013556, RJ013557 post EOM accruals for Facilities, Park Services and Trees (DM 17802475 and DM 17802492) into NA 73122 and reverse them. All net to $0.00. Immaterial to the balance, advisory only, consistent with normal LCC EOM accrual mechanics.

F4. ABN not sighted. Cleanaway ABN is not in the Parks evidence set, so the tax limb ABN element stays open.

## Outstanding actions

1. Obtain Cleanaway Statements for Jul, Sep, Dec 2025 to close the three months with no source document.
2. Obtain the monthly council-wide allocation journals for the seven months not held, to complete the Tier 1 chain and tie each Parks slice to its derivation.
3. Sight the Cleanaway ABN on a council-wide AP document and validate the checksum and register status to clear the tax limb ABN element.
4. Note for the record: Sep-2025 GL line GJ077308 carries attachment flag N in TechOne, the only month with no TechOne attachment.

## Conclusion

73122 is coded correctly and reconciles to the cent. No recode. The account stands AMBER pending the evidence and ABN items above. None is a blocker. On Spero's instruction the account can be marked cleared with the evidence gaps recorded as manifest GAPs, or held AMBER until the five missing statements and the ABN are sighted.
