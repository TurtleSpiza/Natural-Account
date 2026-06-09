# Methodology: LCC Fuel Levy Surcharge

The formal mechanics of the Council stepped and capped fuel levy model per Fact Sheet DM19338551, with the edge cases and design rationale that the Fact Sheet itself leaves implicit.

## The formula

```
Levy ($) = Work_ex_GST × Fuel_Component_% × Fuel_Escalation_%
```

Two multiplicative variables against one constant base. No additive terms, no compounding, no GST inside the calculation itself. GST is added once at the bottom of the invoice, alongside the work and the levy together.

## Each term explained

### Work ex GST

The invoice subtotal before GST, **excluding the levy line itself**. The levy is applied to the underlying work, not to a subtotal that already includes the levy, otherwise the rate compounds on itself.

For a Vinton tax invoice with three work lines and a levy line:

```
4-person crew      2.5hrs × $315.00 = $787.50
EWP up to 28m      2.5hrs × $190.00 = $475.00
LCC Fuel Levy      1 × $37.31       = $37.31
Subtotal ex GST                       $1,299.81
GST                                   $129.98
Total inc GST                         $1,429.79
```

Work ex GST = $787.50 + $475.00 = $1,262.50. NOT $1,299.81 (the subtotal includes the levy).

### Fuel Component %

The contractually agreed proportion of each rate that is attributable to fuel, as opposed to labour, materials, overheads, and margin. This is **negotiated once per contract** and locked in writing. For Vinton under PAR/329E/2021 it is 19.7%, evidenced by the Council-issued contract variation letter dated 20 April 2026 (DocRef 19354756).

The Fuel Component is supplier-and-contract-specific. A second supplier operating heavier diesel-intensive plant may have negotiated 25%. A labour-heavy maintenance contractor may have negotiated 8%. The Fact Sheet's own worked example explains: if a $100 rate comprises 20% fuel, 65% labour, and 15% margin, only the 20% fuel slice gets escalated, not the whole $100.

The Fuel Component does not change between invoices, does not change with fuel price, and only changes if the contract is formally re-varied. This is the structural-exposure dial.

### Fuel Escalation %

The stepped multiplier from the Fact Sheet table, selected by the current Brisbane Diesel Terminal Gate Price (TGP). The table runs in 5% steps across 17¢/L bands, starting at 0% below $1.86/L and capping at 65% above $3.91/L.

