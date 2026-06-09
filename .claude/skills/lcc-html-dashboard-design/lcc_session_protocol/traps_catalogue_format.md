# Traps Catalogue Format

The single highest-leverage section in the task file. Every trap was documented because someone re-investigated something that was already resolved. Reading the catalogue at session start prevents the same waste.

## Structure

```
KNOWN TRAPS — read before starting any account
-----------------------------------------------
{primary identifier} — {one-line explanation of what it actually is, not what it looks like}.
```

One line per trap. No bullets, no narrative. Dense, scannable.

## Trap line anatomy

Each trap follows the same shape:

> `{looks like X} — {is actually Y}. {how to verify}.`

The "looks like" half is what made it a trap (someone misread the surface). The "is actually" half is the resolved truth. The "how to verify" is the document or test that confirms it.

## Worked examples (from NA Analysis v9_s34)

```
73215 FY2024 — fire access track (svc 20471), not mowing.
74141 FY2023 — T&H Levai miscoding INV-30283 (Flagstone Mulching PAR/314E/2017). not truck hire.
73990 — accounting treatment only. capital costs below threshold expensed via GJ svc 20191. never an overrun.
7C112 IJ072068 — cyclone RCM recovery. not an anomaly.
DM 17802475 — Christmas storm Birnam Range Reserve. also appears in 73122 Cleanaway accruals. two separate references, same number.
73544 GJ069279 — QGATE OST inter-branch allocation $9,137. genuine Parks spend, not DA recovery. Luke Spiers email 2-Feb-2024 ref 1303321-1.
73312 A-FE35E476-003 — Beenleigh Town Square FY2024 catch-up billing. underlying rate ~$6k/year not $56k.
7C111 — internal Fleet only. SLA via GJ, ad hoc via PF Invoice, workshop via 9-series. O115 only. no external vendor.
72114 MI-series — Smartrak GPS 29 units PUR 463014 ABN 38 122 889 534. $1,598.60/month FY2023. subscription ends FY2023. not defibrillator.
72114 FY2022-23 Mgmt spike — PKLCC consolidated to svc 20001 in error. $4,830.82 FY2023 and $8,087 FY2022 need recode.
73128 TEC — Total Environmental Concepts ABN 11 600 627 343. sole vendor. all Natural Areas. project-based.
73562 GJ070771 — incorrect move of inv 1246 $14,200 from svc 20151 to svc 20448. must be reversed (item 39).
73114 FY2024 — COP000012 and COP000009 are capital legal fees. should be capitalised not expensed (item 40).
73564 Body2 — 3-year subscription INAU001882 $13,392 at $372/month. monthly GJ recognition via DM#17743446. not a new charge each month.
```

## When to add a trap

Add a trap when **any** of these conditions are met:

- A future session is likely to re-derive the same conclusion if not warned
- The surface narration of the entry contradicts the underlying truth
- Two related entries (DM number, vendor, journal reference) will look like duplicates but aren't
- A vendor name does not match the work being performed (the T&H Levai example)
- An accounting treatment masks operational reality (the 73990 example)
- A periodicity is misleading (the Beenleigh Town Square catch-up example)

## When NOT to add a trap

- Don't add traps for findings. Findings go in the workbook col P / report.
- Don't add narrative or backstory. The session log is for that.
- Don't add traps that only apply to one specific period and won't recur. The trap catalogue is for things that will reach forward into future sessions.

## Cross-referencing

Where a trap connects to an outstanding item, name the item number in the trap line. The 73562 GJ070771 example references "(item 39)" so the next session investigating that journal can find both the trap and the action item.

## Length discipline

If a trap explanation would exceed two sentences, the explanation belongs in the workbook col P, not the catalogue. The catalogue line should be the **summary** that points the reader to the full evidence. Long traps in the catalogue mean nobody reads them.

## Pattern across workstreams

The trap concept transfers across:

- **NA analysis**: vendor/journal/account miscoding traps
- **Forecast HTML**: payload-shape traps (e.g. d3-sankey throwing on negative values), CSS-variable-resolution traps, theme-aware re-render hooks that get missed
- **Concept B PBIP**: schema-rejection traps (FillRule.linearGradient2, selection block in slicer, primaryValueOmitted)
- **Coding review**: systemic miscoding patterns (training catch-all 73544, SaaS-as-subscriptions)

In every case the rule is the same: anything that bit you once and would bite you again belongs in the catalogue.
