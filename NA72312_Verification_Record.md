# NA 72312 Office & Library Equipment — Verification Record

Batch CN-23167 (held). Reviewed 8-Jun-2026. Section 4090000, FY26 (26SLACT), Period 1-12.
Ledger export reconciles to 2 lines, total $2,461.27 ex-GST (footer $2,461.27, matched).
One PCard reconciliation ($218.18) and one AP creditor invoice ($2,243.09).

Verdict: AMBER. $2,461.27 (100%) miscoded in 72312. The whole account belongs in 72313 Furniture & Fittings. Recode held pending one PK confirmation and Finance format acceptance.

## Account composition

Two lines, both in the Minor Asset Acquisition / Minor Assets / Office & Library bucket of 72312.
Line 01 IKEA, PCard reconciliation TE004431, PK000493 svc 20392, Period 2, 7-Aug-2025.
Line 02 Empire Office Furniture, PUR Cred Invoice RL196475, PK000001 svc 20151, Period 11, 21-May-2026.

72312 test (COA p20): minor Office & Library Equipment below the asset threshold. The confusable pair is 72313 Furniture & Fittings (minor furniture and fittings below threshold). Equipment means devices and apparatus. Cabinets, shelving, chairs, desks and their components are furniture and fittings, not equipment. The non-negotiable branch rule states chair and desk components are 72313. techone-output Pattern C records the established recode "Empire chair 73544 to 72313".

## Line 01 — IKEA TE004431 (AUINV26000000180535)

EKET cabinet combination, white. 095.910.17 EKET cab comb w ft 105x35x72 ($240.00 incl headline), built from 506.166.37 EKET cab w dr/1 shlf ($95.00 incl), 706.166.41 EKET cb w 4 comp ($125.00 incl), 403.400.45 EKET foot adjust metal 4-p x2 ($20.00 incl), plus collect-at-store service $5.00 discounted to $0.00. Net $218.18, GST $21.82, total $240.00 incl. GL $218.18 ex matches the invoice net to the cent. ABN 84 006 270 757 checksum PASS. Cover slip (CIA credit card control): requesting officer Rene Harreman, supplier IKEA, description "SHELVING", reason "STORAGE", cost account PK000493, $240.00, cardholder Brad Powell (signed). Delivered to 177 Chambers Flat Road Marsden (Parks Depot).

Four limbs:
- L1 PK AMBER. PK000493 is not in the canonical service map (pk_validator: "PK number 'PK000493' not found in service map"). Service code 20392 crosswalks to PK000022 Park Services (Parks Asset Maint and Repairs). The cover slip confirms PK000493 was the intended cost account, but the PK cannot be validated against the map. Confirm before release.
- L2 NA RED. EKET cabinets and shelving are storage furniture, not office equipment. Description and reason on the cover slip both read as storage furniture. Correct account 72313 Furniture & Fittings.
- L3 Evidence GREEN. IKEA tax invoice (seven elements present) plus signed CIA credit card cover slip. Legible and sufficient.
- L4 Tax GREEN. ABN checksum PASS. GST $21.82 reconciles ($240.00 / 11 = $21.82, $218.18 x 0.1 = $21.82). Under-$1,000 tier; all mandatory elements present. ABR live status to confirm at processing.

RAG: AMBER. Recode direction to 72313 firm. Held on the PK000493 question.

## Line 02 — Empire Office Furniture RL196475

Hawa Dane Pty Ltd T/A Empire Office Furniture. Three components, all swapped or installed on site at the Parks Depot:
- GASLIFT96 140mm gas lift x16 at $36.36 ex = $581.76 ex. Replacement gas lift cylinders for Flow office chairs (chair components).
- SOFT80.WH "Pop-in Power" desk-top power module x9 at $126.36 ex = $1,137.24 ex. GPO and fast-charge USB, secures into an 80mm desk cable hole (desk component).
- SERVICE delivery and assembly $524.09 ex. Labour to swap 16 chair gas lifts and 9 pop-in powers on site (install of the above).

Net $2,243.09, GST $224.31, total $2,467.40 incl. GL $2,243.09 ex matches the invoice ex-GST total to the cent. ABN 33 268 623 611 checksum PASS. Invoice to Logan City Council, 150 Wembley Road, Logan Central; deliver to Parks Depot Marsden, attn Bradley Waugh.

