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
| 1 Service / PK | AMBER | 11 of 20 recharge lines sit at the officer's substantive home PK; 9 do not ($4,416.27). Includes the confirmed Fry cross-section miscode and a likely Anne-Marie / Caroline King name-attribution issue. IT-recharge allocation convention is undocumented and must be confirmed. |
| 2 Natural account | AMBER | IT equipment lines correct in 73564. Six software licence/subscription lines ($1,822.45) belong in 73566 IT Software Licence Fees per the chart and the P10 Canva/VisitUs precedent. Held pending Finance acceptance. |
| 3 Evidence | AMBER | Esri INV000555 and both bulk Apple invoices (INV-13660, INV-17543) sighted and reconciled. Gaps: SEVEN internal-recharge lines carry no attachment ($6,689.87) pending SR backup (L06 SR-0316577, L08 SR-0315241, L11 SR#204868, L15 SR-0312575, L20 SR#201404, L33 SR-0315517, L34 SR#200930); and five external-supply refs (2412569490, INAU004378, GJ076194, GJ075813, TE005499) not yet sighted. |
| 4 Tax | AMBER | Three external invoices COMPLIANT (Esri INV000555; Exceed ICT INV-13660 and INV-17543). FIVE external-supply refs not yet sighted and tax-unverified: 2412569490 Single Incident Support ($522.76), INAU004378 license bundles ($474.00), GJ076194 and GJ075813 Body2 software ($372.00 each), TE005499 Anthropic ($36.14). Internal recharges N/A. |

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

- **L33 Celeste Fry is the confirmed cross-section miscode** carried from the 8-Jun pass: Depots officer, iPhone charged to Trees (svc 20241 / PK000055). Net-movement recode PK000055 -> PK000001 (NA unchanged), held pending confirmation of Fry's attribution (override-acting, pending separation, cutover 05-Jun-2026, both positions map to PK000001).
- **Anne-Marie King carries 5 of the 9 and never appears on her home 20141.** That pattern is either deliberate support-team allocation or systemic recharge misattribution; it cannot be resolved from the ledger. Two of her lines (L08, L24) sit on svc 20191 / PK000082, which is the substantive PK of a different officer, **Caroline King** — a probable name-attribution issue in the IT recharge feed.
- **No PK recode is posted.** The IT-recharge allocation convention (officer home PK vs supported-team PK) is not documented in any installed skill. `lcc-split-pk-recode` and `lcc-asset-accounting` are not installed; the home-PK convention is exactly the logic the split-PK skill would carry, so it is derived and flagged, not asserted. The whole set goes to Finance as one convention question; if the convention is "home PK", net-movement recodes follow.

### 3. Evidence gaps — internal recharges with no attachment ($6,260.87, AMBER)

Seven IJ recharge lines carry no attachment: L06 ($45), L08 ($80), L11 ($195), L15 ($250), L20 ($429), L33 ($1,929.27), L34 ($3,761.60), totalling $6,689.87. Internal recharges are substantiated by the IT Service Request (SR) record (SR-0316577, SR-0315241, SR#204868, SR-0312575, SR#201404, SR-0315517, SR#200930). Separately, five external-supply refs (2412569490 Single Incident Support, INAU004378 license bundles, GJ076194/GJ075813 Body2 software, TE005499 Anthropic) have attachments in TechOne but have not been sighted; their evidence and tax limbs are unverified until inspected.

### 4. Quantum query — L34 Leanne Ness Wilson iPhone ($3,761.60, AMBER)

L34 narrates a single "Apple iPhone 16 Pro, Case & screen protector" at $3,761.60 ex-GST, roughly double the comparable Fry line (L33, $1,929.27) for the identical description. No attachment. Query whether this is two devices, a bundle, or a quantum error before any recode.

### 5. Bulk Apple fleet and Single Incident Support — correct in 73564 (advisory)

- **L35/L36 bulk Apple invoices NOW SIGHTED (Exceed ICT INV-13660 and INV-17543), both COMPLIANT tax invoices and reconciling exactly to the ledger.** They resolve to 8x iPad Air 11 (M3) 256GB @ $1,317.27 ex-GST and 10x iPad Air 13 (M4) 256GB @ $1,635.45 ex-GST, plus matched OtterBox cases, with 18 IMEI serials listed. Each unit is well below any capitalisation threshold, so expense treatment in 73564 is confirmed correct. **Advisory: list the 18-unit iPad fleet (IMEI serials on the invoices) on the Portable & Attractive register.** `lcc-asset-accounting` is not installed; the threshold should still be confirmed.
- **Single Incident Support (L02, L03, L07, L10, L16, $522.76):** cables, daughterboard, battery, onsite labour — IT hardware break-fix, correct in 73564.
- **L01 $0.01 "variance":** rounding, immaterial.

## Held recode

`NA73564_GENJNL_Recode.txt` — 12 lines, NA 73564 -> 73566 full-reversal on the six software lines, PKs preserved, batch nets $0.00, all narrations within 40 characters, all combinations validate unrestricted. Held pending Finance acceptance of the 73564 -> 73566 move (and the Body2 question). The PK recodes (Finding 2) are not staged; they await the convention confirmation.

## Open actions (to the consolidated Finance email)

1. Accept the 73564 -> 73566 recode of the six software licence/subscription lines ($1,822.45); confirm whether the in-flight Body2 monthly recognition (L18, L19) is moved or left in 73564.
2. Confirm the IT-recharge PK allocation convention (officer home PK vs supported-team PK) for the 9 off-home lines ($4,416.27).
3. Confirm Celeste Fry's attribution (override-acting, pending separation) to release the net-movement PK000055 -> PK000001 recode; provide SR-0315517 backup.
4. Resolve the Anne-Marie King / Caroline King attribution on L08 and L24 (svc 20191 / PK000082).
5. Provide SR / IT recharge backup for the six no-attachment lines; sight the two bulk Apple invoices INV-13660 and INV-17543 for the evidence and tax limbs.
6. Query L34 quantum ($3,761.60 single-device narration).
7. Advisory: confirm asset-capitalisation threshold and add the iPad/iPhone fleet to the P&A register.
