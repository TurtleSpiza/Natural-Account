# Handover: consolidated coding-review recode journal

Parks Branch 4090000. Prepared by Spero Karkalemis, Assistant Financial Analyst. 3-Jun-2026.

## Status

The consolidated recode journal is built, balanced, and reconciled, but it is not yet upload-ready. The batch carries 146 lines and nets to $0.00. Four items must be confirmed before it goes to TechOne, and one of those is a hard blocker, so the journal ought to be held until each is closed. Nothing in this pack should be uploaded as-is.

The deliverable is `Parks_4090000_Consolidated_Recode_Journal_3-Jun-2026.xlsx`. It carries four tabs: Summary (KPI cards and three live drill-downs, by stream, by natural account, by PK, each netting $0.00), Consolidated Journal (the full GENJNL PK-ledger), April WINC Detail (39 classified lines), and Verification & Findings (the RAG register reproduced below). Every total is a live formula and the workbook recalculates clean (90 formulas, zero errors).

## What the batch consolidates

The pack is not a single WINC review. It draws together five distinct coding-review streams that had each reached recode stage, and merges them into one balanced GENJNL batch. Each stream balances individually before consolidation, which is the property that lets the combined batch be split back out per Finance's preference if required.

| Stream | Lines | Movement |
|---|---|---|
| WINC 73563 P1 to P10 | 26 | $3,805.50 moved out of 73563 to 73564 / 73512 / 72111 / 72112 / 72113 |
| WINC 73563 Apr-2026 (inv 9901782965) | 12 | $1,187.61 moved out of 73563 to 72111 / 73512 / 73564 |
| 72111 Minor Equipment audit, less J12 | 91 | $21,790.44 moved out of 72111 across 15 destination accounts |
| PCard batch (Officeworks / Flair / Oasis) | 11 | $84.69 booked back into 73563, balance to 72313 / 72248 / 73513 |
| Reali uniforms PK split | 6 | $1,059.76 relocated across PKs, NA 72114 unchanged |

Gross debits equal gross credits at $28,802.17. The net reduction in 73563 across both WINC streams is $4,908.42, being $4,993.11 moved out less $84.69 of diaries and Posca markers correctly booked back into 73563 via the PCard batch. The April invoice itself reconciles to $1,676.26 across 39 Parks lines, of which $1,187.61 was miscoded and $488.65 was correctly sitting in 73563.

## The blocker

Doc46 line J12 recodes twenty desk risers off 72111 to 72313 for $363.64. The same twenty Otto risers are already handled in the PCard batch, where the Officeworks invoice 626529478 is split in full ($398.18, covering twenty Otto risers, two mesh risers, and an adapter). Booking both would double-count the riser relocation, so J12 has been removed from this batch. The removal is the right call only if `TE005091` is the riser line of invoice 626529478. If it proves to be a separate purchase, J12 must be re-added as its two lines and the batch rebalanced. This is arguably the one item that can corrupt the ledger if mishandled, so it ought to be closed first.

## Confirm before upload

| Flag | Item | Finding | Action |
|---|---|---|---|
| RED | J12 / TE005091 | Possible double-count of the riser relocation against Officeworks inv 626529478. J12 currently removed. | Confirm TE005091 is the riser line of that invoice. If a separate purchase, re-add J12. |
| AMBER | Flair Floral $77.27 | Doc45 reverses from 72111, but the P-Card cover slip wrote the cost to 71111 (Full Time Staff). The reversal source must equal the live GL line. | Confirm live GL coding. If 71111, change the reversal source before upload. |
| AMBER | Reali net-movement | NA 72114 is correct throughout; only the PK split is wrong. This stream uses net-movement while the other four use full-reversal. | Confirm Finance accepts net-movement for this batch, or convert to full-reversal. |
| AMBER | Gold Coast parking $6.05 | TE004218, Craig Logan P-Card 16-Jun-2025, miscoded to 73541 Conferences. SEQ parking belongs in 73531. Held out of the batch. | Provide Craig Logan home PK to build the 73541 to 73531 recode line. |
| AMBER | Cabcharge $787.74 | Jan-2026 statement mixes local SEQ legs (73531) and interstate Melbourne / Geelong legs (73533). Held out of the batch. | Provide current GL coding, per-traveller PK, and hotel-to-hotel destinations to split the legs. |

## Carry-forward open item

WINC invoice 9901763737 (Feb-2026, $1,240.45) hits the GL in P9, but the PDF is still absent from the pack, so no line-item classification is possible. It was flagged in the prior findings and remains open. The WINC 73563 audit trail cannot be called complete until that invoice is sighted.

## Methodology and provenance

Full-reversal is the methodology for four of the five streams: the full source line is reversed off the source PK and re-posted across the destination PKs, including a debit back to source for any retained portion. The Reali stream is the exception and uses net-movement, because the natural account (72114 Uniforms) was already correct and only the PK split needed correcting. The mixed format is deliberate and is itself an item for Finance to confirm.

Source documents, all GST-exclusive at line level:

- `Document Line Table (45).xlsx`, TechOne Doc File 1227681, the PCard batch. Balances to $0.00 as extracted.
- `Document Line Table (46).xlsx`, TechOne Doc File 1226060, the 72111 Minor Equipment audit. Balances to $0.00 as extracted.
- `73563_Coding_Review_LineItem_Audit.xlsx`, the prior WINC P1 to P10 audit, Recode Journal sheet.
- `32029386_9901782965_April_2026_.xlsx`, the April WINC source. Parsed by filtering accounts 10179376 (PK000001) and 10428958 (PK000086) and excluding the column-G subtotal rows.
- `april_classified.csv`, the 39-line April classification with suggested accounts and treatment.

Every destination natural account was confirmed to exist in the Chart of Accounts and to be unrestricted. All PKs are valid, and the narration service codes reconcile to the service-section map. The sub-PKs PK000445, PK000083, and PK000493 do not appear in the 101-row parent CSV, but their services (20451 and 20392) are valid. The travel taxonomy was confirmed against the destination rule: 73531 Local SEQ, 73532 Intrastate QLD, 73533 Interstate, 73534 Overseas, 73535 Tollway, 73541 Conferences for registration only, with Gold Coast treated as SEQ.

## Regenerating the workbook

The workbook is reproducible. `build_consol.py` reads the four source workbooks and `april_classified.csv`, rebuilds all four tabs with live formulas, and saves the output. Run it from a directory holding the source files and the CSV, then recalculate with the xlsx skill's `recalc.py`. The J12 exclusion is enforced in the read step, so re-adding J12 means editing that filter and rebalancing.

## Next steps to upload

Close the J12 question first, then the Flair source account, then Finance's format preference for the Reali stream. Pull a fresh GL position for Flair and for the riser line immediately before upload so the reversal sources match the live ledger. Once the three batch items are confirmed, the journal can go to TechOne in the GENJNL upload format, with document and line-number fields stored as text to preserve leading zeros. The two travel items and the Feb WINC invoice are separate workstreams and need not hold the main batch.

The batch is sound and the arithmetic is not in question. The only thing standing between this and upload is the riser double-count and three coding confirmations, and those are answerable without further analysis. It ought to clear review on the first pass once they are closed.

Kind regards,
Spero
