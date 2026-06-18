# NA73124 Security - Verification Record

**Branch 4090000 Parks | Ledger 26SLACT | FY26 periods 1-12 | Prepared 18-Jun-2026 | Overall RAG: AMBER (coding clean, evidence pending)**

## Verdict

The account reconciles to the cent and is **coding-correct: no recode or journal is required**. $264,132.36 across 28 lines ties exactly to the SE2 26SLACT Accum Act p1-12 enquiry. Limbs 1 (PK/service) and 2 (natural account) pass GREEN on every line. The account is held AMBER only because no source invoice was sighted this pass (L3) and the supplier ABN/GST cannot be verified without them (L4). It clears to GREEN on sighting the security invoices and one ABN check.

## Account reconciliation

| Source | Lines | Total ex-GST |
|---|---|---|
| Full branch export (Ledger_73124_18-Jun-2026) | 28 | $264,132.36 |
| SE2 26SLACT Accum Act p1-12, NA 73124 | n/a | $264,132.36 |
| Variance | | $0.00 |

Composition: 25 PUR Cred Invoices (security standing order, ~$27,000/month across P1-P11; gross $288,735.15), 1 creditor credit note (~-$24,600), 1 Issue from Inventory ($24.31), 1 general journal ($380.00).

## Four-limb status

| Limb | Status | Basis |
|---|---|---|
| 1. Service / PK | GREEN | $263,150.30 (17 lines) sits on svc 20302 Parks Security Services (PK Park Services) - security spend correctly attributed to the security service. $957.75 (10 lines) on svc 20151 Depots (PK000001) and $24.31 (1 line) on svc 20181 are consistent with site security. All map to valid Parks services. |
| 2. Natural account | GREEN | Security guarding/patrol services are correctly coded 73124 Security. The ~$27,000/month contract value does NOT push to 73212 Major Contracts: a dedicated named-service account (Security) is the correct home over the generic Major-Contracts floor. No recode candidates. |
| 3. Evidence | AMBER | 27 of 28 lines carry a TechOne attachment flag, but flags are not sighting. The 25 security invoices were not sighted this pass. |
| 4. Tax compliance | AMBER | Supplier ABN/GST not verifiable without the invoices; the supplier identity (QLDPSI standing order references plus INV-35xx series) is confirmed only from the ledger face. |

## Recode candidates

None. The account is correctly coded; no GENJNL is prepared.

## Evidence gap list (to clear L3 and L4)

The 25 security PUR invoices (QLDPSI002750/002792/002888/003121/003170 series plus INV-3518/3525/3817 etc.), the ~$24,600 creditor credit note, and the supplier ABN (run checksum + ABR). Confirm the supplier name and the security contract authorisation (a Council contract, not a proposals-register entry).

## Notes

GL amounts ex-GST throughout. No GST errors raised this pass (no document sighted). Per the standing directive, this verdict and its gaps live in the register and 00_Outstanding_Evidence_and_Actions.md; no email issues.
