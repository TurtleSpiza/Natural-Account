---
name: lcc-excel-dashboard
description: "LCC Parks dashboard and Excel styling standards — colour palette, text colour conventions, number formats, KPI card layout, themed charts, and HTML/Chart.js dashboard deployment rules. Use whenever the user is building a dashboard, KPI view, chart, heatmap, scorecard, or any polished Excel output for Parks management reporting. Also trigger on 'make it look better', 'Power BI feel', 'dark theme dashboard', 'interactive HTML', 'chart styling', 'number format', or any request to format an Excel workbook to LCC presentation standard — even when 'dashboard' isn't said. Covers the matched HTML + xlsx deployment pattern and the SharePoint/Excel Online hyperlink limitations."
---

# LCC Excel and Dashboard Standards

The palette, helpers, and deployment rules that make a workbook or HTML dashboard feel like Parks work rather than default Excel.

## Quality bar (non-negotiable)

Default Excel output is rejected on sight. The fix is not "format at the end", it is to design the frame first and pour data into it. Build every visual deliverable in this order, and do not skip a step:

1. **Frame first.** Block out the grid and choose the single hero element (the one number or chart the eye lands on first) before any data goes in. Everything else is ranked visibly below it by size and weight.
2. **Palette second.** One neutral base, one accent, green and red reserved for meaning only. Never the default Office spectrum at full saturation.
3. **Group into cards.** Information sits in padded panels with equal gutters. Nothing crammed to the cell edge.
4. **Strip all chrome.** Gridlines off, chart borders off, redundant axes deleted, default legends rebuilt as cell labels or removed. The data is the only ink on the surface.
5. **Type scale.** Huge for the hero, medium for labels, small for captions. Bold reserved for values, never for labels.
6. **Direct-label and format every number.** Values on the bars, never make the reader hunt the axis. Currency as `$1,773`, never `1773.00`.
7. **Alignment pass.** Every card edge, baseline, and gutter snaps to an invisible grid before delivery.

These seven are style-agnostic. They apply to a light corporate sheet and a dark dashboard equally. A build that fails any of them is not finished.

## The two ceilings (read before promising a look)

How the workbook is generated caps how good it can look. Be honest about which ceiling applies.

**openpyxl-generated ceiling (the default path).** Achievable and a large jump from raw default:
- Chrome stripped on sheets and charts.
- Gradient *cell* fills (`GradientFill`) for KPI cards and banners.
- Inserted PNG/SVG icons and pre-rendered header banners (`add_image`).
- Conditional-format data bars and colour scales in place of bar charts.
- Native charts (line, bar, doughnut, area) restyled hard from default, with gradient series fills.
- A doughnut-plus-needle gauge (second series as the needle).

**openpyxl cannot do these. Do not promise them on the default path:**
- **Slicers and form-control toggles** — no openpyxl API. Needs a template .xlsx prepared in Excel, then populated.
- **Drawn shapes** (rounded rectangles, callouts) — fake cards with merged cells + `GradientFill`, or drop a pre-rendered PNG card background.
- **Modern waterfall chart** (chartEx) — build it as a stacked-bar trick instead.
- **Reliable sparklines** — use a tiny line chart in a merged cell, or a template.
- **Glow, neon, network graphs, Sankey, dot-density maps** — not Excel at all. Route to HTML (lcc-html-dashboard-design), Power BI (powerbi-design-system), or Geckoboard.

**Hand-built / template ceiling.** To match a sold template (slicers, drawn cards, waterfall, form controls), start from a template .xlsx built once in Excel, then have the code only write values into named ranges. State this trade-off to the user rather than silently delivering a lower-ceiling openpyxl file.

## Colour palette

**Primary (dark theme dashboards):**

| Role | Hex | Use |
|---|---|---|
| PANEL | `1A2236` | Header bars, KPI card background |
| NAVY | `1F3864` | Section headers, table headers |
| BLUE1 | `2F5597` | Primary data fills |
| BLUE2 | `4472C4` | Secondary bars |
| ACCENT | `7C9CFF` | Value highlights, hyperlinks in dark theme |
| MUTE | `595959` | Labels, footnotes |

**Status / variance:**

| Role | Hex | Use |
|---|---|---|
| GREEN_D | `375623` | Under budget, favourable |
| GREEN_L | `E2EFDA` | Favourable row fill |
| AMBER | `C8783C` | Watch items |
| AMBER_L | `FFF2CC` | Watch row fill |
| RED | `C00000` | Over budget, adverse |
| RED_L | `FFE0E0` | Adverse row fill |

**Structural:**

| Role | Hex | Use |
|---|---|---|
| BLUE_L | `D6E4F0` | Light data fill |
| GREY_H | `D9D9D9` | Standard header |
| GREY_L | `F5F5F5` | Alternating row |
| BAND | `F4F6FA` | Alternate band in tables |
| WHITE | `FFFFFF` | Content cells |

