# NA73211 Minor Contracts (below $20,000) - Verification Record

**Branch 4090000 Parks | Ledger 26SLACT | FY26 periods 1-12 | Prepared 11-Jun-2026 | Overall RAG: AMBER**

## Verdict

The account reconciles to the cent but does not clear. $236,378.27 of accumulated actuals across 114 lines and 23 cost codes reconciles exactly to the SE2 enquiry. Six findings are open, the largest being a $5,635 double-posted recode onto PK000022 and approximately $98,005 of contract spend that arguably belongs on 73212 Major Contracts. No line carries sighted Tier 1 evidence in this session, so the evidence and tax limbs are AMBER on every line. No recode dollar is populated and no GENJNL is prepared; findings await Spero's instruction.

## Account reconciliation

| Source | Lines | Total ex-GST |
|---|---|---|
| Full branch export (100221.018) | 114 | $236,378.27 |
| SE2 26SLACT Accum Act p1-12, NA 73211 | n/a | $236,378.27 |
| Variance | | $0.00 |

Section subsets verified as strict row subsets of the full export:

| Section export | Lines | Total | SE2 section row |
|---|---|---|---|
| 100210.102 (Natural Areas) | 42 | $116,963.24 | 4090220 = $116,963.24 |
| 100158.294 (Depots, svc 20151) | 15 | $23,626.58 | 4090210 = $23,626.58 |

Composition: 93 PUR Cred Invoices, 17 general journal lines, 3 creditor credit notes, 1 PCard expense. Internal nettings recomputed: cost code 20001 nets $0.00, 20141 nets $0.01 (the RL195364 variance line), 20261 nets $0.00.

## Findings

### Finding 1. $5,635 double-posted to PK000022 via GJ079190 and GJ079210 (both 6-May-2026)

The underlying cost is one invoice, INV-5888 dated 17-Jan-2026, $5,635 ex-GST ($6,198.50 incl GST), Playforce asset condition assessments, originally coded 1-20261-73211 work order PK000511.

| Journal | Leg | Amount | Reading |
|---|---|---|---|
| GJ079210 | 1-20261-73211 / WO PK000035 | -$5,635 | Correct source credit, clears the invoice off 20261 |
| GJ079210 | 1-20392-73211 / WO PK000022 | +$5,635 | Destination debit |
| GJ079190 | 1-20392-73211 / WO PK000511 | -$5,635 | Credits a leg that never held the cost |
| GJ079190 | 1-20392-73211 / WO PK000022 | +$5,635 | Second destination debit, the duplicate |

Net effect: PK000022 carries $11,270 for a $5,635 invoice, and 20392/PK000511 carries a phantom credit of $5,635. Each journal nets $0.00 within the account and passes the 40-character narration cap, which is precisely the silent-cancellation failure mode the GENJNL direction check exists to catch. Both narrations read "Timber Treatment (PK000510)", which describes neither the Playforce invoice nor any PK appearing on either journal. The proposed remedy is a full reversal of GJ079190; GJ079210 stands. Held for instruction.

### Finding 2. Above-threshold contract spend on a below-$20,000 account, approximately $98,005

The Chart of Accounts is unambiguous: 73211 covers contracts whose total value is below $20,000; 73212 Major Contracts covers $20,000 or above, and the confusion-pair guidance defaults to 73212 where total value is in doubt. Three candidates:

1. **LCC31326, $25,848.08 ex-GST** (period 10, 1-20591-73211, PK000376, "Quote LCC31326"). A single invoice above the threshold on its own face.
2. **Destination Trails Pty Ltd (DES028) series, $43,114 ex-GST**: INV-0352 $23,120 (Quote Q.0249), INV-0354 $17,250 and INV-0355 $2,744 (both Quote Q.0250), across PK000376 and PK000381. The related split pair GJ078945 and GJ079117 was recomputed: each nets $0.00, directions are correct, and the final split of INV-0352 ($15,000 on 20591, $8,120 on 20641) sums to the invoice.
3. **Chronicle standing order series, $29,042.45 ex-GST FY26** (1-20451-73211, PK000083): INV-0785 $480, INV-0856 $2,950, INV-0868 $5,812.45, INV-0873 $19,800. The series total, and arguably INV-0873 alone, puts the contract above threshold.

Recode candidates to 73212 pending contract documents (total contract value is the test, and it ought to be confirmed from the contract or standing order, not inferred from the ledger). No recode dollar populates without Tier 1 sighting.

### Finding 3. Training and equipment items on a contracts account

