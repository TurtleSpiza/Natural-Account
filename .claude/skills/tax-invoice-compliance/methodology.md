# Methodology

The authoritative ruleset for the verifier. All references are to ATO source material as at the dates last updated, primarily QC 22422 (Tax invoices), QC 22431 (Claiming GST credits), QC 22417 (Input-taxed sales), QC 22418 (GST-free sales), QC 22429 (Taxable sales), GSTR 2013/1 (tax invoices), and TAA Schedule 1, section 12-190 (no-ABN withholding).

## 1.0 The tax-invoice value tiers

ATO QC 22422 sets three tiers based on GST-inclusive sale value, each with different evidence requirements.

### 1.1 Under $82.50 (including GST)

No tax invoice required for the recipient to claim a GST credit. One of the following is sufficient:

- Tax invoice
- Cash register docket
- Receipt
- Invoice (non-tax-invoice)
- Diary entry with supplier name, ABN, date, description of items, amount paid

ABN validation is still required, since a credit cannot be claimed against a non-existent or inactive ABN.

### 1.2 $82.50 (including GST) and over, up to $1,000

A tax invoice with the seven mandatory elements (see 2.0) is required.

### 1.3 $1,000 and over (including GST)

A tax invoice with the seven mandatory elements plus the eighth element (buyer identity or buyer ABN) is required.

## 2.0 The seven mandatory tax-invoice elements

Per ATO QC 22422, "Sales under $1,000". A tax invoice for a taxable sale of less than $1,000 must include enough information to clearly determine all seven of the following.

| # | Element | Notes |
|---|---|---|
| 1 | Document is intended to be a tax invoice | Usually shown by the heading "Tax Invoice". For Peppol eInvoices conforming to the A-NZ Invoice Specification, this requirement is satisfied by the framework itself without the literal words |
| 2 | Seller's identity | Trading name or registered business name, must match the ABR record or one of the ABR-registered business names |
| 3 | Seller's Australian Business Number (ABN) | Eleven digits, must pass the ATO checksum (see 3.0), must be Active as at the invoice date |
| 4 | Date the invoice was issued | Calendar date, not a date range. Future-dating is a red flag |
| 5 | Brief description of the items sold | Including quantity where applicable and price. "Goods supplied" with no further detail is not sufficient |
| 6 | GST amount (if any) payable | Either shown separately, or implied by the statement "Total price includes GST" provided GST equals exactly Total divided by 11 |
| 7 | Extent to which each sale on the invoice is a taxable sale | For mixed supplies (taxable plus GST-free or input-taxed), each portion must be identifiable |

## 3.0 The eighth element for sales of $1,000 or more

Per ATO QC 22422, "Sales of $1,000 or more". The tax invoice must additionally show:

- The buyer's identity, OR
- The buyer's ABN

If the buyer is a GST group member, the identity shown can be the recipient, the GST group, the representative member, or any member where there would still be a creditable acquisition.

For sales to more than one recipient, each recipient's identity or ABN must be shown. For sales by more than one entity (co-owners), each co-owner's identity and ABN must be shown, or one co-owner acting as agent co-owner with their identity and ABN shown.

## 4.0 The ABN checksum algorithm

The ATO defines an ABN as valid if the following holds. This is a mathematical test, requires no network access, and either passes or fails decisively.

1. The ABN is exactly eleven digits, with spaces or hyphens removed before testing.
2. Subtract 1 from the first digit, leaving the remaining ten digits unchanged.
3. Multiply each digit by the corresponding weight from the sequence `[10, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19]`.
4. Sum the eleven weighted products.
5. The ABN is valid if and only if the sum is divisible by 89.

A passing checksum proves the ABN is well-formed, but does not prove the ABN is currently active or that the entity is GST-registered. The ABR lookup in Stage 2 is still required.

## 5.0 The no-ABN-withholding rule

Per the Taxation Administration Act 1953, Schedule 1, section 12-190. Where a supplier does not quote an ABN on an invoice for a supply valued at more than $82.50 (including GST), the recipient is required to withhold 47% of the invoice amount and remit it to the ATO as withholding tax.

Exemptions where withholding is not required:

- The supply is wholly of a private or domestic nature for the supplier
- The supplier is an individual under 18 and the payment is below the relevant weekly threshold
- The supply is made by an entity not carrying on an enterprise in Australia
- The supplier has provided a written statement that the supply is not made in the course of an enterprise (the "Statement by a supplier" ATO form 38-509)
- The total payment to the supplier across the income year does not exceed $75

If none of these exemptions applies and the invoice exceeds $82.50 with no ABN quoted, the verdict is `NO_ABN_WITHHOLD`, pay the supplier 53% of the invoice value, remit 47% to the ATO.

## 6.0 GST treatment matrix

The ATO recognises three GST treatments for sales. Each has distinct implications for what a tax invoice may show and what the recipient may claim.

| Treatment | Examples | GST on invoice | Recipient's GST credit |
|---|---|---|---|
| **Taxable** | Most goods and services, taxi travel, ride-sourcing, hospitality, professional services | 10% included | Yes, equal to GST shown |
| **GST-free** | Most basic food, water/sewerage/drainage, eligible medical and health services, eligible education, eligible childcare, eligible exports, going-concern business sales, precious metals, GST-free car parts for eligible disabled persons | None | None (already GST-free) |
| **Input-taxed** | Financial supplies (lending, credit, shares, super), residential rent, sale of existing residential premises | None | None (cannot be claimed) |

