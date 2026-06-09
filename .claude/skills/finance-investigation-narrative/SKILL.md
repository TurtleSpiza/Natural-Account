---
name: finance-investigation-narrative
description: Section-leader investigation email composition for LCC Parks passthrough findings. Hero-number opening, six-beat structure (mechanics, evidence, scenarios, actions, confidence, call-to-action), Finance partner cc'd, register calibrated for non-finance recipients. Use whenever drafting an email to a Section Leader (Marisa, Pat, Andrew, Cameron) communicating a cost-allocation trace finding, passthrough-PK reconciliation, masked-budget surfacing, or any Parks investigation outcome with a recommended action. Triggers on 'email Marisa', 'investigation email', 'PK385 email', 'draft the section-leader email', 'compose the finding email', 'cc Gihani'. Distinct from lcc-finance-batch-email (Finance batch register) and html-email-finance-visual (the visual blocks). This skill is the prose skeleton plus register rules that wraps visual blocks into a coherent investigation email.
---

# finance-investigation-narrative

The skill that turns a finished cost-allocation trace into a section-leader email. The Marisa email about PK385 Urban Bushland is the canonical example — six beats, four to six visual blocks, ~600 words of prose, one decision asked of the recipient, Finance cc'd from the start.

This skill produces the prose skeleton. The visual blocks live in `html-email-finance-visual` and are referenced here by filename. The trace and reconciliation that supplies the content lives in `lcc-cost-allocation-tracing`.

## When to apply

Apply this skill when:

* You have a finished trace from `lcc-cost-allocation-tracing` and need to communicate the finding to a Section Leader who owns the relevant scope (Marisa for Natural Areas, Pat for Parks Maintenance, etc.).
* The finding has a recommended action that requires the Section Leader's agreement before it can be raised with the operational team or Finance.
* The recipient is non-finance and the email needs to land the mechanics in plain language alongside the visual blocks.
* The investigation is large enough to warrant its own email (one finding, one recipient thread). Multi-finding mechanical batches go to Finance via `lcc-finance-batch-email` instead.

Do not apply this skill when:

* The deliverable is a Finance batch query covering multiple unresolved miscodes. That is `lcc-finance-batch-email` — different register, different recipients, different format.
* The deliverable is an operational request to PM, vendor, or contractor. Those use the operational register (shorter, no scenarios, no Finance cc).
* The recipient is internal Finance (Amy, Owen, Gihani-only). The investigation email does cc Gihani, but the primary recipient is the Section Leader.
* You don't yet have a trace finding. Run the trace first via `lcc-cost-allocation-tracing`.

## The six-beat structure

Every investigation email follows this beat sequence. Beats can compress (some merged into one paragraph) but the order does not change.

```
01  HERO NUMBER          One sentence subject line + one-paragraph hook.
                          The headline finding stated as a number reframe.
                          "A $140,000 allocation gap, hiding as $10,808."
                          Then 2-3 sentences of context.

02  MECHANICS            How the misallocation happens. Plain-language walk
                          from vendor invoice to destination PK. Names the
                          journal, the holding account, the operational
                          driver, the governance basis.
                          Visual: allocation_chain.html

03  EVIDENCE             The reconciliation. Per-zone or per-site table
                          showing where the gap sits. Surfaces the outlier
                          line. One paragraph of prose interpreting the
                          table — "five zones close, LZ6 explains 94%".
                          Visual: reconciliation_table.html (and bar chart
                          in the same template)

04  SCENARIOS            EOFY landing under three scenarios: do nothing,
                          fix prospective, fix retrospective. One-line
                          paragraph framing the trade-off, then the table.
                          Visual: scenario_comparison.html

05  ACTIONS              Numbered actions with owner and type. Mechanical
                          actions first (Tracker resets, journal recodes),
                          decisions second (correction scope, basis
                          requests). 2-4 actions total. Each action is one
                          sentence describing what + one sentence
                          describing why or risk.
                          Visual: numbered_summary.html (optional close)

06  CONFIDENCE + CTA     One paragraph that bounds what the data can and
                          cannot answer (confidence statement) and ends
                          with a concrete next step — usually "20 minutes
                          with you and Gihani is all we need."
                          Visual: visibility_register.html (optional)
```

