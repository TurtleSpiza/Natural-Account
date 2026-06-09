---
name: techone-output
description: "TechOne Finance One end-to-end journal output for LCC Parks recode and reclass work. Produces canonical narration strings from the 9 invoice categories (mowing, maintenance, hospitality, training, agency, plant, travel, cleaning, general), enforces the 40-character narrative cap with word-boundary splitting, generates valid PK and SL ledger lines with PKNumber and natural-account validation, blocks restricted accounts (PFS-only, Alliance, LWA, system-only, pending-must-zero). Use whenever generating a TechOne narration, preparing a recode journal, validating a batch before submission, reclassing across PKs, or re-extracting NARR_TEMPLATES from a newer AP coding review HTML. Triggers: 'recode journal', 'GENJNL', 'TechOne upload', 'narration template', 'PK ledger', 'SL ledger', '40-character narrative', 'restricted account', 'cross-branch correction', 'extract NARR'. Cross-cutting infrastructure for lcc-coding-review and lcc-na-analysis."
---

# TechOne Output

The end-to-end playbook for TechOne Finance One journal output. Covers two sequential stages: narration string generation (from canonical invoice categories) and GENJNL line validation plus formatting (with all PKNumber, account, and restriction checks). Used by every workstream that produces a journal: branch coding reviews, NA analysis recodes, cross-branch corrections, payroll-related fixes.

## Core principle

Every journal line must pass three validation gates before submission. Skip any of these and Finance rejects the upload, the recode gets stuck in the next batch cycle, and the audit trail breaks.

1. **Narrative discipline.** 40 characters per narrative field, no tabs, no line breaks. Three narrative fields per line, so 120 chars total, but no field can exceed 40.
2. **PKNumber validity.** PK exists in the service map AND matches the service code on the line.
3. **Account validity.** Natural account exists in the chart AND is not restricted (PFS-only, Logan Water Alliance, system-generated only, pending-must-zero).

## Reference artefacts

| File | What it is |
|---|---|
| `narration_templates.json` | Structured extraction of NARR_TEMPLATES, 9 categories with title, fields, account, template_pattern. Template arrow functions converted to f-string-like patterns with {field_name} placeholders |
| `generate_narration.py` | Loads narration_templates.json, exposes `generate(category, field_values) -> str`. Replicates the in-browser AP Coding Review tool's behaviour including conditional segments (e.g. ` Ref: ${po}` only if PO is set) |
| `extract_narr_templates.py` | Parser. Reads LCC_AP_Coding_Review_v7.html, locates the NARR_TEMPLATES const block, extracts each category by regex + brace-counting, converts arrow function bodies to template patterns. Re-runnable when v8+ HTML lands |
| `category_index.md` | Human-readable reference: 9 categories with field lists, suggested accounts, example output narrations |
| `genjnl_template.xlsx` | Pre-formatted upload skeleton with PK Ledger and SL Ledger sheets. Header row, column widths, blue input formatting, restrictions banner. Drop journal lines into rows 6+ |
| `source_prefix_glossary.md` | Two-character TechOne reference prefix glossary (AP/TE/GJ/IJ/RJ/TC/PW/IN/DM) with meaning and expected evidence |
| `narrative_field_validator.py` | `validate_narrative(n1, n2, n3)` and `split_narrative(text)`. CLI: `python narrative_field_validator.py "<n1>" "<n2>" "<n3>"` |
| `pk_validator.py` | `validate_journal_line(ledger, pk_number, service_code, natural_account, amount, refs)` and `load_reference_data()`. CLI: `python pk_validator.py PK PK000017 20374 73126 59439.74` |
| `worked_examples.md` | 25 worked recode journals from the P10 branch coding review across four patterns (cost centre correction, cross-branch SL ledger, natural-account recode, travel split) |

## Cross-references to `_shared/`

| File | Purpose |
|---|---|
| `lcc_chart_of_accounts.json` | Canonical NA reference, restrictions baked in. `pk_validator.py` reads from here |
| `service_section_pk_map.json` | Canonical service code ↔ PK ↔ section map. `pk_validator.py` reads from here |
| `service_section_pk_map.csv` | Same data in CSV form for direct grep |

## The 9 narration categories

