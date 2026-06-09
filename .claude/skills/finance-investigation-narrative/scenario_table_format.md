# Scenario Table Format

The three-scenario table is the load-bearing visual in Beat 04 of a section-leader investigation email. It carries the EOFY landing under each available correction path and frames the decision the Section Leader is being asked to make.

The PK385 Marisa email's scenario table is canonical:

```
#   Scenario                                              YTD P1-9   Q4         EOFY        vs $164,950
01  Do nothing. Tracker unchanged into Q4.                $175,758   $65,766    $241,524    +$76,574
02  Fix prospectively from April. Leave YTD as-is.        $175,758   $36,444    $212,202    +$47,252
03  Reverse $105k LZ6 YTD excess to PK473. Apply          $109,335   $36,444    $145,779    −$19,171
    Checklist rate Q4.
```

This file documents the column structure, the three-scenario rule, the colour convention, and the prose framing that wraps the table.

---

## The three-scenario rule

Always exactly three scenarios. Two is too few (no contrast between approaches). Four+ is decision paralysis. The three are:

* **01 — Do nothing.** The counterfactual. What happens if the trace finding is filed and no action is taken. Always over budget when the trace is correct, by definition; that's why the trace is being communicated.

* **02 — Fix prospectively.** The cleanest political path. Stop the misallocation from the next period forward. YTD stays as-is. Lower correction magnitude, lower disruption to upstream PKs.

* **03 — Fix retrospectively.** The cleaner accounting answer. Reverse YTD excess back to where it should have been. Higher correction magnitude. Surfaces the masked-budget effect on the upstream PK.

The scenarios are ordered by increasing correction magnitude. Do nothing first, prospective second, retrospective third. The recipient reads down and sees the trade-off.

If the trace doesn't actually have a prospective vs retrospective distinction (e.g. the issue is purely Q4 phasing, no YTD excess), then 02 and 03 collapse into one and the table is two scenarios. Add a fourth scenario if the situation truly warrants it (e.g. a four-way decision involving partial corrections and contract amendments) — but interrogate hard before doing so. Most situations are three.

---

## Column structure

Six columns, fixed order:

| Column         | Width | Content                                            |
|----------------|-------|----------------------------------------------------|
| `#`            | ~5%   | Scenario number, 01 / 02 / 03                      |
| Scenario       | ~40%  | One-sentence description of the action             |
| YTD            | ~12%  | YTD-actual under this scenario at the as-at period |
| Remaining      | ~12%  | Q4 or remaining-period spend under this scenario   |
| EOFY           | ~12%  | YTD + Remaining = EOFY landing position            |
| vs Budget      | ~15%  | Variance to budget, with sign                      |

The YTD column is identical for scenarios 01 and 02 (no retrospective change to YTD). Scenario 03 differs because retrospective reverses YTD.

The Remaining column is identical for scenarios 02 and 03 (both apply the corrected rate going forward). Scenario 01 differs because the bad rate continues.

The EOFY column is what the recipient looks at first. It is the headline of the table.

The vs Budget column is the headline-of-the-headline. It carries the sign and the magnitude. Negative ($-19,171) is under budget; positive ($+47,252) is over.

---

## Colour convention

The scenario_comparison.html template uses these colours:

* **Scenario 01 (Do nothing) — RED background.** `#fdf4f3` light, `#1D1209` KPI-bg-red dark equivalent. Border `#f0e0de`. Variance text `#c0392b`. Conveys: this is the bad path.

* **Scenario 02 (Prospective) — AMBER background.** `#fefdf8` light, `#1A2018` panel-bg-alt dark equivalent. Border `#f0ead8`. Variance text `#b8860b` (light) or `#D4A853` (dark). Conveys: partial correction, still over.

* **Scenario 03 (Retrospective) — GREEN background.** `#f3f9f5` light, `#161D1A` KPI-bg-green dark equivalent. Border `#e0e8e2`. Variance text `#1F6B3E` (light) or `#6FB088` (dark). Conveys: full correction, under budget.

These colours run BOTH on the table row backgrounds AND on the EOFY forecast bar chart that follows the table. Consistency between the two visualisations is the point — the recipient sees the same colour twice and the cognitive load drops.

When scenario 03 doesn't actually land under budget (because the gap is too large for any retrospective correction to close it inside the FY), use AMBER for scenario 03 instead of green. The colour follows the outcome, not the position in the order.

---

## Prose framing

One paragraph precedes the table. Three jobs in two-to-three sentences:

