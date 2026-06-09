# Layout Patterns

The recurring structural patterns across the LCC standalone HTML dashboards. Capital Dashboard, Parks 5-Year Dashboard, the FY26 Forecast HTML, and the crisis tracker all use combinations of these. Pick the patterns that match the brief; don't reinvent.

## Pattern 1: Header banner

The full-width strip at the top with brand colour, eyebrow text, headline, and date.

```html
<header>
  <div class="header-stripe"></div>
  <div class="header-inner">
    <div class="header-label">LOGAN CITY COUNCIL · PARKS · {SECTION}</div>
    <h1>{Dashboard Title}</h1>
    <p>{Subtitle - one line of context}</p>
  </div>
</header>
```

CSS pattern:
- Header background: `var(--header_bg)` (Concept B navy `#1F3864`)
- Stripe at top: 4px gradient (teal → amber → teal-light) for visual punctuation
- Eyebrow text: 10px, letter-spacing 2.5px, all-caps, accent colour
- H1: 26px, light weight, white
- Subtitle: 13px, 55% opacity white

The forecast HTML uses a sticky header variant. The Capital Dashboard uses a static header. The crisis tracker uses a mobile-friendly compressed header with a pulse indicator.

## Pattern 2: KPI strip / KPI cards

The grid of summary tiles below the header.

### 4-card variant (Concept B Capital Dashboard)

```html
<table class="kpi-strip" width="100%">
  <tr>
    <td width="25%"><div class="kpi-card kpi-good">...</div></td>
    <td width="25%"><div class="kpi-card kpi-neutral">...</div></td>
    <td width="25%"><div class="kpi-card kpi-warn">...</div></td>
    <td width="25%"><div class="kpi-card kpi-bad">...</div></td>
  </tr>
</table>
```

Card structure:
- 2px coloured top border (status green/amber/red/neutral)
- Eyebrow line: 8-10px, all-caps, muted
- Value: 18-24px, light weight, txt or accent colour
- Sub: 8-10px, status colour matching the top border

### 12-tile variant (Capital Dashboard 3×4 grid)
For dashboards needing more KPIs at once. Tighter cards (140-160px wide), shorter values (no display-units suffix in the value).

### Mobile compact variant (crisis tracker 4-col 7px gap)

```html
<div class="price-grid">
  <div class="price-card">
    <div class="price-label">BRENT</div>
    <div class="price-val" style="color:var(--amber)">$116</div>
    <div class="price-unit">usd/bbl</div>
  </div>
  ...
</div>
```

Phone-first. CSS Grid `repeat(4, 1fr)` with 6px gaps. 17px values, 8px labels.

## Pattern 3: Section eyebrow + dividing rule

The section break used through the forecast HTML and the PK385 emails.

```html
<div class="section">
  <div class="section-eyebrow">01 · How It Happened</div>
  <hr class="section-rule">
  <h2 class="section-title">{Section heading}</h2>
  <p class="section-lede">{One-line lede}</p>
  ...
</div>
```

The eyebrow is the anchor for navigation in long pages. The forecast HTML uses numbered eyebrows (01-10) so feature insertions can shift the numbering once and stay coherent.

CSS:
- Eyebrow: 10-11px, monospace, letter-spacing 1.5-2.5px, accent colour, all-caps
- Rule: 1px solid border colour
- Title: 22-26px serif (Georgia), light weight
- Lede: 13-15px sans, line-height 1.65

## Pattern 4: Status colour rules (locked thresholds)

| Threshold | Colour | Use |
|---|---|---|
| P(Under Budget) ≥ 80% | green | green light, no action |
| 50% ≤ P(Under) < 80% | amber | watch, plan possible action |
| P(Under) < 50% | red | act now |

For variance ($ or %):
- Positive (under budget) → green
- Within ±5% of zero → muted/neutral
- Negative (over budget) → red

For trend arrows:
- ▲ in red = increased adverse value
- ▲ in green = increased favourable value
- ▼ in green = decreased adverse value
- ▼ in red = decreased favourable value

The arrow direction means "value moved up/down." The colour means "is that good or bad in this context."

## Pattern 5: Allocation chain / stepped flow

The PK385 Allocation Chain visual (visual2_chain) is the canonical example. Used for tracing a cost flow through stages.

