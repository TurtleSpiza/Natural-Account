# Investigation Email Template — Six Beats

This is the prose skeleton for a section-leader investigation email. Substitute placeholder values; lift visual blocks from `html-email-finance-visual/templates/` at the marked insertion points. Output is the email body — paste into Outlook (HTML compose) and send.

The skeleton is calibrated against the canonical PK385 Marisa email. Adapt sentence lengths, but preserve beat boundaries.

---

## Subject line

```
{{PK_OR_TOPIC}} — {{ONE_PHRASE_FINDING}}
```

Examples:

* `PK385 Urban Bushland — Allocation reconciliation` (PK385 Marisa email actual)
* `PK473 Parks Maintenance — Q4 LZ6 split correction` (follow-up email)
* `Cemeteries 73126 — Holding account passthrough check`

The subject states the scope (PK or topic) and the action being asked of the email. It is not the hero number — that opens the body.

---

## Beat 01 — Hero number + opening

The hero number is the subject-line-of-the-body. It reframes the visible misperception against the actual magnitude. See `hero_number_patterns.md` for the six patterns.

```
{{HERO_NUMBER_LINE}}

{{OPENING_PARAGRAPH}}
```

Hero number examples:

* `A $140,000 allocation gap, hiding as $10,808.`           (PK385 actual)
* `$73,432 of monthly invoice has no carve-out for {{PK}}.`
* `Six zones, one outlier, the $117k variance.`

Opening paragraph: 2-3 sentences. State the recipient relationship to the data ("you forwarded the Checklist", "your Section's PK"), name the passthrough nature, name the operational driver and the governance document, name the cc list reason.

PK385 actual:

> PK385 has no direct vendor invoices. Every dollar on it is a Parks Maintenance internal journal splitting the Austspray and Glascott zone invoices using fixed Tracker values. Those values have never been reconciled against the Checklist you forwarded. When I did that reconciliation, one zone explains the entire overspend. Gihani is cc'd so the finance side of any decision is visible from the start.

```
[INSERT VISUAL: kpi_strip.html]
```

The KPI strip carries the four cardinal numbers: YTD actual, FY budget, headline overspend (the small number), EOFY uncorrected (the large number). The contrast between the small-number column and the large-number column is the visual reframe of the hero line.

---

## Beat 02 — Mechanics

Plain-language walk from vendor invoice to destination PK. Three to five sentences. Name:

* The vendor and the invoice value (single lump sum, monthly, etc.)
* The contract reference if applicable
* The destination subject line — and what it does NOT include
* The journal that splits it (who posts, what driver, what % or $ values)
* The basis (or lack of basis) for those split values

PK385 actual:

> The Austspray LZ6 invoice is a single lump sum under contract PAR/338A/2025. It names PK000473 on the subject line only — no Urban Bushland carve-out, no site-level breakdown. Each month Parks Maintenance journals the invoice to two destinations using fixed Tracker values: 81% to PK473, 19% to PK385. Those percentages have no vendor-side basis and predate the current Checklist.

```
[INSERT VISUAL: allocation_chain.html]
```

The allocation chain visual is a five-step numbered trace: vendor invoices → holding account → journal posted → upstream destination → passthrough destination. Step 05 is the one that carries the finding (the misallocated value) and is rendered red.

---

## Beat 03 — Evidence (the reconciliation)

This is the longest beat. Two paragraphs of prose interpreting the reconciliation table.

Paragraph 1: state the headline pattern. How many lines reconcile, how many don't, where the gap concentrates. Use the percentage of the total gap explained by the outlier — "LZ6 alone drives 94% of the $117,286 annualised overcharge" — to anchor the recipient's attention to one line.

Paragraph 2 (optional): a secondary issue going the other way. Zero allocation, double allocation, missing site. Worth flagging because it shows the analysis is not just "find the overspend" but "reconcile the whole table."

PK385 actual:

