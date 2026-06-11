---
name: lcc-coding-review
description: "LCC Parks branch-level account coding audit. Tests every transaction against the canonical Chart of Accounts PDF, evidence-tiered (Tier 1/2/3) sighting, systemic miscoding detection, TechOne GENJNL recode journals. Bundles the full FBT ruleset (50/50 method, Reason Codes A-L, Reason H four-factor test, 19 hospitality scenarios), Consultancy Guide (four-element test, 73601/73603/73605/73607/73609), Travel Guide (73531-73534 destination rule, meals-during-travel exception), and the 679-account chart with FBT/consultancy/travel flags. Use for branch-wide coding review (P10, P11, P12), FBT/hospitality classification, deciding confusable accounts (73511 vs 73512, 73123 vs 73126, 73601 vs 73214, 73533 vs 73534), or checking a Reason code. Triggers: 'coding review', 'natural account', 'FBT', 'reason code', 'hospitality', '73511', '73512', 'consultancy', 'overseas travel', 'recode journal', 'Tier 1', 'systemic miscode'. Distinct from lcc-na-analysis (variance) and lcc-cost-allocation-tracing (passthrough)."
---

# LCC Coding Review

The branch-level audit. Every transaction tested against natural-account definitions. Evidence-tiered. Output is a recode journal in TechOne GENJNL format, plus a workbook with status per account.

Distinct from `lcc-na-analysis`. NA analysis investigates variance one account at a time. Coding review tests coding correctness across an entire branch's worth of accounts in one pass.

## Core principle

No account is cleared without Tier 1 evidence. No recode dollar amount is populated without Tier 1. Suspicious narrations alone do not generate findings. This is the discipline that makes the review defensible.

See `evidence_tier_checklist.md` for what counts at each tier.

## Session start checklist

1. **Read the session header in the previous task file.** It names the branch, period, last-completed account class, and any open Finance batch. Format documented in `lcc_session_protocol/session_header_template.md` (also at `_shared/`).

2. **Confirm the review anchor period.** Check the previous handover for the cutover rule. Mid-month partial periods are excluded.

3. **Pull the source files needed:**
   - GL export (TechOne Ledger Accounts Transactions Table) for the branch
   - PCard cover slips and tax invoices for the period
   - AP creditor invoices for the period
   - 50/50 FBT batch journal references (Finance to provide)

4. **Read the systemic miscodes catalogue** (`systemic_miscodes.json`) before starting any account. Each pattern was burned into the catalogue because someone re-investigated it.

5. **Read the FBT 50/50 batch identifiers** (`fbt_5050_batch_identifiers.md`) before reviewing 73511 or 73512.

## Reference artefacts in this skill

