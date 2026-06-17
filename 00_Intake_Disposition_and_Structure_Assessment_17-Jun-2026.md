# Intake disposition and structure assessment — 17-Jun-2026

Companion to the handover. Every intake folder was opened, every held document was verified and given a disposition, and the repository structure was assessed for quality. The register remains the authoritative account-level state ($560,824.33 ex-GST, 23 accounts); this note records what came in and where it went.

## 1. Structure assessment (all folders)

**Sound.** The repository is well organised and the integrity discipline holds.

- **Deliverables** sit at the root (`00_*` control files) and in per-account `NA<acct>_*` sets plus numbered workstream folders `02_NA73211_Minor_Contracts` through `08_Materials_Recode_PK000372` (new this pass). Evidence is one folder per account, one file per line.
- **Raw intake** is correctly fenced off the manifest: `New/` (un-manifested intake), `Related/` (cross-reference supports), `_Sources_<date>/` (dated received documents), `_CarryForward/` (prior journals). This matches the layout rule.
- **Hygiene is clean.** `.gitignore` already excludes `__pycache__/`, `*.pyc`, `.DS_Store` and Office lock files; none are tracked. The local `__pycache__/` is ignored, not committed.
- **Manifest integrity:** every deliverable carries a SHA-256 in `00_Bundle_Manifest.csv`; the strict verify and the GitHub Actions workflow both pass.

**One observation, not a fault:** five dated `_Sources_*` folders (9, 10, 11, 16, 17-Jun) now coexist, ~110 MB. They are legitimate provenance and correctly un-manifested, but a future session could consolidate the superseded ones once their contents are fully dispositioned (this note begins that work).

## 2. Intake disposition

### Completed this pass

- **Materials Journal intake (37 files) — the major result.** A posted TechOne reclassification (Document Reconstruction XRef 934000000001, PK000372 svc 20551 Fuel Reduction Burn), directive-authorised by Gihani 16-Apr-2026. Verified: 8 pairs, nets $0.00 exactly ($42,841.53), direction correct. Staged as workstream `08_Materials_Recode_PK000372/` with a verification record. It is **already posted**, so it is evidenced, not re-posted, and the CN-23167 batch is unchanged.
  - **EMU INV-0367/0389/0395 ($26,414.08)** SIGHTED as the 72111→73212 legs (new evidence).
  - **Ausecology INV-4029/4030 ($14,840) and EWN 14566/14768** — the named outstanding GAP "Ausecology INV-4029/INV-4030 via GJ078960" is CLOSED; EWN INV-14768 ($375.00) and the EWN/Ausecology 73211 legs are sighted.
  - **Wallum 00059013 ($276.80)** also closed from this intake. NA73211 now has 4 evidence gaps left (was 6).
- **Kinatico intake (5 invoices, 73140) — VERIFIED, correctly held.** ABN 25 111 728 842 checksum PASS, GST exact to the cent on all five. They total $7,996.86 ex-GST, 2.16x the 73140 SE2 balance of $3,703.03: the monthly invoices bill the whole council, so the Parks slice cannot be attributed without the FY26 73140 ledger extract. The hold was the right call; the documents are now verified rather than merely held.

### Dispositioned, needs a Spero ruling (not a clean sighting)

- **Bushcare INV-18177 ($1,137.45, 72411→74114) and INV-17401 ($1,050.00):** Materials legs whose source invoices are not in the bundle; INV-17401 is in the summary but not the posted journal. Recorded as GAPs for audit; the directive does not hold the posted line.
- **Broad Intake SE2 (35 files):** fresh plant-supply and contract invoices (8 Ibrox Park nursery, Waterford ×2, CINC ×2, Nuway) that enlarge the 73211/73126 and 73212 evidenced base but match no *named* gap and need the floor-test ruling (Waterford LCCWLS010 $36,315.14 is over the $20,000 73211/73212 boundary). Two Linkt fleet tollway invoices belong to 73535, which is not yet in review scope. The Trailbuilders payment slip (USD $450 vs GL AUD $626.48) is a currency/phantom-ITC flag, not a tax invoice — held.
- **Six IPWEA documents in `New/`** (R58890 $2,000; invoices 40309/40310; QNT receipts $1,210 and $2,475 ×2): these are the "unplaced, attendees not in Parks" set already recorded in the outstanding register. Confirmed identical; they remain unplaced pending Spero confirming any Parks attendee. No in-scope line matches.

### Raw intake, no in-scope match (left as intake)

- `New/` Officeworks invoice ($521.00 incl), Journal Support consolidated-PK invoice (702344), and two `scan_wilsonai` PDFs (image-only, no text layer — need OCR). None maps to a current in-scope Parks line.
- `New/Branch IT Purchases Feb 26.xlsx` is the 73564 SR-backup schedule already cited as closing SR235810; working paper.
- `Related/` six files (Bunnings BBQ 72111, Daily Blooms 73553, Empire chair 72313, Org Risk INV-251010-2 73601, Reali uniforms 72114) are cross-reference supports for already-sighted lines.
- The three processed bundle zips in `_Sources_17-Jun-2026/` (NA73122, NA73211, NA73544 Doc-Reconstruction) are archived provenance for completed workstreams.

## 3. Net effect

No dollar movement (every item this pass was a sighting or a verification, not a recode). Evidence coverage improved: NA73211 down to 4 gaps, NA73212 gains the EMU legs, NA73140's hold is now evidenced, and the Materials reclassification is documented and verified. Items needing a ruling are listed above and in `00_Outstanding_Evidence_and_Actions.md`; none is silently cleared.
