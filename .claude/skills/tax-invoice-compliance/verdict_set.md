# Verdict Set

The verifier returns exactly one of six verdicts. Each verdict maps to one operational next step. There is no in-between, no escalation pathway, no "mostly compliant" middle ground.

## 1.0 COMPLIANT

**When it fires.** All seven mandatory tax-invoice elements present (or eight for sales of $1,000 or more), ABN passes the ATO checksum, ABR shows the ABN is Active as at the invoice date, ABR shows the supplier is GST-registered as at the invoice date if GST is charged, the supplier name on the invoice reconciles to the ABR entity name or one of the ABR-registered business names, GST math is correct, no BLOCK-tier or FIXABLE-tier red flags.

**Action.** Process the invoice at face value. If LCC is the recipient and the supply is for taxable use, claim the GST credit in the next BAS subject to the four-year credit time limit per MT 2024/1.

## 2.0 COMPLIANT_WITH_NOTE

**When it fires.** All compliance checks pass, but one or more NOTE-tier red flags exist. Examples are recent GST registration (less than 90 days before invoice date), business address being a PO box only, ABN previously cancelled and reactivated, frequent business name changes, round-dollar GST amount, invoice approaching the four-year credit time limit.

**Action.** Process the invoice at face value. Record the note in the supplier master record (for LCC, in the TechOne supplier record under additional notes). On the next transaction from the same supplier, the note should appear so the AP processor can apply additional scrutiny if warranted.

## 3.0 NON_COMPLIANT_FIXABLE

**When it fires.** One or more FIXABLE-tier red flags exist. The invoice is not currently a valid tax invoice, but the defects can be cured by a reissue or by supplementary documentation from the supplier. Examples are missing tax-invoice heading, missing GST amount, missing buyer identity on a $1,000-plus sale, opaque mixed-supply breakdown, GST math inconsistent, GST charged on a GST-free supply, business activity mismatch with the supply description.

**Action.** Block payment pending reissue. The supplier has 28 days from the recipient's request to provide a complete and correct tax invoice, per ATO QC 22431. Do not claim the GST credit until the reissued document is held. If the supplier does not respond within 28 days and the missing information cannot be obtained from other documents, the recipient may seek the Commissioner's permission to treat the document as a valid tax invoice per ATO guidance.

## 4.0 NON_COMPLIANT_BLOCK

**When it fires.** One or more BLOCK-tier red flags exist. The defect cannot be cured by a reissue, or indicates fraud, misrepresentation, or unlawful charging. Examples are ABN checksum failed, ABN not Active on the ABR, GST charged without GST registration, supplier name not reconciled to ABR or ASIC records, business name cancelled on ASIC, future-dated invoice, ABR unreachable.

**Action.** Block payment. Do not claim the GST credit. Escalate to AP for fraud review or supplier verification. For LCC, this should also trigger a supplier master review to confirm the ABN and registered name are correctly recorded. If fraud is suspected, escalate to the Manager Financial Operations and consider whether a report to the ATO under the GST integrity provisions is warranted.

## 5.0 NO_ABN_WITHHOLD

**When it fires.** Invoice value exceeds $82.50 (including GST), no ABN is quoted on the invoice, and no exemption under TAA Schedule 1 section 12-190 applies. Common exemptions are supplies wholly private or domestic, supplies by an individual under 18 below the relevant threshold, supplies by a non-resident not carrying on an enterprise in Australia, supplies covered by a written "Statement by a supplier" ATO form 38-509, total annual payments to the supplier not exceeding $75.

**Action.** Pay the supplier 53% of the gross invoice value. Withhold the remaining 47% and remit it to the ATO as withholding tax via the next BAS, using the No-ABN-quoted withholding label. Issue a PAYG payment summary to the supplier showing the amount withheld. The supplier may apply that withholding as a credit against their income tax liability.

For LCC, this is rare in practice because the supplier master should be populated only with ABN-quoting suppliers. A NO_ABN_WITHHOLD verdict on an existing supplier indicates either the supplier has lost their ABN (cancelled, suspended) or the invoice is from a different entity that has slipped through. Either way, escalate before processing.

## 6.0 INSUFFICIENT_INFO

**When it fires.** The document is too low-quality, too partial, or too obscured for the verifier to make any determination. Examples are a phone photo where the ABN is illegible, an OCR'd PDF where the GST amount is garbled, an invoice with most fields missing such that no compliance test can be run. Also fires when the ABR or ASIC public register is temporarily unreachable.

**Action.** Block payment pending better source documents. Request a clean digital copy from the supplier (PDF or eInvoice format), or retry the verification when the public registers are available. Do not claim the GST credit until a verifiable document is held.

## 7.0 Verdict precedence

Where multiple red flags fire across different severity tiers, the verdict follows the highest-severity flag.

- Any BLOCK flag triggers `NON_COMPLIANT_BLOCK`, regardless of other flags
- Otherwise, any FIXABLE flag triggers `NON_COMPLIANT_FIXABLE`
- Otherwise, any NOTE flag triggers `COMPLIANT_WITH_NOTE`
- Otherwise, the verdict is `COMPLIANT`

The two structural verdicts (`NO_ABN_WITHHOLD` and `INSUFFICIENT_INFO`) take precedence over all of the above when their fire conditions are met, since they reflect a different decision pathway, not a compliance failure to be remedied.

## 8.0 What the verifier reports

A verdict alone is not enough. The verifier returns a structured response with:

- The verdict
- The verifier's confidence (high / medium / low) based on the quality of the input and the verifier's access to the public registers
- The list of fired red flags with severity, code, description, and action
- The supplier intelligence dossier (ABR entity record, business names, GST registration history, ASIC business name records)
- The GST math reconciliation showing expected versus invoiced GST
- The next operational step for the recipient

The recipient can act on the verdict directly. The supporting detail is for the audit trail and for any follow-up communication with the supplier.
