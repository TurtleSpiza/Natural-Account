# Worked Examples

Four worked examples covering the most common compliance scenarios. Each is followed end-to-end from the document upload through to the operational next step.

## 1.0 Example, COMPLIANT, "Fire Management Training" partnership

**The setup.** LCC Parks receives a tax invoice for $880.00 (GST-inclusive) from Fire Management Training, dated 12 March 2026, for a one-day field-staff training course. The invoice shows ABN 33 078 502 894, "Total price includes GST", a brief description "Fire Management Training, one-day course, 8 attendees", and a single line item.

**Stage 1, document compliance.** Heading "Tax Invoice" present. Supplier identity "Fire Management Training" present. ABN 33 078 502 894 present. Date 12 March 2026 present. Description sufficient, including quantity (8 attendees). GST shown via "Total price includes GST" statement, which is valid under ATO QC 22422 element 6 provided GST equals exactly 1/11 of total. Total is $880, so GST should be exactly $80, which it is. Element 7 satisfied, single taxable supply. All seven elements present. Invoice is under $1,000, so element 8 (buyer identity or ABN) is not required.

**Stage 2, ABN validation.** Checksum on 33078502894 passes (mathematical test, verified by `abn_validator.py checksum 33078502894`). ABR public-register fetch at `https://abr.business.gov.au/ABN/View?abn=33078502894` returns:

- Entity name, A.B JOHNSTON & A.N JOHNSTON
- ABN status, Active (from 01 Mar 2006)
- Entity type, Family Partnership
- GST registered, from 01 Apr 2006 (continuous)
- Main business location, QLD 4552
- Business names, Fire Management Training (from 23 Oct 2015), ADVENTURE AND SURVIVAL TRAINING (from 30 Apr 2015)

ABN is Active. GST-registered as at the invoice date (12 March 2026), so the GST charge is valid.

**Stage 3, supplier name reconciliation.** "Fire Management Training" appears on the ABR's business names list for this ABN, registered 23 Oct 2015, still current. ASIC Business Names register extract confirms Status: Registered, Renewal date 23/10/2027, Holder Name A.B JOHNSTON & A.N JOHNSTON, Holder Type Partnership, Holder ABN matches invoice ABN. No cancellation under review. Name reconciles cleanly.

**Stage 4, GST math.** Total $880.00, expected GST = 880 / 11 = $80.00. Implied GST $80.00 (from "includes GST" statement). Match to the cent.

**Stage 5, concerns scan.** No red flags fire. The partnership has held the ABN since 2006, has been continuously GST-registered, holds two registered business names both of which appear genuine and longstanding (Fire Management Training since 2015, Adventure and Survival Training since 2000 originally as a Queensland state business name, transferred to the federal ASIC register in 2015).

**Verdict.** `COMPLIANT`. Process at face value. Claim the $80 GST credit in the relevant BAS. Code per `lcc-coding-review` to the appropriate training natural account (likely 73320 or similar, depending on the FBT classification of the training).

## 2.0 Example, COMPLIANT_WITH_NOTE, recent GST registration

**The setup.** A new Parks contractor, "Green Verge Maintenance Pty Ltd", invoices for $4,400.00 (GST-inclusive) on 5 May 2026 for street-tree pruning. ABN passes checksum. ABR shows the company was incorporated 1 Feb 2026 and GST-registered from 15 Feb 2026.

**Stages 1 to 4.** All elements present, ABN active, GST-registered, name reconciles. GST math correct ($400 GST on $4,000 ex-GST, total $4,400). Buyer identity shown (LCC, ABN 21 627 796 435), satisfying the $1,000-plus eighth element.

**Stage 5, concerns scan.** One NOTE-tier flag fires, `GST_REGISTRATION_RECENT`. GST registration is less than 90 days before the invoice date. Not a compliance failure but worth recording. The supplier is a real, registered company with valid GST registration. The note is that this is an early-stage supplier and additional verification on the second invoice would be prudent.

