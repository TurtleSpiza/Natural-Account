# Email Format Guide

The structured email register Spero uses for management correspondence. This guide is the canonical spec, every element documented here is deliberate. The format coexists with the prose register documented in `style_guide.md` and `checklist_for_drafting.md`, voice rules from those documents still apply within the email's prose passages.

## 1.0 When the email register applies

Apply this format when:

* The email is addressed to a section leader, manager, finance colleague, or other internal stakeholder.
* The email conveys multiple findings, multiple recommendations, or multiple data points that benefit from visual hierarchy.
* The recipient is likely to skim before reading in full, the bold lead-ins act as scan anchors.
* The email is more than ~150 words.

Do not apply this format when:

* The email is a one-line acknowledgement ("Confirmed, thanks Marisa").
* The email is a scheduling reply ("Tuesday 2pm works for me").
* The email is a single ask that flows as prose more naturally than as bullets.
* The recipient is external (vendor, consultant, supplier), use the operational register instead.
* The email is personal correspondence.

## 2.0 The four format elements

### 2.1 Element one, unnumbered text headers

Plain text labels, one to three words, set in Cambria at 15.5px with weight 500 (bold). No numbering, the decimal Harvard format (1.0, 2.0, 2.1) is reserved for the prose register.

A single blank line before each header, a single blank line after. The body content sits flush against the header on the line below.

Canonical headers, in approximate order of appearance:

| Header | Purpose |
|---|---|
| Background | Sets the scene, the YTD position, the framing data point |
| Key findings | The analytical content, the variances, the surprises |
| Open questions | Items requiring the recipient's input or decision |
| Recommended actions | The asks, the next steps, the calls-to-action |
| Next steps | Procedural follow-up, less analytical than recommendations |
| Risks | Items that could derail the position, optional |
| Methodology | A note on how the numbers were derived, used sparingly |

Header text uses sentence case ("Key findings"), not title case ("Key Findings") and not all caps ("KEY FINDINGS"). Sentence case matches the academic register Spero uses elsewhere.

### 2.2 Element two, bold lead-in bullets

Each primary bullet opens with a bold phrase that summarises the bullet's topic, followed by a colon and a space, followed by the explanatory clause in regular weight.

Pattern:
```
- **[Topic phrase]:** [explanatory clause, regular weight, voice rules apply].
```

The bold phrase is the scan anchor, the recipient should be able to read only the bold phrases and grasp the email's structure. The explanatory clause carries the analytical content.

Examples:
* `- **Year to date position:** Parks Maintenance is tracking *$87,500 favourable* against the Period 10 phased budget.`
* `- **Mowing contracts:** quarterly invoicing under *PAR/329* has settled later than the phasing assumed, thus inflating the apparent favourable position.`
* `- **Vacancy assumption:** the two operational crew vacancies are assumed unfilled through year end, *arguably* an optimistic stance for ELT reporting purposes.`

The bold phrase is one to four words ideal, six words maximum. Longer bold phrases lose the scan-anchor function.

### 2.3 Element three, indented sub-bullets

Sub-bullets are indented one level below a primary bullet. Use circle markers (`list-style-type: circle` in HTML) for visual differentiation from the primary disc markers. Same body font and size as the primary bullets. No bold lead-in on sub-bullets, they are explanatory, not topic-level.

Pattern:
```
- **[Topic phrase]:** [primary explanatory clause].
  - Sub-bullet supporting detail one.
  - Sub-bullet supporting detail two.
```

Sub-bullets unpack the primary bullet's claim with detail, supporting figures, qualifications, or two-sided analysis.

Examples:
```
- **Year to date position:** Parks Maintenance is tracking *$87,500 favourable* against the Period 10 phased budget.
  - Materials and Services accounts for $62,300 of the favourable variance.
  - Employee costs contribute the residual $25,200, driven by two vacancies in the operational crew.
```

**Maximum nesting depth: two.** Sub-sub-bullets do not appear in the format, three-deep nesting fragments the email across most email clients (Outlook web in particular renders deep nesting inconsistently). If a sub-bullet itself needs further unpacking, promote the sub-bullet to a primary bullet and add a new bold lead-in.

### 2.4 Element four, italics for emphasis

Italics earn their place in four specific contexts. Outside these contexts, italics should not appear, indiscriminate italicisation flattens the signal.

#### Context a, specific dollar figures and quantified positions when the magnitude is the point

Italicise the figure (and its qualifier) when the sentence's load-bearing claim is the magnitude itself.

