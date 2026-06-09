# LCC Coding Review — Rebuild Notes

**Date:** 8 May 2026
**Source of truth:** `1778210808294_Chart_of_Accounts___Consultancy___FBT___Travel_ETC.pdf` (33 pages)
**Handover:** `Skills_FBT_Hospitality_Coding_Rebuild_v2_Handover.txt`

This file documents every decision the rebuild made, every TODO flagged for human review, every conflict found between the PDF and the prior skill files, and the recommended next-session checklist. The point is to let Spero verify the rebuild without re-reading 700 accounts.

## Files written / modified

| File | Change | Records |
|------|--------|---------|
| `accts.json` | Enriched with PDF descriptions; added `pdf_desc`, `source` keys | 242 (unchanged count) |
| `_shared/lcc_chart_of_accounts.json` | Populated `description`, added `fbt_flag`, `consultancy_flag`, `travel_flag`, `restrictions`, `source` | 679 (unchanged count) |
| `full_chart_of_accounts.json` | Portable copy of the above inside the skill directory | 679 |
| `fbt_classification.json` | NEW — 24 scenarios, Reason A-L glossary, four-factor Reason H, internal catering, GST codes, FBT 50/50 method | 24 scenarios |
| `fbt_reason_codes.md` | NEW — markdown rendering of Reason Codes A-L | — |
| `hospitality_scenarios.md` | NEW — markdown allocation table (24 sub-rows from 19 numbered scenarios) | — |
| `consultancy_guide.md` | NEW — four-element consultant test, consultant vs contractor, five 73600-series accounts | — |
| `overseas_travel_guide.md` | NEW — 73531-73534 destination rule, meals-during-travel exception, LGR s.196 reporting | — |
| `service_section_pk_map.csv` | Portable copy of canonical service map | 101 rows |
| `service_section_pk_map.json` | Portable JSON copy | 101 rows |
| `_shared/service_section_pk_map.csv` | Re-saved with column order ServiceCode,ServiceName,PKNumber,Section (canonical 4-col) | 101 rows |
| `_shared/service_section_pk_map.json` | Regenerated from canonical CSV | 101 rows |
| `SKILL.md` (lcc-coding-review) | Description rewritten — added FBT, consultancy, travel triggers; named the new guide files | — |
| `SKILL.md` (techone-genjnl-format) | Description rewritten — leads with use case, names restricted accounts | — |
| `SKILL.md` (pbir-schema-rules) | Description rewritten — leads with the symptom (error message) | — |

## Decisions made

1. **Both descriptions retained.** The existing accts.json `desc` field was operational and tight (e.g. "Permanent full-time wages via payroll. Wages when on leave not charged here."); the PDF Data Dictionary is descriptive (e.g. "Wages for days at work and RDO's for permanent full time employees paid via payroll..."). Both are useful. Decision: keep `desc` as-is for operational cues, add `pdf_desc` as the canonical authority. Verdict cited as conflict in 111 accounts; not a regression — both fields coexist.

2. **PDF flags applied additively.** `fbt_flag`, `consultancy_flag`, `travel_flag` added to the 679-account chart only on the accounts the PDF explicitly tags (FBT 73511/73513/73514/7B221/7B223 etc.; Consultancy 73601/73603/73605/73607/73609/73602; Travel 73531-73535). No flag silently inferred.

3. **Restricted accounts populated.** Codified from the v1 handover and existing skill text: 73215 (Alliance), 73602 (LWA), 74181-74188 (PFS only), 7BZ11 (system-only), 71000/72118/72119 (pending-must-zero).

4. **fbt_data.json untouched.** The existing 24-entry operational lookup is on the do-not-touch list. Scenarios in the new `fbt_classification.json` cross-link to it via the `scenario_to_fbt_data_id_map` field.

5. **Service map column order normalised.** Existing `_shared/service_section_pk_map.csv` had columns in `ServiceCode,ServiceName,Section,PKNumber` order. Canonical (per zip) is `ServiceCode,ServiceName,PKNumber,Section`. Reordered to canonical, no row changes. Diff confirmed 0 data conflicts across 101 rows.

