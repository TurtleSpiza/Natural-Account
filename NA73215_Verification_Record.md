# NA73215 Verification Record - Major Contracts - Partnership (Alliance)
Prepared 11-Jun-2026 | Spero Karkalemis | Ledger 26SLACT, Branch 4090000, O110-O115, P1-12

Verdict: AMBER. Full account reviewed, $4,739.00 ex-GST across 5 ledger lines (3 carrying dollars, 2 zero split lines). Evidence and tax limbs GREEN on 100% of account dollars. The NA limb is RED: all three invoices are landscape maintenance works booked into 73215 Major Contracts - Partnership (Alliance), a restricted account (Alliance, CEO approval required) that ought to carry Alliance partnership contract spend only. Recode candidate 73215 to 73126 Landscapers & Gardeners, $4,739.00, held un-instructed for Spero.

## Account reconciliation
Ledger extract (NA73215_Ledger_Extract_11-Jun-2026.xlsx) totals $4,739.00 ex-GST and reconciles exactly to SE2 (8-Jun-2026) accumulated actuals P1-12 of $4,739.00. Zero variance. Annual budget is $0; the account self-evidently carries no planned Parks spend, which is consistent with the finding that nothing here belongs on it.

## Lines

### L01 Total Environmental Concepts invoice 3043, $2,340.00 ex (P1, 1-20511-73215, WO PK000366)
- Work: mow entire area and brushcut boundary line including nature strip, 94-98 Bromley St, Cornubia, 4-Jul-2025, under PAR/336K/2024, PO 702328, CR 3706990, attention Ron Clunn.
- Limb 1 PK: GREEN. Invoice names PK000366; ledger work order PK000366, svc 20511 General Landscape Improvement Fund (Park Maintenance). Match. A companion $0.00 line sits on 1-20267-73215 (WO PK000041), carrying no dollars.
- Limb 2 NA: RED. Mowing and brushcutting under a PAR schedule is contract mowing and landscaping work; the chart destination is 73126 Landscapers & Gardeners. 73215 is restricted to Alliance partnership contracts.
- Limb 3 Evidence: GREEN. Tax invoice sighted (C00217226 (4), filed as NA73215_L01).
- Limb 4 Tax: COMPLIANT. ABN 11 600 627 343 checksum PASS; ABR sighted 11-Jun-2026 (TOTAL ENVIRONMENTAL CONCEPTS PTY LTD, active from 25-Sep-2014, GST registered from 3-Nov-2014, QLD). GST $234.00 = 10% of $2,340.00 exact; invoice $2,574.00 incl = GL $2,340.00 x 1.1 exact. $1,000+ tier elements present (buyer identified, LCC ABN quoted).
- GST status: taxable supply, GST charged and claimable; booked ex-GST correctly.

### L02 Austspray invoice 155797, $900.00 ex (P2, 1-20511-73215, WO PK000366)
- Work: initial clean-up of fenceline garden LZ6-175, Marl Crescent, Yarrabilba, 18-Jun-2025, PO 702326, Cr 3716207, attention Peter Cronin.
- Limb 1 PK: GREEN. Invoice names PK000366; ledger matches (svc 20511). A companion $0.00 line sits on 1-20453-73215 (WO PK000440), carrying no dollars.
- Limb 2 NA: RED. Fenceline garden clean-up is landscape maintenance; destination 73126.
- Limb 3 Evidence: GREEN. Tax invoice sighted (C00226645 (4); the intake also carried a byte-identical duplicate C00226645 (5), archived, not separately filed).
- Limb 4 Tax: COMPLIANT. ABN 89 122 731 775 checksum PASS; ABR sighted 11-Jun-2026 (AUSTSPRAY ENVIRONMENTAL WEED CONTROL PTY LTD, active from 17-Nov-2006, GST registered from 1-Dec-2006, QLD). GST $90.00 exact; invoice $990.00 incl = GL $900.00 x 1.1 exact.
- GST status: taxable supply, booked correctly. Note: invoice dated 19-Jun-2025 (FY25) posted P2 FY26; late processing advisory only.

### L03 Austspray invoice 157909, $1,499.00 ex (P10, 1-20511-73215, WO PK000366)
- Work: LZ1-100 Frankland Ave traffic island infill planting, 27-Mar-2026, PO 702326, PK000366, attention Billy Bevan.
- Limb 1 PK: GREEN. Invoice names PK000366; ledger matches (svc 20511).
- Limb 2 NA: RED. Infill planting is landscaping work; destination 73126.
- Limb 3 Evidence: GREEN. Tax invoice sighted (C00279700 (2), filed as NA73215_L03).
- Limb 4 Tax: COMPLIANT. Same supplier dossier as L02. GST $149.90 exact; invoice $1,648.90 incl = GL $1,499.00 x 1.1 exact.
- GST status: taxable supply, booked correctly.

## Findings
1. Systemic NA miscode, 100% of account: $4,739.00 of $4,739.00 (100%) of FY26 spend on 73215 is general landscape maintenance and planting work on the General Landscape Improvement Fund (PK000366, svc 20511), none of it Alliance partnership contract spend. All three lines carry "STANDING ORDER 24/25" in Details, masking the vendor; the sighted invoices supply Tier 1 identification.
2. Restricted-account exposure: 73215 is flagged in the chart as Alliance, restricted, CEO approval required, and pk_validator blocks journal lines that touch it. Spend has nonetheless posted to it through AP. The recode out is corrective; the restriction handling on the credit leg (source 73215) needs Spero's confirmation when the recode is instructed, since the validator will flag the source account.
3. The two $0.00 companion lines (1-20267 WO PK000041, 1-20453 WO PK000440) carry no dollars and need no recode; they evidence that the AP split keyed additional cost lines at zero.

## Recode candidate (HELD, un-instructed)
73215 to 73126, full-reversal, three pairs, $4,739.00, nets $0.00:
- Cr 1-20511-73215 / PK000366 -$2,340.00, Dr 1-20511-73126 / PK000366 +$2,340.00, narration "TEC INV-3043 mowing recode to 73126" (35 chars, validates).
- Cr 1-20511-73215 / PK000366 -$900.00, Dr 1-20511-73126 / PK000366 +$900.00, narration "Austspray INV-155797 recode to 73126" (36 chars, validates).
- Cr 1-20511-73215 / PK000366 -$1,499.00, Dr 1-20511-73126 / PK000366 +$1,499.00, narration "Austspray INV-157909 recode to 73126" (36 chars, validates).
Destination validates clean: pk_validator OK on PK PK000366 / svc 20511 / 73126. Source leg trips the 73215 restriction flag by design; release on Spero's instruction with the restriction acknowledged.

## Four-limb summary
| Limb | Rating | Basis |
|---|---|---|
| L1 PK / service | GREEN | All dollar lines PK000366 svc 20511, matching the invoices |
| L2 Natural account | RED | 100% miscoded into restricted 73215; destination 73126 |
| L3 Evidence | GREEN | 3 of 3 invoices sighted, 100% of dollars |
| L4 Tax | GREEN | All three COMPLIANT; ABNs PASS, ABR active + GST registered, GST exact |
| Overall | AMBER | Recode candidate held for instruction |