* `tracking *$87,500 favourable*`
* `*compresses meaningfully*`
* `the favourable variance has *doubled* since Period 8`

Do not italicise dollar figures that are merely informational, italics signal "the magnitude is the point", not "a number is mentioned here".

#### Context b, system and reference identifiers the reader needs to anchor on

Italicise system names, contract codes, ledger codes, PK numbers, and other identifiers the recipient may need to look up.

* the *EFSTATS* extract
* contract *PAR/329*
* journal posted in *TechOne*
* against *PK385* Urban Bushland

This is a courtesy to the recipient, it flags "this is the exact identifier, not a paraphrase".

#### Context c, judgement words that carry the analyst's conviction

Italicise the analytical verdict words, the places where the analyst is taking a position rather than reporting data.

* *arguably* an optimistic stance
* *no genuine underspend* exists
* the position *compresses meaningfully*
* *self-evidently* the phasing overstates the run rate

This works in concert with the prose register's hedge-then-commit pattern, italics on the commit word reinforce the verdict.

#### Context d, methodological assumptions being flagged for scrutiny

Italicise the assumption-noun phrases the recipient should question.

* the *linear straight line* phasing assumption
* the *timing-driven* nature of the variance
* under the *current run-rate extrapolation*

This signals "this assumption is load-bearing, examine it before relying on the conclusion".

#### Italics do not appear on

* The bold lead-ins of bullets. Doubling bold and italic on the same fragment fragments the eye, the bold says "this is the topic" and the italic says "this is the load-bearing word", keeping them separate preserves both functions.
* The opening salutation or sign-off.
* The closing prose paragraph, unless a call-to-action carries a methodological flag.
* Plain prose passages outside the four contexts above.

## 3.0 Typography spec

### 3.1 Font family

Cambria throughout, with a fallback chain for graceful degradation:

```css
font-family: Cambria, Georgia, 'Times New Roman', serif;
```

Cambria is the user's documented default font for written documents, emails, and formatted outputs. If Cambria is unavailable on the recipient's machine, Georgia is the next closest substitute, then Times New Roman, then the generic serif fallback.

### 3.2 Size and weight

| Element | Size (HTML) | Size (Outlook compose) | Weight |
|---|---|---|---|
| Body | 14.5px | 11pt | 400 (regular) |
| Header | 15.5px | 12pt | 500 (bold) |
| Bold lead-in | 14.5px | 11pt | 500 (bold) |
| Italics | 14.5px | 11pt | 400 (regular, italic) |

Cambria does not have a true 500 weight in most email clients, the renderer substitutes the nearest available weight (typically the same as bold, ~700 in CSS terms). The 500 specification in the HTML template is for fidelity in clients that do interpolate, in practice Cambria reads as either regular or bold with no middle ground.

### 3.3 Line height

Body line-height of 1.55 in HTML, which translates to "Single" spacing with normal paragraph spacing in Outlook compose.

### 3.4 Indentation

Sub-bullets indent by 22px (HTML) or one tab (Outlook compose). Outlook handles this natively when sub-bullets are created with the Increase Indent button.

## 4.0 Standardised salutation and sign-off

### 4.1 Opening salutation

Default: `Hi [First name],`

The default works for all internal recipients including section leaders, finance colleagues, and managers. Comma after the name, single blank line before the opening prose paragraph.

More formal variant, for senior external recipients or first contact: `Dear [Title Surname],`

### 4.2 Sign-off block

Default:
```
Kind regards,
Spero
```

The sign-off block sits on its own with a blank line separating it from the closing prose paragraph. Two lines, "Kind regards," followed by "Spero" on the next line. No additional title, contact details, or signature block, the user has those configured at the email-client level.

Variants are uncommon. "Best regards" reads slightly more formal, "Cheers" reads too casual for the management register, "Kind regards" is the canonical default.

## 5.0 The email skeleton

```
Hi [Name],

[Opening prose paragraph: states what the email is about, sets the
context, and signals the structure to follow. One to three sentences
max. Voice rules apply, hedge-then-commit, signature lexicon, no em-
dashes, Australian English.]

**[First header]**

- **[Lead-in]:** explanatory clause with italics where they earn their
  place.
  - Sub-bullet supporting detail one.
  - Sub-bullet supporting detail two.
- **[Lead-in]:** explanatory clause.

**[Second header]**

- **[Lead-in]:** explanatory clause.
  - Sub-bullet supporting detail.

**[Third header]**

- **[Lead-in]:** explanatory clause carrying the ask or recommendation.

[Closing prose paragraph: offers a follow-up, summarises the call-to-
action, or carries a verdict. One to two sentences max. Voice rules
apply, the close should be decisive, not a recap.]

Kind regards,
Spero
```

