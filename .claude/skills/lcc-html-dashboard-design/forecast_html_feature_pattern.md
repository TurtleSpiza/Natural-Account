# Forecast HTML Feature Module Pattern

The architecture used in `LCC_Parks_FY26_Forecast_v3_F10_WIP.html` to insert numbered features (F5-F10) into a long-form dashboard. The pattern is the basis for any new feature added to that file or to similar stateful HTML reports.

## The architecture

The forecast HTML is a single self-contained `.html` file with:

- One shared payload (`payload_v3.json` data injected as a JS object at load time, conventionally `D`)
- Multiple module IIFEs, each implementing a numbered feature (F5 through F10 currently, more queued)
- A central `setTheme()` function that re-renders all theme-aware modules on toggle
- Section eyebrows numbered 01 through 10, renumbered once when a new feature is inserted
- A nav bar at the top with anchor links to each numbered section

## Module IIFE shape

Every feature module follows the same shape:

```javascript
(function() {
  // Public namespace exposed to setTheme() and other coordinators
  const SANK = window.SANK = {
    state: {
      view: 'A',
      cluster: true,
      filter: null
    },

    // Build the data graph from the payload
    buildGraph(view, cluster) {
      // ...read D.__hierarchy__...
      return { nodes, links, totalValue, flowCount };
    },

    // Render to the DOM
    render() {
      // 1. Read state from toolbar
      // 2. Build graph
      // 3. Clear and re-render SVG
      // 4. Update stats and caption
    },

    // Wire interaction handlers
    attachInteractions() {
      // hover, click, filter
    },

    // Tooltip helpers
    showTooltip(event, html) { /* ... */ },
    hideTooltip() { /* ... */ },

    // One-time initialisation
    init() {
      // Wire toolbar buttons
      // Call render() once
      // Wire window resize (debounced)
    }
  };

  // Self-init on DOMContentLoaded
  document.addEventListener('DOMContentLoaded', SANK.init);
})();
```

Key conventions:

- **Namespace name** is the feature ID (HX, DM, PM, SANK). Capitalised to distinguish from generic helpers.
- **State block** holds all module state. Toolbar buttons mutate it; `render()` reads it.
- **Render is idempotent.** Calling render() repeatedly with the same state produces the same DOM output.
- **Interaction handlers are attached after every render**, not once at init, because re-renders rebuild the DOM nodes the handlers were attached to.

## Theme-aware re-render hook

`setTheme()` is the central toggle for light/dark. It must call every module's `render()` after the palette swap, otherwise modules render with stale colours.

```javascript
function setTheme(theme) {
  document.body.classList.toggle('theme-dark', theme === 'dark');
  // Persist to localStorage
  localStorage.setItem('theme', theme);

  // Re-render all theme-aware modules
  if (typeof renderHeatmap === 'function') {
    try { renderHeatmap(); } catch (e) {}
  }
  // Sankey reconciliation map
  if (typeof SANK === 'object' && SANK && typeof SANK.render === 'function') {
    try { SANK.render(); } catch (e) {}
  }
  // Add new modules here as they are inserted
}
```

The `try/catch` swallows errors during early load when modules may not have initialised yet. This is the only place silent error swallowing is acceptable.

## Section eyebrow numbering

The forecast HTML uses numbered eyebrows (01-10). When a new feature is inserted, ALL subsequent section numbers shift by one. Do this in a single edit pass, not module-by-module.

Before F10 insertion (v3):
```
04 PM operational tracker
05 What-if scenarios       ← was 05
06 Risk register           ← was 06
07 Model accuracy          ← was 07
08 Preliminary vs Final    ← was 08
09 How it was built        ← was 09
```

After F10 insertion (v3_F10_WIP):
```
04 PM operational tracker
05 Reconciliation map      ← NEW (this feature)
06 What-if scenarios       ← was 05, shifted +1
07 Risk register           ← was 06, shifted +1
08 Model accuracy          ← was 07, shifted +1
09 Preliminary vs Final    ← was 08, shifted +1
10 How it was built        ← was 09, shifted +1
```

