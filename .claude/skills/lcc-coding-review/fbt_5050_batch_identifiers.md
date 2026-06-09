# FBT 50/50 Batch Identifiers

The single biggest false-positive source in any 73511/73512 review. Read this before flagging any movement between those two accounts as a miscode.

## What the 50/50 method is

LCC uses the 50/50 method for meal entertainment under FBT. All meal entertainment costs end up taxed at 50% of the actual cost. Mechanically this means Finance posts batch journals that reallocate amounts between 73511 (FBT-applicable hospitality) and 73512 (no-FBT on-premises light refreshments) at the end of each FBT period.

These batches are systematic Finance processing, not coding decisions by Parks staff. They are not miscodes.

## How to identify them

A 73511 ↔ 73512 movement is a 50/50 batch (not a miscode) if any of the following are true:

### Signal 1: Reference prefix
- `AP003xxx` series — Finance-processed FBT adjustment batches
- `GJ07xxxx` series with multiple lines — Finance-posted batch journals

### Signal 2: Line count
- A single journal with 60+ lines moving across 73511/73512 across multiple cost centres is virtually always a 50/50 batch
- GJ078599 alone had 60+ lines

### Signal 3: Narration pattern
- Generic narrations like "FBT 50/50 reallocation" or "Meal Entertainment FBT adjustment"
- No vendor name, no event name, no individual cost reference

### Signal 4: Period timing
- Posted at FBT period boundaries (typically March-April for the FBT year ending 31 March)
- Often appears at end of a financial period as part of Finance month-end close

### Signal 5: Net effect
- 50/50 batches do not change the total spend on hospitality across the two accounts; they just move the FBT-applicable proportion. The combined 73511 + 73512 balance is unchanged before vs after.

## Workflow before flagging any 73511/73512 miscode

1. Pull the listing for both 73511 and 73512 over the period being reviewed
2. Identify all `AP003xxx` and `GJ07xxxx` references
3. Set those aside as 50/50 batches — do not flag
4. Review only the remaining transactions for genuine miscodes (e.g. hospitality coded to 73513, off-site meal coded to 73512, alcohol included anywhere)

## What ARE genuine miscodes worth flagging

- 73511/73512 ↔ 73513 (hospitality vs gifts confusion - see systemic_miscodes.json)
- Off-site meal in 73512 (should be 73511 - location-based rule)
- Alcohol present and amount in 73512 (should be 73511 - alcohol triggers FBT)
- Light refreshment for clients/visitors in 73511 (should be 73512 - same basis as employees)
- Associates/family of employees in 73512 (should be 73511 - associate exemption doesn't apply)

## What about IT 2675 thresholds

The "as light meals become more elaborate, they take on more characteristics of entertainment" judgement (IT 2675 para 7) applies to whether something belongs in 73511 vs 73512 in the first place. It does not affect whether a Finance 50/50 batch is a miscode (it isn't).

## Worked example

A reviewer pulls 73511 listing for FY2025 and finds 87 lines totalling $24,500. 43 of those lines are journal entries with reference `GJ078599` and narration "Meal Entertainment FBT adjustment - 50/50 method." Those 43 lines should be set aside immediately. The remaining 44 lines are the genuine review population.

If those 43 lines had been treated as miscodes, the reviewer would have flagged a $12,000+ "miscoding" that doesn't exist. This is the failure mode this document prevents.
