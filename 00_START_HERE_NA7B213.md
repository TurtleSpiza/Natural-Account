# 00 START HERE — NA7B213 Internal Medical Services (Immunisation)

Mode A per-account deliverable bundle. Account 7B213, FY26 26SLACT. Prepared 16-Jun-2026.

## Verdict
Immunisation cost for the whole Parks branch is posted to Natural Areas PK000432 because
Internal_Medical.XLSM "Lookup Values" row 23 maps all of 4090000 Parks to one PK. Only 3 of
23 named Parks employees are actually Natural Areas. $3,799.50 of the $4,340.80 Parks total
is reallocated to home-section PKs by the staged recode. Overall RAG AMBER (evidence
unsighted, one name held, off-branch and duplicate items open).

## Numbers
- In scope: $4,861.70 ex-GST, 70 lines, P2 to P12 FY26.
- Reallocated (staged recode): $3,799.50, 17 pairs, net $0.00, source PK000432 credit -$3,799.50.
- Stays on PK000432: $541.30 (James Lloyd-Jones $338.30, Renee Hoyle $82.00 correct; Arno Schneider $121.00 held).
- Off-branch (not Parks): $520.90, of which $146.30 is a duplicate. Cross-branch, needs Finance.

## What is in this bundle
| File | What it is |
|---|---|
| 00_START_HERE_NA7B213.md | This file |
| NA7B213_Verification_Record.md | Four-limb record, reconciliation, register row, RAG |
| NA7B213_GENJNL_Recode.txt | Staged PK split-PK recode, 17 pairs, net $0.00, validated |
| NA7B213_Employee_PK_Mapping.csv | Every named person, branch, amount, source PK, destination, RAG |
| NA7B213_Evidence_Manifest.csv | Per-line evidence register; all UNSIGHTED-GAP this session |
| NA7B213_Held_Items.md | Arno, off-branch, duplicate — flagged, not journalled |
| NA7B213_Offbranch_SL_Reversal_DRAFT.txt | Draft cross-branch reversal, for Finance, not for posting as-is |
| NA7B213_Lookup_Fix_Row23.md | Source fix so the miscode stops recurring |
| NA7B213_Evidence/ | Empty by design; README records the GAP |
| 00_Bundle_Manifest.csv | SHA-256 of every deliverable (raw intake excluded) |
| gen_manifest.py, verify_manifest.py | In-bundle integrity gate |
| _Sources_16-Jun-2026/ | Raw intake (ledger export, working paper). Outside the manifest. |

## Integrity gate (run before any re-zip)
    python gen_manifest.py
    python verify_manifest.py --strict
Strict verify must pass before handback. Raw intake under _Sources_* is deliberately
outside the manifest. __pycache__ is excluded.

## Caveats held honestly
- Limb 3 evidence AMBER: no immunisation IJ backing sighted; recorded as GAP.
- lcc-split-pk-recode not installed; recode built on lcc-coding-review + techone-output + first principles. Mechanics are standard PK reversal pairs.
- Sonya Karlsson PK000012, Christian De Leon PK000084, Gregory Cavell PK000012 are Spero-instructed placements (not on the roster).
- SE2 reconciliation not performed; no account-level GREEN until export ties to SE2 to the cent.

## Next actions
1. Supply Arno Schneider's section to add his pair to the recode.
2. Confirm whether Park Maintenance staff resolve to PK000012 vs PK000003 by substantive position.
3. Hand the SL reversal draft and duplicate query to Finance for the off-branch leg.
4. Fix Internal_Medical.XLSM row 23 to a per-section Parks lookup.
