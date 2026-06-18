# NA73535 Tollway Charges - Verification Record

**Branch 4090000 Parks | Ledger 26SLACT | FY26 periods 1-12 | Prepared 18-Jun-2026 | Overall RAG: AMBER (coding clean, evidence pending)**

## Verdict

The account reconciles to the cent and is **coding-correct: no recode or journal is required**. $46,010.25 across 587 lines ties exactly to the SE2 26SLACT Accum Act p1-12 enquiry. Limbs 1 (PK/service) and 2 (natural account) pass GREEN on every line. The account is held AMBER only because the toll provider's monthly statements were not sighted this pass (L3) and GST cannot be verified without them (L4). It clears to GREEN on sighting the statements and confirming the REGO list is the Parks fleet.

## Account reconciliation

| Source | Lines | Total ex-GST |
|---|---|---|
| Full branch export (Ledger_73535_18-Jun-2026) | 587 | $46,010.25 |
| SE2 26SLACT Accum Act p1-12, NA 73535 | n/a | $46,010.25 |
| Variance | | $0.00 |

Composition: 587 DIR Cred Invoices (toll-tag charges, `TAG:...REGO:...`), grouped under 12 distinct toll-account references, P1-P12. Per-trip charges allocated to the using section.

## Four-limb status

| Limb | Status | Basis |
|---|---|---|
| 1. Service / PK | GREEN | Toll charges are spread across 17 Parks service codes (20131/20141/20181/20301/20317/20319/20362/20440/20452 etc.), each a valid Parks service/PK, reflecting the section whose vehicle incurred the toll - the correct attribution model for a shared fleet toll account. |
| 2. Natural account | GREEN | All 587 lines are toll-tag charges (`TAG/REGO`), correctly coded 73535 Tollway Charges. No meals, parking, fuel-levy or other travel content is mixed in. No recode candidates. |
| 3. Evidence | AMBER | All 587 lines carry a TechOne attachment flag (DIR system-fed), but the toll provider's 12 monthly statements were not sighted this pass, and the REGO-to-Parks-fleet confirmation is outstanding. |
| 4. Tax compliance | AMBER | GST on tolls not verified without the statements (tolls are taxable; confirm GST treatment and provider ABN). |

## Recode candidates

None. The account is correctly coded; no GENJNL is prepared.

## Evidence gap list (to clear L3 and L4)

The 12 toll-account monthly statements (Linkt/GoVia, references 9093127298, 9265261567, 9285301698, 9515801867, 9576190486, 9582280910, 9647115363, 949836496691, 949997058483, 9238416657, 9244542533, 9339533467), the REGO list cross-checked to the Parks vehicle fleet, and the provider ABN (checksum + ABR).

## Notes

GL amounts ex-GST throughout. No GST errors raised this pass (no document sighted). Per the standing directive, this verdict and its gaps live in the register and 00_Outstanding_Evidence_and_Actions.md; no email issues.
