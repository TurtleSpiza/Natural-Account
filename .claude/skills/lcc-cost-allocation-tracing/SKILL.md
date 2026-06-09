---
name: lcc-cost-allocation-tracing
description: "LCC Parks cost allocation tracing for PKs that receive zero direct vendor invoices but carry operational spend via journal splits from holding accounts. Use whenever investigating a passthrough PK (e.g. PK385 Urban Bushland), tracing a vendor invoice through a holding account to its destination PKs, reconciling a Tracker, rate card, or split-percentage operational driver against a governance document (Checklist, contract schedule, approved scope), or finding an unexplained allocation that masks another PK's budget position. Triggers: 'passthrough PK', 'allocation trace', 'split journal', 'holding account', 'no direct invoices', 'Tracker vs Checklist', 'Urban Bushland', 'PK385', 'PK473', 'governance reconciliation', '81/19 split', 'EOM accrual mirror'. Distinct from lcc-na-analysis (variance-driven) and lcc-coding-review (correctness-driven). This skill is investigation-driven single-PK trace plus governance reconciliation."
---

# LCC Cost Allocation Tracing

The skill that turns "this PK has spend but no invoices" into a fully evidenced finding. Used for passthrough PKs fed by holding accounts, where the operational driver (Tracker, rate card, split percentage) and the governance basis (Checklist, contract schedule) need reconciliation.

The PK385 Urban Bushland investigation is the canonical worked example. Future passthrough investigations follow the same five-step trace and two-document reconciliation pattern.

## Core principle

A passthrough PK is downstream of a holding account. Tracing it requires three artefacts:

1. **The journal that splits the holding account** (typically a GJ with a credit on the holding side and debits on the destination side)
2. **The operational driver** that produces the split values (Tracker, rate card, percentage agreement — the document referenced in the journal narration)
3. **The governance basis** that defines what the split *should* be (Checklist, contract schedule, approved scope)

If items 2 and 3 disagree, the difference is the finding. The reconciliation is the deliverable.

## Reference artefacts in this skill

| File | What it is |
|---|---|
| `holding_accounts.json` | Known LCC holding accounts (1-20276-73126 first), their split destinations, the operational driver they reference, and known issues |
| `vendor_to_zone_crosswalk.csv` | Austspray and Glascott zone contracts mapped to service codes, PKs, and monthly invoice amounts |
| `worked_example_pk385.md` | The full PK385 / Urban Bushland investigation as a worked example. Five-step trace, zone-by-zone reconciliation, masked-budget analysis, open questions, corrected position |
| `allocation_chain_pattern.md` | The five-step trace pattern, generic, for any passthrough investigation |
| `governance_reconciliation_pattern.md` | The two-document reconciliation discipline. Decision tree for what to do when operational driver and governance basis disagree |

## Cross-references to `_shared/`

| File | Purpose |
|---|---|
| `lcc_chart_of_accounts.json` | NA reference for any account in the trace (e.g. 73126 Landscapers & Gardeners) |
| `service_section_pk_map.csv` | Service code ↔ PK ↔ section validation for trace destinations |
| `lcc_session_protocol/` | Session header, outstanding items, traps catalogue templates for long-running investigations |

## Workflow

### Triage — is this a passthrough investigation?

A request lands as one of:
- "Why is PK X over budget?"
- "What is driving spend on PK Y?"
- "Trace this invoice"
- "Reconcile the Tracker against the Checklist"

Triage by checking three signals on the PK:

1. **Direct invoice count.** Pull the listing. Count AP and TE entries. If both are zero or very low, it's a passthrough.
2. **Journal density.** Most lines are GJ or RJ with split-narration references? Confirms passthrough.
3. **Smooth proportional spend pattern.** Spend tracks proportionally with a sister PK or zone activity? Confirms passthrough.

If two of three signals hold, this skill applies. If they don't, hand to `lcc-na-analysis` (variance investigation) or `lcc-coding-review` (correctness audit).

### The five-step trace

Detailed in `allocation_chain_pattern.md`. Brief:

