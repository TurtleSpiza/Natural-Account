---
name: lcc-na-analysis
description: "LCC Parks Natural Account transaction analysis — GL export parsing, service-section mapping, workbook col P/Q/R writes, evidence standard, known traps, session protocol. Use whenever the user is working on the NA_Analysis workbook, analysing a natural account (O110/O115 cost codes, any 7x/72x/73x/74x/7Bx/7Cx account), reading a TechOne Ledger Accounts Transactions Table, updating the task file, or doing any transaction-level review of Parks spend against budget. Also trigger on phrases like 'confirm account', 'trace invoice', 'pending transaction data', 'update col P', 'session header', 'write findings' — even when 'NA' or 'natural account' isn't said."
---

# LCC Parks NA Transaction Analysis

The workflow that runs every analysis session. Read this before touching the workbook or task file.

## Core principle

Every material finding traces to: vendor name, invoice number or journal reference, service code, dollar amount, date, and reason. Anything short of that stays "Pending transaction data" in col R. Trend-only observations ("level shift", "structural gap") are not findings until the listing confirms the root cause.

## Session start checklist

1. Read the task file session header first. It names the last confirmed account, the next in queue, the workbook version, and the open Finance request count.
2. Attach `service_section_map_1.csv` and `service_pk_section_map_1.csv` if doing analysis.
3. Analysis sessions do not proceed without new transaction data. If no listings are uploaded, the session is housekeeping (task file updates, report writing, email drafting) — not analysis.

## GL export parsing (TechOne Ledger Accounts Transactions Table)

Exports arrive as `.xlsx` with parameter lines above the header. Parse with the calamine engine — about 9x faster than openpyxl on large multi-account exports, with a single-pass header detection that avoids re-reading the file. If calamine is not yet installed in the sandbox, run `pip install python-calamine --break-system-packages --quiet` once at the start of the session.

```python
import pandas as pd

# Use calamine engine — ~9x faster than openpyxl on large exports.
# Falls back automatically if calamine isn't installed.
try:
    raw = pd.read_excel(path, header=None, engine='calamine')
except (ImportError, ValueError):
    raw = pd.read_excel(path, header=None)

# Single-pass header detection — slice, don't re-read.
header_row = next(i for i, r in raw.iterrows()
                  if any('Short Description' in str(v) for v in r.values))
df = raw.iloc[header_row + 1:].copy()
df.columns = raw.iloc[header_row].tolist()
df = df[df['Reference'].notna()]   # drop subtotal/rollup rows
```

Canonical column names after parse: `Short Description`, `Account`, `Period`, `Reference`, `Date`, `Doc Type`, `Details`, `Transaction Amount` (single space — not `TransactionAmount` or `Amount`), `Service Code`, `Description`, `Work Order`.

All GL amounts are **ex-GST**. Multiply by 1.1 for invoice reconciliation (incl-GST).

Read the `Details` narration on every RJ/GJ journal — the dollar amount is meaningless without it. Accruals are normal LCC practice, not anomalies; the narration names the underlying contract or event.

## Service-section map

Join on `ServiceCode` as integer on both sides. Use `Int64` (NaN-safe) rather than `astype(float).astype(int)` — the latter crashes if any row has a missing service code.

```python
svc_map = pd.read_csv('/mnt/project/service_section_map_1.csv')
svc_map['ServiceCode'] = svc_map['ServiceCode'].astype(int)
df['ServiceCode'] = pd.to_numeric(df['Service Code'], errors='coerce').astype('Int64')
df = df.merge(svc_map, on='ServiceCode', how='left')
```

### Map exceptions (not in reference files — apply manually)

- `svc 20261` → `PK000035 Park Maintenance`
- `svc 20455 Contract Mowing Cemeteries` → section `Cemeteries` (no PK)
- `svc 20821 Parks Disaster Management` → section `NA - Not Applicable` (no PK)
- `svc 20211 Free Trees` → `PK000081 Natural Areas` (not Trees)
- `PK000331 Sunday Reserve` → `Natural Areas` (still missing from map)

## Known traps

Read before concluding on any of these accounts:

