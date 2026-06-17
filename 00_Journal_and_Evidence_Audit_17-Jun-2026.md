# Parks 4090000 NA Review — Full Journal and Evidence Audit, 17-Jun-2026

> **Merge correction note, 17-Jun-2026 (lineage reconciliation).** After this audit was written the NA7B213 immunisation recode (34 lines, batch still nets $0.00) was merged in from the PR-8 lineage, so the live journal is now **367 lines**, 16 streams, 13 account recodes. The EVID overlay (`00_Live_Recode_Journal_EVID_17-Jun-2026.xlsx`) was extended to 367 rows: the 34 NA7B213 lines are stamped **INTAKE-HELD** — the whole-branch immunisation recharge source is held as intake at `_Sources_16-Jun-2026/NA7B213_Intake/Internal_Medical.XLSM` (row 23), carried from the PR-8 lineage. It is an internal charge with no per-line external invoice, so the evidence limb stays **AMBER** pending Spero sighting it to each officer line; the 3 ACCA-split deficient lines remain the only held-source-absent lines. The arithmetic and structural verdicts below (net $0.00, zero restricted postings, zero chart breaches, zero cap breaches) hold on all 367 lines. The 333-line figures in the body are the pre-merge point-in-time state.

**Verdict: the live recode journal is arithmetically and structurally clean — 333 lines, batch nets $0.00, zero restricted-account postings, zero narration-cap breaches, and it rebuilds byte-faithfully from its source atoms. Every line is now stamped with a unique evidence-source identifier (EVID). Three lines (the ACCA Education split, $1,181.82) carry no held evidence; 114 lines rest on evidence held only inside a consolidated binder, not as standalone files; and 12 lines sit on PKs absent from the installed service map. None of these are arithmetic faults; all are evidence/crosswalk gaps, recorded honestly.**

The bundle was intaken from the 9 native zips, merged to one tree (601 files), and strict-verified before any work: **424 rows, 424 ok, 0 drift, 0 missing, 0 orphan — PASS.**

## 1. Journal audit — the hard gates

- **Batch balance.** Gross debits $43,259.43, gross credits -$43,259.43, **net $0.00**. Every one of the 15 streams nets $0.00 independently; no stream relies on another to balance.
- **Derived integrity.** The committed `00_Live_Recode_Journal.xlsx` was re-derived from the 11 contributing `NA*_GENJNL_Recode.txt` atoms via `build_live_journal.py`. The rebuild matches the committed journal line-for-line, **0 differing rows**. The journal is not hand-edited; NA73122 correctly contributes 0 lines (NIL recode).
- **Restriction check.** **0** lines post to a restricted account. No PFS-only (74181-188), no Alliance (73215/73602), no system-only (7BZ11) destinations.
- **Chart validity.** **0** lines carry a natural account absent from the 679-account chart. All Resource (NA) codes resolve.
- **Narration discipline.** **0** of the 999 narrative fields (333 lines x 3) exceed the 40-character cap; **0** contain tabs or line breaks.
- **Direction.** Every cross-NA recode posts source-NA negative, destination positive, consistent with its narration. One deliberate exception is correct, not a regression:
  - **72111 SET 3 (scrap-sale income), the sign is intentional.** $448.00 of scrap-plaque income sat as a credit reducing 72111 expense. Moving it out debits 72111 (+$448.00, reversing the contra) and credits 64411 revenue (-$448.00). Revenue is a credit, so the "reversed" sign is the correct accounting direction.
- **Net-movement streams.** 72114 Reali, 73544 Training and 73564 sub-batch B net $0.00 on the **same** NA — pure PK reattributions where the coding is already right and only the PK split is wrong. Correct use of net-movement per the rules.

## 2. Journal audit — the one Limb 1 finding

> **18-Jun update (PK-map):** PK000083 and PK000445 resolve to cost code 20451, PK000493 to 20392, from the 18-Jun 72111 ledger (canonical). Only PK000510/PK000511 remain unmapped. See 00_Analysis_Findings_PKmap_73123_18-Jun-2026.md.