6. **Marsden Stores reconciliation deferred.** The existing `_shared/marsden_stores_inventory.json` (317KB, 750 items, 79 categories) is structurally correct. The zip txt file is alphabetised by category and matches the existing JSON. No regeneration needed unless a v2 catalogue drops. Skipped.

7. **Portability rule applied.** Every reference data file the skill cites is duplicated inside the skill directory. The 270KB chart of accounts now lives at both `_shared/lcc_chart_of_accounts.json` AND `lcc-coding-review/full_chart_of_accounts.json`. The service map similarly. No skill content references absolute local paths — confirmed by sweep (CHECK 6).

## TODOs flagged (human review needed)

### Real account misalignments — accts.json names disagree with PDF (PRIORITY 1)

These six accounts have `desc` and `name` in `accts.json` that contradict the PDF Data Dictionary. The numbers may have been copied from a different chart version or transposed during the v7 HTML harvest. Spero should review each and either correct the local skill file or confirm the v7 name was correct for an LCC-specific reason.

| Code | accts.json name | PDF name | Likely truth |
|------|-----------------|----------|--------------|
| `74114` | Water Truck — External Hire | Wagon 6 cylinder | **PDF — accts.json wrong** (74114 is Wagon 6 cylinder; the 7414x series follows 74111 Bus, 74112 Passenger Vehicles, 74113 Van, 74114 Wagon 6 cyl, 74121+ specialised plant) |
| `74127` | Vacuum Excavation Truck — External Hire | Tractor | **PDF — accts.json wrong** (74127 is Tractor; vacuum truck has a different code or is internal-only via 7C119) |
| `74173` | Safety Equipment (Plant) — External Hire | Safety Equipment (general) | **PDF** (74173 is general safety equipment, not plant-hire-specific) |
| `74187` | Registration & Licences | Rego, Licences & Third Party | PDF wording is fuller; minor |
| `73562` | Multi-Media Services / Photography | Multi-Media Services | PDF wording shorter; minor |
| `73605` | IT Consultancies | Information Technology (IT) Consultancies | PDF wording fuller; minor |

**Recommendation:** correct the three rows above (74114, 74127, 74173) in `accts.json` to match the PDF, and accept the minor naming refinements for the other three at the next pass.

### Chart split failures (low priority)

18 accounts in `_shared/lcc_chart_of_accounts.json` had a name vs PDF-raw mismatch that caused the prefix-match split to fall back to using the full raw text as `description`. The descriptions are still accurate, just slightly polluted with the leading PDF name. Examples: 61222, 61422, 65211, 65213, 66112, 66121, 66122, 6E223, 71995, 72995. See `_enrich_chart_audit.json` for full list. Manual cleanup is cosmetic.

### Cross-skill TODOs

- `narr-templates-extraction` hospitality category has `73512` hardcoded. Should be cross-linked to `fbt_classification.json` so a journal narration with alcohol or off-site context warns to use `73511`. Not done in this rebuild — out of scope.
- `interactive-html-decision-tool` should bundle `fbt_classification.json` as an example dataset so the variant pattern is fillable. Not done — out of scope.
- `techone-genjnl-format` should warn if a journal line targets `73511` without a Reason code. Not implemented — design noted.

## Conflicts found (PDF vs prior skill content)