- **PRINCE2 Agile course, $2,440** (DOC0079602, period 9, 1-20191-73211, PK000082, attendee Duen Jaemjamrat). Still on 73211. Candidate recode to 73544 Training & Development.
- **PSIA Playground Safety Training $4,300, IPWEA Professional Certificate AMP $2,788, Jemma High Back Typist Chair $370.05** (all 1-20141-73211, PK000086). Reversed off 73211 by GJ078546 at exactly -$7,458.05 (arithmetic verified). The chair is a 72313 Furniture & Fittings item per the equipment rule; the training items are 73544 candidates. The destination legs sit outside this export, so where they landed is unverified. The GJ078546 narration on this leg reads "Consulting Pty Ltd", which describes none of the three items.

### Finding 4. GJ078546 (12-Mar-2026) destination legs unverified, and one inbound query

- Reverses $11,098.91 off 1-20001-73211 (Parks WHS Gap Analysis $2,132.63 plus Phase 1 Strategic Workshop $8,966.28, sum exact). Destination unknown from this export; both read as consultancy and the 73600-series is the likely landing, to be confirmed.
- Brings +$2,050 onto 73211 at 1-20451-73211, PK000402: Provac INV-00037183 reversal, grave dig in rock 8-Aug-2025 with dock hire. Plant hire for grave digging sitting on Minor Contracts is a classification query; 73123 Maintenance Services or a plant hire account are the alternatives.

### Finding 5. Depots attribution query, minor

SC10918 creditor credit note, -$154, period 11, "OLD PLAQUES RETURNED FOR S", coded 1-20151-73211 PK000001 (Depots). Plaques are a cemeteries item (svc 20451). The credit ought to follow the account that took the original charge; the original purchase line is not in this account's listing, so the trail starts with AP.

### Finding 6. Advisory only

RL195364 carries a $0.01 "variance" line (period 8, 20141). Immaterial, noted for completeness, not blocking.

## Line verification status

All 114 lines were read, including every Details narration. The four-limb status at account level:

| Limb | Status | Basis |
|---|---|---|
| 1. Service / PK | AMBER | Vendor lines map to valid Parks service codes per svc_map; the PK000511/PK000022/PK000035 work-order tangle in Finding 1 and the SC10918 attribution in Finding 5 are open |
| 2. Natural account | AMBER | Findings 2, 3 and 4 are open classification questions totalling approximately $102,495 |
| 3. Evidence | AMBER | No 73211 source invoice sighted this session. TechOne attachment flags are present on all lines but flags are not sighting. Missing documents are listed in the evidence gap list below |
| 4. Tax compliance | AMBER | Cannot run without sighted invoices |

## Evidence gap list (documents required before limbs 3 and 4 can clear)

Material lines first, by descending value: LCC31326; INV-0352; INV-0873; INV-0354; INV-5747 ($11,105.10, Upgrade Power Mains, 20151); INV-13157 ($8,966.28, Strategic Workshop); TBM 00097461 ($7,344.11); Ausecology INV-4029 and INV-4030 ($8,480 and $6,360, via GJ078960); INV-5888; INV-0856; INV-0868; INV-0087 ($12,800, 20317); 2908705 ($17,000, 20392); INV-0355; 00001400 (PSIA $4,300); 18970 ($3,800 tree removal, 20521); 39657 (IPWEA $2,788); INV-251010(2) ($2,132.63); DOC0079602 ($2,440); INV-38877 ($2,250); plus the standing order series invoices (2906937 onward, 49359879 series, 000590xx/000310xx/000606xx series), EWN INV-14566 and INV-14768, Provac INV-00037183, TBM 00097583/00097626/00097780, IAS21464, 27168, 698933AU, 713170AU, 8171/01366214, 3222869, 3223657, 3223717, 3223786, 9016, INV-1917, 00735, SC10918, TE004838, 34828, 2/9016 quote backups, 00001394 and the GJ078546 source bundle. Every journal line requires its own sighted document; no limb clears off a subset.

## Notes

GL amounts are ex-GST throughout; multiply by 1.1 to reconcile to invoices. GST errors found this session: nil; the GST Errors Register takes no entry. Per the standing directive of 9-Jun-2026 no email issues from this review; all actions live in the register and 00_Outstanding_Evidence_and_Actions.md.

## Addendum, 11-Jun-2026 (intake C00228240: 43 evidence documents sighted, $157,051.42 of the account now evidenced; six classification candidates raised; F1 instruction email sighted; F5 and F6 closed)

The C00228240 intake (56 files) was triaged in full. Every invoice reconciles to its ledger line to the cent on the GL ex-GST x 1.1 test. Canonical copies are filed in NA73211_Evidence/ with SHA-256 fingerprints in NA73211_Evidence_Manifest.csv; the evidence limb moves from zero lines sighted to $157,051.42 of $236,378.27 (66.4% of account dollars). All ABN checksums PASS (18 suppliers). The remainder of the gap list is restated in the manifest GAP rows.

