---
name: tax-invoice-compliance
description: "Decisive verification of an Australian tax invoice against the ATO ruleset (GST Act, GSTR 2013/1, QC 22422). Runs ABN checksum, ABR public-register lookup, ASIC Business Names check, GST math reconciliation, no-ABN-withholding determination, and a supplier intelligence dossier. Covers the under-$82.50, under-$1,000, and $1,000-plus tiers, the seven mandatory elements, RCTIs, GST-free and input-taxed treatment, mixed supplies, rounding, and Peppol eInvoices. Triggers whenever an invoice, tax invoice, supplier bill, PDF, image, or receipt is uploaded or pasted, or when the user asks 'is this tax compliant', 'check this invoice', 'verify the ABN', 'is the GST right', 'should I withhold', 'is this a valid tax invoice', 'check the supplier', 'is this business legitimate', 'ABN lookup', 'ASIC check', or supplies an 11-digit ABN. Returns one of six verdicts: COMPLIANT, COMPLIANT_WITH_NOTE, NON_COMPLIANT_FIXABLE, NON_COMPLIANT_BLOCK, NO_ABN_WITHHOLD, INSUFFICIENT_INFO."
---

# Tax Invoice Compliance Verifier

Decisive verification of an Australian tax invoice against the ATO ruleset, the GST Act, GSTR 2013/1, and the no-ABN-withholding provisions of TAA Schedule 1, section 12-190. Output is one of six verdicts plus a supplier intelligence dossier built from the ABR and ASIC public registers.

## 1.0 Core principle

This skill answers three questions, each of which must be answered before any invoice is paid, processed, or claimed as a GST credit:

1.0.1 **Is the document a legal tax invoice?** That is, does it carry every element the GST Act and ATO require for the recipient to claim an input tax credit. The seven mandatory elements are non-negotiable, with an additional element for sales of $1,000 or more.

1.0.2 **Is the supplier real, and is the GST claim genuine?** That is, does the ABN exist, does the ATO checksum validate, is the entity active, is it registered for GST as at the invoice date, and does the supplier name on the invoice match the ABR-registered entity name or a properly registered business name.

1.0.3 **Is there anything about the business that is concerning?** That is, status flags on ASIC (cancellation under review, recent re-registration), trading name versus registered name discrepancies, address mismatches, business-activity mismatch with the goods or services supplied, or any indicator that the document is fraudulent, mistaken, or non-current.

If any of the three answers is no, the invoice does not get paid at face value. The verdict set in 5.0 maps each failure mode to the correct operational next step.

## 2.0 When this skill triggers

2.0.1 Any time a user uploads or pastes an invoice, tax invoice, supplier bill, receipt, or PDF or image that appears to contain a header such as "Tax Invoice", an ABN field, a GST line, or a supplier name and total.

2.0.2 Any time the user asks any of the following, even casually, "is this tax compliant", "check this invoice", "verify the ABN", "is the GST right", "should I withhold", "is this a valid tax invoice", "check the supplier", "is this business legitimate", "ABN lookup", "ASIC check", "is this supplier real".

2.0.3 Any time the user provides an ABN (eleven digits) and asks anything about it, even without an invoice attached.

2.0.4 Any time the user provides a supplier name and asks whether they are GST-registered, legitimate, or correctly named.