**Accent gradient pair (cards and banners):** `5EE0C1` to `7C9CFF`, matching the Concept B HTML dashboards.

**Heatmap scales (variance columns):**
- Dollar: start `5EE0C1` (favourable) to mid `FFFFFF` (zero) to end `FF6B7A` (adverse).
- Actuals: start `FFFFFF` to mid `C5D8FF` (50th pct) to end `7C9CFF` (max).

## Text colour conventions (standard Excel build)

- Blue `(0,0,255)` — hardcoded inputs, scenario values.
- Black `(0,0,0)` — all formulas and calculations.
- Green `(0,128,0)` — links from other sheets in the same workbook.
- Red `(255,0,0)` — external file links.
- Yellow background — key assumptions, cells needing update.

## Number formats

- Currency: `$#,##0;[Red]($#,##0);-` (negatives in parens, zeros as dash).
- Currency no cents, no colour: `$#,##0;($#,##0);-`.
- Percentage: `0.0%;[Red]-0.0%;-`.
- Whole percent: `0%`.
- Count: `#,##0;-#,##0;-`.
- Ratio / multiple: `0.00"x"`.

Dollar amounts in prose always include `$` and comma formatting. Percentages as figures, not words.

## Style helper functions

Paste these once per workbook build. The first block is the original set, the second is the gap-closing toolkit that enforces the quality bar.

```python
from openpyxl.styles import Font, PatternFill, GradientFill, Alignment, Border, Side
from openpyxl.formatting.rule import DataBarRule, ColorScaleRule
from openpyxl.drawing.image import Image as XLImage

def fill(color):      return PatternFill('solid', fgColor=color)
def font(sz=10, bold=False, color='000000', name='Calibri'):
    return Font(name=name, size=sz, bold=bold, color=color)
def cen(wrap=False):  return Alignment(horizontal='center', vertical='center', wrap_text=wrap)
def lft(wrap=True):   return Alignment(horizontal='left', vertical='center', wrap_text=wrap)
def rgt():            return Alignment(horizontal='right', vertical='center')
def top_wrap():       return Alignment(horizontal='left', vertical='top', wrap_text=True)

BORDER = Border(
    top=Side(style='thin', color='AAAAAA'),
    bottom=Side(style='thin', color='AAAAAA'),
    left=Side(style='thin', color='AAAAAA'),
    right=Side(style='thin', color='AAAAAA'),
)
```

```python
# --- gap-closing toolkit (enforces the quality bar) ---

def grad(c1, c2, degree=90):
    "Gradient cell fill for KPI cards and banners. degree 90 = top-to-bottom."
    return GradientFill(degree=degree, stop=(c1, c2))

def strip_sheet_chrome(ws, hide_headers=False):
    "Run on every sheet. Hide headers on the Dashboard sheet only."
    ws.sheet_view.showGridLines = False
    ws.sheet_view.showRowColHeaders = not hide_headers

def strip_chart_chrome(chart, drop_value_axis=True):
    "Remove default furniture. Direct-label instead of leaning on axes."
    chart.legend = None                      # rebuild as cell labels if needed
    chart.x_axis.majorGridlines = None
    chart.y_axis.majorGridlines = None
    chart.x_axis.delete = False              # openpyxl gotcha: axes vanish without this
    chart.y_axis.delete = drop_value_axis    # True drops the value axis entirely
    chart.x_axis.tickLblPos = 'low'

def kpi_card(ws, anchor_row, anchor_col, label, value, span=3,
             bg='1A2236', label_clr='FFFFFF', value_clr='FFFFFF',
             value_fmt='$#,##0;($#,##0);-', gradient=None):
    "PANEL card: small label row above a large merged value row."
    from openpyxl.utils import get_column_letter
    c0 = get_column_letter(anchor_col)
    c1 = get_column_letter(anchor_col + span - 1)
    # label row
    ws.merge_cells(f'{c0}{anchor_row}:{c1}{anchor_row}')
    lab = ws.cell(anchor_row, anchor_col, label)
    lab.font = font(9, color=label_clr); lab.alignment = cen()
    # value row
    ws.merge_cells(f'{c0}{anchor_row+1}:{c1}{anchor_row+1}')
    val = ws.cell(anchor_row+1, anchor_col, value)
    val.font = font(20, bold=True, color=value_clr); val.alignment = cen()
    val.number_format = value_fmt
    paint = grad(*gradient) if gradient else fill(bg)
    for r in (anchor_row, anchor_row+1):
        for col in range(anchor_col, anchor_col+span):
            ws.cell(r, col).fill = paint
    ws.row_dimensions[anchor_row].height = 18
    ws.row_dimensions[anchor_row+1].height = 50

def insert_icon(ws, path, anchor, w=28, h=28):
    "Drop a PNG/SVG icon or pre-rendered banner. Closes most of the gap to template-grade."
    img = XLImage(path); img.width = w; img.height = h
    ws.add_image(img, anchor)

def add_databars(ws, cell_range, color='7C9CFF'):
    "Use in place of a bar chart where the value sits in a table."
    ws.conditional_formatting.add(
        cell_range, DataBarRule(start_type='min', end_type='max', color=color))

def add_color_scale(ws, cell_range,
                    lo='5EE0C1', mid='FFFFFF', hi='FF6B7A'):
    "Variance heatmap: favourable to zero to adverse."
    ws.conditional_formatting.add(cell_range, ColorScaleRule(
        start_type='min', start_color=lo,
        mid_type='num', mid_value=0, mid_color=mid,
        end_type='max', end_color=hi))
```

