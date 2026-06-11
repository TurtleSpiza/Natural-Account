# NA 73511 Entertainment & Hospitality (FBT) — Verification Record

Account 73511, Section 4090000 Parks, FY26 (26SLACT). Source: annotated TechOne ledger export received 9-Jun-2026 (`NA73511_Evidence/NA73511_Ledger_Extract_9-Jun-2026.xlsx`), worked 10-Jun-2026. Batch CN-23167. The export carries two reviewer annotation columns ("True Description", "Why it Can't be FBT"); these are claims to verify, not Tier 1 evidence and not Spero instructions, so nothing on this account is journalled this pass.

## Population and reconciliation

126 ledger lines reconcile to **$5,384.57 ex-GST** across seven service codes (20411/20591/20661 Natural Areas, 20151 Depots, 20001 Management, 20191 Planning, 20361 Park Services). Document mix: 55 creditor invoices (officer reimbursements dominate), 39 PCard expenses, 18 general journals, 13 AP journals, 1 PUR creditor invoice.

**Finance FBT 50/50 batches set aside (Finding 1).** Five Finance batches sit in the account per the lcc-coding-review batch identifiers (GJ076295, GJ076539, AP003647, AP003682, AP003801): 31 lines, of which 29 negative reversal legs each pair exactly to an original line (58 lines netting $0.00) and 2 positive AP003801 re-posts ($91.85, Woolworths Trailcare) remain live. The 58 paired lines are set aside as processed; the net review population is **68 lines = $5,384.57 exactly** (reconciles to the cent).

## Four-limb verdicts

**Limb 1 — Service/PK and employee: AMBER.** Every line's service crosswalks to its home PK (svc-level coding intact). Officer attribution is mixed: Todd Preussner and Adam Barter (Natural Areas, PK000434) are section-consistent on the Natural Areas codes; Aisha Wilson (Depots, PK000001) is reimbursed on 20411 Natural Areas, off-home — observation noted. Paul Gregory Mann (Park Maintenance, PK000003) and the joint payee "MR D ROSMARIN MRS C ROSMARIN" (Rosmarin matches Candy Rosmarin, Planning PK000082) need section confirmation. Allan Hoffmann (32 lines), Sara Bahry, Kerry Warnholtz and "Salisnew Peter Mervyn" are not in the Parks employee map — identification open.

**Limb 2 — Natural account: AMBER (candidates quantified, none journalled).** The annotation set, tested against the chart and the FBT ruleset, yields:

- **F2 — Officer amenity reimbursements, $334.71 (42 lines), candidate 73512.** 36 annotated lines (Hoffmann, Preussner, Barter, Wilson, Bahry — milk, biscuits, ice, fruit: on-premises light refreshments, Reason B, no FBT) plus 6 unannotated amenity-pattern lines ($74.28).
- **F3 — Non-employee catering, $301.71 (9 lines), candidate 73512.** Trailcare/volunteer/Bushcare/GCCC catering (incl the two AP003801 re-posts $91.85): non-employee hospitality, not 50/50 meal entertainment.
- **F4 — Training catering, $125.91 (2 lines), candidate 73512.** Coles Online $98.64 (food for on-premises training, Reason F) and Woolworths $27.27 (R U OK Day, not entertainment). Plus **Warnholtz invoice 001, $744.30, candidate 73544** Training & Development — narrated "Training", material, payee not in the employee map, source document unsighted (GAP).
- **F5 — Bunnings depot utensils, $23.56, candidate 72111** (not hospitality). **Daily Blooms $88.14 (TE005091 batch), classification query:** "Flowers for Cemeteries Customer" — 73513 is employee-scoped per the chart, so a customer sympathy gesture has no clean Parks home; cross-section Cemeteries question, held for ruling.
- **F6 — STAY-FBT, $3,664.79 (7 lines), 73511 correct.** Greenbank Services Club ($636.36 + $181.82), Ampol $32.73, Coles $53.27, Ace's Grocery $38.07, Woolworths Online $277.09, and **INV-9747 $2,445.45 — vendor not identified on the ledger, source invoice unsighted (GAP)**; 68% of the stay-put value rests on one unsighted document.
- **Unannotated residual, $97.27 (4 lines), pending:** TE005081 -$6.36 credit, Hoffmann $5.45, Banjos TE004580 $49.09 (Trailcare-pattern), Salisnew $49.09.