## File index

```
SKILL.md                          This playbook.
investigation_email_template.md   The full six-beat skeleton with placeholder
                                  prose and visual-block insertion points.
                                  Lift this when starting a new investigation
                                  email from scratch.
register_distinctions.md          Comparison table: section-leader register vs
                                  finance-batch register vs operational
                                  register. Tone, recipients, structure,
                                  vocabulary, what to cut.
hero_number_patterns.md           Six patterns for the headline number reframe.
                                  How to find the "X hiding as Y" framing for a
                                  given trace finding.
scenario_table_format.md          The three-scenario table structure (do
                                  nothing / prospective / retrospective).
                                  When each scenario applies. How to
                                  populate the columns.
confidence_statement_patterns.md  How to bound the claim without hedging into
                                  uselessness. Three patterns: data-bounded,
                                  evidence-bounded, scope-bounded.
canonical_marisa_email.md         The PK385 Marisa email annotated beat-by-
                                  beat. The reference example.
```

## Workflow

Step 1. Confirm the trace is finished. The reconciliation must surface a single dominant outlier or a small set of named lines. If the finding is still ambiguous, finish the trace first — do not write the email around uncertainty.

Step 2. Identify the recipient and the cc list. The Section Leader who owns the scope is the primary recipient. Gihani Munaweera (Senior Financial Analyst, Parks) is cc'd by default for any PK-allocation finding. Amy Forgione is cc'd if the action requires a Finance journal she'll process. Owen Jensen rarely on this register — he sees the Finance batch instead.

Step 3. Write the hero number first. Pick the framing from `hero_number_patterns.md`. The hero number does two things: states the headline and states the misperception simultaneously. "$140,000 allocation gap, hiding as $10,808" is not "we have a $10,808 variance" — it is the revealed magnitude alongside the visible magnitude. Spend disproportionate time here. The rest of the email follows from this.

Step 4. Lift the six-beat skeleton from `investigation_email_template.md`. Substitute the names, numbers, accounts, contracts. Keep beat boundaries visible to yourself even though the recipient won't see headers — the structure is the discipline.

Step 5. Insert visual blocks from `html-email-finance-visual/templates/` at the points called out in the skeleton. Picking templates: `kpi_strip` opens, `allocation_chain` carries beat 02, `reconciliation_table` carries beat 03, `scenario_comparison` carries beat 04, `numbered_summary` optionally closes beat 05, `visibility_register` optionally bounds beat 06. Most investigations use four to six of the nine available templates, not all nine.

Step 6. Calibrate the register against `register_distinctions.md`. The most common drift is finance-batch register leaking in: cite-the-account, mechanical, "please action" phrasing. Pull it back to section-leader register: explain mechanics, name the consequence, ask for a decision.

Step 7. Confidence statement. Read `confidence_statement_patterns.md`. The bound is part of the credibility — "the 19% has no documented basis I've found" is stronger than "I think the 19% might be wrong" because it states what you know and what you don't. The recipient extracts the same conclusion either way; the first one survives the question "are you sure?" intact.

Step 8. CTA. Always concrete. "20 minutes with you and Gihani" beats "let me know if you have questions." Name the duration, name the participants, offer to set it up. The recipient should be able to reply "Tuesday 10am" and have everything they need.

Step 9. Send-readiness check. Lint the visual blocks via `html-email-finance-visual/email_html_lint.py`. Read the prose aloud — anything that trips you reads as clumsy to the recipient. Confirm the cc list matches what the actions require (do not cc Finance on a not-yet-decided action).

## Reference artefacts

This skill draws on:

* `lcc-cost-allocation-tracing/worked_example_pk385.md` — the trace that supplies content for the canonical email. Re-read both together; the email is the trace's communication layer.
* `html-email-finance-visual/templates/` — the nine visual blocks, referenced by filename in `investigation_email_template.md`.
* `full_chart_of_accounts.json` (also at `_shared/lcc_chart_of_accounts.json`) — confirm account names match the chart before naming them in the email.
* `service_section_pk_map.json` (also at `_shared/`) — confirm PK numbers and section ownership before naming them in the email.