| File | What it is |
|---|---|
| `accts.json` | 242-account database — name, operational `desc`, PDF Data Dictionary `pdf_desc`, miscode rules, source page citations |
| `full_chart_of_accounts.json` | Full 679-account chart with PDF descriptions, FBT/consultancy/travel flags, restrictions. Authoritative for any coding decision. |
| `fbt_classification.json` | Machine-readable FBT allocation table — 24 scenarios, Reason A-L glossary, four-factor Reason H, internal catering, GST codes, 50/50 method |
| `fbt_reason_codes.md` | Reason A-L definitions with the four-factor Reason H breakout |
| `hospitality_scenarios.md` | 19 numbered hospitality scenarios from PDF p68 with quick decision rules |
| `consultancy_guide.md` | Four-element consultant test, consultant-vs-contractor, five 73600-series accounts |
| `overseas_travel_guide.md` | 73531-73534 destination rule, meals-during-travel exception, LGR s.196 reporting |
| `confusion_pairs.json` | 28 confusion pairs with side-by-side correct/incorrect examples |
| `vendor_lookup.json` | 18 known Parks vendors with suggested accounts and warnings |
| `vendor_hints.json` | Hardcoded vendor → account hints used by the AI tool |
| `section_contacts.json` | Parks section coordinator names and contacts |
| `svc_map.json` | 101 service codes mapped to PK number and section (with documented exceptions). Svc 20392 carries a `sub_pks` block: PK000493 Flying Gang validates alongside primary PK000022 (added 11-Jun-2026 for the 72312 IKEA line) |
| `pk_map.json` | 96 PK numbers reverse-mapped to service code and section (PK000493 Flying Gang added 11-Jun-2026), plus a `non_crosswalk_pks` block documenting PKs that do NOT validate: PK000510/PK000511 are work-order pseudo-PKs (Gihani 6-May-2026 email, `02_NA73211_Minor_Contracts/Related/`; 510 re-posts to PK000023, 511 to PK000022) and PK000415/PK000429 are unmapped journal PKs pending confirmation (GJ076924). The `service_section_pk_map.csv` carries primary PKs only; sub-PKs live in the JSON maps |
| `service_section_pk_map.csv` and `.json` | Canonical service map (portable copy of `_shared/`) |
| `marsden_stores_inventory.json` and `.csv` | 750 stores items across 79 categories with codes, descriptions, units. Use when an ALLSTORE/CHAMBERS issue (IN-prefixed transaction) needs a description-to-NA decision. Also the evidence basis for stores-issue/adjustment lines under the Marsden convention (Spero 10-Jun-2026): a 6-digit item-number match in the line Details satisfies the evidence limb — see `evidence_tier_checklist.md`. (Portable copy of `_shared/`.) |
| `lcc_session_protocol/` | Session header, outstanding items, traps catalogue, session log, closed log templates (portable copy of `_shared/`) |
| `quiz_bank.json` | 103-question coding quiz (mixed / miscode traps / FBT) |
| `fbt_data.json` | Operational 24-entry FBT allocation lookup (used by the AI tool; cross-linked from `fbt_classification.json`) |
| `scenarios.json` | 10 quick-reference scenarios |
| `systemic_miscodes.json` | Catalogue of 13 recurring miscoding patterns observed in Parks Branch 4090000 |
| `evidence_tier_checklist.md` | Tier 1/2/3 definitions and dispositions |
| `fbt_5050_batch_identifiers.md` | How to spot Finance 50/50 batches before treating any 73511/73512 movement as a miscode |
| `REBUILD_NOTES.md` | Audit trail of the May 2026 rebuild against the canonical PDF |

## Portability

Every reference file the skill needs is bundled inside this directory. The skill is fully portable to claude.ai web — nothing is `_shared/`-only. The portable copies kept in sync with `_shared/`:

| Local copy | Mirrors |
|---|---|
| `full_chart_of_accounts.json` | `_shared/lcc_chart_of_accounts.json` |
| `service_section_pk_map.csv` and `.json` | `_shared/service_section_pk_map.{csv,json}` |
| `marsden_stores_inventory.json` and `.csv` | `_shared/marsden_stores_inventory.{json,csv}` |
| `lcc_session_protocol/` | `_shared/lcc_session_protocol/` |

## Workflow

### Per-account review loop

1. **Pull the listing for the account.** Use the calamine loader from `lcc-na-analysis/scripts/techone_loader.py` if available, otherwise plain pandas.

2. **Filter out 50/50 batches** if the account is 73511 or 73512.

3. **Review each material line.** Walk the listing top-down. For each line:
   - Is the narration self-sufficient or does it need a source document?
   - Does the vendor name match an entry in `vendor_lookup.json` or `vendor_hints.json`? If yes, is the account correct for that vendor?
   - Does the account match the description in `accts.json` and `full_chart_of_accounts.json` (also at `_shared/lcc_chart_of_accounts.json`)?
   - Is the cost centre / service code valid per `svc_map.json`?
   - Is there a Tier 1 evidence chain available?

4. **Set status per the evidence tier:** Cleared, Review, Action Needed, Not Reviewed.

5. **For Action Needed lines:** populate recode $ and prepare a journal line in the format specified by `techone-output`.

6. **Write findings:** brief notes in the workbook column for the account. The workbook is the source of truth for findings, not the task file.

### Per-pattern detection

In parallel with the per-account loop, watch for systemic patterns. When a pattern in `systemic_miscodes.json` matches what you see, flag the entire pattern rather than each line individually. The branch-wide view is what catches these.

### Recode journal preparation

For every Action Needed line:

1. Reference the destination account (correct NA from the chart)
2. Validate the destination cost centre against `svc_map.json`
3. Validate the destination PK against `pk_map.json` if PK ledger
4. Format the journal line per `techone-output` (40-char narrative cap, PK vs SL ledger format)
5. Stage all recode journals in a single workbook sheet ready for Finance upload

## Output deliverables

### Workbook (per session)

- One row per account
- Columns: Account | Account name | Period actual | YTD actual | Status | Findings | Required action | Recode $ | Notes
- Status taxonomy: `Cleared`, `Review`, `Action Needed`, `Not Reviewed`
- Workbook is source of truth for findings. Task file is coordination only.