**Sighted and reconciled exactly (GL ex x 1.1 = invoice incl):**
- INV-5747 Reactive Generators $11,105.10 / $12,215.61 (PO 711136; Parks Depot generator repower, after-hours).
- LCC31326 INCON Solutions T/A Edenstone Masonry NQ $25,848.08 / $28,432.89 (200 rock armour stormbreakers, pallets, freight ex Townsville; attention Peter Salinsnew). ABR SIGHTED 11-Jun-2026: ABN active from 14-Nov-2023, GST registered from 29-Apr-2024, business name Edenstone Masonry NQ from 25-Jul-2024, QLD 4811 - entity and trading name match the invoice; GST $2,584.81 = 10% exact. NOTE-tier concerns, not blocking: young entity, C.O.D. with 50% deposit demand, cashless terms. Classification note: this is a materials supply, not a contract service; the F2 contract-floor question on this line is arguably a stores/materials question instead.
- Destination Trails INV-0352 $23,120.00 / $25,432.00 (PO 715300, Q.0249 Horseshoe Loop), INV-0354 $17,250.00 / $18,975.00 (PO 715302, Q.0250 Bahrs Scrub), INV-0355 $2,744.00 / $3,018.40 (extras, Billabong Trail). The F2 Destination Trails series total $43,114.00 is now fully evidenced. The Document Reconstruction (filed in Related/) shows $15,000 of INV-0352 moved 20591 to 20641 on 15-Apr-2026.
- INV-0087 Firesight $12,800.00 / $14,080.00 (PO716210). NEW CANDIDATE: the scope is a bushfire risk analysis with mitigation-option assessment - written report, recommendations, new concepts for Council judgement; the four-element consultancy test reads as met. 73601 candidate (raised alongside F2/F3, held for ruling).
- INV-5888 Play Force $5,635.00 / $6,198.50 (PO 713687, asset capture small/medium/large $1,505 + $1,890 + $2,240). Confirms the F1 quantum and the line content (Playforce asset capture, not timber treatment).
- Chronicle Rip series, fully evidenced at $29,042.45: INV-0785 $480.00 (map edits, Beenleigh monumental s5), INV-0856 $2,950.00 (aerial imagery, Maclean and Eagleby), INV-0868 $5,812.45 (software licence renewal, 7 cemeteries, 12 months from 1-Jan-2026), INV-0873 $19,800.00 (360 mapping, four cemeteries). NEW CANDIDATES: INV-0868 is a software subscription (73566 candidate, mirroring the 73564 ruling); the mapping/imagery items are arguably survey services. Cemeteries content on svc 20451 throughout.
- GJ078960 leg EWN invoice 14566 $75.00 / $82.50 (planned-burns notifications, Aug-2025). EWN INV-14768 remains a GAP.
- 27168 Tennyson Group $1,058.00 / $1,163.80 (PO 713717, Quote 43084: "Too Wet to Mow" corflute signs x6). NEW CANDIDATE: printed signage, 72222 per the standing Tennyson decals ruling.
- INV-1917 CAASie $3,363.00 / $3,699.30 (QU-0080/PO714242; the invoice is addressed to Corporate Communications). Content query: CAASie is digital-billboard advertising; classification and ownership to confirm.
- 18970 RST Systems $3,800.00 / $4,180.00 (PO 712547, attention Celeste Fry; ledger narration Tree removal).
- IAS21464 Independent Arboricultural Services $800.00 / $880.00 (PO 715410, contact Lee-Anne Niblett).
- 39657 IPWEA $2,788.00 GL / invoice $3,100.00 ex + $310.00 GST less $343.20 payment received = $3,066.80 due, EXACT. The invoice document gap closes (this also evidences the 73544/GJ078546 IPWEA leg); the $343.20 prior-payment posting trace remains, now characterised as $312.00 ex + $31.20 GST.
- 00001400 PSIA $4,300.00 / $4,730.00 (ref 714723; Playground Safety Training 24-25 Feb-2026, Fiona Perry and Kerrie Ford; ABN 63 631 848 729). The F3 PSIA leg content is confirmed training; 73544 destination candidate stands.
- RL195364 Empire Office Furniture $370.05 + $0.01 / $407.06 (Jemma chair, Cust Ref 714591, Julie Villiers, delivered Parks Depot). F6 CLOSED: the $0.01 variance line is the supplier's GST rounding cent (GST $37.01 on $370.05). The chair remains the 72313 candidate.
- DOC0079602 DDLS T/A Lumify $2,440.00 / $2,684.00 (PO715104, PRINCE2 Agile Foundation, Duen Jaemjamrat, 23-Mar-2026). F3 confirmed training; 73544 candidate stands.
- SC10918 Worssell -$154.00 / -$169.40 credit (17kg old plaques returned for scrap, 7-May-2026). F5 CLOSED as a trace: the credit is scrap income. NEW CANDIDATE: scrap income does not belong in an expense account; 64411 Cemeteries candidate, mirroring the standing 72111 scrap ruling, and the cemeteries attribution question (plaques; credit sits on Depots PK000001) stands for the same ruling.
- TE004838 Message Media $242.40 / $266.64 (Sinch MessageMedia INV05480153, 23-Sep-2025, bulk SMS re tree requests; requesting officer Ngametua Ruatoe, cardholder Craig Logan). NEW FINDING F7: the credit-card cover slip codes PK000055-73212; the line posted to 1-20241-73211. Coding mismatch held for ruling (the SMS content is arguably neither account).
- Lockwise Locksmiths, ten invoices on the 1-20392-73211 standing order (PO 709747), all exact: 2907532 $121.30, 2907801 $302.50, 2908018 $130.50, 2908241 $182.00, 2908351 $206.00, 2908470 $176.50, 2908632 $85.00, 2908653 $159.00, 2908664 $251.00, 2908883 $301.00 ($1,914.80 total). The series opener 2906937 ($10,200.00) is NOT Lockwise-scale and remains a GAP, as does 2908705 ($17,000.00).
- T2 Electrical 3223657 $3,060.00 / $3,366.00 and 3223717 $378.00 / $415.80 (job 2221939, Parks Depot; invoices show Order 802502, reallocated to PO 714635 per the Aisha Wilson to AP email of 3-Feb-2026, approved Kirsty Quinn, filed in Related/). T2 3222869 ($480.00) and 3223786 ($1,340.00) remain GAPs.
- Telstra account 493 5987 935 (PA - Parks), ten of eleven monthly bills sighted against the 49359879-series: Jul-25 $968.07/$1,064.88, Aug-25 $640.73/$704.80, Sep-25 $1,048.22/$1,153.04, Oct-25 $905.61/$996.17, Nov-25 $910.85/$1,001.93, Jan-26 through May-26 $807.21/$887.93 x5. All exact on the /1.1 basis. Dec-25 ($727.95 / $800.75) remains the GAP. GST advisory: AP books ex-GST as incl/1.1 while Telstra discloses actual GST (mixed GST-free content) - Oct-25 disclosed $90.46 vs $90.56 claimed (+$0.10 over-claim), Nov-25 disclosed $91.19 vs $91.08 (-$0.11 under). Cents-level, both directions; recorded as a pattern entry on the GST Errors Register (GSTE-28), no GENJNL. Classification query: a branch telephone account is arguably telecommunications, not Minor Contracts; held with the candidate set.

