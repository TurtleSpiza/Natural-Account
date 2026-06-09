73563 PRINTING & STATIONERY — WINC LINE-ITEM CODING AUDIT
Support Package
Prepared 8-May-2026 — Spero Karkalemis, Parks Branch 4090000

==============================================================================
WHAT'S IN THIS ZIP
==============================================================================

00_README.txt                              This file.

05_findings.txt                            Plain-text findings report. Read first.

06_workbook_audit.xlsx                     Full audit workbook — Summary, Line
                                           Items (filterable), Recode Journal
                                           (TechOne PK ledger format).

--- Source files ---
07_GL_listing_source.xlsx                  TechOne Ledger Accounts Transactions
                                           Table — 73563 across Parks branch,
                                           38 lines, P1–P10 FY25-26.
08_DocumentReconstruction_096380.xlsx      IN stockroom issue Doc 202602051062
                                           777000000014 (Marsden depot).
09_DocumentReconstruction_096380.pdf       Same, PDF copy.

--- Working data ---
01_parks_lineitems_raw.csv                 249 line items extracted from
                                           TAXINVOICE sheets of 9 WINC PDFs.
02_parks_lineitems_classified.csv          Same plus suggested_acct, status,
                                           suggested_category per line.
03_parks_miscoded_items.csv                Miscoded subset only (114 lines).
04_winc_parks_summary.csv                  WINC SUMMARYIN sheet rolled up to
                                           cost-centre level for both Parks
                                           accounts.

--- Output rollups ---
10_recode_summary_by_pk.csv                Recode totals per PK + destination.
11_recode_by_invoice.csv                   Recode impact per WINC invoice.
12_distinct_miscoded_items.csv             Each unique miscoded item with qty,
                                           occurrences and total $.
13_distinct_ok_stationery_items.csv        Each unique correctly-coded item
                                           kept in 73563.

==============================================================================
HEADLINE
==============================================================================

WINC Parks total: $6,261.48 over 9 invoices (P1 to P10).
Stationery (73563 OK):  $2,455.98   135 lines
Miscoded:               $3,805.50   114 lines   (60.8% of dollars)

Recode by destination:
  73564 IT Equipment & Applications        $1,732.31    32 lines
  73512 Hospitality Non-FBT (Reason B)     $1,318.86    42 lines
  72111 Minor Equipment & Supplies           $754.59    36 lines
  72112 Chemical & Pesticide                  $15.56     2 lines
  72113 Safety Equipment                     -$15.82     2 lines

==============================================================================
RECONSTRUCTION STEPS
==============================================================================

To rebuild everything from scratch:

1. Open the 9 WINC creditor invoice xlsx files.
2. For each, parse the TAXINVOICE sheet and capture rows where ACCOUNT is
   10179376 or 10428958. Skip "Transaction Total" and "Cost Centre Total"
   subtotal rows (they have the text in column G not column A).
3. Concatenate to produce 01_parks_lineitems_raw.csv.
4. Apply the classifier (regex against ITEM DESCRIPTION) to produce
   02_parks_lineitems_classified.csv.
5. The classifier is documented in 05_findings.txt > Methodology section.

==============================================================================
