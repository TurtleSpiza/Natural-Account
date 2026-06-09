# Checklist for Drafting in Voice

Eight items. Apply during drafting, not after. The linter catches mechanical violations; this checklist catches register drift.

## 1. Open with the thesis, not the warm-up

The writer states the position in the first sentence and begins arguing it. Documents that ease into the topic with two paragraphs of context before the claim do not match the corpus.

```
Bad:    "There are many considerations when evaluating budget remaining
        forecasting in local government. This document examines them."

Good:   "Budget remaining forecasting in a local government context is
        arguably one of the more underappreciated analytical exercises in
        the finance function..."
```

The "good" version states the claim ("arguably one of the more underappreciated"), commits to it via the structure of the sentence, and signals the argumentative chain with the long opening clause.

## 2. Hedge then commit, don't hedge then trail off

The signature move is "arguably... ought to". A claim is qualified, then committed to. Hedges that stand alone — "perhaps", "it could be argued", "in certain circumstances" — do not appear in the corpus and signal a different voice.

```
Bad:    "Perhaps the forecasting methodology should be improved."

Good:   "The forecasting methodology, however unglamorous, ought to be
        treated as a first-order deliverable rather than a spreadsheet
        artefact."

Better: "Arguably the forecasting methodology, however unglamorous,
        ought to be treated as a first-order deliverable rather than
        a spreadsheet artefact."
```

The "arguably" + "ought to" pair is the highest-density signal of the voice.

## 3. Prose paragraphs that chain reasoning are the default

Bullets are reserved for genuinely enumerable content: recommendation lists, risk profiles, advantages-and-disadvantages comparisons. A response that is predominantly bullets — even with full-sentence bullets — does not match.

If the content can flow as prose, it should. The structure of long comma-chained sentences is a feature, not a bug; it forces the writer to make causal links explicit and the reader to follow them.

```
Bad:    "The forecast affects:
        - Programs being starved of intervention attention
        - Reprioritisation of funds away from on-track sections
        - The ELT's decision-making process"

Good:   "A forecast that understates year-end spend will result in
        programs being starved of intervention attention until the
        variance becomes unmanageable, conversely an overstatement
        results in unnecessary reprioritisation of funds away from
        sections that were on track."
```

The prose version surfaces the causal direction and the cumulative effect. The bullets list outcomes without their mechanism.

## 4. Australian English throughout

"optimise", not "optimize". "favourable", not "favorable". "behaviour", not "behavior". "labour", not "labor". "centre", not "center". "analyse", not "analyze".

The linter catches these mechanically. The discipline is to draft in Australian English from the start, not to draft in American and find-replace afterwards — find-replace misses subtler drifts ("realise" vs "realize", "pretence" vs "pretense").

## 5. Use the signature lexicon

Density-ranked markers from the 63k word corpus:

* **arguably** (32 instances) — the dominant signal. At least one per ~500-2000 words.
* **ought to** (9) — for normative judgements.
* **however,** (mid-sentence, comma-introduced) — never as opener.
* **self-evidently** (8) — for closing arguments.
* **so to speak** (7) — for softening idioms.
* **cumulatively** (4) — for summary connectors. "Cumulatively speaking" is even higher signal.
* **i.e.** — to gloss a technical term inline rather than in parentheses.

Causal connectors used densely (often 2-3 per paragraph):

* thus, therefore, consequently, in turn, as a result, ultimately

The marker density is what makes the voice recognisable. A draft with zero "arguably" and zero "however,X,Y" structures will read as Claude-default, not Spero.

## 6. No em-dashes, ever

The hard rule. Em-dashes (`—`) and en-dashes (`–`) do not appear in the 63k word corpus. The writer reaches for one of three alternatives:

* A comma, when the parenthetical is short.
* Parentheses, when the parenthetical is longer or more separable.
* A full stop and a new sentence, when the parenthetical breaks the flow.

```
Bad:    "Budget remaining forecasting — arguably underappreciated — is
        a judgement exercise."

Good:   "Budget remaining forecasting, arguably underappreciated, is a
        judgement exercise."

Or:     "Budget remaining forecasting (arguably underappreciated) is a
        judgement exercise."
```

The Claude default produces em-dashes constantly. Override deliberately.

## 7. Mechanical argument chains, not implied logic

The writer rarely leaves inference to the reader. Each link in the chain is surfaced. The consequence of each step is stated. The cumulative verdict is delivered at the end of the paragraph or section.

```
Bad:    "Tariffs caused economic problems, including unemployment."

Good:   "It was more expensive for US businesses to purchase supply
        costs to create goods, decreasing the viability of business
        conditions, in turn business owners were attempting to
        dismiss workers. Other nations retaliated with their own
        tariffs against the US, further exacerbating the poor
        economic conditions."
```

The "good" version names the mechanism (cost rise → viability drop → dismissals → retaliation → exacerbation). The reader sees each step. The writer's confidence is grounded in the chain.

## 8. Close with a verdict, not a summary

The last paragraph delivers a decisive judgement. "In summary, X, Y, Z were discussed" does not appear in the corpus. The closes that do appear:

* "Government intervention in trade policy not only isn't viable, but it's also dangerous..."
* "Super is a long-term 'game'."
* "Continuous vs discrete data so to speak."

A verdict close uses an intensifier ("decisively", "self-evidently", "the only", "ought to be"), commits to a position, and ends. A summary close re-states what was said and trails off. The first matches; the second does not.

## Pre-flight check before sending

Run the linter:

```
python style_lint.py draft.md
```

Address the errors. Review the warnings — most should be fixed, some may be intentional. Skip the info-level findings unless something jumps out.

Read the draft aloud. If a sentence trips you, it will trip the reader. Long comma-chained sentences must still be readable; if they're not, break them with a full stop, not an em-dash.

Check the close. Last paragraph carries the verdict?

Check "arguably" appears. If 0 instances and >500 words, add one.

Send.
