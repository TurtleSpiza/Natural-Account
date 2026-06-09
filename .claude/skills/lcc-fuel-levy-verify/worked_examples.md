# Worked Examples

Three Vinton Tree Services invoices verified end to end, May 2026.

## Inputs locked from source documents

- **Fuel Component 19.7%** — Contract variation letter dated 20 April 2026, DocRef DM19354756, from Council to Vinton Tree Services, attention Mat Vinton, under PAR/329/2021. Formula explicitly stated as `Fuel Levy surcharge = Fuel Escalation Percentage (%) × Fuel Component (19.7%)`.
- **Brisbane Diesel TGP** — AIP daily series, inclusive of GST, cents per litre.

## Example 1: INV 19634 (Eagleby, Wed 6 May 2026)

| Field | Value | Source |
|---|---|---|
| Supplier | Vinton Tree Services | Invoice header |
| Contract | PAR/329E/2021 | Invoice header |
| Work date | 6 May 2026 (Wed) | "Completed 06/05/2026" on the invoice |
| Site | Behind 3 Temma St, Eagleby (PK000482) | Invoice line |
| Work lines (ex GST) | $787.50 (4-person crew × 2.5hr) + $475.00 (EWP × 2.5hr) = **$1,262.50** | Invoice lines |
| Charged levy (ex GST) | **$37.31** | Invoice "LCC Fuel Levy - Diesel" line |
| Subtotal ex GST | $1,299.81 | Invoice |

### Verification

```
TGP on 6 May 2026          = 225.3¢/L = $2.253/L incl GST
Band                       = $2.21-$2.37/L
Fuel Escalation %          = 15%
Fuel Component %           = 19.7%
Max levy                   = $1,262.50 × 19.7% × 15% = $37.31
Charged levy               = $37.31
Variance                   = $0.00
```

**Verdict: OK_EXACT_MATCH.** Charged levy matches the ceiling to the cent. **Action: pay invoice at face value ($1,429.79 inc GST).**

## Example 2: INV 19651 (Cornubia, Thu 7 May 2026)

| Field | Value | Source |
|---|---|---|
| Work date | 7 May 2026 (Thu) | "Completed 07/05/2026" |
| Site | 15 Ballan Court, Cornubia (PK000073) | Invoice line |
| Work lines (ex GST) | $1,338.75 (crew) + $807.50 (EWP) + $720.00 (cut/disperse) + $270.00 (stump) = **$3,136.25** | Invoice lines |
| Charged levy (ex GST) | **$92.68** | Invoice |
| Subtotal ex GST | $3,228.93 | Invoice |

### Verification

```
TGP on 7 May 2026          = 222.8¢/L = $2.228/L incl GST
Band                       = $2.21-$2.37/L
Fuel Escalation %          = 15%
Fuel Component %           = 19.7%
Max levy                   = $3,136.25 × 19.7% × 15% = $92.68
Charged levy               = $92.68
Variance                   = $0.00
```

**Verdict: OK_EXACT_MATCH.** **Action: pay at face value ($3,551.82 inc GST).**

## Example 3: INV 19657 (Greenbank, Fri 8 May 2026)

| Field | Value | Source |
|---|---|---|
| Work date | 8 May 2026 (Fri) | "Completed 08/05/2026" |
| Site | 251-267 Ison Road, Greenbank (PK000477) | Invoice line |
| Work lines (ex GST) | $1,811.25 (crew × 5.75hr) + $1,092.50 (EWP × 5.75hr) + $450.00 (crane × 2.5hr) + $450.00 (stump × 2.5hr) = **$3,803.75** | Invoice lines |
| Charged levy (ex GST) | **$74.93** | Invoice |
| Subtotal ex GST | $3,878.68 | Invoice |

### Verification

```
TGP on 8 May 2026          = 218.7¢/L = $2.187/L incl GST
Band                       = $2.04-$2.20/L     <-- one band lower than 6 and 7 May
Fuel Escalation %          = 10%               <-- one step lower
Fuel Component %           = 19.7%
Max levy                   = $3,803.75 × 19.7% × 10% = $74.93
Charged levy               = $74.93
Variance                   = $0.00
```

**Verdict: OK_EXACT_MATCH.** **Action: pay at face value ($4,266.55 inc GST).**

## Why all three match to the cent

The TGP genuinely moved down across the three work dates. Friday 8 May closed at 218.7¢/L, which dropped from the $2.21-$2.37 band (15%) into the $2.04-$2.20 band (10%). Vinton tracked it correctly to the day, applying 15% on Wed and Thu when the TGP was 225.3 and 222.8, and applying 10% on Fri when the TGP dropped to 218.7. Self-evidently the supplier is referencing the AIP Brisbane TGP daily and selecting the band per the Fact Sheet stepped table for each invoice's specific date of work, rather than applying a flat monthly rate. Arguably this is the gold standard for how Council expects this surcharge to be operated.

## Batch total

| Invoice | Date | Charged | Max | Variance | Verdict |
|---|---|---|---|---|---|
| 19634 | 6 May | $37.31 | $37.31 | $0.00 | OK_EXACT_MATCH |
| 19651 | 7 May | $92.68 | $92.68 | $0.00 | OK_EXACT_MATCH |
| 19657 | 8 May | $74.93 | $74.93 | $0.00 | OK_EXACT_MATCH |
| **Total** | | **$204.92** | **$204.92** | **$0.00** | **Clear to pay** |

## Reverse-engineering walkthrough

Before the contract variation letter (DM19354756) was sighted, the Fuel Component was an unknown. The reverse-engineering approach across three invoices confirmed 19.7% as the only consistent solution.

For INV 19634:
```
Combined rate = $37.31 / $1,262.50 = 2.9552%
```

Candidate decompositions:

| Escalation % | Implied Fuel Component % |
|---|---|
| 5% | 59.10% |
| 10% | 29.55% |
| **15%** | **19.70%** ← clean round figure, defensible for tree services |
| 20% | 14.78% |
| 25% | 11.82% |

Applying the same decomposition to INV 19651 and INV 19657:
- INV 19651: 2.9552% combined → 15% × 19.7% (same band)
- INV 19657: 1.9700% combined → 10% × 19.7% (different band, same Fuel Component)

The 19.7% Fuel Component is the only value that holds across all three invoices regardless of the TGP band Vinton applied. This is the structural-vs-market separation: the Fuel Component is contract-static, the Escalation % is market-dynamic.

The 20 April 2026 contract variation letter then formally confirmed the inference at exactly 19.7%.

## Failure-mode examples (what the calculator catches)

### Supplier over-claim
If Vinton charged $55.00 instead of $37.31 on INV 19634:
- **Verdict: OVER_CLAIM_REJECT.** Variance +$17.69. Action: reject the levy line; request reissue capped at $37.31, or process the excess as a creditor adjustment.

### Wrong supplier (not in register)
If a new contractor "SomeOther Pty Ltd" sends an invoice with a fuel levy:
- **Verdict: BLOCK_SUPPLIER_NOT_IN_REGISTER.** Action: block payment, locate the contract variation letter, add the supplier to the register with source reference, re-run.

### Future-dated work, stale TGP
If a work date is past the latest TGP entry by more than 15 business days:
- **Verdict: BLOCK_TGP_SERIES_TOO_STALE.** Action: block payment, refresh `brisbane_diesel_tgp.csv` from AIP, re-run. Never extrapolate or guess.

### TGP below baseline
If TGP is at or below $1.70/L and a supplier still charges a levy:
- **Verdict: OVER_CLAIM_REJECT.** No levy is permitted below baseline; reject the line.
