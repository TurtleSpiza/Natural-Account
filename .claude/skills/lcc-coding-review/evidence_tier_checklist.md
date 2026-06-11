# Evidence Tier Checklist

Three tiers. The rule that drives the entire branch coding review. No account is cleared without Tier 1. No recode dollar amount is populated without Tier 1.

## Tier 1 — Cleared

The only tier where status moves to **Cleared** in the workbook and a recode dollar amount can be populated.

Evidence required, by source:

### P-Card transactions
- Tax invoice (vendor original, GST-inclusive total visible)
- Cover slip (cardholder signed, requesting officer named, account specified, business purpose stated)

Both required. A tax invoice without a cover slip is Tier 2. A cover slip without a tax invoice is Tier 3.

### AP creditor invoices
- Original supplier invoice (PDF or hard copy in TechOne)

Sufficient on its own.

### Internal cross-charges (7B-series, 7C-series)
- Signed internal agreement OR
- Email confirmation from the charging branch confirming the charge basis

### ALLSTORE / CHAMBERS inventory issues
- Stores issue slip naming the requester and the cost centre

### Stores-issue and stock-adjustment lines (Marsden convention, Spero 10-Jun-2026)
A stores-issue or stock-adjustment line (Despatch Stock Requisition, IN-prefixed/STKISS) evidences against the Marsden stores inventory bundled in this skill (`marsden_stores_inventory.{json,csv}`): the 6-digit item number in the line Details matching the inventory code satisfies the evidence limb. The tax limb is GREEN on the nature basis that an internal stores issue is no GST event (the GST sat on the original stores purchase), recorded per line. Known catalogue trap: codes 207141-207144 appear twice in the inventory, once as envelopes and once as Steel Blue footwear flagged in-catalogue as a typo for 208141-44; the true items are the envelopes (documented on the 73563 stores lines, 10-Jun-2026). A truncated item code in the export defeats the match and the line stays on the ordinary tiers.

## Tier 2 — Review

Status remains **Review**. Do not populate recode $ even if the miscoding seems obvious.

- Partial documentation (listing without invoices, invoice without cover slip)
- Cover slip with cost-account that doesn't match what was posted (suggests coder override)
- Cover slip total doesn't match posted amount (often the GST-inclusive vs ex-GST difference; verify but flag)
- Missing cardholder signature on PCard cover slip
- Narration that is plausible but unverified

## Tier 3 — Review

Status remains **Review**. Cannot confirm or deny coding.

- Narration only (transaction listing line, no source document)
- Reimbursement supported by a non-receipt (e.g. promotional email, screenshot, generic confirmation)
- Recurring "Project Organisational Consulting" narrations from a single supplier with no invoice
- Lump-sum payments where item detail is unspecified

## Disposition labels in the workbook

| Label | When |
|---|---|
| Cleared | Tier 1 evidence confirms the coding is correct as posted |
| Review | Tier 2 or 3 evidence; coding may or may not be correct |
| Action Needed | Tier 1 evidence confirms the coding is wrong AND the correct destination is identified |
| Not Reviewed | Account had nil balance and was not reviewed |

## Anti-patterns

**Recoding without Tier 1 evidence.** Even if a transaction "obviously" looks miscoded based on the narration, do not populate a recode $ until the source document confirms it. The cost of an unjustified recode is higher than the cost of leaving the item at Review for one more period.

**Clearing on listing-narration alone.** A clean-looking listing line is Tier 3. If it survives a future review unchanged it migrates to Cleared, but the first sighting at narration level is Tier 3.

**Treating cover slip as substitute for invoice.** Cover slip is one half of the Tier 1 chain for PCard. Without the tax invoice, the chain is broken.

## Worked examples from P10 review

**Tier 1, Cleared:**
- Securecorp 73124 patrol invoices sighted (multiple) - $210,542.40 YTD coding confirmed correct despite no budget allocation

**Tier 1, Action Needed:**
- 25 confirmed recodes totalling $33,192.04 across 73544/73513/73543/72411/73421/7B411/73531/73532/73533

**Tier 2, Review:**
- Prescription safety glasses in 72113 - $385.02, $450, $402.59, $1,231.71 - invoices not sighted, no cover slips. May be personal benefit depending on circumstances.

**Tier 3, Review:**
- 73601 Management Consultancies $46,003.66 - narrations identical from one supplier, invoices not sighted, four-element consultant test cannot be applied
- WHOLESALE SA* O #18766 $2,375.00 in 72113 - General Expenses category narration only, no cover slip, P-Card from a wholesale supplier
- 73533 Quinn $137.85 Uber - submitted "receipt" is Uber promotional marketing email, no trip detail