- **111 accts.json `desc` entries differ from PDF wording.** All retained side-by-side via `pdf_desc`. See first 50 in `_enrich_accts_audit.json`. Not a regression — operational `desc` keeps the discipline of "use for / not use for" cues that the PDF doesn't bother spelling out.
- **227 chart-of-accounts entries are PDF-silent** (mostly current asset / liability / equity codes that the Data Dictionary doesn't cover). These keep `source: 'PDF Natural Accounts List only (no Data Dictionary entry)'`. Expected — the Data Dictionary covers Revenue and Expense accounts in detail; balance-sheet accounts are listed by code only.
- **0 conflicts in service map.** All 101 rows reconcile across the canonical CSV and the existing _shared CSV.

## Validation results

| Check | Result |
|-------|--------|
| 1. Account count preservation (accts.json 242, chart 679) | **PASS** |
| 2. FBT scenario reconciliation (24/24, all reason codes A-L valid, all account refs resolve) | **PASS** |
| 3. Systemic miscodes / confusion pairs reference real accounts | **PASS** (8 false positives confirmed as service codes / invoice numbers / intentional non-existent flags) |
| 4. Schema diff is additive only (added: `pdf_desc`, `source`, `flags`, optional `todo_pdf_split`) | **PASS** |
| 5. Service map reconciliation (canonical adopted, 0 row conflicts) | **PASS** |
| 6. Portability sweep (zero local paths in skill content) | **PASS** |
| 7. SKILL.md descriptions all <1024 chars | **PASS** |

## Recommended next-session checklist

1. **Fix accts.json names for 74114, 74127, 74173** to match PDF. Re-run `extract_ap_review_objects.py` ingestion if Parks Finance AI v7 HTML is the source of these errors and a v8 needs to encode the correction.
2. **Confirm `74187` Registration & Licences** is the LCC-shortened name. If the longer "Rego, Licences & Third Party" is what Finance uses on cover slips, adopt it.
3. **Decide whether to suppress the v7 `desc` field** in favour of PDF-only on certain accounts where the v7 desc is operationally tight but contradicts PDF wording (e.g. 73214 says "Hays/Chandler Macleod/Adecco" but PDF doesn't name vendors). Decision needed: keep both, or move v7 detail into `rules` and let `desc` mirror the PDF.
4. **Marsden Stores inventory** — bundled at `marsden_stores_inventory.json` (317 KB) and `.csv` (57 KB). Reconcile against any v2 catalogue drop.
5. **Cross-link `narr-templates-extraction`** so the hospitality narration template references `fbt_classification.json` and warns when alcohol or off-site is in the narration text.
6. **Bundle `fbt_classification.json` into `interactive-html-decision-tool`** as an example dataset so the FBT decision tree variant is fillable.
7. **Add restricted-account warning to `techone-genjnl-format`** — refuse to produce a recode line targeting `73215` without a reason, refuse `74181-188` for any non-PFS branch, warn on `73511` lines without a Reason code.
8. **Re-zip `lcc-coding-review.zip`** and re-upload to claude.ai web (delete-then-upload).
9. **Test on claude.ai web** after re-upload: `"what's the right account for staff morning tea on premises with no alcohol"` should land on `lcc-coding-review` and answer "73512, Reason B (refreshment, not entertainment), GST code C, FBT exempt — see hospitality_scenarios.md scenario 6 / PDF p68."

## Audit artefacts

Generated during the rebuild and stored alongside the source PDF (outside this skill, on the local build machine):
- `_pdf_extracted.txt` — full PDF text (100 KB)
- `_pdf_dictionary_split.json` — parsed Data Dictionary entries with name/desc split (452 entries with page numbers)
- `_enrich_accts_audit.json` — accts.json enrichment counts (241 enriched, 1 PDF-silent, 6 split TODOs) and conflict list (111 desc differences)
- `_enrich_chart_audit.json` — chart enrichment counts (452 enriched, 227 PDF-silent) and 18 cosmetic split failures
- `_servicemap_audit.json` — service map reconciliation diff (0 conflicts across 101 rows)

These can be regenerated by re-running the rebuild script against the PDF. They are not bundled inside the skill because they are build-time audit logs, not runtime references.

## Source page reference (for citations in skill content)

| Section | PDF pages |
|---------|-----------|
| Natural Accounts List (codes only, 679 accounts) | 1-13 |
| Data Dictionary for Revenue and Expenses (descriptions) | 14-29 |
| Hospitality & Entertainment Guide allocation table | 30 (PDF p68 in source numbering) |
| Reason Codes A-L glossary + 50/50 method | 31 (PDF p69) |
| Consultancy Guide | 32 (PDF p71) |
| Overseas Travel Guide | 33 (PDF p72-73) |