A supplier who charges GST on a GST-free supply has done so in error. The recipient is entitled to a refund from the supplier per ATO guidance on imported services and digital products being wrongly charged GST. The recipient cannot claim the wrongly-charged GST as a credit, since the supply was not in fact taxable.

A supplier who treats a taxable supply as GST-free has under-collected GST. From the recipient's perspective this is the supplier's problem, but the recipient also cannot claim a GST credit on a supply where no GST was charged. The invoice itself remains valid as a non-tax-invoice.

## 7.0 Rounding rules

Per ATO QC 22422, "Rounding of GST".

For a single taxable sale on the invoice, round GST to the nearest cent (0.5 cents rounds up).

For multiple taxable sales on the invoice, two methods are permitted, the supplier picks one:

- **Total invoice rule**, sum the GST across all taxable sales, then round to the nearest cent (0.5 cents rounds up). Alternative form, where every taxable sale's GST is exactly 1/11 of its price, sum the GST-exclusive values, calculate GST on the total, round to the nearest cent.
- **Taxable sale rule**, calculate GST per taxable sale, round each as appropriate, sum the rounded individual GST amounts, then round the total to the nearest cent.

Supplier and recipient do not need to use the same rounding rule.

## 8.0 The 28-day rules

Three separate 28-day rules apply.

8.0.1 **Supplier issuance**. If the recipient requests a tax invoice, the supplier has 28 days to provide one, unless the sale is under $82.50.

8.0.2 **Recipient under non-cash accounting**. If the recipient is under non-cash (accruals) GST accounting and does not have the tax invoice, the GST credit cannot be claimed in the relevant BAS until a valid tax invoice is held. Once held, the credit can be claimed in any later BAS within the four-year credit time limit.

8.0.3 **RCTI issuance**. Where an RCTI is used, the recipient (issuing the RCTI) must give the original or a copy to the supplier within 28 days of the date of the sale or the date the value is determined.

## 9.0 Recipient-created tax invoices (RCTI)

Per ATO QC 22422, "Recipient-created tax invoices", and the Recipient Created Tax Invoice Determination 2023.

An RCTI can only be issued if all of the following hold:

- Both parties are GST-registered at the time the RCTI is issued
- Both parties have agreed in writing that the recipient may issue an RCTI and the supplier will not issue a tax invoice
- The agreement is current and effective when the RCTI is issued
- The Commissioner's RCTI Determination 2023 lists the type of goods or services covered

A valid RCTI must:

- Contain everything required of a normal tax invoice plus an indication that the document is intended to be an RCTI
- Show both the supplier's and the recipient's ABNs, both registered for GST as at issuance
- If GST is payable, show that it is payable by the supplier

The recipient must check the supplier's GST registration via the ABR before issuing the first RCTI, and periodically thereafter while issuing RCTIs on an ongoing basis. If the supplier deregisters from GST, RCTI issuance must stop immediately.

## 10.0 eInvoices and the Peppol framework

Australia has adopted the Peppol framework as the national eInvoicing standard. Per ATO QC 22422, "eInvoicing". An eInvoice conforming to the A-NZ Invoice Specification under Peppol satisfies the requirement that the document is intended to be a tax invoice, even if the literal words "Tax Invoice" do not appear, provided all the other mandatory data fields are present.

This skill treats a Peppol eInvoice with the mandatory data fields as compliant for element 1, the heading test, and runs the remaining elements normally.

## 11.0 Partly taxable sales

Per ATO QC 22422, "Taxable and non-taxable sales", and GSTR 2001/8.

A tax invoice that includes both taxable and non-taxable items (GST-free or input-taxed) must clearly identify which items are taxable. The invoice must also show the GST amount on the taxable portion only, and the total amount payable across all items.

If the breakdown is opaque (a single line item bundling taxable and non-taxable supplies without apportionment), the verdict is `NON_COMPLIANT_FIXABLE`, action is to request a reissue with the breakdown.

## 12.0 When you do not claim a GST credit

Per ATO QC 22434. Even with a valid tax invoice in hand, the recipient cannot claim a GST credit in these situations:

- The recipient is not GST-registered
- The purchase has no GST in its price (GST-free or input-taxed)
- The purchase is from a supplier not GST-registered (no GST in price)
- The purchase is for wages (no GST on wages)
- The purchase is for a private or domestic purpose (to the extent of private use)
- The purchase relates to making input-taxed supplies (such as residential rent)
- The purchase is real property under the margin scheme
- The purchase is for entertainment expenses non-deductible for income tax
- The purchase is for the portion of a car above the car limit
- The four-year credit time limit has ended

This skill confirms the tax-invoice compliance and the supplier validity. The downstream determination of whether the credit can actually be claimed depends on the recipient's circumstances, which are outside this skill's scope.

## 13.0 The four-year credit time limit

Per ATO QC 22431, "Credit Time limit", and MT 2024/1.

A GST credit must be included in an assessment before the end of the four-year credit time limit. The four years run from the lodgment due date of the BAS for the tax period in which the credit could have first been claimed.

Under cash accounting, that is the tax period payment is made.

Under non-cash (accruals) accounting, that is the first tax period an invoice was issued or any payment was made, whichever is earlier.

If the four years pass without the credit being included in an assessment, the entitlement ceases. The Commissioner has no discretion to extend the limit. Two narrow exceptions apply, see ATO QC 22431.

This skill flags any invoice older than three and a half years as a NOTE-tier concern, since the four-year clock may be close to running out.
