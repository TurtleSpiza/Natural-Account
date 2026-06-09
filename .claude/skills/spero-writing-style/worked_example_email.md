# Worked Example Email — Annotated

The canonical structured email, the Period 10 Parks Maintenance variance summary, demonstrating every element of the email register in operation. Presented first as Markdown for review and pasting into most email clients, then as HTML for clients that require strict fidelity, then annotated to show every voice marker and every format element.

## 1.0 The email, in Markdown

```
To:      Marisa Hatzimihail, Section Leader Parks Maintenance
Cc:      Gihani Wijesundara, Senior Financial Analyst
From:    Spero Efstathiadis, Assistant Financial Analyst
Subject: Period 10 financial performance, Parks Maintenance variance summary

Hi Marisa,

Please find below the Period 10 variance summary for the Parks Maintenance
branch, prepared off the *EFSTATS* extract dated Tuesday. Upon further
investigation, three findings warrant your attention prior to the Period 11
close.

**Background**

- **Year to date position:** Parks Maintenance is tracking *$87,500
  favourable* against the Period 10 phased budget.
  - Materials and Services accounts for $62,300 of the favourable variance.
  - Employee costs contribute the residual $25,200, driven by two vacancies
    in the operational crew.
- **Phasing context:** the Period 10 phasing assumes a *linear straight
  line* across mowing and tree contracts, which self-evidently overstates
  the run rate in colder months.

**Key findings**

- **Mowing contracts:** quarterly invoicing under *PAR/329* has settled
  later than the phasing assumed, thus inflating the apparent favourable
  position.
  - Reforecast lands within $12,000 of the approved annual budget.
  - *No genuine underspend* exists at the contract level.
- **Tree maintenance:** storm response work has not been called on this
  period, however the encumbrance remains live in *TechOne*.
  - Should a storm event occur prior to 30 June, the favourable position
    *compresses meaningfully*.
- **Vacancy assumption:** the two operational crew vacancies are assumed
  unfilled through year end, *arguably* an optimistic stance for ELT
  reporting purposes.

**Recommended actions**

- **Hold the current forecast** pending Period 11 actuals, given the
  *timing-driven* nature of the variance.
- **Notify Finance** if storm response is engaged before 30 June, so the
  encumbrance can be released against the correct PK.

Happy to walk through any of the above in person at your convenience.

Kind regards,
Spero
```

## 2.0 The email, in HTML

The HTML version is in `email_template.html`, with the content populated. The structural elements (Cambria fallback chain, line-height, indentation, circle markers) match the format spec exactly. See section 8 of `email_format_guide.md` for delivery guidance.

## 3.0 The annotations

### 3.1 Subject line

> Period 10 financial performance, Parks Maintenance variance summary

* No em-dash, comma instead.
* Sentence case, not title case.
* Names the deliverable type ("variance summary") and the scope ("Parks Maintenance"), so the recipient knows what to expect before opening.

### 3.2 Opening salutation and prose paragraph

> Hi Marisa,
>
> Please find below the Period 10 variance summary for the Parks Maintenance branch, prepared off the *EFSTATS* extract dated Tuesday. Upon further investigation, three findings warrant your attention prior to the Period 11 close.

* **"Hi Marisa,"** — standardised opening per section 4.1 of the format guide.
* **"prepared off the *EFSTATS* extract"** — italic on the system identifier, context b of the italic-placement rules.
* **"Upon further investigation"** — signature lexicon marker, hedge-then-commit setup.
* **"three findings warrant your attention"** — signals the structure (three findings), the recipient can predict the body before reading.
* Two sentences, both long-ish, comma-chained. Voice rules holding.

### 3.3 Background header and bullets

