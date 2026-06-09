# LCC Session Protocol — shared templates

The discipline that runs every long-lived LCC workstream. Used by `lcc-na-analysis` (34 sessions and counting), the LCC_Parks_FY26_Forecast HTML feature builds (queue of 6 features F5-F10), and the Concept B PBIP rebuilds. Same shape across all three.

## Why it exists

Sessions end. Context evaporates. The next session needs to know: where did we leave off, what is in flight, what is blocked on someone else, what traps are documented, what is closed and shouldn't be reopened. Without the protocol, every session re-derives state from chat history. With it, the next session reads four files and is current.

## Files in this folder

| File | What it is |
|---|---|
| `session_header_template.md` | The four lines at the top of every task file. Last confirmed, next in queue, workbook/file version, open Finance request count. |
| `outstanding_items_format.md` | Numbered items, starring convention for batched Finance queries, the rule that closing preserves original numbering. |
| `traps_catalogue_format.md` | One-line-per-trap convention. Read at session start to avoid re-investigation. |
| `session_log_format.md` | Per-session entries: sN: changes, file version bump, key confirmations. |
| `closed_log_format.md` | Resolution log. Closed items keep their original number, never get renumbered. |

## Rules of the protocol

1. **One source of truth per workstream.** Workbook col P (NA analysis) or feature HTML (forecast builds) is the source of truth for findings. Task file is the coordination layer only. Don't duplicate findings narrative across both.

2. **Update the artefact and the task file in the same step.** Never one without the other. The task file at end of session must reflect the workbook at end of session.

3. **Increment the version on every structural change.** Workbook v9_29 → v9_30 not v9_29_revised. File version is the breadcrumb that links the task file to a specific workbook state.

4. **Star items destined for batched Finance email.** Never drip-feed Finance. All starred items go in one consolidated email per session.

5. **Closed items keep their number.** Item 33 closed in session 27 stays as item 33 in the closed log. Renumbering breaks every cross-reference in prior session logs.

6. **Read the traps catalogue first.** Before progressing the next-in-queue item, scan the traps. Every trap was documented because someone re-investigated something that was already resolved.

## Adopting the protocol for a new workstream

Copy the five template files into the workstream's working folder, fill in the workstream-specific bits, and start logging from session 1. The Concept B PBIP handovers (v3, v4) and the Forecast HTML handover v7 are worked examples.