**F1 instruction email sighted (filed in Related/).** Gihani MandalaWaththage to Spero, 6-May-2026, "Journal Please": transfer the attached transactions PK000510 to PK000023 and PK000511 to PK000022. GJ079190 and GJ079210 (both 6-May-2026) each posted to PK000022. Read against the instruction, the PK000510 batch belonged to PK000023; GJ079190 (narrated "Timber Treatment (PK000510)") posting $5,635 to PK000022 is therefore either the PK000510 batch misposted to the wrong destination or a straight duplicate of GJ079210. Either way the F1 reversal candidate stands, now with the originating instruction in evidence; the correct destination on any re-post (PK000023 versus none) is part of the ruling. This also explains PK000510/PK000511: work-order pseudo-PKs Gihani asked to clear, not service-map entities.

**Tax limb position.** GST math reconciles exactly on every sighted document. ABN checksums PASS on all eighteen suppliers. ABR sighted for INCON (above) and previously for IPWEA. ABR sightings for the remaining suppliers are queued (Destination Trails, Firesight, Reactive Generators, Chronicle Rip, Play Force, RST, CAASie, Tennyson, T2, Lockwise, IAS, PSIA, DDLS, EWN, Worssell, Empire, Telstra, Message4U); the tax limb stays AMBER on that residual and the unsighted lines.

**Play Force AP-ledger context (filed to sources).** The intake's AP ledger export (account PLA073, Play Force, ABN 89 677 476 541) lists 29 further invoices INV-7594 to INV-7733, P11-P12, $97,347.39 - relevant to the F2 contract-floor question on the Play Force engagement and to the 73212 Play Force series; archived under _Sources_11-Jun-2026/C00228240_intake/ for the floor test.

**Limb position after this addendum.** L1 AMBER (F1/F7 PK questions open, otherwise unchanged). L2 AMBER (candidate set now F2/F3 plus Firesight 73601, Chronicle 73566/survey, Tennyson 72222, SC10918 64411, Telstra telecoms, TE004838, INCON materials). L3 AMBER, narrowed from $0 to $157,051.42 sighted; gap rows restated in the manifest. L4 AMBER (math exact on sighted; ABR queue and unsighted lines). Overall AMBER. No recode dollar populated; everything held for Spero's rulings per the standing directive.
