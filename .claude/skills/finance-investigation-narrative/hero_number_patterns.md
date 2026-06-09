# Hero Number Patterns

The hero number opens the body of a section-leader investigation email. It does two jobs in one sentence: state the headline finding AND state the misperception that has been hiding it. The Marisa email's "A $140,000 allocation gap, hiding as $10,808" is the canonical form.

This file catalogues six hero-number patterns. Each has a use case, a structure, and worked examples. Pick the one that matches the trace's shape.

The hero number is the highest-leverage sentence in the email. It is what the Section Leader will quote when they forward the thread to a Director or to PM. Spend disproportionate time on it.

---

## Pattern 1 — Reveal vs Visible

**Use when:** The variance report or the Section Leader's mental model shows a small or moderate number, but the trace reveals a much larger underlying mechanism.

**Structure:** `A {{REVEALED_AMOUNT}} {{NATURE}}, hiding as {{VISIBLE_AMOUNT}}.`

**Examples:**

* `A $140,000 allocation gap, hiding as $10,808.`        (PK385 actual)
* `An $87k unbudgeted overspend, hiding as a $9k phasing lag.`
* `A $52,000 contract overrun, hiding as period-end timing.`

**Why it works:** The two numbers in one sentence force the recipient to compare them. The "hiding" verb introduces the trace finding without using the word "trace."

**Caveat:** Only use when the revealed number is at least 5× the visible number AND when the visible number is genuinely already in the recipient's awareness. If the recipient hasn't already seen the variance report, this pattern is confusing — they don't have the visible number to compare against.

---

## Pattern 2 — One Outlier Drives N

**Use when:** The reconciliation surfaces one dominant outlier line that explains most of the gap. Multi-zone or multi-site investigations.

**Structure:** `{{N}} {{LINES}}, one outlier, the {{TOTAL_GAP}}.`
or `{{N}} {{LINES}} reconcile. One {{OUTLIER}} drives {{PCT}} of the {{TOTAL_GAP}}.`

**Examples:**

* `Six zones, one outlier, the $117k variance.`
* `Five sites within Checklist. LZ6 alone drives 94% of the $117,286 annualised overcharge.`     (PK385 actual, used in Beat 03 prose)
* `Eight contracts reconcile. PAR/338A is the entire $52k.`

**Why it works:** The recipient's instinct on a multi-line investigation is "do I have to look at all of these?" Pattern 2 answers no — there's one place to look — before the body even starts.

**Caveat:** Only valid when the outlier truly does drive most of the gap (at least 80%). If the gap is spread across multiple lines, use Pattern 4 (Concentrated Spread) instead.

---

## Pattern 3 — Subject Line Has No Carve-Out

**Use when:** The vendor invoice subject line names one PK only, but the journal splits to multiple PKs. Pure passthrough findings where the issue is documentary, not arithmetic.

**Structure:** `{{INVOICE_AMOUNT}} of monthly invoice has no carve-out for {{PASSTHROUGH_PK}}.`

**Examples:**

* `$73,432 of monthly invoice has no carve-out for PK385.`
* `Every Glascott LZ8 invoice names PK473 alone — yet $4,200/month lands on PK385.`

**Why it works:** It states the documentary discrepancy directly. The recipient understands "carve-out" intuitively; the absence of one is what licenses the trace.

**Caveat:** Requires the invoice subject line really is silent on the passthrough PK. If the invoice has a multi-PK breakdown that has been ignored, the issue is internal-allocation, not documentary, and Pattern 1 fits better.

---

## Pattern 4 — Concentrated Spread

**Use when:** The gap is real and spreads across several lines but with concentration in 2-3 of them, not a single dominant outlier.

**Structure:** `{{TOTAL_GAP}} sits in {{CONCENTRATED_LINES}} of {{TOTAL_LINES}} lines.`

**Examples:**

* `$54k of variance sits in three accounts of twenty-eight reviewed.`
* `The $32,000 sits across LZ6, LZ8, and the contract escalation — three lines of fourteen.`

**Why it works:** Honest about the shape of the data when there isn't one outlier. Tells the recipient where to focus without overstating concentration.

**Caveat:** Less punchy than Pattern 1 or 2. Use only when the data really is spread; if there's one outlier, force it back to Pattern 2.

---

## Pattern 5 — Budget Sized Right, Tracker Sized Wrong

**Use when:** The trace confirms the FY budget was correctly sized at the time it was set, and the variance is purely an operational-driver mismatch.

**Structure:** `The budget was right. The {{OPERATIONAL_DRIVER}} drifted.`

**Examples:**

* `The budget was right. The Tracker drifted.`
* `The Checklist sized PK385 correctly. Six months of Tracker values say otherwise.`
* `Budget $164,950, Checklist confirms $164,950, Tracker has charged $175,758.`

**Why it works:** Affirms the Section Leader's prior work (the budget) before delivering the finding. They are more receptive to a finding that says "your budget was right" than one that implies the budget was wrong.

**Caveat:** Only valid when the budget actually was sized correctly. Do not use as a courtesy if the budget was the problem.

---

## Pattern 6 — Two Documents Disagree

**Use when:** The investigation is fundamentally a reconciliation of two documents (governance vs operational) and the headline is the disagreement itself.

**Structure:** `{{GOV_DOC}} says {{GOV_VALUE}}. {{OP_DOC}} says {{OP_VALUE}}.`

**Examples:**

* `Checklist approves $2,306 per round. Tracker charges $13,993.`
* `Contract schedule prices LZ6 at $11,000/month. Glascott invoice runs $14,500.`

**Why it works:** Maximum factual density. Two numbers, two source documents, the contradiction is the finding.

**Caveat:** Drier than the other patterns. Best for follow-up emails where the recipient already knows the context, or for Sections that prefer evidence-first communication. The PK385 Marisa email used Pattern 1 in the hero line and Pattern 6 inside Beat 03 prose — both have their place.

---

## Anti-patterns

* **"There may be an issue with..."** — kills the hero number. The whole point is to state the finding strongly. Hedging belongs in the confidence statement, not the headline.
* **Two hero numbers in one email.** If the trace surfaces two findings, send two emails or pick one to lead with and absorb the other into the body. The hero number is singular by design.
* **Hero number with no follow-through.** If you open with "$140k" the body has to surface and substantiate the $140k somewhere. Opening with a number that doesn't reappear in the visuals is bait-and-switch and the recipient notices.
* **Hero number in the subject line AND the body.** Subject line gets the topic. Body opens with the hero number. Repeating the hero number in both is heavy-handed and feels like marketing.

---

## Decision tree — picking the pattern

```
Is there a small visible number (variance report) hiding a much larger reveal?
   └─ YES → Pattern 1 (Reveal vs Visible)
   └─ NO ↓

Is there one dominant outlier line driving 80%+ of the gap?
   └─ YES → Pattern 2 (One Outlier Drives N)
   └─ NO ↓

Is the issue that the invoice subject doesn't name the passthrough PK?
   └─ YES → Pattern 3 (Subject Line Has No Carve-Out)
   └─ NO ↓

Is the gap spread across 2-3 lines without a single dominant outlier?
   └─ YES → Pattern 4 (Concentrated Spread)
   └─ NO ↓

Is the budget itself correct and the variance is pure operational drift?
   └─ YES → Pattern 5 (Budget Sized Right, Tracker Sized Wrong)
   └─ NO ↓

Is the headline a direct two-document contradiction?
   └─ YES → Pattern 6 (Two Documents Disagree)
   └─ NO ↓

Reread the trace. The hero number is hiding somewhere; if none of the
patterns fit, the trace finding may not actually be email-ready yet.
```
