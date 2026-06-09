# NA 72111 Minor Equipment & Supplies, Reconciliation Note (account held)

Reviewed 9-Jun-2026. Section 4090000, FY26 (26SLACT). Account balance $67,055.47 ex-GST (SE2).

Verdict: AMBER, not closeable. Two separate review passes exist for this account and they overlap, so they cannot be summed. One RED blocker (TE005091) remains open. The account stays held in CN-23167 and reconciliation to 100% is not yet achievable.

## Two populations, partially overlapping

- Pass 1, AP-invoice review (8-Jun register row). $3,433.91 across five AP creditor and stock lines, $2,260.36 miscoded. Tennyson vehicle stickers $335.00 to 72222, Ultimate PPE trousers and pants $694.68 to 72113, serial-numbered STIHL GTA 40 $439.68 to 72315, INITIATOR insecticide and fertiliser $791.00 to 72112.
- Pass 2, Doc46 journal-document audit (3-Jun, carried in `_CarryForward/72111_Doc46_Audit_source.xlsx`). 93 lines recoding $22,391.77 off 72111 (or $22,028.13 net of the held J12 riser line) across eleven destinations: 72113 $5,149.09, 72311 $4,286.05, 72249 $2,942.24, 73211 $1,707.25, 72112 $1,613.37, 72231 $1,409.84, 73220 $1,383.29, 72248 $1,360.00, 72315 $1,250.00 (Petersen Castings cemetery monument material), 72222 $927.00, 72313 $363.64 (the J12 risers, held).

## The overlap

The two passes are not disjoint. Tennyson Group reference 27577, $335.00, svc 20241 PK000055, recode 72111 to 72222, appears in both the 8-Jun AP review (line L02) and Doc46 (line J22). Posting both would double-count the relocation. Any merged 72111 recode must dedupe the overlapping transactions before posting; Tennyson 27577 is the confirmed overlap and the full line-by-line dedupe across the 93 Doc46 lines and the five AP lines has not been completed.

## The RED blocker (TE005091)

Doc46 line J12 recodes twenty desk risers $363.64 from 72111 to 72313. The same risers are already split in the PCard batch recode of Officeworks invoice 626529478. Booking both double-counts the riser relocation, so J12 was removed from the consolidated journal and stays removed unless TE005091 proves to be a separate purchase. Confirm with Finance whether TE005091 is the riser line of invoice 626529478.

## Why the account does not close

The standing standard verifies each account to 100% before close. The two passes together touch roughly $25,825 of the $67,055 balance; the remainder (ecology fuel-reduction already reversed by GJ078960, stores issues, standing orders, over-threshold one-offs) is untested. Closing 72111 requires: the population dedupe, the TE005091 resolution, and the open Finance confirmations carried on the 8-Jun register (PPE 72113 versus 72114, STIHL asset threshold and P&A register, 72222 for printed decals, INITIATOR stores item).

## Open actions

1. Resolve TE005091 (riser line of inv 626529478, or separate purchase). Sets whether J12 re-enters the batch.
2. Dedupe the Doc46 and AP-invoice populations before any 72111 recode posts. Tennyson 27577 confirmed in both; complete the full line match.
3. Carry the 8-Jun Finance confirmations (PPE destination, STIHL threshold, decal account, INITIATOR) into the consolidated Finance email.
