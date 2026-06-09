# Confidence Statement Patterns

The confidence statement closes the investigation email. It is the bound on the claim — what the data does and does not answer. Done well, it preempts the question "are you sure?" and gives the Section Leader something to forward without further qualification. Done badly, it reads as hedging and undermines everything that came before.

The PK385 Marisa email v6 light folds confidence into the closing CTA paragraph. Other investigations need a more explicit one-paragraph confidence statement before the CTA. This file catalogues three patterns for the explicit version and the rule for when each applies.

---

## The principle

Confidence is not hedging. Hedging is "we may have a possible issue." Confidence is "the gap is firm; the basis for the Tracker value is the open question."

The hero number, mechanics, evidence, and scenarios should all read as fact. The confidence statement is where the email names the bound — what is firm, what is open — without hedging the rest.

A good confidence statement gives the recipient a list of two-to-three things they can quote in their own escalation:

* The reconciliation is firm.
* The masked-budget surfacing on PK473 is firm.
* The vendor basis for the Tracker value is the open question.

Each of those is a discrete claim. Each can be defended on its own evidence. The recipient can lift any of them into a forwarded email without needing to qualify it.

---

## Pattern A — Data-Bounded

**Use when:** The trace is complete on the data side; the only open question is documentary (a memo, a rate card, a written basis that may exist somewhere).

**Structure:** Name what's firm. Name what is documentary-only and may shift. Name the only thing that would change the picture.

**Example (close to PK385 actual):**

> The 19% has no documented vendor basis I've been able to find. If PM produces a memo or rate card, the picture may shift — that's the only way I see this resolving differently. The reconciliation against the Checklist is firm; the question is what authorises the Tracker value.

Notes on this pattern:

* "Have been able to find" is honest about the search, not the conclusion. The conclusion (no basis exists) is provisional but the search is comprehensive.
* "Only way I see this resolving differently" pre-empts "but what about X?" by stating that X has been considered.
* "The reconciliation is firm" anchors the user back on the strong claim.

**When NOT to use:** If you genuinely haven't searched comprehensively for the documentary basis, do not say "I've been able to find" — say "I haven't yet asked PM to produce a basis." Honesty about scope of search distinguishes data-bounded from confession-of-incomplete-work.

---

## Pattern B — Evidence-Bounded

**Use when:** The trace has known data limitations — partial-period data, a contract that hasn't been read end-to-end, an account that wasn't in the export — and the conclusion is conditional on those limitations.

**Structure:** Name the strong claim. Name what the evidence base is. Name what would extend it.

**Example:**

> Through Pd9, the LZ6 split has been consistent at 19% across nine periods. The pattern in Pd10–12 will follow unless the Tracker is amended. I have not yet seen the original Pd1 journal that sets the split — if that journal references a memo I haven't pulled, the basis question may resolve there. Pulling that journal is a one-week request to Finance.

Notes on this pattern:

* States the strong claim ("nine periods consistent") with its evidence base.
* States what is unseen ("Pd1 journal").
* Gives a concrete next step that would close the bound.

**When NOT to use:** If the unseen evidence is unlikely to change the conclusion, do not flag it. Confidence statements are not exhaustive disclosure — they flag the bounds that matter to the decision being asked.

---

## Pattern C — Scope-Bounded

**Use when:** The trace covers one PK or one zone or one contract, and the recipient might reasonably ask "does this apply elsewhere?" The answer is "I haven't checked but here's how to find out."

**Structure:** Name the scope of the trace. Acknowledge the adjacent scope. Name the test for whether the same issue exists there.

**Example:**

> This trace covers PK385 only. Glascott's other zones (LZ7, LZ8) flow through the same holding account and the same Tracker. If you'd like the same reconciliation applied there, I can run it — same five-step trace, same Checklist comparison.

Notes on this pattern:

* Does NOT claim the issue extends ("Glascott LZ7 is also wrong"). Claiming without evidence overstates.
* Does NOT dismiss the question ("only PK385 is affected"). Dismissing without evidence understates.
* Offers the work as a follow-up. The recipient now knows the option exists.

**When NOT to use:** If you have already checked the adjacent scope and the issue does not extend, say so cleanly: "I checked LZ7 and LZ8; both reconcile cleanly to the Checklist." That is a stronger close than Pattern C and worth using when honest.

---

## Folded confidence — the PK385 v6 light variant

The PK385 Marisa email folds confidence into the CTA paragraph rather than carrying an explicit confidence statement:

> Full reconciliation workbook attached — zone detail, LZ6 deep dive, monthly pattern, and budget position. A 20-minute call before raising anything with PM would be the fastest way to agree scope. Let me know a time and I'll set it up.

What's happening here:

* "Full reconciliation workbook attached" is the implicit confidence claim — the data depth is in the attachment, the email is the summary.
* "A 20-minute call before raising anything with PM" is an implicit acknowledgement that PM has the unseen evidence (the basis for the 19%) and the call is to pre-align before that conversation.
* No explicit "we are confident in X" sentence exists; the workbook attachment and the gating-on-PM-call carry the bound implicitly.

Use folded confidence when:

* The investigation has a workbook attachment that genuinely covers the data depth.
* The next step (the call) is itself the mechanism for closing the open bound.
* The recipient is high-context and will read the implicit signals correctly.

Use explicit confidence when:

* No attachment exists, or the attachment doesn't carry the same density.
* The recipient is low-context or new to the issue.
* The escalation is likely (the email will be forwarded to a Director or to PM directly), and the confidence statement needs to survive that forwarding intact.

---

## Anti-patterns

* **"I think" / "I believe" / "I feel."** First-person belief language softens facts that should land as facts. "The reconciliation shows" is stronger than "I believe the reconciliation shows."

* **"It's possible that..." opening.** If something is genuinely possible, name what would falsify it. "If PM produces a basis, the picture shifts" is concrete; "it's possible there's a basis I haven't found" is dead air.

* **Hedge-stacking.** "We may have a possible potential issue with the allocation that could potentially be incorrect." Each hedge softens the next; the result is meaningless. One acknowledged uncertainty per claim, named precisely.

* **Confidence as apology.** "I'm sorry if this turns out to be wrong but..." is not confidence, it is preemptive apology. The recipient does not want apology; they want the bound stated.

* **Burying the bound.** A confidence statement halfway through Beat 03 prose ("of course, this assumes the Tracker hasn't been amended since Pd9") is invisible. The bound goes in Beat 06 where it has its own paragraph and the recipient knows to look for it.

* **Closing without confidence on a contested investigation.** If the trace is going to be contested by PM, the confidence statement is the thing that makes the investigation defensible. Skipping it on a contested investigation is leaving the credibility on the table.

---

## Quick decision

```
Is the only open question documentary (memo, rate card, written basis)?
   → Pattern A (Data-Bounded)

Is the trace conditional on data you haven't seen yet?
   → Pattern B (Evidence-Bounded)

Could the issue extend to adjacent scope you haven't checked?
   → Pattern C (Scope-Bounded)

Does the email carry an attachment plus a follow-up call that closes the
bound implicitly?
   → Folded (no explicit confidence statement; ensure CTA is concrete)

None of the above clearly fits?
   → Reread the trace. The bound is somewhere; find it before sending.
```

A trace that has no bound to state is suspicious. Either the trace really is complete (rare, and worth saying explicitly: "this is fully evidenced; no open questions remain") or the bound exists and hasn't been articulated. Send no investigation email without first asking: what would change the conclusion?