| Category    | Title                          | Account | Field count |
|-------------|--------------------------------|---------|-------------|
| mowing      | Contract Mowing / Landscaping  | 73126   | 6           |
| maintenance | Maintenance / Repairs          | 73123   | 5           |
| hospitality | Hospitality / Catering         | 73512   | 5           |
| training    | Training / Conference / Study  | 73544   | 5           |
| agency      | Agency / Temp Labour           | 73214   | 4           |
| plant       | Plant / Equipment Hire         | 74123   | 5           |
| travel      | Travel / Transport             | 73533   | 5           |
| cleaning    | Cleaning / Waste / Sanitary    | 73121   | 5           |
| general     | General Invoice                | (none)  | 5           |

Detail in `category_index.md`. The 9 categories cover the bulk of LCC Parks invoice narrations.

## Stage 1: Generate the narration string

```python
from generate_narration import generate

result = generate('mowing', {
    'narr_vendor':  'Austspray',
    'narr_service': 'Zone mowing',
    'narr_zone':    'Zone 3',
    'narr_period':  'March 2026',
    'narr_po':      'PO 485102',
    'narr_svc':     '20371'
})
# -> "Austspray, Zone mowing Zone 3 March 2026 Ref: PO 485102 Svc 20371"
```

Per-field optionality follows the source templates: fields not provided fall back to placeholder strings ("[Contractor]" etc.), and conditional segments (the ` Ref: ` block, the ` Svc ` block) only appear when the corresponding field is non-empty.

Narrations produced here typically exceed 40 chars by design; Stage 2 splits at word boundaries across the three narrative fields.

For a quick lookup of fields and example output for any category, read `category_index.md` rather than opening the source HTML.

## Stage 2: PK ledger vs SL ledger

### PK ledger (typical Parks recodes)

Use when both source and destination are within the Parks branch (4090000) cost-centre structure.

Columns: `LDG | Account number | Fund account | Resource Group Code | Resource Code | Amount | Narrative1 | Narrative2 | Narrative3`

- `LDG` = `PK`
- `Account number` = PKNumber (e.g. `PK000017`)
- `Fund account` = same PKNumber (mirrors col B)
- `Resource Group Code` = `JOURNAL`
- `Resource Code` = natural account (e.g. `73126`)
- Amount: Dr positive, Cr negative

### SL ledger (cross-branch corrections)

Use when source is Parks and destination is another branch (LCI 18611, Logan Water 16xxx, etc.) or vice versa.

Columns: `LDG | Account number | Fund account | Amount | Narrative1 | Narrative2 | Narrative3`

- `LDG` = `SL`
- `Account number` = full account string `1-<branch>-<NA>` (e.g. `1-18611-73564`)
- `Fund account` = same full account string
- No Resource Group Code or Resource Code columns, natural account encoded in the string

A cross-branch recode pairs a PK ledger reversal line with an SL ledger re-post line.

## Stage 3: Prepare and validate the recode batch

1. **Identify each miscoded line** in the source workbook (typically `lcc-coding-review` workbook col Q "Required action").
2. **Generate the narration** for each line using `generate_narration.py` with the appropriate category. For non-template recodes (one-off corrections), write the narration directly.
3. **Load the GENJNL template** from `genjnl_template.xlsx`.
4. **For each recode, add two lines:**
   - Reversal (Cr at source PKNumber + wrong NA) with negative amount
   - Re-post (Dr at destination PKNumber + correct NA) with positive amount
5. **Split the narrative** within the 40-char cap per field. Use `narrative_field_validator.split_narrative()` to break a long narrative across the three fields cleanly at word boundaries.
6. **Validate every line** with `pk_validator.py`. Resolve any FAIL outputs before proceeding.
7. **Confirm Dr/Cr balance.** Sum of all amounts in the batch must equal zero.
8. **Stage the workbook** for Finance upload. Single workbook, both PK Ledger and SL Ledger sheets populated as needed.

### Validation pre-submission

```bash
# Narrative cap check
python narrative_field_validator.py "Iakopo cemetery deposit refund rev" "Customer refund not auth payment" "Recode to 73412"

# Full PK/account/restriction check
python pk_validator.py PK PK000402 20451 73412 3199.09
```

Both should return `OK`. If either returns `FAIL`, fix before submission.

### Building from existing miscoded lines

A common workflow: a coding review identifies 25 miscodes across multiple accounts. Rather than authoring each journal pair by hand, build a small loop:

