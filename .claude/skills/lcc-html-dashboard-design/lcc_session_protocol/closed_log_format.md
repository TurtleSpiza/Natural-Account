# Closed Log Format

The resolution record. Items that came off the outstanding list, with the disposition that closed them. Numbered identically to where they sat when they were open, never renumbered.

## Structure

```
CLOSED LOG
----------
{N}    {context tag}    {one-line resolution: what was confirmed, recoded, or written off, with reference}
```

## Numbering rule (the one inviolable rule)

**Closed items keep the number they had when they were open.** If item 33 closes, it appears as 33 in the closed log. The outstanding items list now has a gap at 33. Do not fill the gap. Do not renumber the closed item.

This rule exists because the session log references items by number. If item 33 closed in s27 and gets renumbered to fill a gap, every prior session log entry that referenced item 33 now points to the wrong thing.

## Worked examples (from NA Analysis v9_s34)

```
CLOSED LOG
----------
2    73122 Oct-2024 $167,267 — within normal range. FY2026 variable $181k-$265k/month. no action.
29   72231 watering vendor — Canasta Holdings ABN 26 660 260 426 (LD Total). invs 130926-135034 Dec-2023 to Mar-2024 total $78,414. hand watering newly planted areas (Underwood, Lancaster, Kilkenny, Jean, Roadside). recode raised as item 66.
33   73313 FY2023 — 215 rows $4,954. Telstra T311 direct + DM 15956749 IT device billings + mobile activations PJ007879 $1,260.
36   7B123 FY2021-22 — FY21 $102 rates adjustments immaterial. FY22 $6,702: bird removal $6,667 + rodent control $73 + infrastructure charge -$190 + rates $153.
55   73128 TEC FY2026 — inv 3090 31-Jul-2025 $6,860 svc 20821. TEC confirmed engaged.
```

Note items 2, 29, 33, 36, 55 are out of order — that's correct. They closed in different sessions. Order is by closing session, not by number.

## Disposition types

Every closed item line should make clear which disposition closed it. Common types:

- **Confirmed correct.** "$167,267 — within normal range. no action."
- **Confirmed and recoded.** "miscoding to 73128/73211 confirmed, recode raised as item 66" (note the cross-reference to the new outstanding item that the closure spawned).
- **Confirmed cease.** "subscription ends FY2023, account ceased."
- **Confirmed immaterial.** "FY21 $102 rates adjustments immaterial."
- **Vendor / counterparty identified.** "Canasta Holdings ABN 26 660 260 426 (LD Total)."

If a closure spawns a new outstanding item (e.g. confirms a miscoding that needs recoding), the closed-log entry names the new item number. This keeps the audit chain visible.

## What goes in a closed line

- The original item number (unchanged)
- The context tag (account code or other identifier)
- A one-line resolution summary
- Any cross-reference to a new item if the closure spawned one
- Dollar amount and document reference where relevant

## What does NOT go in a closed line

- Long narrative. The full finding lives in workbook col P.
- The investigation that led to the resolution. Session log handles that.
- A description of what the original outstanding item was. The original item line, plus this resolution line, together form the audit chain.

## Reading the closed log

The closed log is for two readers:

1. **The next session**: scan for any items that look like they're about to be re-opened. If you find yourself about to investigate something and the closed log shows it was already done, stop. Re-read the closure.

2. **Auditors / handover recipients**: shows that an item was raised, investigated, and resolved with a documented basis. The dollar quantum, the document reference, the disposition. This is the audit trail.

## Maintenance

Closed log items don't get updated. If new information emerges that contradicts a closure, the correct move is to re-open the item with a new number, not to retroactively edit the closed entry. The original closure stays as the historical record of what was decided at the time.

## Anti-pattern: closing prematurely

The discipline is "close when fully evidenced," not "close when convenient." An item closed without Tier 1 evidence will frequently re-open six months later when fresh transactions surface the same anomaly. If unsure, leave it open.