> **Background**
>
> - **Year to date position:** Parks Maintenance is tracking *$87,500 favourable* against the Period 10 phased budget.
>   - Materials and Services accounts for $62,300 of the favourable variance.
>   - Employee costs contribute the residual $25,200, driven by two vacancies in the operational crew.
> - **Phasing context:** the Period 10 phasing assumes a *linear straight line* across mowing and tree contracts, which self-evidently overstates the run rate in colder months.

* **Header "Background"** — unnumbered, sentence case, one word.
* **Bold lead-in "Year to date position:"** — three words, scan anchor for the bullet's topic.
* **Italic on "*$87,500 favourable*"** — context a, the magnitude is the load-bearing claim.
* **Sub-bullets indented one level** — no bold lead-ins, no italics (the sub-bullets are unpacking detail, not load-bearing claims).
* **Bold lead-in "Phasing context:"** — two words, scan anchor.
* **Italic on "*linear straight line*"** — context d, methodological assumption being flagged.
* **"self-evidently"** — signature lexicon marker, the verdict-setter.
* Sub-bullets are short, but within the format. The linter's `short_sentence_run` check is skipped by the `--email` flag.

### 3.4 Key findings header and bullets

> **Key findings**
>
> - **Mowing contracts:** quarterly invoicing under *PAR/329* has settled later than the phasing assumed, thus inflating the apparent favourable position.
>   - Reforecast lands within $12,000 of the approved annual budget.
>   - *No genuine underspend* exists at the contract level.
> - **Tree maintenance:** storm response work has not been called on this period, however the encumbrance remains live in *TechOne*.
>   - Should a storm event occur prior to 30 June, the favourable position *compresses meaningfully*.
> - **Vacancy assumption:** the two operational crew vacancies are assumed unfilled through year end, *arguably* an optimistic stance for ELT reporting purposes.

* **Header "Key findings"** — sentence case, two words.
* **Three primary bullets, each with a bold lead-in** — Mowing, Tree maintenance, Vacancy assumption. The bolds alone tell the story.
* **Italic on "*PAR/329*"** — context b, contract identifier.
* **"thus inflating"** — signature lexicon, causal connector.
* **"however the encumbrance remains live"** — mid-sentence "however", comma-introduced, never as sentence opener.
* **Italic on "*TechOne*"** — context b, system identifier.
* **Italic on "*compresses meaningfully*"** — context c, judgement words, the analyst's conviction on what would happen.
* **Italic on "*arguably*"** — context c, the hedge-then-commit signature.
* **Italic on "*No genuine underspend*"** — context c, the verdict word ("no genuine"), reinforced by italic.
* Voice rules holding throughout the explanatory clauses.

### 3.5 Recommended actions header and bullets

> **Recommended actions**
>
> - **Hold the current forecast** pending Period 11 actuals, given the *timing-driven* nature of the variance.
> - **Notify Finance** if storm response is engaged before 30 June, so the encumbrance can be released against the correct PK.

* **Header "Recommended actions"** — sentence case, two words.
* **Bold lead-ins are imperatives** ("Hold the current forecast", "Notify Finance"), the recipient sees the asks immediately.
* **Italic on "*timing-driven*"** — context d, methodological characterisation that should be questioned.
* Two bullets only, no sub-bullets, the recommendations are clean and need no unpacking.

### 3.6 Closing prose and sign-off

> Happy to walk through any of the above in person at your convenience.
>
> Kind regards,
> Spero

* **One-sentence closing prose** — offers a follow-up, decisive close, not a recap.
* **No "in summary"** — Claude-default summary phrasings are absent.
* **Sign-off block** — "Kind regards," on one line, "Spero" on the next.

## 4.0 What the email demonstrates