Typical structure runs three headers, four to six primary bullets per header, one to three sub-bullets where unpacking is needed. Shorter emails may run two headers, longer emails (rare in this register) may run four.

## 6.0 Voice rules that still apply

Every voice rule from the prose register applies inside the email's prose passages, that is, the opening paragraph, the body of each bullet, the closing paragraph. The voice rules do not police the structural format itself (the headers, the bullet markers, the indentation).

The rules to maintain:

* **No em-dashes anywhere.** Commas, parentheses, or full stops, never `—` or `–`.
* **Australian English throughout.** "favourable", "optimised", "behavioural", "analysed".
* **Signature lexicon.** "arguably", "ought to", "self-evidently", "cumulatively speaking", "so to speak", "however" mid-sentence. The bold lead-ins are not the place for signature words, they belong in the explanatory clauses and in the opening and closing prose.
* **Hedge-then-commit.** Where a claim is qualified, qualify with "arguably" or "upon further investigation", then commit to the verdict.
* **Magnitude adjectives backed by dollar amounts.** "significant favourable variance" without a dollar figure reads as Claude-default, "significant favourable variance of $87,500" matches the voice.
* **Decisive close.** The closing prose paragraph carries a verdict or a call-to-action, not a recap. "Happy to walk through any of the above in person at your convenience" is a decisive offer, "In summary, three findings have been discussed" is a Claude-default recap and does not appear.

## 7.0 Linting an email

Run the linter with the `--email` flag:

```bash
python style_lint.py path/to/email_draft.md --email
```

The `--email` flag suppresses two checks that would produce false positives on the email format:

* `bullet_heavy` is skipped, the format uses bullets by design.
* `short_sentence_run` is skipped, sub-bullets are intentionally short.

All other voice rules continue to apply, em-dashes, American spelling, "However" as sentence opener, banned hedges ("perhaps", "it could be argued"), magnitude adjectives without dollar amounts, low arguably density, weak close.

Library usage:

```python
from style_lint import lint_text

findings = lint_text(email_text, register="email")
```

## 8.0 Delivering the email

Two output formats, depending on the recipient's mail client and the user's workflow.

### 8.1 Markdown delivery

For most situations, Markdown is the right format. Outlook web, Outlook desktop, Gmail, and Apple Mail all interpret Markdown reasonably when pasted into compose, the `**bold**` becomes bold, the `*italic*` becomes italic, the bullet structure is preserved, and the Cambria font is picked up from the user's default compose-font setting.

```
Hi Marisa,

Please find below the Period 10 variance summary, prepared off the
*EFSTATS* extract dated Tuesday.

**Background**

- **Year to date position:** Parks Maintenance is tracking
  *$87,500 favourable* against the Period 10 phased budget.
  - Materials and Services accounts for $62,300 of the favourable variance.
  - Employee costs contribute the residual $25,200.

...

Kind regards,
Spero
```

### 8.2 HTML delivery

When the email is being sent through a system that does not auto-convert Markdown (some web-based ticketing systems, some governance platforms), or when the user wants strict fidelity to the Cambria font specification regardless of the recipient's defaults, use `email_template.html`.

The template includes the Cambria fallback chain, the line-height spec, the indentation, and the sub-bullet circle markers. Fill the placeholders, paste the HTML body into a compose-as-HTML field, send.

## 9.0 The format checklist

Before sending, confirm:

* Salutation is "Hi [Name]," (or "Dear [Title Surname]," for formal).
* Opening prose paragraph is one to three sentences, sets context, signals structure.
* Headers are unnumbered, sentence-case, one to three words.
* Every primary bullet has a bold lead-in followed by colon-space and explanatory clause.
* Sub-bullets (where present) are indented one level, no deeper, no bold lead-in.
* Italics appear only on dollar figures (when magnitude is the point), system identifiers, judgement words, and methodological assumptions.
* Italics do not appear on the bold lead-ins.
* Voice rules hold inside every prose passage (no em-dashes, Australian English, signature lexicon present, hedge-then-commit, magnitude adjectives anchored).
* Closing prose paragraph is one to two sentences, carries a verdict or call-to-action, not a recap.
* Sign-off block is "Kind regards," on one line, "Spero" on the next.
* Linter run with `--email` flag, errors addressed, warnings reviewed.

If all eleven items hold, send.