**12 lines sit on PKs that are absent from every installed map** (service_section_pk_map, pk_map, employee_pk_map — 95 PKs total). The service/officer crosswalk cannot be confirmed for these from canonical data. This is the same class as the known PK000510/511 gap.

| PK | Lines | Streams |
| --- | --- | --- |
| PK000493 | 21, 22, 308, 309 | 72312->72313 Furniture; Carried 3-Jun |
| PK000445 | 283, 284 | Carried 3-Jun |
| PK000083 | 285-290 | Carried 3-Jun |

These are net-movement / carried lines where the recode corrects the NA, so the gap is an evidentiary crosswalk note, not a blocker. **Action: obtain the canonical PK record for PK000083, PK000445, PK000493 (and the carried PK000510/511) and extend the installed map.**

## 3. Evidence audit — sources, hashes, completeness

- **204 evidence files on disk** across 18 `*_Evidence` trees; **22 evidence manifests** read; **285 manifest rows** reconciled.
- **SHA-256 verification: 142 manifest rows carried a listed hash; all 142 recompute exactly. 0 mismatches.** A further 77 present files carried no listed hash and were fingerprinted fresh for the register.
- **Evidence Source Register built: 322 distinct sources** — 219 present on disk, 103 recorded-but-absent (flagged).

**The material evidence finding — NA73128 manifest is out of sync with its folder.** The NA73128 manifest lists ~56 individual TCB invoice PDFs (L01-L62), each with a SHA-256 and a SIGHTED status, but the folder holds only 3 files. The per-line PDFs were consolidated into `NA73128_SecondIntake_Binder_C00216123.pdf` (present, 2 MB) and the manifest rows were never reconciled. The underlying evidence survives inside the binder, but its 56 per-line SHA-256 fingerprints are dangling — they point at standalone files that no longer exist, so they cannot be hash-verified individually. **Action: either re-extract the 56 standalone PDFs, or restate the manifest rows to point at the binder (and ideally a page anchor) so each TCB line has an addressable, verifiable source.** 114 journal lines depend on this binder.

**Other recorded gaps (all known, none new surprises):**
- **NA73122 — 4 Cleanaway charge-months unsighted** (Aug, Oct, Nov 2025; Mar 2026). Consistent with the AMBER/NIL-recode position; NA73122 has no journal lines, so no recode is exposed.
- **Declared GAP markers — NA73211 (22 rows) and NA73601 (8 rows)** are intentional audit-GAP placeholders for unsighted invoices, correctly recorded per the evidence rule, not missing-file errors.
- **37 orphan files** are present inside `*_Evidence` folders but absent from their per-account evidence manifest (ledger extracts, ABN PDFs, coverslips, WINC monthly statements, Uber/travel support, DocReconstructions). They are bundle-manifested (the 424/424 holds) but not per-account-manifested. **Action: extend the per-account evidence manifests to list them, or annotate them as supporting context.**

## 4. The deliverable — a unique identifier on every line

Every evidence source has a stable **EVID** (`EVID-0001`...`EVID-0322`), keyed on SHA-256 where available and on path otherwise. Each of the 333 journal lines is stamped with the EVID(s) of its supporting source, plus the strongest sighting status held and a deficiency flag.

**Resolution method.** A specific per-line invoice token in the narration (INV number, doc/PIK/TE/SC/RL/INAU/IJ/GJ reference) maps the line to its exact evidence file; where the narration carries no invoice number (WINC item lines, carried Doc46/PCard journals, the TCB binder), the line maps to its governing consolidated source. Non-discriminating tokens (account numbers, year strings, the batch id) were excluded to prevent false attribution.

| Attribution | Lines |
| --- | --- |
| Per-line file (specific invoice/document) | 194 |
| Consolidated stream source | 139 |
| No source at all | 0 |

**Line evidence status (strongest held):**

| Status | Lines | Meaning |
| --- | --- | --- |
| PRESENT | 168 | Standalone file on disk, hash-verifiable |
| CONSOLIDATED | 114 | Held inside TCB binder C00216123, not standalone |
| PRESENT* | 48 | On disk but not in the per-account manifest (orphan) |
| GAP | 3 | No held source — see below |