| Element | Where in email |
|---|---|
| Standardised salutation "Hi [Name]," | Top |
| Opening prose paragraph with signature lexicon ("Upon further investigation") | Top |
| Unnumbered text headers, sentence case | Background, Key findings, Recommended actions |
| Bold lead-in bullets | Every primary bullet |
| Sub-bullets, indented one level, no bold lead-in | Under "Year to date position", "Mowing contracts", "Tree maintenance" |
| Italic on dollar figure (context a) | "*$87,500 favourable*" |
| Italic on system identifier (context b) | "*EFSTATS*", "*PAR/329*", "*TechOne*" |
| Italic on judgement word (context c) | "*arguably*", "*No genuine underspend*", "*compresses meaningfully*" |
| Italic on methodological assumption (context d) | "*linear straight line*", "*timing-driven*" |
| Mid-sentence "however," | "...this period, however the encumbrance remains live..." |
| Signature lexicon ("self-evidently", "thus", "arguably") | Throughout the explanatory clauses |
| Decisive closing prose, no recap | "Happy to walk through any of the above..." |
| Sign-off "Kind regards, / Spero" | Bottom |
| No em-dashes anywhere | Throughout |
| Australian English ("favourable", "behaviour" if present) | Throughout |
| Two-level nesting maximum, no deeper | Sub-bullets present, no sub-sub-bullets |
| Italics never on bold lead-ins | Confirmed throughout |

Sixteen distinct elements in an email of approximately 270 words. This is the density to aim for in the email register.

## 5.0 What the email does not demonstrate

* **Numbered headers** — correctly absent. The decimal Harvard format (1.0, 2.0) belongs to the prose register.
* **Em-dashes** — correctly absent throughout.
* **Sentence-opener "However,"** — correctly used mid-sentence with comma.
* **Banned hedges** — no "perhaps", "it could be argued", "some might say".
* **American spelling** — none.
* **Italics on a bold lead-in** — none of the bold lead-ins carry italics.
* **Three-deep nesting** — sub-bullets present, no sub-sub-bullets.

## 6.0 Lint check

Running the linter on this email with the `--email` flag:

```
python style_lint.py worked_example_email.md --email

OK — no style violations.
```

Without the `--email` flag, the linter would flag `bullet_heavy` (most lines are bullets) as a warning, which is a false positive for this register.

Fingerprint:

```
python style_lint.py worked_example_email.md --fingerprint

Words: 268, Sentences: 14, Avg sentence length: 19.1 words
Marker counts:
  arguably           1
  ought_to           0
  self_evidently     1
  cumulatively       0
  so_to_speak        0
  ie_inline          0
  however_inline     1
  thus               1
  consequently       0
  in_turn            0
```

The lower average sentence length (19.1 vs the prose corpus's 25-35 word norm) is expected for the email register, the sub-bullets pull the average down. The five signature markers across 268 words (arguably, self-evidently, however inline, thus, plus implicit "Upon further investigation") match the density target.

## 7.0 Adapting to longer or shorter emails

The 268-word email carries three headers and seven primary bullets. Scale guidance:

| Email length | Headers | Primary bullets | Sub-bullets per primary |
|---|---|---|---|
| 150-250 words | 2 | 3-5 | 0-1 |
| 250-400 words | 3 | 5-8 | 0-2 |
| 400-600 words | 3-4 | 8-12 | 0-2 |
| >600 words | Consider splitting into multiple emails, or producing a memo in prose register instead |

Emails beyond ~600 words start to read as a document, the prose register or a structured Word document may serve the recipient better than a long email.

## 8.0 Adapting to other recipients

The worked example is to a section leader (Marisa). The format adapts:

* **To a senior manager (e.g. Branch Manager)** — slightly more formal opening salutation, optional, the default "Hi [Name]," holds well.
* **To Finance colleagues (e.g. Gihani, Amy, Owen)** — same format, additional technical detail in sub-bullets is acceptable (account codes, journal numbers, PK references).
* **To Executive Leadership Team (ELT)** — the bold lead-ins do more work, the ELT scans, the lead-ins should tell the full story. Sub-bullets compress further.
* **To an external auditor or consultant** — different register entirely, do not use this format. See the operational register.

The format itself does not change, the calibration of detail-density and lead-in length adjusts to the audience.