> Five of six zones sit close to their Checklist-approved amounts. LZ6 is the outlier — Tracker charges $13,993/month against Checklist-approved scope of $2,306/round, six times the approved level. LZ6 alone drives 94% of the $117,286 annualised overcharge.
>
> LZ3 is a secondary issue in the other direction: two Checklist-approved sites (Sturdee Park, Lake Breeze Park) receive $0 allocation. Worth confirming with PM whether the work is occurring before adding the LZ3 line.

```
[INSERT VISUAL: reconciliation_table.html]
```

The reconciliation table has the outlier row visually highlighted (background colour, bold red text). The paired-bar chart inside the same template shows Checklist vs Tracker per zone. Both are needed — the table for the per-line numbers, the bar chart for the visual disproportion.

---

## Beat 04 — Scenarios

One framing paragraph, then the three-scenario table. See `scenario_table_format.md` for the column structure.

PK385 actual:

> Without action, PK385 finishes at $241,524 — $76,574 over the $164,950 annual budget. Two corrections are available. The retrospective option is the cleaner accounting answer but exposes PK473 at ~116% immediately, which is probably why the current split has persisted.

```
[INSERT VISUAL: scenario_comparison.html]
```

The scenario_comparison template carries both the scenario table and the EOFY forecast bar chart with the budget marker. After the visual, an optional confirmation note in a callout box ("Scenario 3 confirms the Checklist was right") closes the beat.

PK385 actual confirmation note:

> The retrospective landing of $145,779 is consistent with your Checklist's "Remaining funds $11,690 ex GST." The budget was correctly sized throughout. PK385 looks stressed because the Tracker has been charging it for work that belongs on PK473.

---

## Beat 05 — Actions

Framing sentence, then 2-4 numbered action cards.

Framing sentence: name which actions are mechanical and which require decisions.

PK385 actual:

> Actions 1 and 2 are mechanical Tracker corrections. Actions 3 and 4 need your and Gihani's agreement first — the way the ask is framed determines whether PK473's real position becomes visible.

Action card structure:

```
{{N}}  {{ONE_LINE_ACTION_HEADLINE}}                      {{OWNER}} · {{TYPE}}
       {{ONE_LINE_DETAIL_OR_RISK}}
```

Owner: who will execute. Section Leader, Finance, Parks Maintenance, you.

Type: `Mechanical` (low-judgement, just-do-it) or `Decision` (needs the recipient to choose). Visual styling differs in the template — green for mechanical, amber for decision.

PK385 actions:

```
01  Reset Tracker LZ6 PK385 slice from $13,993 to $2,306 per round
    Removes the $11,687/month misallocation. Straightforward — no judgement
    on work quality.
    Owner: Parks Maintenance · Type: Mechanical

02  Add LZ3 allocation at $770/round
    Sturdee Park and Lake Breeze Park are on the Checklist but receive $0.
    Confirm with PM whether work is occurring before requesting the add.
    Owner: Parks Maintenance · Type: Mechanical

03  Decide correction scope — prospective or retrospective
    Retrospective is cleaner but exposes PK473 at ~116-124%. Prospective
    stops the damage without surfacing the PK473 position.
    Owner: Marisa + Gihani · Type: Decision

04  Request written basis of $13,993 from PM before raising any change
    No vendor document or rate card supports the 19%. If PM can't produce
    a basis, the correction is low-risk. If they can, we review it first.
    Owner: Marisa + Gihani · Type: Decision
```

```
[INSERT VISUAL: numbered_summary.html — optional]
```