If the request involves a fuel levy surcharge line under a PAR/* contract, hand over to `lcc-fuel-levy-verify` for the surcharge ceiling check, but still run this skill on the rest of the invoice for tax-invoice compliance and ABN validity.

If the request involves account coding (which natural account to recode to), hand over to `lcc-coding-review` for the coding decision, but still run this skill first to confirm the invoice is even valid.

## 3.0 Bundled artefacts

| File | What it is |
|---|---|
| `methodology.md` | Full ATO ruleset distilled, the seven mandatory tax-invoice elements, the $82.50 / $1,000 tiers, RCTI rules, rounding rules, eInvoice (Peppol) rules, no-ABN-withholding rule, GST treatment matrix (taxable / GST-free / input-taxed), the 28-day issuance rule |
| `abn_validator.py` | Python verifier with `validate_checksum()`, `lookup_abr()`, `lookup_asic_business_names()`, `assess_concerns()`, and a CLI entry point. Performs the offline ATO checksum, then web-fetches the ABR and ASIC public pages, then runs the concerns scan |
| `red_flags.json` | Catalogue of red-flag patterns observed on non-compliant or fraudulent invoices, each tagged with severity (BLOCK / FIXABLE / NOTE) |
| `verdict_set.md` | The six decisive verdicts with mapping to operational next step |
| `worked_examples.md` | Four worked examples end to end, including the Adventure and Survival Training / Fire Management Training partnership (ABN 33 078 502 894) as the canonical "two business names under one ABN" case |

## 4.0 The verification workflow

The skill runs five stages in sequence. Each stage must clear before the next begins, except where a stage produces a BLOCK verdict, in which case the workflow halts immediately and the verdict is issued.

### 4.1 Stage 1, document compliance

Test the document against the seven mandatory tax-invoice elements per ATO QC 22422 and GSTR 2013/1. For sales of $1,000 or more, also test the eighth element (buyer identity or ABN). See `methodology.md` section 2.0 for the full element list with sighting requirements.

If any element is missing and the missing information cannot be obtained from other documents the supplier has provided, the verdict is `NON_COMPLIANT_FIXABLE`, action is to request a complete reissue from the supplier within the ATO's 28-day window.

If the document looks like an eInvoice (Peppol Invoice) and does not carry the words "Tax Invoice", check whether it conforms to the A-NZ Invoice Specification under Peppol. If it does, the heading requirement is satisfied by the Peppol framework itself, per ATO guidance.

### 4.2 Stage 2, ABN validation

Run the ATO checksum algorithm offline first, by way of `abn_validator.py validate_checksum`. This is a mathematical test, requires no network access, and either passes or fails decisively. If the checksum fails, the verdict is `NON_COMPLIANT_BLOCK`, as the ABN cannot be valid.

If the checksum passes, fetch the public ABR record at `https://abr.business.gov.au/ABN/View?abn={abn}` and, where supplier history matters (recent name changes, status changes), also fetch the historical view at `https://abr.business.gov.au/AbnHistory/View?id={abn}`.

From the ABR record, extract:

- Entity name
- ABN status (Active, Cancelled, Suspended)
- Entity type (Individual, Partnership, Company, Trust, Family Partnership, etc.)
- GST registration status (Registered, with effective from-date)
- Main business location (state, postcode)
- Business names and trading names

If the ABN is not Active as at the invoice date, the verdict is `NON_COMPLIANT_BLOCK`. The supplier is not entitled to charge GST on an inactive ABN.

If GST appears on the invoice but the ABR shows the supplier is not GST-registered as at the invoice date, the verdict is `NON_COMPLIANT_BLOCK`. The supplier has charged GST without being registered, which is unlawful and forfeits the recipient's input tax credit.

### 4.3 Stage 3, supplier-name reconciliation via ASIC

The name printed on the invoice must match either the ABR entity name or one of the registered business names. For a partnership trading under a business name, the invoice should show the business name and the partnership's ABN, and the ABR's registered business name list must include that business name.

Fetch the relevant ASIC Business Names extract. For each registered business name shown on the invoice, confirm:

- Status is Registered (not Cancelled, not under cancellation review)
- The Holder ABN on the ASIC record matches the ABN on the invoice
- Principal place of business and address for service of documents are present and plausible

If the supplier name on the invoice is neither the ABR entity name nor a registered business name held by that ABN, the verdict is `NON_COMPLIANT_BLOCK`, and the concern is misrepresentation, possible fraud, or stale records.

If the business name on the invoice is cancelled or under cancellation review on ASIC, the verdict is `NON_COMPLIANT_BLOCK`. The supplier is not legally permitted to trade under that name.

### 4.4 Stage 4, GST calculation reconciliation

For each taxable line, confirm:

- If GST-inclusive amounts are shown, GST equals Total divided by 11, to the cent, applying the ATO rounding rules (Total invoice rule or Taxable supply rule, per GSTR 2013/1)
- If GST-exclusive amounts are shown with a separate GST line, GST equals Subtotal multiplied by 0.10
- If the invoice states "Total price includes GST" as a shorthand under ATO QC 22422 element 6, the implied GST must equal Total divided by 11

For mixed supplies (taxable plus GST-free, or taxable plus input-taxed), confirm the taxable portions are clearly identified per ATO QC 22422 element 7, and that GST is only applied to the taxable portion. If the breakdown is opaque, the verdict is `NON_COMPLIANT_FIXABLE`, action is to request a reissue with a clear taxable-portion breakdown.

If GST has been charged on a GST-free supply (such as basic food, water, sewerage and drainage, eligible health services, exports within the 60-day rule), the verdict is `NON_COMPLIANT_FIXABLE`, action is to seek a refund of the wrongly charged GST per ATO guidance on reverse-charged sales.

### 4.5 Stage 5, supplier intelligence and concerns scan

With the ABN validated and the supplier name reconciled, generate a supplier intelligence dossier covering:

- Entity name, entity type, ABN, GST registration date, and status
- All registered business names and historical trading names, with ASIC status and date ranges
- Main business location and any recent state or postcode changes
- Inferred business activity (from registered business names and any web presence)
- Whether the goods or services described on the invoice are plausibly within the supplier's apparent business activity

Run the red-flags scan from `red_flags.json` against the gathered data. Any BLOCK-tier flag escalates the verdict to `NON_COMPLIANT_BLOCK`. Any FIXABLE-tier flag triggers `NON_COMPLIANT_FIXABLE`. NOTE-tier flags do not change the verdict but appear in the dossier so the recipient is aware before processing.

## 5.0 The decisive verdict set

The verifier returns exactly one of six statuses. Each maps to one operational next step. See `verdict_set.md` for the full mapping.

| Status | When it fires | Action |
|---|---|---|
| `COMPLIANT` | All seven (or eight) elements present, checksum passes, ABN active, GST-registered, supplier name reconciled, GST math correct, no red flags | Process the invoice at face value, claim the GST credit where eligible |
| `COMPLIANT_WITH_NOTE` | All compliance checks pass, but a NOTE-tier flag exists (e.g. business address mismatch, recent name change with documented continuity, address-for-service is a PO box) | Process the invoice, record the note in the supplier master record |
| `NON_COMPLIANT_FIXABLE` | Missing element that can be supplied via reissue or supplementary document, OR GST wrongly charged on a GST-free supply, OR mixed-supply breakdown opaque | Block payment pending reissue, give supplier ATO's 28-day window to provide a complete and correct tax invoice |
| `NON_COMPLIANT_BLOCK` | ABN checksum fails, OR ABN inactive on invoice date, OR GST charged without GST registration, OR supplier name not reconciled to ABR or ASIC, OR business name cancelled or under cancellation review | Block payment, do not claim GST credit, escalate to AP for fraud review or supplier verification |
| `NO_ABN_WITHHOLD` | Invoice value exceeds $82.50, no ABN supplied, and no exemption applies under TAA Schedule 1, section 12-190 (such as supplies wholly of a private or domestic nature, or supplies by an individual under the hobby threshold) | Pay the supplier 53% of the invoice value, remit 47% to the ATO as withheld tax, issue a payment summary to the supplier |
| `INSUFFICIENT_INFO` | The document is too low-quality, too partial, or too obscured to verify, OR the ABR or ASIC public register is temporarily unreachable | Block payment pending better source documents, OR retry the verification when registers are available |

## 6.0 The recipient's GST credit claim

If the invoice is `COMPLIANT` or `COMPLIANT_WITH_NOTE` and the recipient is GST-registered, the recipient is entitled to claim the GST credit per ATO QC 22431, subject to the four-year time limit per MT 2024/1.

For purchases under $82.50 (including GST), a tax invoice is not strictly required to claim the GST credit. A cash register docket, receipt, or even a diary entry with supplier name, ABN, date, description, and amount is sufficient per ATO guidance. The skill still runs Stage 2 ABN validation for these, since an invalid ABN forfeits the credit regardless of value.

For purchases above $82.50 (including GST), a valid tax invoice is required to claim the credit. The recipient has the four-year credit time limit to do so. Under cash accounting, the credit is claimable in the tax period payment is made. Under non-cash (accruals) accounting, the credit is claimable in the first tax period an invoice is issued or payment is made, whichever is first, provided a valid tax invoice is held.

## 7.0 What this skill does not do

7.0.1 **Account coding decisions.** Which natural account to code the invoice to is the province of `lcc-coding-review`. This skill confirms the invoice is valid, the coding skill confirms the coding is correct.

7.0.2 **Fuel levy ceiling verification.** Fuel surcharge lines on PAR/* contracts go to `lcc-fuel-levy-verify`. This skill confirms the invoice itself is compliant, the levy skill confirms the surcharge does not exceed the contract ceiling.

7.0.3 **Cash-flow timing of GST credit claims.** This is determined by the recipient's GST accounting method (cash versus non-cash) and the tax period rules per ATO QC 22431. This skill establishes whether the credit is claimable at all, not when.

7.0.4 **Income-tax deductibility.** A valid tax invoice does not automatically make the underlying expense deductible. Entertainment, private-use portions, and capital items have separate income-tax treatment. This skill confirms the GST compliance only.

7.0.5 **FBT classification.** Hospitality and entertainment FBT determinations are handled by the FBT module of `lcc-coding-review`. This skill simply confirms the tax invoice for the hospitality supply is valid.

## 8.0 LCC-specific notes for AP processing

LCC is GST-registered and entitled to claim GST credits on most purchases. The exceptions are purchases used for input-taxed activities (which Parks does not generally undertake), private-use portions, and certain entertainment expenses.

LCC's TechOne AP system has its own validation rules, but the ATO compliance test is the prior authority. Where TechOne accepts an invoice that fails this skill's verification, the journal should be held and the supplier contacted for a reissue, not paid through.

For PCard transactions, the docket or merchant receipt must meet either the under-$82.50 simplified evidence standard (diary entry with supplier name, ABN, date, description, amount) or the full tax invoice standard for higher-value purchases. PCard transactions where neither standard is met cannot have their GST credit claimed and should be flagged in the monthly PCard cover slip.

For recipient-created tax invoices (RCTI), where LCC issues the invoice on behalf of the supplier (rare, requires a written RCTI agreement and the supply to be on the Commissioner's RCTI Determination 2023 list), Stage 1 testing also requires the document to be marked as an RCTI and both parties' ABNs and GST registrations to be sighted as at the issue date.