1. Confirm passthrough status (zero direct invoices)
2. Identify the holding account (credit side of a recent GJ)
3. Trace the holding account back to source AP invoice
4. Identify the split basis (Tracker DM, percentage, fixed value)
5. Reconcile against the governance document (Checklist, contract schedule)

### The two-document reconciliation

Detailed in `governance_reconciliation_pattern.md`. Build a per-zone or per-site table comparing:

- Governance value (what the Checklist / rate card approves)
- Operational value (what the Tracker / split actually allocates)
- Variance (gap, with annual extrapolation)

Surface the outlier line. In PK385, LZ6 alone drove 94% of the gap. The other zones were within rounding.

### The masked-budget check

Always read both ends of the passthrough. A passthrough that overcharges the destination PK is relieving the upstream PK. Check the upstream PK's budget position before recommending the correction.

For PK385, correcting the LZ6 split immediately surfaces a $105-126k overspend on PK473 that the Tracker has been hiding. The political dynamics of that surfacing are why the correction sometimes doesn't happen, even when the analysis is unambiguous.

### Output

Every passthrough trace produces:

1. **One-paragraph summary** — passthrough nature, holding account, headline gap
2. **Five-step trace narrative** — with specific journal references and dollar amounts
3. **Reconciliation table** — granular (per zone, per site, per rate line)
4. **Open questions list** — unresolved items requiring PM, vendor, or Finance input
5. **Corrected position calculation** — YTD and EOFY if the operational driver were amended
6. **Masked-budget impact** — the upstream PK position that the current allocation is hiding

The PK385 case at `worked_example_pk385.md` is the template.

## What this skill does NOT do

- Branch-wide coding review. That's `lcc-coding-review`.
- Account variance investigation across all 168 NAs. That's `lcc-na-analysis`.
- Forecasting impact of the correction. That's `lcc-parks-forecast` (Probability of remaining under budget if the split is corrected).
- The actual recode journal preparation. That's `techone-output` once the correction is agreed.
- Section-leader email composition. That's the (TBD) `finance-investigation-narrative` skill, which builds the Marisa-style email from the trace findings.

## Cross-skill flow

```
lcc-cost-allocation-tracing (this skill — the trace and reconciliation)
              │
              ├─→ techone-output (recode journal preparation)
              │
              ├─→ lcc-finance-batch-email (Finance batch covering open data requests)
              │
              └─→ finance-investigation-narrative (section-leader email — TBD as separate skill)
```

The trace itself sits inside this skill. Everything downstream (recode journals, Finance emails, section-leader communications) hands off to the appropriate sibling skill.

## When to start a new task file

Long-running passthrough investigations (PK385 has spanned multiple sessions) benefit from the session protocol in `lcc_session_protocol/` (also at `_shared/`). The header at top, outstanding items numbered, traps catalogue, session log. The PK385 investigation specifically would benefit from a task file because the open questions (LZ6 19% basis, LZ3 zero allocation, LZ5 double-billing) span multiple sessions and multiple stakeholders.

## Anti-patterns

### Treating the destination PK in isolation

A passthrough PK's variance is a function of the upstream PK and the operational driver, not the destination's own activity. Reading PK385 in isolation produces "$10,808 reported overspend." Reading PK385 alongside PK473 and the Tracker produces "$140,246 annualised overcharge with no vendor basis."

### Trusting the operational driver because it has a DM number

DM numbers are TechOne document references, not approval stamps. The Tracker has DM# 17767639 because it's stored in TechOne, not because it's approved. Approval lives in the governance document (Checklist DM# 14719249), not the operational document.

### Recommending the correction without checking the upstream

A correction that moves $105-126k off PK385 has to land somewhere. If that somewhere is over budget, the conversation changes from "fix the allocation" to "expose a previously-masked overspend." Always check the upstream first. The recommendation in the deliverable should name both effects.

### Ignoring zero allocations

LZ3 has 2 approved sites and $0 allocation. That's a finding too. Either work is happening and not charged (PK385 underspending against approved scope), or work is not happening (Checklist has dead sites). Both require investigation. Zero is never "fine" in a trace.
