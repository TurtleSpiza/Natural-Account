# Worked Example Paragraph — Annotated

The canonical demonstration paragraph from the style guide, annotated to show every voice marker in operation.

## The paragraph

> Budget remaining forecasting in a local government context is arguably one of the more underappreciated analytical exercises in the finance function, often dismissed as a mechanical roll-forward of actuals against phased budget, when in practice it is a judgement exercise with significant downstream consequences for the ELT's decision-making process. A forecast that understates year-end spend will result in programs being starved of intervention attention until the variance becomes unmanageable, conversely an overstatement results in unnecessary reprioritisation of funds away from sections that were on track. Cumulatively speaking, the cost of a poor forecast compounds over the quarter, and thus the forecasting methodology, however unglamorous, ought to be treated as a first-order deliverable rather than a spreadsheet artefact.

## The annotations

### Sentence 1 — opening with hedge-and-commit

> "Budget remaining forecasting in a local government context **is arguably** one of the more underappreciated analytical exercises in the finance function..."

* **"arguably"** — the dominant signature marker. Hedges the claim, but the structure of the sentence commits to it.
* **"in a local government context"** — parenthetical scoping. Tells the reader what frame applies.
* The opening already sets the position. The reader knows by sentence one that the writer thinks budget remaining forecasting is underappreciated AND that the writer is going to argue this.

> "...often dismissed as a mechanical roll-forward of actuals against phased budget, when in practice it is a judgement exercise with significant downstream consequences for the ELT's decision-making process."

* **"often dismissed as..."** — concession. Anticipates the counter-argument.
* **"when in practice it is..."** — pivot. Names what the writer thinks is true.
* **"significant downstream consequences"** — magnitude adjective. Note it is anchored later in the paragraph by the cumulative-cost claim; in a tighter draft, a dollar figure here would strengthen it. (The linter would flag this.)
* The opening sentence is one sentence, ~50 words, comma-chained. Multiple subordinate clauses. This is the corpus norm.

### Sentence 2 — the A-to-B-to-C causal chain

> "A forecast that understates year-end spend will result in programs being starved of intervention attention until the variance becomes unmanageable..."

* Mechanical chain: understatement → starvation → unmanageability. Each link explicit.
* No leap. The reader sees A → B → C without having to fill gaps.

> "...conversely an overstatement results in unnecessary reprioritisation of funds away from sections that were on track."

* **"conversely"** — counter-case explicit. Symmetric structure.
* **"reprioritisation"** — Australian spelling. Linter would flag "reprioritization" if drift slipped in.
* The sentence does both directions of the failure mode. The writer doesn't just argue one side; he names both and shows that both are bad.

### Sentence 3 — summary connector + obligation register + close

> "**Cumulatively speaking**, the cost of a poor forecast compounds over the quarter..."

* **"Cumulatively speaking"** — the corpus's signature summary opener. Signals: the previous claims are about to be summed.

> "...and thus the forecasting methodology, however unglamorous, **ought to** be treated as a first-order deliverable rather than a spreadsheet artefact."

* **"thus"** — causal connector. Links the cumulative cost to the recommendation.
* **"however unglamorous"** — mid-sentence "however," not as sentence opener. Preceded by a comma, not a period.
* **"ought to"** — obligation register. Stronger than "should". Signals normative necessity.
* **"first-order deliverable rather than a spreadsheet artefact"** — the verdict. Decisive close. No "in summary" hedge; the sentence stops on the position.

## What the paragraph demonstrates

| Voice marker                          | Where in paragraph                          |
|---------------------------------------|---------------------------------------------|
| "arguably" hedge-and-commit           | Sentence 1                                  |
| Long opening sentence (~50 words)     | Sentence 1                                  |
| Comma-chained subordinate clauses     | Sentence 1                                  |
| Concession + pivot                    | Sentence 1 ("often dismissed... when")      |
| A-to-B-to-C causal chain              | Sentence 2                                  |
| Symmetric counter-case                | Sentence 2 ("conversely")                   |
| "Cumulatively speaking" summary       | Sentence 3                                  |
| "thus" causal connector               | Sentence 3                                  |
| "however" mid-sentence                | Sentence 3 ("however unglamorous")          |
| "ought to" obligation                 | Sentence 3                                  |
| Decisive verdict close                | Sentence 3 ("first-order deliverable...")   |
| Australian spelling                   | "reprioritisation"                          |

Eleven distinct voice markers in three sentences, ~120 words. This is the density to aim for.

## What the paragraph does not demonstrate

* **Em-dashes.** Correctly absent. The parentheticals are set off with commas instead.
* **Bullet lists.** Pure prose.
* **Mid-paragraph "However,..."** as opener. The "however" appears mid-sentence as expected.
* **Banned hedges.** No "perhaps", "it could be argued", "some might say".
* **American spelling.** All Australian.

## Lint check

Running the linter on this paragraph:

```
python style_lint.py worked_example.md --info

OK — no style violations.
```

(It does not flag "significant downstream consequences" because the linter scans within ~200 chars for an anchoring quantity, and the cumulative cost claim later in the paragraph counts as the anchoring evidence — though strictly a dollar figure in the same sentence would be better.)

Fingerprint:

```
python style_lint.py worked_example.md --fingerprint

Words: 124, Sentences: 3, Avg sentence length: 41.3 words
Marker counts:
  arguably           1
  ought_to           1
  self_evidently     0
  cumulatively       1
  so_to_speak        0
  ie_inline          0
  however_inline     1
  thus               1
  consequently       0
  in_turn            0
```

## Adapting to longer pieces

The 124-word paragraph carries 5+ signature markers. Scaled up to 500-1000 words, expect:

* "arguably" — 1-2 instances minimum
* "ought to" — 1 instance if the piece carries a recommendation
* "however," — 2-4 instances mid-sentence
* "thus" / "consequently" / "in turn" — 4-8 combined
* Long sentence (40+ words) — at least every other paragraph

Below those densities, the voice reads as Claude-default. The linter doesn't enforce these densities directly (only flags `arguably` count = 0 at >500 words), but the discipline is to write toward them.