## Cross-skill flow

```
lcc-cost-allocation-tracing
  produces: trace + reconciliation + open questions + corrected position
       │
       ▼
finance-investigation-narrative   [THIS SKILL]
  produces: section-leader email body (six beats, ~600 words prose)
       │
       ├──── pulls visual blocks from ────▶ html-email-finance-visual/templates/
       │
       ▼
techone-genjnl-format
  produces: the recode journal that delivers Action 01, attached or sent
            after the Section Leader confirms the correction scope
```

If the email asks for a decision and the Section Leader says yes, the techone-genjnl-format skill produces the journal that actions it. If they say no or want more, the trace re-opens and a follow-up email may be needed — the same six-beat structure, narrower scope.

## Register rules — the short version

The full table is in `register_distinctions.md`. The short version:

* **Recipient is non-finance.** Explain mechanics in plain language. "Parks Maintenance journals the invoice using fixed Tracker values" — not "the GJ splits 1-20276-73126 by an unverified driver."
* **Cite documents by what they are, not by their DM number alone.** "Your Checklist (DM# 14719249)" — the recipient knows it as the Checklist; the DM is auxiliary.
* **Names belong to people.** "Gihani is cc'd so the finance side is visible from the start" — not "Senior Financial Analyst is in the loop." Use first names where the recipient knows them.
* **The recommendation must include a "before this happens" gate.** "Before raising the correction, ask PM for the basis." Section Leaders distrust unconditional recommendations and the gate gives them a clean off-ramp if the trace turns out incomplete.
* **One decision at a time.** Mechanical actions can be plural. The decision the Section Leader is asked to make is singular — usually "prospective or retrospective." Do not ask two decisions in one email.

## Anti-patterns

* **Leading with the small number.** The variance report shows $10,808 over. Leading with that frames the issue as small. Lead with the underlying gap ($140,000) and state the small number as the symptom.
* **Hedging the hero number.** "We may have a potential allocation issue" softens the hero number into uselessness. The hero number should be the strongest factual statement in the email. Confidence elsewhere is for the bounds and the decision, not the headline.
* **Dropping Gihani off the cc.** Finance is visible from the start of the conversation by design. The Section Leader knows the question is being asked with Finance in the loop, which means the answer commits a path. If Gihani is not cc'd, the ask reads as a hypothesis instead of an investigation.
* **Asking for confirmation of mechanics in the email body.** Mechanics that are still in flux belong in the trace, not the email. If the email needs to say "I think the journal works like this, can you confirm?" the trace is not finished.
* **Stacking nine visual blocks.** The PK385 email used five (kpi_strip, allocation_chain, reconciliation_table + bar chart, scenario_comparison + scenario bar chart, numbered_summary). Most investigations use four to six. Nine is a dashboard, not an email.
* **Section headers in caps.** The Marisa v6 light variant uses small-caps eyebrow labels (`01 · How the Overspend Happened`). Plain ALL-CAPS section headers are operational-register, not section-leader register.

## Known traps

* **The "do nothing" scenario embarrasses.** When scenario 01 is "do nothing → over budget by $76k," recipients sometimes read that as accusation. It isn't — it's the counterfactual that makes scenarios 02 and 03 legible. Frame it as "this is the trajectory if no change is made," not "this is what will happen if you don't act."
* **The masked-budget consequence.** When the correction surfaces an overspend on the upstream PK, the email must name that effect explicitly. The Section Leader needs to know the political dynamic before agreeing to the action — otherwise they agree, the upstream surfaces, and they feel ambushed. Name it. The Marisa email's Action 03 names exactly this.
* **PK385 is a passthrough; PK473 is upstream.** Do not invert these in the email. Passthrough = receives spend via journal split, no direct invoices. Upstream = receives the invoice direct, splits it via journal. A passthrough overcharge masks an upstream overspend. Always name both.
* **The Tracker is operational; the Checklist is governance.** Do not let the Tracker carry approval weight in the prose. The Checklist is what Marisa owns. The Tracker is what PM operates against. Reconciliation goes Checklist → Tracker, not the reverse.