```python
import sys
sys.path.insert(0, "techone-output")  # adjust to wherever this skill is unpacked
from pk_validator import load_reference_data, validate_journal_line
from narrative_field_validator import validate_narrative, split_narrative
from generate_narration import generate

refs = load_reference_data()

miscodes = [
    # (source_pk, source_svc, wrong_na, dest_pk, dest_svc, correct_na, amount, category, fields)
    ("PK000402", "20451", "73421", "PK000402", "20451", "73412", 3199.09, "general", {...}),
    ...
]

for src_pk, src_svc, wrong_na, dst_pk, dst_svc, right_na, amt, cat, fields in miscodes:
    # Validate the destination
    issues = validate_journal_line("PK", dst_pk, dst_svc, right_na, amt, refs)
    if issues:
        print(f"FAIL on {fields.get('narr_vendor','?')}: {issues}")
        continue
    # Build the narration and split for the 40-char fields
    base_narr = generate(cat, fields)
    n1, n2, n3 = split_narrative(f"{base_narr} recode {wrong_na} to {right_na}")
    # Append to journal sheet (caller's responsibility)
    ...
```

## Re-extracting NARR_TEMPLATES from a new HTML version

When `LCC_AP_Coding_Review_v8.html` (or later) lands:

```bash
python extract_narr_templates.py path/to/LCC_AP_Coding_Review_v8.html \
    --output narration_templates.json
```

The parser:
1. Reads the HTML file.
2. Locates the `const NARR_TEMPLATES = {` line and matches braces forward to find the end.
3. For each category, extracts `title`, `fields[]`, `account`, and the body of the `template` arrow function.
4. Converts the arrow function body to a template pattern. JS template literals like `` `${f.narr_vendor||'[Contractor]'}` `` become `{narr_vendor|[Contractor]}`. Conditional segments (`${f.po?' Ref: '+f.po:''}`) become structured conditional records.
5. Writes the result as JSON.

Verify after extraction: category count matches expectation (9 in v7), each category has account, fields, template_pattern, and `generate_narration.py` against a known input matches in-browser tool output.

## What this skill does NOT do

- Identify miscodes. That's `lcc-coding-review` (branch-wide) or `lcc-na-analysis` (account-by-account).
- Submit to TechOne. That's a manual Finance step (Amy Forgione, Owen Jensen).
- Validate against budget. That's `lcc-parks-forecast` if the question is about variance impact.
- Track which journals have been processed. That's part of the session-protocol task file, use `lcc_session_protocol/outstanding_items_format.md` (also at `_shared/`).
- Handle free-form narrations outside the 9 categories. The template runtime is template-bound; for one-off narrations, write them directly and pass through Stage 2 validation only.

## Anti-patterns

### Editing narration_templates.json directly
The JSON is generated. Edit the source HTML and re-extract, or send the change upstream so the v8 HTML reflects it. Direct edits drift.

### Drip-feeding Finance one journal at a time
Stage the entire batch in one workbook, validate every line, send to Finance once per session. Finance processes batches more reliably than streams of one-off lines.

### Hand-typing narratives without validation
The 40-char cap is silently truncated. A narrative like "Recode from 73544 Training & Development to 73433 Other Fees & Charges per branch coding review" gets cut at character 40 to "Recode from 73544 Training & Development", losing the destination and rationale. Use `split_narrative()` to break cleanly.

### PK ledger format used for cross-branch
PK ledger only handles Parks-to-Parks moves. A cross-branch correction (Parks → LCI, Parks → Logan Water) MUST use SL ledger format with the full account string. The PK validator's `ledger="SL"` mode enforces this.

### Posting to a restricted account
74181-188 (PFS-only), 73215/73602 (Logan Water Alliance only), and 7BZ11 (system-generated only) are unconditional restrictions. The PK validator catches these. Posting to one of them gets rejected by Finance and creates rework.

### Bypassing the runtime to "save typing"
The runtime handles conditional segments correctly. Manually building narrations from the JSON's pattern strings without the runtime drops conditional logic and produces "Ref: " segments with empty values.

## Cross-skill flow

```
Vendor invoice / contract document / lcc-coding-review finding / lcc-na-analysis finding
              │
              ▼
techone-output [THIS SKILL]
   Stage 1: Generate narration string from category + fields
   Stage 2: Choose PK or SL ledger format
   Stage 3: Validate (40-char cap, PKNumber, account, restrictions, balance)
              │
              ▼
lcc-finance-batch-email (compose Finance email with the journal attached)
              │
              ▼
Finance team (Amy Forgione, Owen Jensen) submits to TechOne
```

The session-protocol artefacts in `lcc_session_protocol/` (also at `_shared/`) track which journals are in flight and which have closed across this chain.
