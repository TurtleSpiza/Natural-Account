# Canonical Marisa Email — Annotated

The PK385 Marisa email is the reference example for this skill. v6 light is the canonical variant. This file annotates the email beat-by-beat with notes on why each move was made, what could have been done differently, and what to lift directly when adapting to a new investigation.

Source files:

* `Downloads/PK385_email_Marisa_v6_light.html` — canonical light variant (HTML)
* `Downloads/PK385_email_Marisa_v5_dark.html` — canonical dark variant (HTML)
* `Downloads/PK385_email_body.txt` — plain-text prose, no HTML wrapping

The investigation that produced this email lives in `lcc-cost-allocation-tracing/worked_example_pk385.md`.

---

## Header bar

```
NATURAL AREAS · SECTION 4090220 · PD9 MAR 2026                  22 Apr 2026
```

Carries: section name (Marisa's), section code, period reference, send date.

The section name is what Marisa sees on her own reports. The section code matches the chart of accounts. The period reference (PD9 MAR 2026) anchors the data to a specific month. The send date is right-aligned because it's auxiliary.

Lift verbatim, substitute the four placeholders.

---

## Subject line area

```
PK000385 · Urban Bushland · Investigation Findings
A $140,000 allocation gap, hiding as $10,808.
```

Two lines. The first is the eyebrow — small caps, grey, scoping. The second is the hero number, large, dark.

Eyebrow content: the PK number (full 6-digit), the PK common name (Urban Bushland), the email type (Investigation Findings). All three are needed because the recipient files emails by all three at different times.

Hero number: Pattern 1 from `hero_number_patterns.md` — Reveal vs Visible. The dollar amounts and the grammatical structure ("X, hiding as Y") together do the reframe.

Sentence-level note: the comma after "gap" is intentional. It marks the visual reframe — the reader pauses, sees "hiding as $10,808," and re-reads "$140,000 allocation gap" with the new context. Without the comma the sentence reads as a single clause and the reframe is weaker.

---

## KPI strip (visual1)

Four cards across:

```
YTD Actual P1-9     FY26 Budget          Headline Overspend    EOFY if Uncorrected
$175,758            $164,950             $10,808               $241,524
106.5% of budget    $21,250/month phased Variance report shows +$76,574 over budget
```

The four cards do four jobs:

1. Card 1 anchors the actual.
2. Card 2 anchors the budget. (Together, cards 1 and 2 establish the baseline.)
3. Card 3 names the small visible number from the variance report. The colour is red because the reader expects red-for-overspend, but the number is small.
4. Card 4 names the large EOFY number. Same red. The contrast between cards 3 and 4 is the reframe.

The accent colour on cards 1 and 2 is green (`#1F6B3E` and `#4a8a6a`) — informational. Cards 3 and 4 are red (`#c0392b`) — finding.

Lift directly. Substitute the four numbers and the four sub-line captions.

---

## Salutation + opening paragraph

```
Hi Marisa,

PK385 has no direct vendor invoices. Every dollar on it is a Parks
Maintenance internal journal splitting the Austspray and Glascott zone
invoices using fixed Tracker values. Those values have never been
reconciled against the Checklist you forwarded. When I did that
reconciliation, one zone explains the entire overspend. Gihani is cc'd
so the finance side of any decision is visible from the start.
```

Five sentences. Each does work:

1. Names the passthrough nature directly. "No direct vendor invoices" is a fact most Section Leaders don't realise about their own PKs.
2. Names the mechanism: Parks Maintenance, internal journal, two vendors, Tracker.
3. Names the gap (the unreconciled status of the Tracker against the Checklist) AND positions Marisa as the document owner ("the Checklist you forwarded").
4. Previews the finding ("one zone explains the entire overspend") to stage Beat 03.
5. Names the cc reason. Critical sentence — it is what makes Gihani's presence on the thread feel inclusive rather than escalatory.

The opening paragraph is dense. ~70 words doing five jobs. Re-read aloud — every sentence pulls weight, none is throat-clearing.

---

## Beat 02 — Mechanics + allocation chain (visual2)

```
01 · How the Overspend Happened

The Austspray LZ6 invoice is a single lump sum under contract
PAR/338A/2025. It names PK000473 on the subject line only — no Urban
Bushland carve-out, no site-level breakdown. Each month Parks
Maintenance journals the invoice to two destinations using fixed
Tracker values: 81% to PK473, 19% to PK385. Those percentages have
no vendor-side basis and predate the current Checklist.
```

Section eyebrow `01 · How the Overspend Happened` — small caps, green. The eyebrow + thin green underline is the section-divider pattern. Lift the styling unchanged.

Prose: four sentences. The structure is contract → invoice subject → journal → split percentages. Each sentence sets up the next. The closing "predate the current Checklist" is the bridge into the trace finding (the Tracker is operating against an obsolete basis).

Allocation chain visual: five steps, numbered 01-05. The steps in PK385 are: Austspray invoices LZ6 → holding account → Parks Maintenance posts journal → 81% routed to PK473 → 19% routed to PK385. Step 05 carries the finding (the misallocation) and is rendered in red. Steps 01 and 04 are rendered in green (information-only). Steps 02 and 03 are neutral grey.

Lift directly. Adapt the five step labels to the new investigation's chain.

---

## Beat 03 — Evidence + reconciliation table + bar chart (visual3)

```
02 · Are the Costs Correct

Five of six zones sit close to their Checklist-approved amounts. LZ6
is the outlier — Tracker charges $13,993/month against Checklist-
approved scope of $2,306/round, six times the approved level. LZ6
alone drives 94% of the $117,286 annualised overcharge.

LZ3 is a secondary issue in the other direction: two Checklist-approved
sites (Sturdee Park, Lake Breeze Park) receive $0 allocation. Worth
confirming with PM whether the work is occurring before adding the
LZ3 line.
```

Two paragraphs. Paragraph 1 is the headline pattern (5 of 6 close, 1 outlier, 94% of gap). Paragraph 2 is the secondary issue going the other way (zero allocation on LZ3).

Reconciliation table: seven rows (six zones + total), seven columns (Zone, Sites, Checklist/round, Tracker/month, Annual gap, % invoice, Status). The LZ6 row is rendered with red background, bold red text, and a red-top-and-bottom border to draw the eye. All other rows are alternating white/grey.

Bar chart below the table: per-zone Checklist (green) vs Tracker (light green when close, red when over). LZ6's bars are physically larger (height 13px vs 11px) and the row has a red background tint. The visual disproportion (red bar 266px vs green bar 88px) carries the "6× the approved level" finding.

Lift directly. Adapt the column count to the investigation's reconciliation shape (per-site instead of per-zone, per-account instead of per-zone, etc.).

---

## Beat 04 — Scenarios + scenario table + bar chart (visual4)

```
03 · EOFY — Three Scenarios

Without action, PK385 finishes at $241,524 — $76,574 over the $164,950
annual budget. Two corrections are available. The retrospective option
is the cleaner accounting answer but exposes PK473 at ~116%
immediately, which is probably why the current split has persisted.
```

Three sentences:

1. EOFY landing for do-nothing, framed against budget.
2. "Two corrections are available" — preview that the table has 2 corrections, not 3, even though it has 3 rows.
3. The most editorial sentence in the email. Names the political dynamic explicitly: the upstream PK473 surfacing is "probably why the current split has persisted." Use this kind of sentence sparingly.

Scenario table: three rows, six columns (#, Scenario, YTD P1-9, Q4, EOFY, vs $164,950). Row backgrounds: red, amber, green per the convention in `scenario_table_format.md`.

EOFY forecast bar chart: four rows (01, 02, Budget marker, 03). Bars in matching colours. Budget marker is a 2px-tall black row positioned where $164,950 falls on the same scale. Order is 01, 02, marker, 03 because that's roughly where the marker sits numerically.

Confirmation note in green-bordered callout:

```
SCENARIO 3 CONFIRMS THE CHECKLIST WAS RIGHT

The retrospective landing of $145,779 is consistent with your
Checklist's "Remaining funds $11,690 ex GST." The budget was
correctly sized throughout. PK385 looks stressed because the
Tracker has been charging it for work that belongs on PK473.
```

Three sentences. Each affirms Marisa's prior work. The eyebrow is small-caps green, body text is regular weight. The "Remaining funds $11,690 ex GST" is a direct quote from the Checklist itself — using her language, not paraphrasing.

Lift directly. Substitute the scenario numbers, the budget value, and the confirmation-note quote. If the budget was wrong, skip the confirmation note entirely.

---

## Beat 05 — Actions

```
04 · What Needs to Happen

Actions 1 and 2 are mechanical Tracker corrections. Actions 3 and 4
need your and Gihani's agreement first — the way the ask is framed
determines whether PK473's real position becomes visible.
```

One framing sentence. Names which actions are mechanical and which require decisions. The second sentence names the political consequence ("PK473's real position becomes visible") so the recipient can't miss it.

Four action cards:

```
01  Reset Tracker LZ6 PK385 slice from $13,993 to $2,306 per round
    Removes the $11,687/month misallocation. Straightforward — no
    judgement on work quality.
    Owner: Parks Maintenance · Type: Mechanical (green border + bg)

02  Add LZ3 allocation at $770/round
    Sturdee Park and Lake Breeze Park are on the Checklist but receive
    $0. Confirm with PM whether work is occurring before requesting
    the add.
    Owner: Parks Maintenance · Type: Mechanical (green border + bg)

03  Decide correction scope — prospective or retrospective
    Retrospective is cleaner but exposes PK473 at ~116-124%.
    Prospective stops the damage without surfacing the PK473 position.
    Owner: Marisa + Gihani · Type: Decision (amber border + bg)

04  Request written basis of $13,993 from PM before raising any change
    No vendor document or rate card supports the 19%. If PM can't
    produce a basis, the correction is low-risk. If they can, we
    review it first.
    Owner: Marisa + Gihani · Type: Decision (amber border + bg)
```

Two mechanical, two decisions. The decision cards are amber-bordered to visually separate them. The mechanical cards are green-bordered.

Card structure: one-line action headline, owner + type chip in the right margin of the headline row, one-line detail or risk below. Cards never exceed two lines of body text.

Action 04 is the highest-leverage card. It gates everything else on PM producing the basis. If PM can't produce one, the correction follows. If they can, the correction is reviewed. The Section Leader is given a clean off-ramp either way.

Lift the card structure. Adapt headlines, detail lines, owners, and types to the investigation. Preserve the green-mechanical / amber-decision colour distinction.

---

## Beat 06 — Closing + signature

```
Full reconciliation workbook attached — zone detail, LZ6 deep dive,
monthly pattern, and budget position. A 20-minute call before raising
anything with PM would be the fastest way to agree scope. Let me know
a time and I'll set it up.

Thanks,

Spero Efstathiadis
Assistant Financial Analyst · Parks · Logan City Council
```

Three sentences:

1. Names the attachment and what's in it.
2. Frames the next step as a 20-minute call.
3. Concrete CTA — "let me know a time and I'll set it up."

This is folded confidence (no explicit "I am confident X" sentence) — the workbook attachment is the implicit confidence claim, and the gating-on-call is the implicit acknowledgment that the basis question (PM's input) is the open thread.

Signature: name, title, team, org. All on one line below the name. Small font, grey.

Lift the structure verbatim. The 20-minute-call CTA is reusable across most investigations.

---

## Footer bar

```
PK385 Investigation · v6 · Pd9 Mar 2026          DM# 14719249 (Checklist) · DM# 17767639 (Tracker)
```

Carries: investigation reference, version tag, period reference, governance + operational document DM numbers.

The DM numbers in the footer are Audit-trail-grade. They are not in the body prose because the recipient doesn't navigate by DM during reading, but they are in the footer because anyone forwarding this email needs the citations.

Lift verbatim, substitute placeholders.

---

## What was cut from earlier drafts

The v3 and v4 drafts (not preserved as named files but referenced in the build history) had:

* A masked-budget visualisation (visual6 lift) showing PK473 at ~116-124%. Cut from v6 light because it duplicated information already in Action 03's body text. Kept as a reference visual in `html-email-finance-visual/templates/masked_budget.html` for use in follow-up emails after the decision lands.

* A site-level breakdown of LZ6 (visual7 lift) listing the seven LZ6 sites with their per-site Checklist amounts. Cut from v6 light because the per-site detail belongs in the workbook, not the email body. Kept as a reference visual.

* A visibility register (visual8 lift) — YES/NO question table bounding what the data answers. Cut from v6 light because the body prose carries the same bounds implicitly. Kept as a reference visual for investigations where the bound needs to be more visible.

* A monthly pattern visual (visual5 lift) showing the 9-month flat-line fingerprint of the fixed Tracker journal. Cut from v6 light because the consistency was already named in the prose. Kept as a reference visual for fingerprint-of-fixed-journal investigations where the visual is the finding itself.

The v6 light version uses 5 of 9 visuals. The v5 dark version was nearly identical with the dark palette substituted. Most investigations will use 4-6 of the 9.

---

## What to lift directly

When adapting this canonical to a new investigation:

* Header bar: lift verbatim, swap section name, code, period, send date.
* Eyebrow + hero number: lift the structure (eyebrow + Pattern 1 hero number); choose the hero pattern that matches the trace.
* KPI strip: 4-card pattern, lift the layout, swap the four numbers and four captions.
* Salutation: "Hi {{NAME}}," — first name only.
* Opening paragraph: lift the 5-sentence structure (passthrough nature → mechanism → gap → preview → cc reason), substitute specifics.
* Section eyebrow + thin underline: lift styling, change number and label.
* Allocation chain visual: lift, adapt step count and labels.
* Reconciliation table: lift, adapt column count.
* Scenario table: lift exactly, three scenarios, six columns.
* Confirmation note: lift styling; only include if confirming valid prior work.
* Action cards: lift structure, green-mechanical / amber-decision.
* Closing: lift the 20-minute-call CTA structure verbatim.
* Footer: lift verbatim, substitute placeholders.

What NOT to lift:

* The specific dollar amounts, PK numbers, contract references, zone names. These are PK385-specific.
* The "probably why the current split has persisted" sentence. The political-dynamic-naming move requires its own evidence in each investigation.
* The "Scenario 3 confirms the Checklist was right" callout if scenario 3 doesn't actually confirm prior work.
* Action 04's exact wording — "before raising any change" gate is reusable but the specifics are case-dependent.