### Recode journals sheet

- Pre-formatted GENJNL upload ready for Finance
- Both PK ledger and SL ledger sheets if both formats present
- Narrative validated against 40-char cap

### Task file (per session)

Use the templates in `lcc_session_protocol/` (also at `_shared/`):

- Session header at top with last confirmed account, next in queue, workbook version, open Finance batch count
- Outstanding items numbered (starring the ones for batched Finance email)
- Traps catalogue (one line per trap)
- Session log (one line per session)
- Closed log (kept-numbering)

### Standing items list

Carry forward unresolved items every session. From the P10 review, the 15 standing items currently outstanding include:

- 72113 WHOLESALE SA* O #18766 $2,375 - cover slip not sighted (highest-risk unresolved)
- 73212 Major Contracts large reversal - journal-level explanation needed
- 73124 Security $210,542 against no budget
- 73421 Tankei refund $519.73 shortfall - written explanation needed from Cemeteries
- 73511 INV-9747 $2,445.45 - supplier and event purpose unidentified
- 73533 Quinn $137.85 Uber - no valid receipt
- 73544 Bendelta INV-13157 $8,966.28 - engagement brief needed
- 73544 Empire Office Furniture $4,300 GJ078546 - invoice not sighted
- 73601 Management Consultancies $46,003.66 - invoices not sighted
- 74187 McGavin cover slip $109.71 - doesn't reconcile to YTD
- 7B411 Preussner SCIN1005 $931.20 - no PDI form sighted
- 7B411 Jill Provins Adobe Acrobat DC $362 IJ074158 - second item separate from $320 already journalled
- 71000 Timesheet Clearing $7,455.63 - 8+ periods stuck
- 71227 Years of Service Allowance - account doesn't exist in chart
- Unreviewed major balances: 71111 ($3.96M), 72111 ($86k), 7B112 ($272k), 7B113 ($219k)

## Writing style

Per `spero_writing_style.md` (in `_shared/` if present, otherwise the corpus). Plain, declarative, dollar-amount-led. No em-dashes as separators. No hedging without specific reason. No magnitude adjectives without dollars attached.

Findings narrative goes in the workbook. The task file uses the structured formats from `lcc_session_protocol/` (also at `_shared/`).

## What this skill does NOT do

- Variance investigation. That's `lcc-na-analysis`. If a coding question turns into "why is this account at 200% of budget", hand off.
- Forecasting. That's `lcc-parks-forecast`.
- Allocation tracing across PKs. That's `lcc-cost-allocation-tracing` (e.g. PK385 Urban Bushland passthrough work).
- Power BI dashboards. That's the `powerbi-*` skills.

## Cross-references

- `lcc-na-analysis` for variance-driven investigation when a coding question turns out to also be a budget question
- `techone-output` for the actual journal upload format and PK/SL ledger discipline
- `lcc_session_protocol/` (also at `_shared/`) for the session header / outstanding items / traps / log discipline
- `full_chart_of_accounts.json` (also at `_shared/lcc_chart_of_accounts.json`) for any account definition lookup
- `service_section_pk_map.csv` (also at `_shared/`) (and `.json`) for cost centre validation

## Employee to PK resolution

Use when a person-attributable cost (uniform, PPE, boots, training, travel, reimbursement, or any line where a named person is the only PK clue) must be coded to a PK.

Bundled files: `employee_pk_map.json` (lookup, keyed on Emp ID), `employee_pk_map.csv` (mirror), `resolve_employee_pk.py` (resolver).

Rule:
- Cost code -> service number = trailing 5 digits of the 6-digit cost code; PK via `svc_map`. Never invent a PK on a miss.
- Key on Emp ID, never first name alone (the data has 9 shared first names).
- Acting/temp: the dated row (TEV or Expected End) is the current/acting PK until the cutover; the undated row is the substantive/revert PK from the next day.
- Every acting / TEV / override / pending-separation line is AMBER: confirm with Parks Finance.
- Trainee and corporate cost codes (e.g. 112521, 116501) do not crosswalk; resolve by directive only.

Call: `resolve_employee_pk(emp_id, invoice_date) -> (pk, rag_note)`

Refresh: regenerate from a fresh EOM People & Positions extract each FBT period; bump `ingest_anchor` and `source_sha256`. Adding Position Occupancy Type and the substantive Revert PK to the extract removes the current/acting inference.