```html
<table>
  <!-- Step 01 -->
  <tr>
    <td class="step-num">01</td>
    <td class="step-card">
      <div class="step-title">{What happens at this step}</div>
      <div class="step-detail">{Specifics, dollar amount, reference}</div>
      <div class="step-tag">{Document or system involved}</div>
    </td>
  </tr>
  <!-- Connector line between steps -->
  <tr><td colspan="2"><div class="step-connector"></div></td></tr>
  <!-- Subsequent steps... -->
</table>
```

Visual identity:
- Step number: large light-weight serif (Georgia 16-22px)
- Step card: panel background with a coloured left border (3px) indicating outcome (green = correct routing, red = problem destination)
- Connector: 2px width, panel_strong colour, between rows

The pattern handles 3-7 steps comfortably. Beyond that the visual gets crowded — split into two diagrams.

## Pattern 6: Comparison cards (before / after, current / corrected)

Side-by-side cards showing a before/after state. Used in PK385 visual4_scenarios and visual6_pk473.

```html
<table width="100%">
  <tr>
    <td width="48%">
      <div class="comparison-card comparison-bad">
        <div class="comparison-eyebrow">Before — Uncorrected EOFY</div>
        <div class="comparison-value">$241,524</div>
        <div class="comparison-sub">+$76,574 over budget</div>
      </div>
    </td>
    <td width="4%" class="comparison-arrow">→</td>
    <td width="48%">
      <div class="comparison-card comparison-good">
        <div class="comparison-eyebrow">After — Corrected EOFY</div>
        <div class="comparison-value">$145,779</div>
        <div class="comparison-sub">−$19,171 under budget</div>
      </div>
    </td>
  </tr>
</table>
```

## Pattern 7: Reconciliation table (per-zone, per-site)

Standard tabular format for governance reconciliation.

```html
<table class="recon">
  <tr class="recon-header">
    <th>Zone</th>
    <th>Sites</th>
    <th>Checklist $/round</th>
    <th>Tracker $/month</th>
    <th>Annual gap</th>
    <th>% inv</th>
    <th>Status</th>
  </tr>
  <tr><!-- per-zone row --></tr>
  ...
  <tr class="recon-total"><!-- total row --></tr>
</table>
```

Status badge styling: small uppercase label, status colour, border-radius 4px, padding 2-4px. Examples: `UNDER`, `LIGHT OVER`, `MAJOR OVER`, `NO ALLOC`.

## Pattern 8: Sankey reconciliation (forecast HTML F10)

D3 + d3-sankey for flow visualisation. Used in the forecast HTML feature F10 to show service/OP-code → section flows.

Structural requirements:
- D3 7.x via CDN
- d3-sankey 0.12.x via CDN
- SVG container with computed viewBox based on node count
- Two-column layout: middle column = source nodes, right column = target nodes
- Negative values cause d3-sankey to throw — clamp to zero with `Math.max(0, value)` and store the signed value separately for tooltip display
- Theme-aware re-render hook in `setTheme()` so palette changes don't leave stale colours

See the v7 forecast handover for the SANK module specification.

## Pattern 9: Mobile-compact section card with collapsible body

The crisis tracker's primary structural unit. Each topic is a section card that can collapse to its header.

```html
<div class="sec">
  <div class="sec-header" onclick="toggle(this)">
    <div class="sec-left">
      <span class="sec-icon">⚓</span>
      <span class="sec-title">Strait of Hormuz</span>
      <span class="sec-badge">D38</span>
    </div>
    <span class="chevron open">▼</span>
  </div>
  <div class="sec-body open">
    <!-- content -->
  </div>
</div>
```

JS toggle:
```js
function toggle(header) {
  const body = header.nextElementSibling;
  const chevron = header.querySelector(".chevron");
  const isOpen = body.classList.contains("open");
  body.classList.toggle("open", !isOpen);
  chevron.classList.toggle("open", !isOpen);
}
```

Use whenever the dashboard needs to fit on a phone screen and the user controls what to see at any moment.

## Cross-references

For palettes and tokens see `theme_tokens.json`.

For ECharts theme JSON (used by Capital Dashboard and Parks 5-Year Dashboard) see `echarts_theme.json`.

For the forecast HTML feature-module IIFE pattern (used by F5-F10 and any future feature insertion), see `forecast_html_feature_pattern.md`.

For email-rendering constraints (table-only layout, inline CSS, no flexbox), the PK385 Marisa email visuals are the worked examples — see them at `LCC_Parks_FY26_Forecast` Downloads folder. A separate `html-email-finance-visual` skill (when authored) will own that distinct ruleset.