The shift happens once. Subsequent edits to the file don't need to renumber unless another feature is inserted.

## Payload injection

Data lives in a separate `payload_v*.json` file and is injected as a `<script>` block at the top of the HTML:

```html
<script>
  const D = {
    __hierarchy__: { /* per-section data */ },
    __section_order__: [ 'Management', 'Depots', 'Natural Areas', /* ... */ ],
    __total__: { ytd_modelling: 34068087.04, bu_annual_ish: 47440000 },
    /* ... */
  };
</script>
```

Modules read from `D` at render time. The payload is unchanged between feature builds — features add modules that consume the same data, they don't usually require new data shapes (when they do, the payload version bumps).

## Insertion-point convention in the HTML

The forecast HTML handover v7 documents specific line-number anchors for inserts:

```
Line ~10-12     CDN script tags (D3, d3-sankey, etc.)
Line ~1808      Nav-link insertion point
Line ~2009      </style> — module CSS injects just before this
Line ~2200      Section HTML insertion (between PM and What-If)
Line ~2432      setTheme body — module re-render hook injects here
Line ~4330      Before final </script> — module IIFE injects here
```

Future features follow the same anchors. Capture the line numbers in the session handover when finishing a build so the next session knows where to insert.

## CDN dependencies

The forecast HTML pulls D3 and d3-sankey from cdnjs. For features that don't need D3 (e.g. text-based bridges), no new CDN dependency. For features needing a new lib, add the CDN tag at line ~10-12 and document it in the handover.

```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/d3/7.8.5/d3.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/d3-sankey/0.12.3/d3-sankey.min.js"></script>
```

For self-contained shipping (council firewall paranoia), inline the library as a `<script>` block instead of pulling from CDN. This is what the Capital Dashboard does (1.3MB inlined ECharts). Trade-off: file size vs CDN reliability.

## Validation before ship

Before shipping any feature build:

1. **Section count balanced.** `grep -c "<section" == grep -c "</section>"`.
2. **Eyebrow count == 10** (or whatever the current section count is).
3. **JS brace balance.** Use a Python script to count `{ } ( ) [ ]` pairs.
4. **No `undefined` strings in rendered state.** Sanity check for typos like `SANK.stat` instead of `SANK.state`.
5. **Headline numbers preserved.** The summary numbers ($34.07M YTD, $47.4M BU annual, $49.7M budget) should appear unchanged.
6. **Feature-specific anchors present.** `grep '#sankSvg'` and `grep 'SANK.init'` should both return results if F10 is in.

Don't open in Power BI Desktop — this is standalone HTML. Open in a browser. Mobile and desktop viewports both. Toggle theme to confirm re-renders work.

## Anti-patterns

### Re-rendering inside an interaction handler instead of mutating state and re-rendering

Bad:
```javascript
node.on('click', function(d) {
  // Re-build DOM directly here
  d3.select(this).attr('opacity', 0.5);
});
```

Good:
```javascript
node.on('click', function(d) {
  SANK.state.filter = d.id;
  SANK.render();   // re-renders with new state
});
```

The whole point of `state + render()` is idempotency. Direct DOM mutation in handlers diverges from state and breaks the next theme toggle.

### Module reading from `document.getElementById` instead of from `D`

If the module needs a value that's part of the dashboard data, read from the payload `D`, not from rendered DOM. DOM values come and go; payload values are stable.

### Forgetting the setTheme hook

Symptom: theme toggle works for some modules but the new module stays in old colours. Fix: add the new module to setTheme's re-render block.

### Hard-coding viewport dimensions

Modules should read container width at render time and resize accordingly. Hard-coded `width=900` breaks when the viewport changes or when the user switches to mobile.

## Cross-references

For palettes the modules read see `theme_tokens.json`.

For the layout patterns the modules render into (header, KPI strip, section eyebrow) see `layout_patterns.md`.

The current state of the F-feature queue is in the `LCC_Parks_Session_Handover_v7.txt` (when present in Downloads). F10 is in progress; F5/F6/F7/F8/F9 are queued.
