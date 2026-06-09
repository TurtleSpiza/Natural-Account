---
name: narr-templates-extraction
description: NARR_TEMPLATES extraction and runtime. Parses the 9 narration-builder categories from LCC_AP_Coding_Review_v7.html (arrow-function template literals that don't parse as JSON5) into structured JSON, plus a Python runtime that generates TechOne narration strings from category and field values. Use whenever generating TechOne journal narrations programmatically (mowing, maintenance, hospitality, training, agency, plant, travel, cleaning, general invoice), inspecting canonical narration patterns, needing the suggested account code per category, or re-extracting NARR_TEMPLATES from a newer AP coding review HTML. Triggers on 'NARR_TEMPLATES', 'narration template', 'generate narration', 'narration builder', 'TechOne narration', 'mowing narration', 'extract NARR'. Distinct from techone-genjnl-format which validates the 40-character cap; this skill produces the string first.
---

# narr-templates-extraction

The skill that parses NARR_TEMPLATES from the LCC AP Coding Review HTML and provides a Python runtime that generates the same narration strings the in-browser tool produces. Solves the v1-handover-deferred problem: arrow-function template literals don't parse as JSON5, so a custom JS-fragment parser is required.

The 9 categories cover the bulk of LCC Parks invoice narrations: mowing (73126), maintenance (73123), hospitality (73512), training (73544), agency (73214), plant (74123), travel (73533), cleaning (73121), and general (no fixed account).

## When to apply

Apply this skill when:

* The user is generating a TechOne narration string programmatically — outside the AP Coding Review HTML browser tool.
* The user wants to know what the canonical narration pattern is for a specific category (e.g. "what fields does the mowing template need?").
* The user is preparing a batch of recode journals via `techone-genjnl-format` and wants pre-formatted narrations from the templates.
* The AP coding review HTML has been updated to v8+ and NARR_TEMPLATES needs to be re-extracted.

Do not apply this skill when:

* The user is inside the AP Coding Review HTML tool itself — the in-browser narration builder works there. This skill is for outside-browser use.
* The user wants narration validation (40-char cap, word-boundary truncation). That's `techone-genjnl-format`.
* The user wants free-form narration outside the 9 categories. The skill is template-bound; for one-off narrations, write them directly.

## File index

```
SKILL.md                          This playbook.
narration_templates.json          Structured extraction of NARR_TEMPLATES.
                                  9 categories × {title, fields, account, template_pattern}.
                                  Template arrow functions converted to Python f-string-like
                                  patterns with {field_name} placeholders.
extract_narr_templates.py         Parser. Reads LCC_AP_Coding_Review_v7.html, locates the
                                  NARR_TEMPLATES const block, extracts each category by
                                  regex + brace-counting, converts arrow function bodies
                                  to template patterns, writes narration_templates.json.
                                  Re-runnable when v8 HTML lands.
generate_narration.py             Runtime. Loads narration_templates.json, exposes
                                  generate(category, field_values) -> str. Replicates
                                  the in-browser tool's behaviour, including the
                                  conditional segments (e.g. ` Ref: ${po}` only if PO is set).
category_index.md                 Human-readable reference: 9 categories with their
                                  field lists, suggested accounts, and example
                                  output narrations.
```

## Workflow — generating a narration

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
# → "Austspray — Zone mowing Zone 3 March 2026 Ref: PO 485102 Svc 20371"
```

Per-field optionality follows the source templates: fields not provided fall back to the placeholder strings ("[Contractor]" etc.) — and conditional segments (the ` Ref: ` block, the ` Svc ` block) only appear when the corresponding field is non-empty.

## Workflow — inspecting a category

Read `category_index.md` for the 9 categories. Each entry includes:

* Title (display name)
* Fields (id, label, placeholder)
* Suggested account (chart-of-accounts code)
* Template pattern (in human-readable form)
* One example output

This is faster than opening the HTML source for a quick lookup.

## Workflow — re-extracting from a new HTML version

When `LCC_AP_Coding_Review_v8.html` (or later) lands:

```bash
python extract_narr_templates.py path/to/LCC_AP_Coding_Review_v8.html \
    --output narration_templates.json
```

The parser:

1. Reads the HTML file.
2. Locates the `const NARR_TEMPLATES = {` line and matches braces forward to find the end.
3. For each category in the object, extracts the `title`, `fields[]`, `account`, and the body of the `template` arrow function.
4. Converts the arrow function body to a template pattern. JS template literals like `` `${f.narr_vendor||'[Contractor]'}` `` become `{narr_vendor|[Contractor]}` in the structured pattern. Conditional segments (`${f.po?' Ref: '+f.po:''}`) become structured conditional records.
5. Writes the result as JSON.

Verify after extraction:

* Category count matches expectation (9 in v7).
* Each category has account, fields, template_pattern.
* Run `generate_narration.py` against a known input and compare output to the in-browser tool.

## The 9 categories at a glance

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

Detail in `category_index.md`.

## Cross-skill flow

```
Cronometer / Hevy / vendor invoice / contract document
       │
       ▼
narr-templates-extraction [THIS SKILL]
  → produce a narration string from category + fields
       │
       ▼
techone-genjnl-format
  → validate the narration against 40-char cap and PK validity
  → format as a GENJNL row
       │
       ▼
TechOne Finance One upload
```

The 40-char cap enforcement lives in `techone-genjnl-format` because it is a TechOne-side rule, not an LCC-narration-template rule. The narrations produced here can exceed 40 chars (most do, by design); `techone-genjnl-format` truncates at word boundaries.

## Anti-patterns

* **Editing narration_templates.json directly.** The JSON is generated. Edit the source HTML and re-extract, or send the change upstream so the v8 HTML reflects it. Direct edits drift.
* **Adding a 10th category.** The 9 categories cover the LCC Parks invoice population. A 10th category should first appear in the v7→v8 HTML revision; the skill picks it up via re-extraction. Don't fork.
* **Using this skill for non-LCC narrations.** The categories, fields, and account suggestions are LCC-Parks-specific. For other contexts, build a separate templates JSON.
* **Bypassing the runtime to "save typing."** The runtime handles conditional segments correctly. Manually building narrations from the JSON's pattern strings without the runtime drops conditional logic and produces "Ref: " segments with empty values.

## Reference artefacts

* `Downloads/LCC_AP_Coding_Review_v7.html` lines 4162-4271 — canonical NARR_TEMPLATES source.
* `lcc-coding-review/scenarios.json` — 10 quick-ref scenarios; some overlap with these categories but have a different shape.
* `techone-genjnl-format/narrative_field_validator.py` — validates output narrations against the 40-char cap.
* `full_chart_of_accounts.json` (also at `_shared/lcc_chart_of_accounts.json`) — the suggested-account codes resolve here.