## 5. Evidence-deficient lines (the only journal lines with no held evidence)

**3 lines, all in 73544 Training PK splits, the ACCA Education INV-11404 split, $1,181.82 ex-GST, nets $0.00:**

- L159 73544 -$1,181.82 / L160 73544 +$590.91 / L161 73544 +$590.91 — a same-NA PK reattribution, so the coding limb is fine; the ACCA Education invoice itself is not held. Consistent with the handover's outstanding 73544 journal backups. **Action: sight ACCA Education INV-11404 before clearing the evidence limb on these three lines.**

The Harreman / Papatheodosi / Petersen chargeback lines (L153-L158) do hold present evidence (GJ079650 reconstruction plus the chargeback list, approval and confirmation); an earlier worst-case read over-flagged them and has been corrected to best-available status.

## 6. Tax limb

The journal lines do not themselves carry ABNs; tax compliance is evidenced per source in the per-account verification records and the **GST Errors Register (~30 rows)**, per the mandatory GST-errors rule. The NA73128 TCB stream carries 16 lines flagged `SIGHTED GST ERROR` (the disclosed-GST-versus-booking pattern, GSTE entries) — recorded on the register, not only in line notes. No journal line was cleared on tax off an unsighted source.

## 7. Findings register

1. **NA73128 manifest desync (high).** 56 per-line TCB SHA rows dangle; evidence consolidated into binder C00216123. 114 journal lines affected. Reconcile the manifest.
2. **Evidence-deficient lines (medium).** L159-161, ACCA Education INV-11404, $1,181.82, no held invoice. Sight before clearing.
3. **Unmapped PKs (medium, Limb 1).** PK000083/000445/000493 (and carried 000510/000511) absent from installed maps; 12 lines. Extend the map.
4. **Per-account manifest orphans (low).** 37 on-disk evidence files unlisted in per-account manifests. List or annotate.
5. **NA73122 unsighted months (low, known).** 4 Cleanaway charge-months; NIL recode, no exposure.

## 8. What was not changed

This is a read-and-overlay audit. **No manifested deliverable was edited**, so the bundle manifest still strict-verifies 424/424. The three audit artefacts are new overlays. Folding the EVID column into `00_Live_Recode_Journal.xlsx`, reconciling the NA73128 manifest, and updating the register are Mode B incorporation steps, to be run on your go with the standard sequence: edit, regenerate `00_Bundle_Manifest.csv`, `verify_manifest.py --strict`, dated correction note, re-zip.

## Deliverables

- `00_Live_Recode_Journal_EVID_17-Jun-2026.xlsx` — all 333 lines with EVID(s), strongest evidence status, deficiency flag, and source filenames.
- `00_Evidence_Source_Register_17-Jun-2026.xlsx` — 322 sources: EVID, status, account, file, SHA-256, GL ex-GST, invoice incl GST, journal lines supported.
- `00_Journal_and_Evidence_Audit_17-Jun-2026.md` — this report.

---

## Correction, 17-Jun-2026 (later same day)

Two of the five findings above are revised after the `Document_Reconstruction_96` / `Materials_Journal` intake:

- **Finding on the 3 deficient ACCA lines (L159-161) is withdrawn.** The ACCA INV-11404 invoice was already held at evidence row L10 (SHA 6126cdf2) since 10-Jun. The deficiency flag was a matcher miss in this overlay's build, not a true gap. Lines 159-161 are relinked to EVID-0148, status PRESENT, and the deficiency is cleared. There are now **zero** evidence-deficient lines in the journal.
- **The six outstanding 73544 internal journal backups are closed.** IJ074222, GJ078710, GJ078895, GJ077155, GJ079267 and GJ078296 are sighted as balanced Document Reconstruction exports (each nets $0.00), folded at L23-L28 and manifested.

Findings 2 (NA73128 binder desync), 3 (12 unmapped PKs) and 4 (37 orphans) are unchanged. The bundle was re-manifested and strict-verified after these edits.
