---
name: lcc-html-dashboard-design
description: "LCC standalone HTML dashboard design system. Concept B palette, header banner, KPI strip, section eyebrow, status colour patterns, ECharts theme for polished dashboards (Capital, Parks 5-Year), feature-module IIFE pattern for the FY26 Forecast HTML (F5-F10), mobile-compact pattern for crisis-tracker style work. Use whenever building a standalone HTML dashboard, adding a feature module to an existing one (Sankey, waterfall, drop-zone), inserting a numbered section into the forecast HTML, applying Concept B branding to a new dashboard, or designing a phone-first interactive view. Triggers: 'standalone HTML dashboard', 'Concept B palette', 'forecast HTML feature', 'F5/F6/F7/F8/F9/F10', 'add a Sankey', 'KPI strip', 'section eyebrow', 'theme toggle', 'ECharts theme', 'crisis tracker style', 'dashboard module IIFE'. Distinct from lcc-excel-dashboard (HTML+xlsx pair) and html-email-finance-visual (email rendering). This skill is browser-rendered standalone HTML."
---

# LCC HTML Dashboard Design

The system used by the LCC Capital Dashboard, the Parks 5-Year Dashboard, the FY26 Forecast HTML (with its F5-F10 feature queue), and the mobile-first crisis tracker. Concept B palette, shared layout patterns, ECharts theme, feature-module IIFE pattern.

Distinct from `lcc-excel-dashboard` (which is matched HTML+xlsx pair work) and from any future `html-email-finance-visual` skill (which has email-rendering constraints that make flexbox and external CSS unusable).

## Reference artefacts in this skill

| File | What it is |
|---|---|
| `theme_tokens.json` | Concept B Light, Concept B Dark, and Crisis Compact palettes as CSS-variable-ready tokens |
| `echarts_theme.json` | Two registered ECharts themes (light, dark) for use with `echarts.registerTheme()` |
| `layout_patterns.md` | Nine recurring structural patterns with HTML and CSS examples |
| `forecast_html_feature_pattern.md` | Module IIFE architecture for inserting F-features into the forecast HTML, with section-eyebrow numbering, theme-aware re-render, payload injection, and validation |

## Cross-references

- `pbir-schema-rules/theme_skeleton_*.json` — same Concept B palette in Power BI theme JSON form
- `lcc-excel-dashboard` — matched HTML+xlsx pair (when both formats need to ship together)
- `lcc_session_protocol/` (also at `_shared/`) — session header / outstanding items templates for long-running dashboard build cycles (e.g. forecast HTML F5-F10 queue)

## When this skill applies

Apply this skill when:

- Building a new standalone HTML dashboard (e.g. monthly Parks management view)
- Adding a feature module to the FY26 Forecast HTML (Sankey reconciliation map, backtest visualiser, variance waterfall, scenario matrix)
- Applying Concept B branding to inherited HTML
- Designing a mobile-first interactive view (crisis-tracker pattern)
- Building a comparison / before-after view with KPI cards

When this skill does NOT apply:

- Email-rendering HTML (table-only, inline CSS, no flexbox) — that's a separate skill (TBD `html-email-finance-visual`)
- Excel dashboards or matched HTML+xlsx pairs — that's `lcc-excel-dashboard`
- Power BI report visuals — that's `powerbi-build`, `powerbi-beautify`, or `pbir-schema-rules`

## Workflow

### New dashboard build

1. Pick the variant: Concept B (Capital / 5-Year / Forecast lineage) or Crisis Compact (mobile-first)
2. Lift the relevant CSS variables from `theme_tokens.json`
3. Build the structural shell using the layout patterns from `layout_patterns.md`:
   - Header banner with stripe (pattern 1)
   - KPI strip (pattern 2 — pick the variant matching the brief)
   - Section eyebrows numbered for nav (pattern 3)
4. Add charts via ECharts using `echarts_theme.json` (register theme, init with theme name, set options)
5. Wire the theme toggle and the theme-aware re-render (see `forecast_html_feature_pattern.md` for the pattern)
6. Validate: section count balanced, eyebrow count matches, JS brace balance, headline numbers preserved

### Feature module insertion (forecast HTML)

The FY26 Forecast HTML has a queue of features (F5-F10). Each one is a module IIFE inserted at documented anchor lines.

1. Open the latest WIP file (e.g. `LCC_Parks_FY26_Forecast_v3_F10_WIP.html`)
2. Locate the insertion anchors per the session handover:
   - Line ~10-12: CDN script tags for new dependencies
   - Line ~1808: nav-link
   - Line ~2009: end of `<style>` — module CSS injects before this
   - Section HTML insertion point (between existing sections)
   - setTheme body — module re-render hook
   - Before final `</script>` — module IIFE