Candidate movement total if all confirmed: $1,530.19 out of 73511 ($762.33 to 73512, $744.30 to 73544, $23.56 to 72111), with $88.14 in query. No GENJNL is staged: the basis is annotation-level, awaiting Spero's ruling (standing directive: only instructed lines are journalled).

**Limb 3 — Evidence: AMBER, one line RED.** No receipts or invoices are sighted for any net line; the export carries no attachment flag. Per the evidence rule the limb cannot clear off the annotated ledger alone. RED on F7: Hoffmann $4.18 (18-Oct-2025) annotated "Doesn't Reconcile to Receipts" by the original reviewer. The 58 Finance-batch paired lines are evidenced on the netting basis (pair nets $0.00), recorded as such, not as document sighting.

**Limb 4 — Tax: AMBER.** No tax invoices sighted, so no per-line GST verification is possible. Exposure pattern flagged: the reimbursement and PCard population is dominated by supermarket food where GST-free basic food booked at gross/11 creates phantom ITCs (the Coles-milk class, GSTE-01 precedent); to be tested line by line when receipts arrive. Any errors found will be recorded on `00_GST_Errors_Register.xlsx`.

## Overall: AMBER

| Limb | Verdict | Gate |
|---|---|---|
| L1 Svc/PK + Emp | AMBER | Hoffmann/Bahry/Warnholtz/Salisnew unidentified; Wilson off-home; Mann/Rosmarin to confirm |
| L2 NA | AMBER | $1,530.19 candidates + $88.14 query await Spero ruling; $97.27 unannotated |
| L3 Evidence | AMBER (1 RED) | No receipts sighted; INV-9747 and Warnholtz 001 GAPs; $4.18 doesn't-reconcile |
| L4 Tax | AMBER | No invoices sighted; GST-free food mix untested |

## Open actions

1. Spero ruling on the candidate set: $762.33 to 73512 (amenity / non-employee / training catering), $744.30 Warnholtz to 73544, $23.56 utensils to 72111.
2. Daily Blooms $88.14 customer-gift classification (73513 is employee-scoped; cross-section Cemeteries).
3. Sight INV-9747 ($2,445.45) and identify the vendor — the largest single line on the account.
4. Sight Warnholtz invoice 001 ($744.30) and identify the payee.
5. Identify Hoffmann, Bahry, Warnholtz and Salisnew against People & Positions; confirm Mann and Rosmarin line sections.
6. Obtain receipts for the PCard/reimbursement population to run the per-line GST-free food check.
7. Classify the four unannotated lines ($97.27).

## Addendum, 11-Jun-2026: INV-9747 SIGHTED, vendor identified, stay-FBT verdict substantiated

The largest line on the account is now evidenced. INV-9747 ($2,445.45 ex-GST) is Greenbank Services Club: tax invoice dated 12-Nov-2025, reference Parks Branch PO 713482, "EOY CELEBRATION - TOP DECK - 3RD DECEMBER 2025", package $3,590.00 (bond $200.00, room hire $700.00, food $2,690.00), less bond received 30-Sep-2025 and a $700.00 payment received, amount due $2,690.00. GL $2,445.45 x 1.1 = $2,690.00 exact.

- Limb 2 NA: the line STAYS in 73511. An end-of-year staff celebration at a licensed club is squarely FBT entertainment; the stay-FBT verdict that previously rested on the unsighted invoice now rests on Tier 1.
- Limb 4 Tax: COMPLIANT. ABN 64 442 003 715 checksum PASS; ABR sighted 11-Jun-2026 (GREENBANK CONSOLIDATED LIMITED, active from 24-May-2000, GST registered from 1-Jul-2000, registered business name GREENBANK SERVICES CLUB from 28-May-2021, matching the invoice). GST disclosed $308.18 = (package $3,590.00 less GST-excluded bond $200.00) / 11 exact; the GST inside the $2,690.00 food balance is $244.55, matching the GL ex-GST base.
- Residuals on this vendor: the $700.00 room hire was paid on a separate earlier payment not yet traced to a ledger line (likely another reference or FY timing); the $200.00 bond should have returned or netted, trace pending. Neither blocks this line.

Evidence filed: NA73511_Evidence/NA73511_L01_Greenbank_INV-9747.pdf. The account's remaining opens are unchanged otherwise (candidate-set ruling, Warnholtz 001, payee identifications, PCard food receipts, four unannotated lines).
