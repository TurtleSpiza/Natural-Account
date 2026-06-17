# Materials Journal reclassification — PK000372 (Fuel Reduction Burn, svc 20551)

Verification record, 17-Jun-2026. Workstream folder `08_Materials_Recode_PK000372/`.

## What this is

The March Materials variance on the Fuel Reduction Burn service (Natural Areas, svc 20551 / PK000372) was a coding error: Planned Burn contractor invoices were booked to **72111 Minor Equipment and Supplies**, which is restricted to sub-$200 items, instead of the correct contract and water accounts. Gihani MandalaWaththage approved the correction on 16-Apr-2026 ("Please process the journals"); the approval pack is `Materials_Journal_Approval_Gihani_16-Apr-2026.pdf`.

This is an **already-posted** TechOne journal, not a proposal: `Materials_DocReconstruction_XRef934000000001.xlsx` is a Document Reconstruction of posted document `202604161079934000000001`, Ledger 26SLACT, Account 1-20551-73211, Transaction 2. It is therefore **evidenced and verified here, not re-posted** — it does not enter the CN-23167 batch, and the live recode journal is unchanged.

## Arithmetic and direction (verified)

8 pairs, 16 lines, all at PK000372 / svc 20551. **Nets $0.00 exactly** ($42,841.53 debit = $42,841.53 credit). Direction correct on every pair: the source legs (72111 Minor Equipment, 72411 Bulk Water) are credited, the destination legs debited.

| Pair | Invoice | From | To | Amount ex-GST |
|---|---|---|---|---|
| 1 | EMU INV-0367 | 72111 | 73212 Major Contracts | 11,256.00 |
| 2 | EMU INV-0389 | 72111 | 73212 | 14,407.68 |
| 3 | EMU INV-0395 | 72111 | 73212 | 750.40 |
| 4 | Ausecology INV-4030 | 72111 | 73211 Minor Contracts | 6,360.00 |
| 5 | Ausecology INV-4029 | 72111 | 73211 | 8,480.00 |
| 6 | Bushcare INV-18177 | 72411 Bulk Water | 74114 Water Truck | 1,137.45 |
| 7 | EWN 14566 | 72111 | 73211 | 75.00 |
| 8 | EWN 14768 | 72111 | 73211 | 375.00 |
| | | | **Total** | **42,841.53** |

## Evidence status

- **EMU INV-0367 / 0389 / 0395 (the $26,414.08 to 73212):** SIGHTED, source invoices held in `NA_Materials_Evidence/`, GST exact to the cent. These are new sightings; they evidence the 73212 destination legs.
- **Ausecology INV-4029 / INV-4030 and EWN 14566 / 14768 (the $15,290.00 to 73211):** already sighted in the NA73211 evidence manifest (the 72111→73211 legs; the Materials intake supplied confirming copies). The named outstanding GAP "Ausecology INV-4029/INV-4030 ($14,840 via GJ078960)" is closed.
- **Bushcare INV-18177 (the $1,137.45 to 74114):** GAP — the source invoice is not in the bundle. Recorded for audit; the directive does not hold the posted line.
- **Bushcare INV-17401 ($1,050.00, 72111→74114):** appears in the page-2 approval summary but is **not in the posted journal** and has no source invoice. Confirm with Spero whether it is in or out of the batch.

## Verdict

Posted reclassification, directive-authorised, arithmetically and directionally clean. Evidence limb GREEN on the EMU and Ausecology/EWN legs; AMBER on the two Bushcare legs pending the source invoices. No recode dollar is created here — the movement is already in the ledger.