Four limbs:
- L1 PK GREEN. PK000001 svc 20151 Parks Leadership and Administration. pk_validator: VALID.
- L2 NA RED. Chair gas lifts are chair components, the pop-in power is a desk component, and the labour is the install of both. The non-negotiable rule places chair and desk components in 72313. Correct account 72313 Furniture & Fittings.
- L3 Evidence GREEN. Full tax invoice, all seven elements, item-level detail. Legible and sufficient.
- L4 Tax GREEN. ABN checksum PASS. GST $224.31 reconciles ($2,467.40 / 11 = $224.31, $2,243.09 x 0.1 = $224.31). Over-$1,000 tier; buyer identity (Logan City Council) present.

Data-quality note: the ledger Details narration reads "Quote RL 48500", which neither matches the invoice number RL196475 nor reflects that the document is a tax invoice, not a quote. Not a blocker. Noted for the booking record.

RAG: AMBER. Recode $2,243.09 ex to 72313, same PK000001. Direction firm and fully validated; held only on Finance format acceptance.

## GST status (Limb 4, per-line reconciliation)

Both lines reconcile booked-to-document and carry no GST-free or offshore element. IKEA $218.18 ex with $21.82 GST shown ($240.00 / 11); Empire $2,243.09 ex with $224.31 GST ($2,467.40 / 11). Both are standard-rated taxable supplies, so the booked ex-GST grosses to the invoice at 1.1 and the input tax credit is valid on each. GST status GREEN.

## Account reconciliation

Ledger total $2,461.27 ex-GST = footer $2,461.27. Reclassified out of 72312: $2,461.27 (both lines). Remaining correctly in 72312: $0.00. The account does not retain a single line.

## Recode (held, batch CN-23167)

Full-reversal, four lines, two pairs, each nets to zero, batch nets $0.00. Natural account is wrong on both lines and the PK is preserved as transacted, so full-reversal per the standing rule. Line B validated against pk_validator (PK exists, matches service code, destination 72313 unrestricted). Line A NA and amount valid; PK flagged. See NA72312_GENJNL_Recode.txt.

## Overall RAG

AMBER. The account does not clear. The recode direction is firm on both lines (both to 72313 Furniture & Fittings). Line B (Empire, $2,243.09) is fully validated and ready. Line A (IKEA, $218.18) is held on the PK000493 question.

## Open actions

1. Confirm the correct PK for line A. PK000493 is not in the canonical service map; service code 20392 crosswalks to PK000022. If PK000493 is invalid, the re-post leg goes to the confirmed PK. Batch to Amy Forgione and Owen Jensen.
2. Confirm Finance accepts the 72312 to 72313 recode and the full-reversal format for this batch.
3. On confirmations, release the held recode in CN-23167.
4. Advisory: correct the line 02 booking narration "Quote RL 48500" to reference invoice RL196475 if the source record is editable.

## Method notes

- 72312-versus-72313 call made on lcc-coding-review (COA p20 descriptions), the non-negotiable rule "chair and desk components are 72313", and techone-output Pattern C ("Empire chair 73544 to 72313"). No specific confusion-pair entry exists for 72312/72313; the COA descriptions plus the branch rule carry the decision.
- lcc-asset-accounting not installed. Both lines sit in the Minor Asset Acquisition bucket below the capitalisation threshold and stay minor-asset expense; the only question resolved here is which minor-asset account (72312 vs 72313), which the COA descriptions decide directly. No capitalisation-threshold logic was applied.
- lcc-split-pk-recode not installed. Neither line splits across PKs, so no split logic was required. Full-reversal format follows the standing rule that NA-wrong recodes use full-reversal.

---

## Addendum, 9-Jun-2026 (IKEA line PK resolved)

The Line 01 IKEA PK is resolved. PK000493 is confirmed valid as transacted: Flying Gang, Park Services, svc 20392 (analyst sub-PK ledger). The earlier "svc 20392 maps to PK000022" note reflected the installed maps, which carry only the primary PK000022 for svc 20392 and do not hold the Flying Gang sub-PK. PK000493 is preserved as transacted; there is no PK movement on the IKEA line.

PK limb now GREEN. The only remaining 72312 action is Finance acceptance of the 72312 to 72313 full-reversal recode, then release of CN-23167. Caveat: pk_validator will fail PK000493 until the Flying Gang sub-PK is added to lcc-coding-review, so the IKEA recode line will not pass automated validation against the current maps.
