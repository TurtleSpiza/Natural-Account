# Session Header Template

The four lines at the top of every task file. Rewrite at the **end** of every session, not the start. The header reflects state as the session closes, ready for the next session to pick up cold.

## Template

```
{Workstream Name} | Task File {version}_s{session number}

SESSION HEADER — rewrite at end of every session
-------------------------------------------------
last confirmed:  {what was completed in the most recent session, with reference}
next in queue:   {what the next session should pick up, with any blockers named}
workbook:        {workbook filename at current version, e.g. NA_Analysis_v9_29.xlsx}
report:          {associated report file if applicable, e.g. LCC_Parks_NA_Report_Draft_S10.docx}
accounts:        {progress counters, e.g. ~54 confirmed | ~12 pending | 47 negligible/closed}
```

## Worked example (from NA Analysis v9_s34)

```
LCC Parks — NA Analysis | Task File v9_s34

SESSION HEADER — rewrite at end of every session
-------------------------------------------------
last confirmed:  73123 Maintenance Services FY2024 listing added (s34)
next in queue:   73131 Insurance Premium — needs Finance listing first (item 6)
workbook:        NA_Analysis_v9_29.xlsx
report:          LCC_Parks_NA_Report_Draft_S10.docx
accounts:        ~54 confirmed | ~12 pending | 47 negligible/closed
```

## Worked example (from Forecast HTML handover v7)

```
LCC PARKS FY2026 FORECAST — SESSION HANDOVER v7

STATUS: F10 in progress. Structural scaffolding done in v3_F10_WIP.html but
SANK* JS namespace not yet written. File will render a blank white box inside
§05 until the JS is added — do not ship as-is.

CURRENT FILE
------------
LCC_Parks_FY26_Forecast_v3_F10_WIP.html   (4,336 lines, 271.7 KB)

ATTACH TO NEXT CHAT
-------------------
Required:
  - This handover                     LCC_Parks_Session_Handover_v7.txt
  - Current WIP HTML                  LCC_Parks_FY26_Forecast_v3_F10_WIP.html
  - Payload (unchanged)               payload_v3.json

FIRST MESSAGE TO SEND: "continue F10 — write the SANK JS"
```

## Variants

### NA analysis variant
Counts are progress against a finite known set (accounts, journals, finance items). Use exact numbers.

### Forecast HTML variant
Status is feature-state-in-flight, with the explicit "do not ship as-is" flag where applicable. Always names the current WIP file, the attachments needed for next session, and the literal first message to type.

### PBIP build variant
Adds the build pipeline state: which step in `build_concept_b.py → fix_pbip.py → validate → zip` was last completed, and the open IT/external blockers (e.g. Azure subscription pending).

## What goes in `next in queue`

Be specific enough that the next session can act without re-deriving state. "73131" is not enough. "73131 Insurance Premium — needs Finance listing first (item 6)" is correct: names the artefact, names what's blocking it, and cross-references the item number in the outstanding-items list so the next session knows where to look.

## What does NOT go in the header

- Findings narrative. That lives in the workbook col P or the report. The header is coordination only.
- Long backstory. The session log is for that.
- Speculation about future work. That's the queue, not the header.
