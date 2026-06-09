# NA73564 IT Equipment & Applications — Verification Record

Batch CN-23167. Section 4090000, FY26 (26SLACT), OP O110, Period 1 to 12. Source: TechOne Ledger Accounts Transactions Table, export 9-Jun-2026 (36 lines). Reviewed 9-Jun-2026.

**Overall RAG: AMBER. Account does not close.**

The account reconciles to **$43,393.37 ex-GST** across 36 lines and 9 service codes. This is the full 73564 account: the $1,929.27 Celeste Fry line carried at the 8-Jun pass plus the $41,464.10 remainder that was an open scope question. The remainder is now in scope and reviewed.

## Account reconciliation

- Lines: 36. Sum of Transaction Amount: **$43,393.37 ex-GST**.
- Notional gross-up (ex x 1.1): $47,732.71. Note most spend is internal IT recharge (IJ/GJ); GST was handled at the original AP layer, so the gross-up is reconciling-only.
- Document mix: 20 named-employee IT adhoc recharges (IJ/GJ/SR), 6 software licence/subscription lines, 5 "Single Incident Support" hardware break-fix lines, 2 bulk Apple fleet invoices (INV-13660, INV-17543), 1 variance ($0.01), 2 OtterBox case lines.

## Four-limb result

| Limb | RAG | Basis |
|---|---|---|
| 1 Service / PK | AMBER | 11 of 20 recharge lines sit at the officer's substantive home PK; 9 do not ($4,416.27). Three of the nine are now confirmed by Spero directive (9-Jun) and staged as net-moves: L04 Robertson 20151->20319 ($30), L25 Dressman 20191->20001 ($500), L33 Fry 20241->20151 ($1,929.27), total $2,459.27. Six remain open ($1,957.00), all Anne-Marie King bar L11 Lilly Shearman, including the likely Anne-Marie / Caroline King name-attribution issue. IT-recharge allocation convention now set to officer home PK for the confirmed set. |
| 2 Natural account | AMBER | IT equipment lines correct in 73564. Six software licence/subscription lines ($1,822.45) belong in 73566 IT Software Licence Fees per the chart and the P10 Canva/VisitUs precedent. Held pending Finance acceptance. |
| 3 Evidence | AMBER | Esri INV000555 and both bulk Apple invoices (INV-13660, INV-17543) sighted and reconciled. Gaps: SEVEN internal-recharge lines carry no attachment ($6,689.87) pending SR backup (L06 SR-0316577, L08 SR-0315241, L11 SR#204868, L15 SR-0312575, L20 SR#201404, L33 SR-0315517, L34 SR#200930); and five external-supply refs (2412569490, INAU004378, GJ076194, GJ075813, TE005499) not yet sighted. |
| 4 Tax | AMBER | Three external invoices COMPLIANT (Esri INV000555; Exceed ICT INV-13660 and INV-17543). FIVE external-supply refs not yet sighted and tax-unverified: 2412569490 Single Incident Support ($522.76), INAU004378 license bundles ($474.00), GJ076194 and GJ075813 Body2 software ($372.00 each), TE005499 Anthropic ($36.14). Internal recharges N/A. |

**GST status (Limb 4, per-line).** Internal IJ/GJ/SR recharges are N/A: GST was settled at the original AP layer, so the x1.1 gross-up is reconciling-only and no credit is claimed here. For the external lines the booked-to-document GST check is the live risk: overseas digital suppliers may be GST-free imported services carrying no Australian GST, so any booked input tax credit must be verified against an Australian tax invoice before it stands. Anthropic (TE005499) is the clearest case, with Esri and the Body2 GJ lines to confirm on sighting. Esri INV000555 and both Exceed ICT invoices reconcile; the five unsighted external refs are GST-unverified. GST status AMBER.

## Findings

### 1. Software licence / subscription miscoded to 73564 — recode to 73566 ($1,822.45, AMBER)

Six lines are software licence or subscription fees and belong in **73566 IT Software Licence Fees**, not 73564 IT Equipment & Applications. The chart draws the line cleanly ("IT software licence fees" vs "IT purchases"), and the P10 review set the precedent by recoding Canva Pro and VisitUs SaaS into 73566. The 73564 name carries the word "Applications", which is the only thing creating doubt; there is no documented confusion pair, so the move is put to Finance rather than posted unilaterally.

| Line | Item | Ref | $ ex-GST | Transacted PK | Recode |
|---|---|---|---|---|---|
| L05 | Anthropic Claude Team | TE005499 | 36.14 | PK000087 | 73564 -> 73566 |
| L09 | Basic License Bundle | INAU004378 | 132.00 | PK000084 | 73564 -> 73566 |
| L17 | Pro License Bundle | INAU004378 | 342.00 | PK000084 | 73564 -> 73566 |
| L18 | Body2 Cameras annual sub | GJ076194 | 372.00 | PK000001 | 73564 -> 73566 |
| L19 | Body2 Cameras annual sub | GJ075813 | 372.00 | PK000001 | 73564 -> 73566 |
| L29 | Esri ArcGIS Online Creator | INV000555 | 568.31 | PK000068 | 73564 -> 73566 |

- **Body2 lines (L18, L19) flagged within the recode.** These are correct monthly recognition of a multi-year Body2 subscription (known trap: 3-year subscription, $372/month GJ recognition, not a new charge each month). They are not duplicates. Finance may elect to leave the established Body2 recognition stream in 73564 rather than move an in-flight multi-year sub; the recode stages them but the email asks the question.
- **PKs preserved as transacted.** Only the natural account moves; each line keeps its existing PK. Full-reversal format (NA wrong). Batch nets $0.00, all narrations within the 40-character cap, all PK/service/account combinations validate as unrestricted.

### 2. IT-recharge PK attribution — 9 lines off the officer's home section ($4,416.27, AMBER)

Of 20 named-employee recharge lines, 9 sit at a service/PK other than the officer's substantive home cost centre:

| Line | Officer | Home svc/PK | Charged svc/PK | $ ex-GST |
|---|---|---|---|---|
| L04 | Brenda Robertson (Trees) | 20319 / PK000433 | 20151 / PK000001 | 30.00 |
| L08 | Anne-Marie King (Planning) | 20141 / PK000086 | 20191 / PK000082 | 80.00 |
| L11 | Lilly Shearman (Planning) | 20141 / PK000086 | 20001 / PK000087 | 195.00 |
| L12 | Anne-Marie King (Planning) | 20141 / PK000086 | 20001 / PK000087 | 195.00 |
| L21 | Anne-Marie King (Planning) | 20141 / PK000086 | 20001 / PK000087 | 438.00 |
| L24 | Anne-Marie King (Planning) | 20141 / PK000086 | 20191 / PK000082 | 500.00 |
| L25 | Sara Dresman (Management) | 20001 / PK000087 | 20191 / PK000082 | 500.00 |
| L28 | Anne-Marie King (Planning) | 20141 / PK000086 | 20001 / PK000087 | 549.00 |
| L33 | Celeste Fry (Depots) | 20151 / PK000001 | 20241 / PK000055 | 1,929.27 |

- **Three attributions confirmed by Spero directive (9-Jun-2026); net-moves now staged in sub-batch B.** L04 Brenda Robertson (Trees) iPhone $30 wrongly on Depots 20151/PK000001, moves to her Trees home 20319/PK000433. L25 Sara Dressman (Branch Management) Poly headset $500 wrongly on Planning 20191/PK000082, moves to 20001/PK000087. L33 Celeste Fry (Depots) iPhone $1,929.27 wrongly on Trees 20241/PK000055, moves to 20151/PK000001 (the 8-Jun confirmed cross-section miscode, now released). All three are net-movement recodes, NA 73564 unchanged, batch nets $0.00. Limb 1 (attribution) is now cleared on these three; their Limb 3 evidence (SR219175, SR235810, SR-0315517 backups) is still unsighted.
- **Anne-Marie King carries 5 of the 9 and never appears on her home 20141.** That pattern is either deliberate support-team allocation or systemic recharge misattribution; it cannot be resolved from the ledger. Two of her lines (L08, L24) sit on svc 20191 / PK000082, which is the substantive PK of a different officer, **Caroline King** — a probable name-attribution issue in the IT recharge feed.
- **Three net-moves staged, six still open.** The IT-recharge allocation convention (officer home PK vs supported-team PK) is not documented in any installed skill, but Spero has now set it to officer home PK and confirmed three officers (Robertson, Dressman, Fry), so those net-moves are staged in sub-batch B of the held recode. The remaining six lines ($1,957.00, five Anne-Marie King plus L11 Lilly Shearman) stay open pending the same confirmation, and the L08/L24 Anne-Marie vs Caroline King name-attribution question still has to be resolved before those two move. `lcc-split-pk-recode` is still not installed; the convention is now directive-set rather than derived.

### 3. Evidence gaps — internal recharges with no attachment ($6,260.87, AMBER)

Seven IJ recharge lines carry no attachment: L06 ($45), L08 ($80), L11 ($195), L15 ($250), L20 ($429), L33 ($1,929.27), L34 ($3,761.60), totalling $6,689.87. Internal recharges are substantiated by the IT Service Request (SR) record (SR-0316577, SR-0315241, SR#204868, SR-0312575, SR#201404, SR-0315517, SR#200930). Separately, five external-supply refs (2412569490 Single Incident Support, INAU004378 license bundles, GJ076194/GJ075813 Body2 software, TE005499 Anthropic) have attachments in TechOne but have not been sighted; their evidence and tax limbs are unverified until inspected.

### 4. Quantum query — L34 Leanne Ness Wilson iPhone ($3,761.60, AMBER)

L34 narrates a single "Apple iPhone 16 Pro, Case & screen protector" at $3,761.60 ex-GST, roughly double the comparable Fry line (L33, $1,929.27) for the identical description. No attachment. Query whether this is two devices, a bundle, or a quantum error before any recode.

### 5. Bulk Apple fleet and Single Incident Support — correct in 73564 (advisory)

- **L35/L36 bulk Apple invoices NOW SIGHTED (Exceed ICT INV-13660 and INV-17543), both COMPLIANT tax invoices and reconciling exactly to the ledger.** They resolve to 8x iPad Air 11 (M3) 256GB @ $1,317.27 ex-GST and 10x iPad Air 13 (M4) 256GB @ $1,635.45 ex-GST, plus matched OtterBox cases, with 18 IMEI serials listed. Each unit is well below any capitalisation threshold, so expense treatment in 73564 is confirmed correct. **Advisory: list the 18-unit iPad fleet (IMEI serials on the invoices) on the Portable & Attractive register.** `lcc-asset-accounting` is not installed; the threshold should still be confirmed.
- **Single Incident Support (L02, L03, L07, L10, L16, $522.76):** cables, daughterboard, battery, onsite labour — IT hardware break-fix, correct in 73564.
- **L01 $0.01 "variance":** rounding, immaterial.

## Held recode

`NA73564_GENJNL_Recode.txt` — 18 lines in two sub-batches, batch nets $0.00, all narrations within 40 characters, all combinations validate unrestricted. Sub-batch A: 12 lines, NA 73564 -> 73566 full-reversal on the six software lines, PKs preserved, held pending Finance acceptance of the 73564 -> 73566 move (and the Body2 question). Sub-batch B (added 9-Jun): 6 lines, three net-movement PK attribution recodes (Robertson, Dressman, Fry, $2,459.27), NA 73564 unchanged, attribution confirmed by Spero, held only on the SR-backup evidence sighting. The remaining six off-home lines (Finding 2) are still not staged; they await confirmation.

## Open actions (to the consolidated Finance email)

1. Accept the 73564 -> 73566 recode of the six software licence/subscription lines ($1,822.45); confirm whether the in-flight Body2 monthly recognition (L18, L19) is moved or left in 73564.
2. PK allocation convention set to officer home PK by Spero (9-Jun). Three lines confirmed and staged (Robertson 20151->20319, Dressman 20191->20001, Fry 20241->20151, $2,459.27); six remain open ($1,957.00, five Anne-Marie King plus L11 Lilly Shearman) pending the same confirmation.
3. Sight the SR backups behind the three staged net-moves (SR219175 Robertson, SR235810 Dressman, SR-0315517 Fry) to clear their evidence limb; attribution is already confirmed.
4. Resolve the Anne-Marie King / Caroline King attribution on L08 and L24 (svc 20191 / PK000082) before those two lines move.
5. Provide SR / IT recharge backup for the six no-attachment lines; sight the two bulk Apple invoices INV-13660 and INV-17543 for the evidence and tax limbs.
6. Query L34 quantum ($3,761.60 single-device narration).
7. Advisory: confirm asset-capitalisation threshold and add the iPad/iPhone fleet to the P&A register.
