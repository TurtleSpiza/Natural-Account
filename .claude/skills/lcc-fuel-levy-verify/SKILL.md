---
name: lcc-fuel-levy-verify
description: "LCC Parks decisive verification of supplier fuel levy surcharges against the Council stepped and capped fuel levy model (Fact Sheet DM19338551). Computes Levy = Work_ex_GST x Fuel_Component_% x Fuel_Escalation_%, looks up the Brisbane Diesel TGP for the work date, selects the band, and returns one of seven decisive verdicts (exact match, under-claim, over-claim reject, below-baseline, missing register, missing TGP, stale TGP). Use whenever verifying a supplier invoice with a 'LCC Fuel Levy', 'Fuel Levy Surcharge', or 'Fuel Levy - Diesel' line under any PAR/* contract. Triggers on 'verify fuel levy', 'check fuel surcharge', 'is the fuel levy correct', 'reverse engineer the fuel rate', 'Vinton invoice', 'PAR/329 levy', 'TGP band', 'fuel escalation %'. Distinct from lcc-coding-review and lcc-na-analysis. This skill is single-invoice ceiling verification against the Fact Sheet ruleset."
---

# LCC Fuel Levy Verifier

Decisive single-invoice verification of supplier fuel levy surcharges against the Council Fact Sheet (DM19338551). Computes the ceiling, compares to the charged levy, returns one of seven defined verdicts.

## The formula

```
Levy ($) = Work_ex_GST × Fuel_Component_% × Fuel_Escalation_%
```

| Term | Source | Cadence |
|---|---|---|
| Work_ex_GST | Invoice subtotal ex GST, EXCLUDING the levy line itself | Per invoice |
| Fuel_Component_% | Contract variation letter or schedule, locked per supplier | Locked, only changes on re-variation |
| Fuel_Escalation_% | Stepped band selected by Brisbane Diesel TGP (incl GST) on the work date | Per invoice, market-tracking |

Read `methodology.md` for the full mechanics including why the model is structured this way, edge cases (cross-day works, band boundaries, baseline floor, cap ceiling), and the GST treatment.

## Bundled artefacts

| File | What it is |
|---|---|
| `fuel_levy_calculator.py` | Importable verifier with `verify()`, `reverse_engineer()`, `get_tgp()`. CLI: `python fuel_levy_calculator.py verify --supplier X --contract Y --work-date YYYY-MM-DD --work-ex-gst N --charged-levy M` |
| `fuel_components_register.json` | Per-supplier Fuel Component %, sighted from Council-issued contract variation letters. Authoritative for payment. |
| `branch_fuel_levy_proposals.json` | Non-authoritative register of suppliers observed invoicing a fuel levy without a sighted contract variation. Used to name the proposed rate in the BLOCK verdict. Add a supplier here when an invoice arrives needing a more informative block than the generic "not in register". |
| `brisbane_diesel_tgp.csv` | AIP Brisbane Diesel terminal gate price daily series, cents per litre inclusive of GST |
| `methodology.md` | Formula explained, edge cases, GST treatment, anti-patterns |
| `worked_examples.md` | Three Vinton invoices from May 2026 worked end to end |

## When this skill triggers