**Verdict.** `COMPLIANT_WITH_NOTE`. Process. Record the note in the supplier master record. On the next transaction, the note appears and the AP processor can decide whether to apply additional scrutiny.

## 3.0 Example, NON_COMPLIANT_FIXABLE, missing buyer identity over $1,000

**The setup.** A consultancy invoice for $2,750.00 (GST-inclusive) is received. All standard elements present (heading, supplier, ABN, date, description, GST, taxable-portion identification), GST math correct, ABN active and GST-registered. However, the invoice shows no buyer identity, no buyer ABN, just "Attn: AP" in the address line.

**Stages 1 to 4.** All seven mandatory elements present. ABN valid and active. GST registered. GST math correct.

**Stage 5, concerns scan.** One FIXABLE-tier flag fires, `MISSING_BUYER_IDENTITY_OVER_1000`. Per ATO QC 22422, sales of $1,000 or more must show the buyer's identity or ABN as the eighth element. The defect is cureable by reissue.

**Verdict.** `NON_COMPLIANT_FIXABLE`. Block payment. Request reissue with the buyer name "Logan City Council" or LCC's ABN 21 627 796 435 shown on the invoice. Supplier has 28 days under ATO QC 22431. Once the reissued invoice arrives, re-run the verification.

## 4.0 Example, NON_COMPLIANT_BLOCK, GST charged without registration

**The setup.** A small landscaping contractor invoices $660.00 (GST-inclusive) on 8 April 2026, with $60 GST shown. ABN checksum passes. ABR fetch shows:

- Entity name, J. Smith Landscaping
- ABN status, Active
- GST status, Not currently registered (cancelled 1 January 2025, never re-registered)

The contractor's ABN is real and active, but they cancelled their GST registration over a year ago, presumably because their turnover fell below the $75,000 threshold. They are continuing to issue invoices that look like tax invoices and charging GST as if they were registered.

**Stages 1 to 2.** Elements all present, ABN valid and active.

**Stage 3.** Supplier name reconciles to the ABR entity name.

**Stage 4.** GST math correct on the face of it ($60 = $660 / 11).

**Stage 5, concerns scan.** One BLOCK-tier flag fires, `GST_CHARGED_WITHOUT_REGISTRATION`. The supplier is not GST-registered as at the invoice date, so they cannot lawfully charge GST and the recipient cannot claim a credit on it.

**Verdict.** `NON_COMPLIANT_BLOCK`. Block payment. Contact the supplier:

- Confirm whether they have re-registered for GST (in which case the ABR may not yet reflect it, request evidence of registration)
- If they have not re-registered, request reissue as a normal (non-tax) invoice for $600, with no GST line
- Recover the wrongly charged $60 GST per ATO guidance, do not claim it as an input tax credit since no GST was actually payable on a non-taxable supply

Record the supplier's GST status in the supplier master so future invoices are processed correctly. Consider notifying the ATO if the supplier is systematically issuing fake tax invoices, as this is a GST integrity matter.

## 5.0 What changes for an RCTI

If LCC issues a recipient-created tax invoice (rare, requires a written RCTI agreement under the Commissioner's RCTI Determination 2023), the verifier runs the same five stages with two adjustments:

5.0.1 **Stage 1 element 1** is satisfied by the document indicating it is a recipient-created tax invoice, not by "Tax Invoice" alone. The phrase "Recipient-Created Tax Invoice" or "RCTI" must appear in the heading.

5.0.2 **Stage 2 ABN validation** is run on both parties' ABNs, since both must be GST-registered as at the issue date for the RCTI to be valid. Both parties' ABNs and GST registration statuses must be sighted in the ABR.

If LCC's own GST registration has lapsed, no RCTI can be issued. If the supplier's GST registration has lapsed, no RCTI can be issued. Either way, fall back to a normal supplier-issued tax invoice.

The recipient must give the original or a copy of the RCTI to the supplier within 28 days of the date of the sale or the date the value is determined. This is the only 28-day rule that runs against the recipient rather than the supplier.