Use `numbered_summary.html` instead of, or alongside, the action cards if you want the closing emphasis on a 1-2-3 narrative recap (how it happened, what's happening now, what changes if uncorrected). The PK385 email used both — action cards in the body, numbered summary at the close.

---

## Beat 06 — Confidence + CTA

Optional but recommended. One paragraph. Two patterns:

Pattern A — confidence + CTA in one paragraph (PK385 actual):

> Full reconciliation workbook attached — zone detail, LZ6 deep dive, monthly pattern, and budget position. A 20-minute call before raising anything with PM would be the fastest way to agree scope. Let me know a time and I'll set it up.

Pattern B — explicit confidence statement first, then CTA (longer, used when the trace has known gaps):

> The 19% has no documented vendor basis I've been able to find. If PM produces a memo or rate card, the picture may shift — that's the only way I see this resolving differently. The reconciliation against the Checklist is firm; the question is what authorises the Tracker value.
>
> 20 minutes with you and Gihani is all we need.

```
[INSERT VISUAL: visibility_register.html — optional]
```

The visibility register is a YES/NO question table that bounds what the data can answer. Useful when the recipient might ask "but did you check X?" and the table preempts each X with the answer. Most emails do not need it; the canonical PK385 email did not include it in the v6 light, though it was prepared as visual8.

---

## Closing

```
Thanks,

{{NAME}}
{{TITLE}}  ·  {{TEAM}}  ·  {{ORG}}
```

PK385 actual:

```
Thanks,

Spero Efstathiadis
Assistant Financial Analyst · Parks · Logan City Council
```

---

## Header / footer (HTML email only)

The HTML email wraps the prose body in a header bar and a footer bar lifted from the v6 light variant. Header carries: section name, section code, period reference, send date. Footer carries: investigation reference, version tag, governance document DM numbers.

Header (HTML):

```
{{SECTION_NAME}} · SECTION {{SECTION_CODE}} · {{PD_REF}}      {{SEND_DATE}}
```

Footer (HTML):

```
{{TOPIC}} Investigation · v{{VERSION}} · {{PD_REF}}    DM# {{DM_GOVERNANCE}} ({{GOV_DOC_NAME}}) · DM# {{DM_OPERATIONAL}} ({{OP_DOC_NAME}})
```

PK385 actual:

```
NATURAL AREAS · SECTION 4090220 · PD9 MAR 2026                  22 Apr 2026
PK385 Investigation · v6 · Pd9 Mar 2026   DM# 14719249 (Checklist) · DM# 17767639 (Tracker)
```

Both header and footer are inside the table-as-layout structure of the v6 light variant. The plain-text email body version (in `PK385_email_body.txt`) does not carry these bars — they are HTML-only.

---

## Length budget

The PK385 Marisa email body (excluding visuals) is roughly 600 words. Beat-by-beat:

```
Beat 01 hero + opening      ~70 words
Beat 02 mechanics            ~65 words
Beat 03 evidence            ~110 words (two paragraphs)
Beat 04 scenarios            ~100 words (framing + confirmation note)
Beat 05 actions              ~140 words (framing + four cards)
Beat 06 confidence + CTA     ~50 words
                            ~535 words prose
                          + 5 visuals
```

Investigations smaller than PK385 (one-zone finding, single-month issue) compress to ~300-400 words and 3-4 visuals. Investigations larger than PK385 are usually two emails, not one big email — the second email handles the masked-budget surfacing as a follow-up after the first decision lands.

---

## Hand-assembly walkthrough

Step 1. Copy this skeleton into a new draft. Search-replace placeholders.

Step 2. Open the canonical Marisa email (PK385_email_Marisa_v6_light.html) in a browser and read it side-by-side. The pacing of sentences matters more than the templated structure.

Step 3. For each beat, write the prose first, then mark the visual insertion point. Do not paste visuals into a half-written beat — it commits you to the wrong block before the prose is settled.

Step 4. Lift visual blocks from `html-email-finance-visual/templates/`. Substitute placeholders. Render-check in Outlook.

Step 5. Stitch: paste the prose, then the visual, then the next prose, then the next visual. The email is now assembled.

Step 6. Lint the visuals (`email_html_lint.py --all`). Read the prose top-to-bottom once, fixing anything that trips. Confirm cc list. Send.