1. State the EOFY landing under "do nothing" with the magnitude over budget.
2. Name how many corrections are available (one or two).
3. Hint at the trade-off the recipient will be asked to make.

PK385 actual:

> Without action, PK385 finishes at $241,524 — $76,574 over the $164,950 annual budget. Two corrections are available. The retrospective option is the cleaner accounting answer but exposes PK473 at ~116% immediately, which is probably why the current split has persisted.

Notes on the canonical:

* "$76,574 over" is repeated from the KPI strip earlier in the email. Repetition is fine — the strip introduced the number, the prose anchors it before the table.
* "Two corrections are available" tells the recipient the table has three rows but two are corrections — managing expectations on what the decision is about.
* "Probably why the current split has persisted" is the most editorial line in the entire email. It states the political context without accusing anyone. Use this kind of line sparingly — once per email, never twice — and only when the political dynamic genuinely needs to be named.

---

## After the table — the confirmation note

An optional callout box closes Beat 04. The pattern: a green-bordered note that confirms the correctness of the recipient's prior work.

PK385 actual confirmation note:

> Scenario 3 confirms the Checklist was right. The retrospective landing of $145,779 is consistent with your Checklist's "Remaining funds $11,690 ex GST." The budget was correctly sized throughout. PK385 looks stressed because the Tracker has been charging it for work that belongs on PK473.

Why include it:

* The Section Leader did the budget work. Affirming it before asking for a decision lowers the temperature.
* It separates the budget question from the allocation question. The budget is fine; the allocation is wrong. Two different things, both being clearly stated.
* It pre-empts the question "did I get the budget wrong?" so the recipient doesn't go there mentally.

When to skip it: if the budget was wrong, or if the affirmation would feel forced. The note is a discipline of honesty — only use it when scenario 03 genuinely confirms the prior work.

---

## The EOFY forecast bar chart

The scenario_comparison.html template carries a second visual after the table: a four-row horizontal bar chart showing each scenario's EOFY value against the budget marker. Bars in the same colours as the table rows, plus a thin black "Budget: $X" marker line.

Rows:

```
01 Do nothing      [████████████████████████]  $241,524 (red)
02 Prospective     [█████████████████████]     $212,202 (amber)
Budget             [────]                      $164,950 (black thin)
03 Retrospective   [██████████████]            $145,779 (green)
```

The budget marker is a 2-3px tall row positioned proportionally where $164,950 falls on the same scale as the bars. Bars to the left of the marker = under budget; bars to the right = over.

Bar widths: scaled linearly with the longest bar (do-nothing scenario, usually) at ~370px and others scaled down proportionally. The budget marker scales with the same ratio.

Order: 01, 02, [budget marker], 03. The marker sits between 02 and 03 because that's roughly where it falls numerically — but it can also sit elsewhere depending on the data. Place it where the value falls; do not force a position.

---

## Common scenario-table mistakes

* **Three identical YTD columns.** If all three scenarios show the same YTD, scenario 03 is not actually retrospective. Reread the trace.
* **Variance signed as absolute.** Always show the sign. `+$76,574` and `−$19,171` are not interchangeable with `$76,574` and `$19,171`. The recipient infers the direction from the sign.
* **Currency formatting drift.** Use $ with thousand-separator commas throughout: `$241,524`, not `$241524` or `241524 AUD`. Consistency matters when the eye is scanning rows.
* **Scenario descriptions over 12 words.** The Scenario column is a one-line description. Wrap to two lines if absolutely needed but never three. Detail belongs in the prose framing or the action cards, not in the table.
* **Adding a "recommended" column.** The recipient is being asked to choose. Marking one scenario as "recommended" inside the table pre-empts the decision. The framing paragraph and the action cards can lean toward a path; the table itself stays neutral.
* **Missing the budget marker on the bar chart.** The bars without the marker is just three bars. The marker is what makes the chart legible at a glance.

---

## When to use a different visual instead

The three-scenario table is for EOFY landing under correction options. Use a different visual when:

* The decision is between two operational approaches with no FY landing implication. Use a side-by-side card pair from `masked_budget.html` (the two-state percentage cards).
* The decision is monthly, not annual. Use the monthly_pattern.html visual to show the per-month trajectory under each option.
* There are more than three scenarios because the situation genuinely is multi-dimensional. Reconsider whether one email is the right shape — most multi-dimensional decisions split into a sequence of single-dimensional ones.
* The investigation has no decision attached. Skip Beat 04 entirely and close on Beat 05 actions only. Not every investigation surfaces a Section-Leader decision.
