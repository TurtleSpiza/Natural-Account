# Governance Reconciliation Pattern

The two-document reconciliation that every passthrough trace ends with. One document drives the actual GL posting. Another document defines what the posting should be. The gap is the finding.

## The two-document shape

Every passthrough has both:

| Document | Role | Example |
|---|---|---|
| **Operational driver** | Drives the actual journal split | Green Maintenance Budget Tracker (DM# 17767639) |
| **Governance basis** | Defines what the split *should* be | Urban Bushland Checklist (DM# 14719249) |

If the two documents agree, the allocation is governed correctly and the trace closes as Cleared. If they disagree, the trace produces a finding, and the next step is either to amend the operational driver or update the governance basis.

## Reading the two documents

### Operational driver — what to read

- **Where it lives.** Usually a TechOne DM or a SharePoint workbook owned by Parks Maintenance.
- **What it allocates.** Per-period dollar values per destination PK or per cost centre. May be a percentage split (e.g. 81/19) or a fixed dollar value (e.g. $13,993/month).
- **How it changes.** Should have a version history. Often does not. The PK385 Tracker carries no version log — meaning nobody can say when the LZ6 PK385 line was last reviewed.
- **Who owns it.** Usually a section coordinator. The owner is responsible for the values being correct.
- **What basis is documented.** Sometimes there is a working paper or rate-card derivation. Often there isn't. "It has always been 19%" is not a basis.

### Governance basis — what to read

- **Where it lives.** Often a separate TechOne DM, a council-approved scope document, a contract schedule, or an email trail.
- **What it defines.** The approved scope (sites covered, services included, per-unit rates, per-period allowances).
- **How it gets approved.** A formal process — for the Urban Bushland Checklist this is: funding confirmed, email to Natural Areas, mapping layer updated, approval email saved.
- **What it excludes.** Often more important than what it includes. Checklist item 1.1 explicitly excludes ovals, roadsides, landscaped garden beds — meaning anything posting to PK385 for those types is a miscoding.

## The reconciliation

Three columns minimum: governance value, operational value, gap.

| Unit | Governance basis | Operational value | Variance |
|---|---|---|---|
| {site / zone / cost centre} | {approved $/round or $/period} | {actual $/period being allocated} | {$ and %} |

Build the table at the most granular level both documents support. For PK385 that was per-zone (LZ1 through LZ6). For other passthroughs it might be per-site, per-rate-line, or per-vendor.

Aggregate the table at the bottom. The total gap is the headline number.

## Decision tree after reconciliation

```
Does the operational driver match the governance basis?

├── Yes (within rounding) → CLEAR. Document the trace, close the item.
│
└── No → finding. Branch on which document is right:
    │
    ├── Governance basis is current and correct → operational driver is wrong.
    │       Action: amend the driver (Tracker, rate card) to match the basis.
    │       Reverse YTD excess via GJ.
    │
    ├── Governance basis is outdated → driver may be reflecting current scope.
    │       Action: update the governance basis (Checklist, contract schedule).
    │       Confirm the new scope was approved through the formal process.
    │       Document the basis in writing.
    │
    └── Both documents are inconsistent or unclear →
            Action: escalate to the document owners.
            Hold the trace as Pending until a documented basis exists.
```

The PK385 case is in the first branch — Checklist is current, Tracker is overcharging — but the recommended action requires Parks Maintenance cooperation because correcting it surfaces a $117k masked overspend on PK473.

## What to do with the finding

A reconciliation finding is rarely actionable by Finance alone. Most produce three downstream actions:

1. **A recode journal** — uses `techone-genjnl-format` to reverse the YTD excess to the correct destination
2. **A driver amendment** — the section coordinator updates the Tracker / rate card / split percentage
3. **A communication** — section-leader email explaining the gap, the proposed correction, and the budget implications (especially when correcting one PK exposes a previously-masked overspend on another)

The third is often the slowest because of the political dynamics. Correcting the PK385 split immediately moves $105-126k of overspend from PK385 to PK473, making PK473's real position visible. That's why the corrections sometimes don't happen — not because Finance is unwilling, but because Parks Maintenance has incentives to keep PK473 looking on-budget.

## Common pitfalls

### Treating the operational driver as authoritative

Easy to do. The Tracker is what's driving the GL. The Tracker has a DM number and is referenced in journal narrations. It feels official. But the Checklist is the actual approved scope. The Tracker is just a worksheet that someone built once and nobody has updated.

When in doubt, the document that went through formal council approval is the governance basis. The document referenced in journal narrations is the operational driver.

### Treating the governance basis as static

Approved scope changes. A Checklist from 2022 may not reflect 2026 reality. Before declaring the operational driver wrong, confirm the governance basis is current. If the Checklist doesn't include sites that genuinely have approved Urban Bushland work, the gap may reflect a Checklist update that never happened.

### Reconciling at the wrong granularity

Reconciling at "$21,922/month vs $12,148/round" tells you the aggregate gap but doesn't surface the LZ6 outlier. Per-zone reconciliation surfaces it immediately. Always go granular before declaring a per-line root cause.

### Ignoring the upstream effect

Correcting a passthrough split changes both endpoints. The destination PK gets less. The upstream PK or holding account effectively gets more. Always check the upstream budget position before recommending the correction. Brad White (Parks Manager) and the budget owners need to see both effects to make the call.

## Cross-references

- `worked_example_pk385.md` — the full PK385 reconciliation, end-to-end
- `allocation_chain_pattern.md` — the five-step trace that precedes the reconciliation
- `holding_accounts.json` — known holding accounts and their typical destinations
- `lcc_session_protocol/outstanding_items_format.md` (also at `_shared/`) — how to document open governance questions for the Finance batch email

When the reconciliation produces a recode journal, use `techone-genjnl-format`. When it produces a section-leader communication, that's a separate workflow (TBD as a `finance-investigation-narrative` skill).