## KPI card layout (standard eight)

Row of cards, one per metric, built with `kpi_card`:

1. Actuals YTD
2. Budget
3. Forecast
4. Variance ($)
5. Projected over/under
6. Chance under budget (%)
7. High-risk sections (count)
8. Worst driver (account name)

Each card: `PANEL` background (or the accent gradient on the hero card only), label in `font(9, color='FFFFFF')`, value in `font(20, bold=True, color='FFFFFF')`. Row height 18 (label) and 50 (value). Merge 3 cells per card. The hero card is one size larger than the rest, never all eight at equal weight.

## Standard chart set

- Actual vs budget vs forecast — line.
- Cumulative spend vs budget — line.
- Confidence interval bands — shaded area.
- Variance waterfall — stacked-bar trick (openpyxl has no native waterfall).
- Top overspend drivers — horizontal bar, direct-labelled.
- Section comparison — grouped bar.
- Section x period variance — heatmap via `add_color_scale`.
- Traffic lights — restrained green/amber/red only, no clutter.

Run `strip_chart_chrome` on every chart. Per-bar DataPoint colouring for variance bars: green if favourable, red if adverse, applied via `series.data_points[i].graphicalProperties.solidFill = colour`.

## Zero formula errors before delivery

Every build ends with a recalc pass. Verify 2-3 sample cross-sheet references manually before scaling. No hardcoded computed values — every calculation is a visible formula. All assumptions in dedicated cells with named ranges, never embedded in formulas.

## HTML dashboard deployment — the rules

The combination of Chart.js HTML + matching xlsx shipping pattern only works under specific conditions. Get any of these wrong and the deliverable silently fails.

**What works:**

- Both files in the same local folder (Documents, Desktop, USB, mapped network drive).
- Filenames match exactly what the Excel hyperlink expects. Windows `(2)`, `(5)` suffixes break the link silently.
- HTML opens via direct double-click in File Explorer, or via relative hyperlink in xlsx when both files are in the same local folder.
- Edge full-screen via F11 for presentation mode.

**What does not work:**

- SharePoint web and OneDrive web cannot serve HTML files — they download, 404, or strip JavaScript in a sandboxed preview.
- Excel Online (browser) cannot resolve relative hyperlinks to local HTML.
- Council-managed Edge often downloads rather than opens HTML when triggered from within Excel.

**Deployment instruction to user:**

1. Package both files as a zip (`Parks_Dashboard.zip`) — mail filters that strip `.html` will usually pass `.zip`.
2. Receiver extracts zip to a local folder on their C: drive — not SharePoint web, not OneDrive web.
3. Open the xlsx from the local folder, click the HTML button. Or double-click the HTML directly.
4. F11 for full screen in Edge.

If full interactivity inside Microsoft is required, Power BI is the answer, not embedded HTML.

## Chart.js HTML standards

- Dark theme: background `#0E0E0E` or `#1A2236`. Text `#FFFFFF` or `#E0E0E0`.
- Chart.js from `cdn.jsdelivr.net/npm/chart.js` — most council firewalls allow this CDN. If blocked, inline Chart.js into the file (+~200KB, no other cost).
- Always validate JavaScript syntax before delivery. Silent JS failures render a blank canvas with no error — unacceptable.
- Self-contained: one HTML file, no external assets except the Chart.js CDN.
- Tabbed layout for multi-section dashboards. Dropdown selectors drive all charts on a tab simultaneously.

## Baseline workbook architecture (forecasting and analysis builds)

For reference, when building from scratch:

`Raw_Data -> Assumptions -> Data_Preparation -> Forecast_Model -> Model_Testing -> Forecast_Evaluation -> Dashboard -> Methodology -> Data_Dictionary`

Dashboard sheet is the last visible sheet but often built first (to pin the layout), then backfilled.