| Trap | What it looks like | What it actually is |
|---|---|---|
| 73215 FY2024 | Mowing overspend | Fire access track work, svc 20471 |
| 74141 FY2023 | Truck hire | T&H Levai INV-30283 Flagstone Mulching PAR/314E/2017 |
| 73990 | Operational overrun | Accounting treatment — capital below threshold expensed via GJ svc 20191 |
| DM 17802475 (73212) | Monthly standing contract | EOM accrual for Christmas storm Birnam Range remediation |
| 73544 GJ069279 | DA recovery transfer | Parks' pro-rata share of QGATE OST program ($9,137) |
| 7C112 IJ072068 | Internal plant hire | Cyclone RCM recovery |
| 73312 A-FE35E476-003 | Recurring electricity | Beenleigh Town Square FY2024 catch-up (~$6k/yr underlying, not $56k) |
| 73123 / 73212 | Either read in isolation | Reclassification event — read combined: +$21M on 73212, -$10.8M on 73123 |
| 72248, 73531 | Workbook dollar figures | Reconstructed from column values — individual invoice amounts require Finance confirmation |

## Workbook write protocol

File: `NA_Analysis_v9_##_s##.xlsx` | Sheet: `NA_Analysis` only (never touch main data).
Headers at row 6. Data from row 7. Col P = 16, Col Q = 17, Col R = 18.

**Every written cell:**

```python
from openpyxl.styles import Alignment, Font, PatternFill
import copy

def write_cell(ws, row, col, value, source_cell=None):
    c = ws.cell(row=row, column=col)
    c.value = value
    c.alignment = Alignment(wrap_text=True, vertical='top')
    if source_cell and source_cell.font:
        c.font = copy.copy(source_cell.font)   # full Font() copy when changing colour
    else:
        c.font = Font(name='Calibri', size=10, color='000000')
    return c
```

For white fills: `PatternFill(fill_type='solid', fgColor='FFFFFF')` — `fgColor` not `fill`, and `fill_type='solid'` is required or openpyxl drops the colour silently.

Col P is narrative (see writing style below). Col Q is numbered actions starting with a verb. Col R is one word status + one sentence.

## Col P / Q / R contract

**Col P — Root cause and evidence.** Lead with the dollar amount and the gap to budget. Then vendor, invoice or journal reference, contract reference, service code, section, dollar amount, date, reason — per material item. State what is missing if incomplete.

**Col Q — Actions.** Numbered. Start each with a verb. Name the person (Amy Forgione, Owen Jensen, Clayton Te Maipi, Adam Barter, Brad White), the system, or the dollar amount. If transaction data is not yet received, action 1 is always "Request transaction listing from Finance".

**Col R — Status.** One word plus one sentence. Word is one of `Confirmed`, `Pending transaction data`, `Partial`, `Closed`. Do not mark `Confirmed` until the listing is fully analysed and root cause is fully explained at the transaction level.

## Writing style

Plain, direct. No em-dashes, en-dashes, or hyphens as separators — use full stops and paragraph breaks. No bullet points or bold in col P. No ALL CAPS section headers inside cell text.

Lead with the fact and the dollar amount. Dollar signs and comma formatting always: `$123,456`. Percentages as figures: `40.3%`.

No speculative language in findings (`should`, `could`, `may`) — facts only, recommendations go in col Q. No hedging (`appears`, `possibly`, `likely`) unless paired with a specific reason. No magnitude adjectives (`significant`, `substantial`) without a dollar amount attached.

## Session end protocol

1. Update the workbook and the task file in the same step. Never one without the other.
2. Rewrite the session header in the task file: last confirmed, next in queue, workbook filename, open Finance request count.
3. Log closed items inline — preserve original item numbers when closing from the outstanding list.
4. Increment workbook version: `NA_Analysis_v9_{N}_s{session}.xlsx`.
5. Finance items are batched into a single email, never drip-fed.

## Key analytical anchors (for context only — do not restate unless asked)

- 104 accounts complete. Four accounts drive 84% of total spend.
- 40.3% spend growth FY21 to FY25. FY2024 was the worst budget control year.
- Nine accounts over budget all five years. Six under all five years.
- 73212 / 73123 reclassification is the single most distorting event in the dataset.
- Internal charges (7B-series, 7C-series) have been structurally underbudgeted every year.

## Key contacts

- Finance: Amy Forgione, Owen Jensen (all outstanding items batched to both).
- Natural Areas: Clayton Te Maipi, Adam Barter.
- Parks Manager: Brad White (5501).
- Referenced in GL narrations: Kyle Fidler, Lisa Hodgson, Jennifer Moir.