The TGP is read from the **AIP Brisbane daily series, inclusive of GST** (per the Checker's default GST treatment, matching the AIP publication basis), and the band lookup uses the TGP as published on the **date of work** (not the date of invoice, not the date of payment, not a monthly average).

The Escalation % changes per invoice because the TGP changes daily. This is the market-tracking dial.

## The bands

| TGP $/L (incl GST) | Fuel Escalation % |
|---|---|
| < $1.70 | 0% (no levy) |
| $1.70 - $1.86 | 0% |
| $1.87 - $2.03 | 5% |
| $2.04 - $2.20 | 10% |
| $2.21 - $2.37 | 15% |
| $2.38 - $2.54 | 20% |
| $2.55 - $2.71 | 25% |
| $2.72 - $2.88 | 30% |
| $2.89 - $3.05 | 35% |
| $3.06 - $3.22 | 40% |
| $3.23 - $3.39 | 45% |
| $3.40 - $3.56 | 50% |
| $3.57 - $3.73 | 55% |
| $3.74 - $3.90 | 60% |
| $3.91 - $4.00 | 65% (cap) |
| > $4.00 | 65% (cap, no further increase) |

Bands are inclusive at both ends. $2.20 = 10%, $2.21 = 15%. A 1¢ move can shift the band; this is intentional and the supplier is expected to track it daily.

## Why the model is structured this way

### Why two multipliers and not one flat rate

The 50/50 risk share is built into the bands. A $0.34/L rise in raw diesel from $1.70 to $2.04 produces only a 10% escalation, not a 20% rise, because Council and the supplier each absorb half the move. The other 50% sits with the supplier as a contractually accepted business risk. The Fact Sheet calls this "50/50 shared risk", and the asterisk on the Stepped Surcharge Table reads "This % has already had the 50/50 applied."

Then that 10% only attacks the fuel slice (e.g. 19.7%) of the contract rate, not the whole rate, because labour, materials, overheads, and margin do not move with diesel.

### Why the Fact Sheet bans certain things

- **"Prospective only"** exists because backdating creates a recompute liability on already-paid invoices and incentivises supplier gaming on dating.
- **"Separate invoice line"** exists so the surcharge is visible to AP and reviewable at any future point without re-deriving it. A supplier rolling the levy silently into hourly rates makes audit impossible.
- **"No combination with other escalation mechanisms"** exists because some contracts also have CPI clauses or annual rate reviews, and stacking would double-dip.

### The "lower of" rule

If the supplier requests a specific rate or surcharge percentage independently, Council recalculates using the stepped table and pays the lower of the two. This protects Council from supplier overstatement without forcing Council to overpay when the supplier under-claims (the latter goes through as charged, since the supplier has self-evidently accepted the lower figure).

In verifier terms:
- Charged ≤ Council ceiling → pay as charged (`OK_EXACT_MATCH` or `OK_SUPPLIER_UNDER_CLAIM`)
- Charged > Council ceiling → reject or cap at Council ceiling (`OVER_CLAIM_REJECT`)

## Edge cases

### Cross-day works

A job spanning 6 to 8 May 2026 straddles a band boundary in the May 2026 series (15% on 6 and 7 May, 10% on 8 May). The Checker workbook's convention is to use the **Date of Work** entered, so the contract owner picks one day.

The Fact Sheet's Methodology open item flags this as needing a documented convention for multi-day jobs (earliest day, latest day, weighted average). Until that policy is settled:

- For single-day jobs (Vinton's typical pattern), this is a non-issue.
- For multi-day jobs, default to the **earliest** day's TGP as the most conservative for Council. If the supplier's invoice shows the later day's higher band, raise it with the supplier.

### TGP exactly on a band boundary

Bands are written as ranges with both endpoints inclusive. The calculator rounds TGP to 2 decimal places via `round(tgp, 2)` to avoid the float-precision bug that broke the prior Checker workbook (2.0099999999998 silently falling out of the 1.87-2.03 band).

A TGP that lands at exactly 2.20 reads as 10%; at 2.21 it reads as 15%. The 1¢ step is the supplier's accepted precision floor.

### Cap at $4.00/L

Above $4.00/L the escalation plateaus at 65% and does not increase further. This is the supplier's accepted risk ceiling under the 50/50 design. If diesel hits $5.00/L the supplier eats the additional move; if it hits $10.00/L the supplier eats that too.

### Below baseline

Below $1.70/L the escalation is 0% and no levy applies. This is the symmetric floor; the model does not credit Council back when diesel falls below baseline, it just stops surcharging.

If a supplier charges a levy when the TGP is at or below $1.70/L, that is an over-claim regardless of the amount. The verifier returns `OVER_CLAIM_REJECT` even for small amounts.

### GST treatment of the TGP lookup

This is an unresolved policy question in the workbook. AIP publishes inclusive of GST; the Checker defaults to using the inclusive figure. Switching to exclusive shifts every band by approximately 9% and changes the levy materially.

The Methodology sheet flags this as a Procurement-confirmation item. The verifier defaults to inclusive (matches the AIP publication basis); if Procurement formally confirms an exclusive basis, the bundled TGP series can be regenerated using the `$/L (excl GST)` conversion and the calculator re-pointed at it.

## Anti-patterns the verifier catches

- A supplier charging the levy on the **GST-inclusive base** instead of ex-GST: the variance comes out as 10% over the ceiling (the GST), and the verifier flags `OVER_CLAIM_REJECT`.
- A supplier applying the **escalation to the whole rate** instead of just the fuel component: variance comes out 5× over (1 / 0.197 ÷ 1), `OVER_CLAIM_REJECT`.
- A supplier **double-dipping** by also applying a contractual CPI increase on top: depends on the magnitudes, however the levy line itself usually still verifies; the double-dip would show in the work value being inflated above the per-unit rates. Cross-check work value against the rate card.
- A supplier using a **stale TGP** from a prior month: variance comes out under or over depending on direction; the reverse-engineer function will show the implied TGP band, which the user can compare to the AIP series for the actual work date.
- A supplier using a **different state's TGP** (Sydney was 225.3¢/L, identical to Brisbane on 6 May 2026, however on other days they diverge): same detection mechanism as stale TGP.
- A supplier **rounding the TGP up** to push into the next band: the verifier's exact band lookup catches this if the AIP figure for the day sits in the lower band.

## How to add a new supplier

When Council issues a contract variation locking a new supplier's Fuel Component:

1. Sight the variation letter. Note the supplier name, ABN, contract reference, Fuel Component %, effective date, and the document reference (DM number or TRIM number).
2. Add an entry to `fuel_components_register.json` under `suppliers` with all fields populated and the `source_document` field set to the full reference (not just "contract", which is unverifiable).
3. Test the first invoice from that supplier with the verifier. If the verdict comes back `OK_EXACT_MATCH`, the register entry is correct.

## How to refresh the TGP series

1. Open https://www.aip.com.au/pricing/terminal-gate-prices
2. Pull the Brisbane Diesel daily series for any days not yet in `brisbane_diesel_tgp.csv`
3. Append rows in `YYYY-MM-DD,cents_per_litre_incl_gst,source` format
4. Cadence: refresh at least weekly. The verifier warns at 5 business days stale and refuses at 15 business days stale.

The AIP publishes weekday-only (Mon-Fri); weekends and public holidays carry forward the prior business day's published TGP. The verifier handles this via last-before lookup.