3. Renumber section eyebrows if a new numbered section is added (one-pass shift)
4. Author the module per the IIFE shape in `forecast_html_feature_pattern.md`
5. Wire the setTheme hook to call the new module's render() on theme toggle
6. Validate as above

The forecast HTML feature queue (per v7 handover):

| Order | Feature | Status |
|---|---|---|
| 1st | F10 Reconciliation Sankey | In progress (shell built, JS pending) |
| 2nd | F5 Backtest visualiser | Queued (data ready, animation complexity) |
| 3rd | F7 Pulse drop-zone | Queued (data ready, parser complexity) |
| 4th | F6 Extended history | Queued (needs payload_v4 first) |
| 5th | F9 Variance waterfall | Queued (needs Spero input) |
| 6th | F8 Scenario matrix | Queued (needs specs) |

### Concept B palette quick application

For a new dashboard adopting Concept B:

```css
:root {
  --bg: #ECEEF2;
  --panel: #FFFFFF;
  --panel-alt: #F1F5F9;
  --border: #CBD5E1;
  --header-bg: #1F3864;
  --header-fg: #FFFFFF;
  --txt: #0F172A;
  --muted: #475569;
  --accent-teal: #0F766E;
  --accent-gold: #B45309;
  --status-green: #047857;
  --status-amber: #C2410C;
  --status-red: #B91C1C;
  --font-sans: 'Segoe UI', Tahoma, Geneva, sans-serif;
  --font-serif: Georgia, 'Times New Roman', serif;
  --font-mono: Consolas, 'Courier New', monospace;
}

body.theme-dark {
  --bg: #0A0E1A;
  --panel: #121826;
  --panel-alt: #1A2236;
  --border: #243049;
  --header-bg: #0E1422;
  --header-fg: #5EE0C1;
  --txt: #E8EDF7;
  --muted: #94A3B8;
  --accent-teal: #5EE0C1;
  --accent-gold: #FFB547;
  --status-green: #6FB088;
  --status-amber: #D4A853;
  --status-red: #C94A3D;
}
```

## Anti-patterns

### Inlining hex colours throughout the CSS instead of using CSS variables

Defeats theme switching. Always reference via `var(--accent-teal)`. The forecast HTML's theme toggle works because every coloured element reads from CSS variables.

### Hard-coding section numbers

When a new feature inserts at section 05, sections 05 through 09 shift to 06 through 10. Don't hardcode "Section 5" in a heading or a nav link — use the numbering pattern in `layout_patterns.md` and renumber in one pass.

### Using flexbox in something that might end up as email

If there's any chance the HTML will be repurposed for email rendering (e.g. dashboard HTML lifted into an Outlook send), flexbox breaks in Outlook. The PK385 visuals are table-only specifically because they were intended for embedded-image email use. Decide upfront whether the output is browser-only or email-friendly. This skill assumes browser-only.

### Rendering ECharts without registering the theme first

`echarts.init(el, 'concept_b_light')` fails silently if `'concept_b_light'` isn't registered. Register first with `echarts.registerTheme('concept_b_light', { /* ... */ })`, then init.

### Forgetting the setTheme re-render for new modules

Symptom: theme toggle works for some charts but the new chart stays in old colours. Fix: add a `try { newModule.render(); } catch (e) {} ` block to setTheme.

### Loading data from external files at runtime

Standalone HTML dashboards should be self-contained. Inline the payload as a JS object at the top of the file. Loading from a separate JSON via `fetch()` requires a server or breaks the file:// protocol that users will actually open the dashboard with.

The exception is the forecast HTML's `payload_v3.json` — but that's by convention loaded as a `<script src="payload_v3.json">` block inserted at deploy time, not via `fetch()`.

## Build sequence for the polished dashboards

The Capital Dashboard and Parks 5-Year Dashboard share a build sequence:

1. **Source data prep** — flatten the model to a JSON object suitable for inline injection
2. **HTML shell** — header banner, nav, section eyebrows
3. **CSS variables** — Concept B palette tokens
4. **Chart containers** — empty `<div>` per chart with stable IDs
5. **ECharts init** — register theme, init each container with the theme name
6. **chart.setOption()** — series, axes, tooltips
7. **Theme toggle** — wire button, persist to localStorage, re-render all charts on toggle
8. **Validation** — section/eyebrow balance, JS brace balance, headline numbers preserved
9. **Self-containment** — inline ECharts library (~1MB) so the file works offline

For the FY26 Forecast HTML, the build sequence is feature-by-feature insertion rather than wholesale build. See `forecast_html_feature_pattern.md`.
