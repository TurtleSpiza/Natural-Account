# Allocation Chain Pattern

The five-step trace that turns "this PK has spend but no invoices" into a fully evidenced finding.

The pattern is generic. The PK385 Urban Bushland investigation is the canonical worked example. Use this document for any new passthrough trace.

## When to apply

Apply this pattern whenever:

- A PK shows operational YTD spend but a transaction listing on it returns zero direct vendor invoices
- All entries on the PK are GJ or RJ journals with split-narration references
- Spend appears smooth and proportional to invoice activity on a sister PK
- A "Tracker" or "split percentage" governance document is referenced in the GJ narration

These are the signatures of a passthrough PK fed by a holding account.

## The five steps

### Step 1: Confirm passthrough status

Pull the PK's transaction listing. Count the AP-prefixed and TE-prefixed entries (direct vendor invoices). If both are zero or near-zero relative to total spend, the PK is a passthrough.

The PK385 investigation: zero direct invoices despite $175,758 YTD. That immediately frames the work as a trace, not an account audit.

### Step 2: Identify the holding account

Pick a recent GJ entry on the PK. Read the journal narration. Look for:

- A reference to a vendor name or vendor invoice number
- A DM number that points to a Tracker or rate-schedule document
- A matching dollar amount on the credit side of the journal

The credit side of the GJ is the holding account. For PK385, it was `1-20276-73126` Parks Maintenance holding.

### Step 3: Trace the holding account back to source

Pull the holding account's transaction listing for the same period. Find the AP entry that matches the credit-side amount and date.

For LZ6: GJ078805 dated 07-Apr-26 split $73,432.77 across PK473/PK385. The holding account listing showed an AP entry for Austspray INV-157860 dated within days. Match confirmed.

### Step 4: Identify the split basis

Read the GJ narration for the basis of the split. Common patterns:

- A DM reference (e.g. DM# 17767639 = Green Maintenance Budget Tracker)
- A percentage (e.g. "81/19 split per Tracker")
- A fixed dollar value (e.g. "$13,993 to PK385 per Tracker")

Pull the named document. Read the basis it claims to apply.

### Step 5: Reconcile against the governance document

Find the governance document that *should* drive the split. Common shapes:

- A Checklist (approved scope at site level, with per-round dollar values)
- A rate card (cost per unit times approved volume)
- A contract schedule (approved scope per period)
- An email approval trail (one-off allocation decisions)

Compare the split basis (from step 4) to the governance basis (from step 5). If they match, the allocation is governed correctly. If they don't, that's the finding.

For PK385: the Tracker drives $21,922/month. The Checklist approves $12,148/round. The two have never been reconciled. The gap is $117,288 annualised, with LZ6 alone driving 94% of it.

## Common traps

### The vendor invoice is misleading

Vendor invoices reference whatever PK the vendor was given by Council, not necessarily where the cost ends up. Austspray's LZ6 invoice references PK000473. That doesn't mean the cost stays there. The split happens on the Council side.

### Accruals mirror the same fixed values

End-of-month RJ accruals book the split values BEFORE the vendor invoice arrives. This is normal practice but is also the strongest evidence that the split is a fixed allocation, not a calculated one. A truly calculated split would have to wait for the invoice to know how much to allocate.

### One side over, one side under

Don't read the destination PK in isolation. Always read the upstream cost centre too. A passthrough that overcharges PK A may be relieving PK B. The PK385 Tracker reduces reported overspend on PK473 by inflating reported spend on PK385. Ignoring PK473 misses the picture.

### Zero allocation is a finding too

LZ3 has 2 approved Urban Bushland sites but receives $0 in the Tracker. Either work is happening and not being charged (PK385 underspending against approved scope), or work is not happening (Checklist has dead sites). Both are findings. Zero is not "fine."

## Output format

Every passthrough trace should produce:

1. **A one-paragraph summary** stating the passthrough nature, the holding account, and the headline gap
2. **A five-step trace narrative** confirming steps 1-5 with specific journal references and dollar amounts
3. **A zone-by-zone or site-by-site reconciliation table** comparing governance basis to actual split
4. **An "open questions" list** of unresolved items requiring Parks Maintenance / vendor / Finance input
5. **A corrected position calculation** showing what YTD and EOFY look like if the split is amended

See `worked_example_pk385.md` for the canonical filled-in version.

## Cross-references

- `holding_accounts.json` — known LCC holding accounts with their split destinations
- `vendor_to_zone_crosswalk.csv` — Austspray and Glascott zone contracts mapped to service codes and PKs
- `governance_reconciliation_pattern.md` — the Checklist vs Tracker discipline (or any two-document reconciliation)
- `worked_example_pk385.md` — full PK385 case study
- `full_chart_of_accounts.json` (also at `_shared/lcc_chart_of_accounts.json`) — natural account 73126 Landscapers & Gardeners definition
- `service_section_pk_map.csv` (also at `_shared/`) — service code ↔ PK ↔ section validation

When the trace produces a recode journal, hand off to `techone-genjnl-format` for the GENJNL upload format.

When the trace produces a finding requiring section-leader communication, hand off to `lcc-finance-batch-email` (Finance batch) or to a separate investigation-narrative skill if it's section-leader-facing.