Any time the user uploads or references a supplier invoice that contains a fuel levy line under a PAR/* contract. Specifically:

- `LCC Fuel Levy - Diesel` line on a Vinton Tree Services tax invoice
- `Fuel Levy Surcharge` line on a Glascott or other Parks contractor invoice
- Questions like "is this fuel levy correct", "verify the surcharge", "what should the rate be"
- Reverse-engineering questions like "what band did they use", "what TGP would produce this levy"
- Multi-invoice batches where each line has its own fuel levy that needs checking against the day's TGP

If the user shares an invoice with no fuel levy line, this skill does not apply; coding correctness goes to `lcc-coding-review`.

## The decisive verdict set

The calculator returns exactly one of these eight statuses. There is no in-between. Each maps to one operational next step.

| Status | When it fires | Action |
|---|---|---|
| `OK_EXACT_MATCH` | Charged levy matches the ceiling to the cent | Pay invoice at face value |
| `OK_SUPPLIER_UNDER_CLAIM` | Charged levy is below the ceiling | Pay at face value (Fact Sheet 'lower of' rule); optionally note the discrepancy back to the supplier |
| `OK_NO_LEVY_BELOW_BASELINE` | TGP is at or below $1.70/L baseline, supplier charged zero | Pay invoice at face value |
| `OVER_CLAIM_REJECT` | Charged levy exceeds the ceiling, OR levy charged when TGP is below baseline | Reject the levy line; request supplier reissue capped at the ceiling, or process the excess as a creditor adjustment |
| `BLOCK_BRANCH_PROPOSAL_NO_VARIATION` | Supplier is in `branch_fuel_levy_proposals.json` but no contract variation is on file in `fuel_components_register.json` | Hold the levy line. Request the contract variation under the named PAR contract; once received, add to `fuel_components_register.json` and re-run |
| `BLOCK_SUPPLIER_NOT_IN_REGISTER` | Supplier is in neither register | Block payment; locate the contract variation letter, add the supplier with source reference, re-run |
| `BLOCK_NO_TGP_FOR_WORK_DATE` | No TGP entry on or before the work date in `brisbane_diesel_tgp.csv` | Block payment; refresh TGP from AIP, re-run |
| `BLOCK_TGP_SERIES_TOO_STALE` | Latest TGP is more than 15 business days before the work date | Block payment; refresh TGP from AIP, re-run |

Never invent a TGP, never extrapolate, never approve when the inputs aren't sighted. The "block" statuses exist because uncertain inputs producing a confident-sounding answer is worse than refusing to answer.

## Workflow

### Per-invoice verification

1. **Extract from the invoice:**
   - Supplier name (must match an entry in the register, case-insensitive)
   - Contract reference (audit trail only, not used in maths)
   - Date of work (the day the job was completed, NOT the invoice date)
   - Work ex GST excluding the levy line: sum of all non-levy line items, ex GST. For multi-line jobs this is `Subtotal - Charged Levy`. Verify against the invoice's printed subtotal minus the printed levy line, the two should match.
   - Charged levy: the supplier's `LCC Fuel Levy - Diesel` or `Fuel Levy Surcharge` line, ex GST

2. **Run the calculator:**
   ```bash
   python fuel_levy_calculator.py verify \
       --supplier "Vinton Tree Services" \
       --contract PAR/329E/2021 \
       --work-date 2026-05-06 \
       --work-ex-gst 1262.50 \
       --charged-levy 37.31
   ```

3. **Read the verdict.** The status alone tells you the next step. The verdict text explains why. The action text tells you what to do operationally.

4. **For batches, run each invoice separately.** Each invoice has its own work date and therefore its own TGP and band. Cross-day jobs may straddle band boundaries (see `methodology.md`).

### Reverse-engineering when one input is missing

If you have the work value and the charged levy but you need to figure out what TGP band the supplier referenced, use the reverse function:

```bash
# With a known supplier (Fuel Component locked from the register):
python fuel_levy_calculator.py reverse \
    --supplier "Vinton Tree Services" \
    --work-ex-gst 1262.50 \
    --charged-levy 37.31

# Without a supplier (returns all candidate band x component splits):
python fuel_levy_calculator.py reverse \
    --work-ex-gst 1262.50 \
    --charged-levy 37.31
```

The supplier-locked mode returns the implied escalation %, the nearest band, the TGP range that band corresponds to, and a `clean_band_match` boolean indicating whether the supplier's implied rate sits exactly on a band step.

The no-supplier mode returns every possible band × component split. Use this when you don't yet have a contract variation letter and need to infer the Fuel Component from clean round-number figures (e.g. 19.7% jumping out as a defensible fuel share for a tree-services contractor).

### Programmatic use

```python
from fuel_levy_calculator import FuelLevyVerifier

v = FuelLevyVerifier()
result = v.verify(
    supplier="Vinton Tree Services",
    contract="PAR/329E/2021",
    work_date="2026-05-06",
    work_ex_gst=1262.50,
    charged_levy=37.31,
)
print(result.status)   # "OK_EXACT_MATCH"
print(result.verdict)  # full sentence verdict
print(result.action)   # operational next step
print(result.max_levy) # 37.31
print(result.variance) # 0.0
```

For batch verification, iterate over invoices in a workbook or a list of tuples and write the results to a status column.

## Output format expected from the skill

When the user asks Claude to verify one or more invoices, structure the response as follows.

**Single invoice:**

A short opening line stating the verdict ("Clear to pay at face value", "Reject the levy line", "Block payment until X is sighted"), followed by a verification table showing the inputs used and the calculation, followed by the next-action sentence. No long preamble.

**Batch of invoices:**

A summary table with one row per invoice showing date of work, TGP, band, escalation %, work ex GST, max levy, charged levy, variance, status. Then a verdict per invoice in plain prose, then a batch total and a single combined next-action paragraph.

Always cite the source for each input (the AIP TGP series for the band, the contract variation letter for the Fuel Component, the invoice itself for the work value and charged levy).

## Maintaining the bundled data

### Refreshing the Brisbane Diesel TGP series

The AIP publishes the Brisbane Diesel TGP daily at https://www.aip.com.au/pricing/terminal-gate-prices. Pull the series at least weekly. Append new rows to `brisbane_diesel_tgp.csv` in `YYYY-MM-DD,cents_per_litre_incl_gst,source` format. Use the **inclusive of GST** figure as published; the calculator handles the band lookup in dollars per litre.

Rule of thumb: refresh whenever a new invoice's work date is within 5 business days of the latest entry. The calculator warns at 5 business days stale and refuses at 15 business days stale.

### Adding a supplier to the register

When a new contract variation letter is issued naming a supplier and their Fuel Component %:

1. Open `fuel_components_register.json`
2. Add a new entry under `suppliers` with: `supplier`, `contract`, `fuel_component_pct` (as a decimal, e.g. 0.197 for 19.7%), `source_document` (full document reference, e.g. `DM19354756 - Council to ... 20 April 2026`), `effective_from`, `approver`, and any notes
3. Never add a supplier without sighting the source document. The register's purpose is to be the audit-trail for what Fuel Component was applied, with the evidence pointer baked in.

### Updating an existing supplier's Fuel Component

If a contract variation re-locks a supplier's Fuel Component at a new percentage:

1. Move the existing entry into the `historical` block with `effective_to` set to the day before the new variation takes effect
2. Add the new entry under `suppliers` with the new percentage and the new source document reference

Do not overwrite. The history matters for verifying prior-period invoices.

## What this skill does NOT do

- Verify the coding of the underlying work (which natural account, which PK). That's `lcc-coding-review`.
- Verify the supplier's BSB or banking details. That's per Spero's invoice verification rule, handled separately.
- Generate a GENJNL recode journal if the levy is wrong. If the verdict is `OVER_CLAIM_REJECT`, the supplier needs to reissue; if Council needs to process the excess as a creditor adjustment, see `techone-genjnl-format` for the journal mechanics.
- Calculate fuel-related expenditure forecasts. That's `lcc-parks-forecast`.
- Maintain budget against the fuel levy line. That's part of standard variance analysis under `lcc-na-analysis`.

## Cross-references

- **Fact Sheet DM19338551** is the source of truth for the model. The Fact Sheet is paraphrased in `methodology.md`; the bands are hardcoded in the calculator and derived by formula from the four core parameters (baseline $1.70, cap $4.00, cap escalation 65%, step 5%, band width 17¢).
- **Companion checker workbook DM19338551 v2** is the spreadsheet equivalent of this skill. The skill produces the same answer with stricter discipline (no silent stale-TGP fallback, no Excel float-precision risk, explicit verdict taxonomy).
- `techone-genjnl-format` for any recode journal triggered by an over-claim.
- `lcc-coding-review` for verifying that the underlying work was coded to the right natural account.
- `spero-writing-style` for prose tone in the verification email back to the supplier.

## Style note

Verdicts and actions are written in Spero's voice: plain, declarative, dollar-amounts-led, no em-dashes as separators, no hedging without a specific reason. The calculator returns these directly; the skill should reproduce them verbatim in user-facing outputs rather than rewording.
