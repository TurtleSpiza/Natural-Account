# Register Distinctions

Three Parks Finance email registers exist. They share infrastructure (HTML visuals, account citations, journal references) but differ on tone, recipient, structure, and what gets cut. Picking the wrong register is the single biggest source of email rework.

## Three registers at a glance

| Dimension              | Section-Leader (this skill)         | Finance-Batch (lcc-finance-batch-email)  | Operational                              |
|------------------------|-------------------------------------|------------------------------------------|------------------------------------------|
| Primary recipient      | Marisa, Pat, Andrew, Cameron        | Amy Forgione, Owen Jensen                | Jon (PM), Steve (PM), vendor contact     |
| CC                     | Gihani by default                   | Gihani by default                        | Section Leader sometimes                 |
| Frequency              | One per investigation               | One per period (P10, P11)                | As needed                                |
| Word count             | ~500-700 prose                      | ~150-300 prose, mostly tables            | ~50-150 prose                            |
| Visual blocks          | 4-6 from html-email-finance-visual  | 0-1, mostly tables                       | 0                                        |
| Hero number            | Required, opens the body            | Banned — facts not framing               | Banned                                   |
| Decision asked         | One, named explicitly               | Zero — all mechanical                    | One, narrow                              |
| Confidence statement   | Required, bounds the claim          | Optional, single-line                    | Optional                                 |
| Action types           | Mechanical + Decision mixed         | Mechanical only                          | Operational request                      |
| Document citations     | Plain English + DM secondary        | DM-first, account-first                  | Vendor reference, contract clause        |
| Voice                  | Investigation findings              | Action items, recoded                    | Direct ask                               |
| What gets cut          | Account-level pedantry              | Mechanism explanation                    | Reconciliation, scenarios                |

## Section-Leader Register

**The Marisa register.** Recipients are Section Leaders who own scope but do not operate inside the GL. They need to understand the mechanics in plain language, see the magnitude, and make one decision.

* **Open with the reframe, not the data point.** "$140,000 hiding as $10,808" — not "We have a variance of $10,808 to discuss." The reframe IS the value of the email.
* **Explain mechanics, do not name them.** "Parks Maintenance journals the invoice using fixed Tracker values" — not "the GJ from holding 1-20276-73126 splits via DM-referenced operational driver."
* **Cite the document by what it is.** "Your Checklist (DM# 14719249)" — DM is auxiliary. The recipient knows the Checklist; they may or may not know the DM number.
* **Name the consequence, including the political one.** "The retrospective option exposes PK473 at ~116%" — not "various downstream effects."
* **Ask for one decision.** Not "approve all of these" — "decide whether prospective or retrospective."
* **End with a concrete CTA.** "20 minutes with you and Gihani" beats "let me know if you have questions."

What gets cut: account-code pedantry (no full chart references in the body), GL mechanics jargon (debit/credit talk), and references to other PK numbers that aren't part of this finding.

## Finance-Batch Register

**The Amy/Owen register.** Recipients are Finance staff who process recodes, confirm miscodes, run journal uploads. They want unambiguous mechanical instructions and don't need the why beyond a one-line context.

* **Lead with the action, not the finding.** "Please action the recodes below" — not "We've found an interesting pattern."
* **One row per item.** Tabular. PK, account, amount, source ref, recode-to.
* **DM-first, account-first.** Citations carry the DM and the account because that is what Finance keys on.
* **Mechanical actions only.** Decisions go elsewhere. If the batch contains a decision, that item moves to a section-leader email instead.
* **No hero number.** No reframing. Facts and rows.
* **Confidence is optional and short.** "Items 3 and 7 are pending vendor confirmation; everything else is fully evidenced" — single line, no paragraph.

What gets cut: prose mechanics, scenarios, EOFY landing, narrative arc. The batch is dense and structural by design.

## Operational Register

**The PM and vendor register.** Recipients are operational staff who do the work, raise the invoices, run the contracts. They want the narrowest possible ask answered fast.

* **Open with the ask.** "Can you confirm the LZ6 split basis?" — not "We've been investigating PK385 and the trace shows..."
* **One question, one paragraph of context max.** If there are two questions, send two emails or use a numbered list.
* **No scenarios. No EOFY landing.** Operational doesn't need them and including them invites scope creep into the answer.
* **No Finance cc by default.** Finance enters when a Finance journal is being requested, not when an operational question is being asked.
* **CTA is "by [date]" or "next week" — concrete.** "Let me know" floats; deadlines move.

What gets cut: hero number, mechanics walk-through, reconciliation tables, scenario tables, confidence statements. The email is a single ask.

## Picking the register from the situation

```
"I have a finished trace and a recommended action that needs Section Leader sign-off."
                                                          → Section-Leader register

"I have a list of P10 outstanding miscodes that need Finance to action recodes."
                                                          → Finance-Batch register

"I need PM to confirm a single fact, or to request a single change."
                                                          → Operational register
```

Edge cases:

* **Trace finding that surfaces an operational question first.** If the answer to the operational question changes the recommendation, send the operational email FIRST and wait. Then the Section Leader email lands with the answer baked in.

* **Multi-PK finding spanning two Section Leaders.** Two emails, one each, because the political dynamics differ per Section. Do not co-address — it dilutes the decision request.

* **Section Leader asks for the recoded amounts directly.** Reply with the Finance-batch register inline. The reply borrows the Finance-batch shape because it is answering a mechanical question, even though the recipient is a Section Leader.

## Cross-register pollution — the most common drift

The most common drift is Finance-Batch register polluting Section-Leader emails. Symptoms:

* "Please action recode of $13,993 from PK385 to PK473." — this is Finance-Batch language. Section Leader register: "We'd want to redirect $13,993 of the LZ6 charge per round; happy to walk through whether you'd want that prospective or retrospective."

* Tables with full account codes when the prose did not introduce why the codes matter. Section-Leader recipients skip these.

* "DM# 17767639" without "the Tracker" alongside. Section Leaders do not memorise DM numbers.

* Closing with "Cheers" or "Regards" — both fine, but if the email is otherwise terse and tabular it has slipped to Finance-Batch register and the recipient's brain has already filed it as "for Finance to handle."

The reverse drift (Section-Leader register polluting Finance-Batch) is rarer but exists: hero numbers in a batch email, scenario discussion, recommendations needing approval. These slow Finance down. Pull them out into a separate Section-Leader email and keep the batch mechanical.

## Anti-patterns common to all three registers

* **Mixed audiences in one email.** "Hi Marisa, please can you and Amy sign off on..." dilutes the ask. Two emails, one each, cc'd appropriately.
* **Hidden questions inside paragraphs.** If the email asks for a decision, the decision is named in a heading, an action card, or the closing line. Not buried mid-paragraph.
* **Stale data referenced.** A Pd9 email built on Pd8 data is a Pd8 email with a stale label. Refresh the trace before drafting.
* **Reply-all on a section-leader thread without re-confirming Gihani.** The CC list of the original is the cc list of the reply unless someone asks otherwise.
