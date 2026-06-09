# Category Index

Human-readable reference for the 9 NARR_TEMPLATES categories. For each category: fields, suggested account, template pattern, one example output.

## 1. mowing — Contract Mowing / Landscaping

**Account:** 73126 (Landscapers & Gardeners)

**Fields:**

| Field id      | Label              | Example placeholder                              |
|---------------|--------------------|--------------------------------------------------|
| narr_vendor   | Contractor         | Austspray, Glascott                              |
| narr_service  | Service            | Zone mowing, vegetation management               |
| narr_zone     | Zone / Location    | Zone 3, Logan Reserve, MZ09                      |
| narr_period   | Period             | March 2026, Q3 FY2026                            |
| narr_po       | PO / Contract Ref  | PO 485102, DM 16845001                           |
| narr_svc      | Service Code       | 20371                                            |

**Pattern:**

```
{vendor} — {service} {zone} {period}[ Ref: {po}][ Svc {svc}]
```

**Example:**

```
Austspray — Zone mowing Zone 3 March 2026 Ref: PO 485102 Svc 20371
```

## 2. maintenance — Maintenance / Repairs

**Account:** 73123 (Maintenance Services)

**Fields:**

| Field id      | Label              | Example placeholder                              |
|---------------|--------------------|--------------------------------------------------|
| narr_vendor   | Contractor         | Weis, Riverdale                                  |
| narr_work     | Work Type          | BBQ repair, fence fix, irrigation                |
| narr_asset    | Asset / Location   | Berrinba Wetlands, Depot                         |
| narr_po       | PO / WO Ref        | PO 483340, WO 12345                              |
| narr_svc      | Service Code       | 20481                                            |

**Pattern:**

```
{vendor} — {work} at {asset}[ Ref: {po}][ Svc {svc}]
```

**Example:**

```
Weis — BBQ repair at Berrinba Wetlands Ref: PO 483340 Svc 20481
```

## 3. hospitality — Hospitality / Catering

**Account:** 73512 (Entertainment & Hospitality Non-FBT)

**Fields:**

| Field id      | Label              | Example placeholder                              |
|---------------|--------------------|--------------------------------------------------|
| narr_event    | Event              | Team planning day, staff farewell                |
| narr_venue    | Venue              | LEC, Council boardroom, restaurant               |
| narr_food     | Food / Drink       | Morning tea, lunch, dinner + wine                |
| narr_attend   | Attendees          | 12 staff, 3 external guests                      |
| narr_onsite   | On/Off-site        | On-site (Council premises)                       |

**Pattern:**

```
{event} — {food} at {venue}, {attend}, {onsite}
```

**Example:**

```
Team planning day — Morning tea at LEC, 12 staff, On-site (Council premises)
```

**Note:** No conditional fields — all fields render with placeholder fallbacks if missing. If alcohol involved, account flips to 73511 (Entertainment FBT) — outside NARR_TEMPLATES scope; flag at use time.

## 4. training — Training / Conference / Study

**Account:** 73544 (Training & Development)

**Fields:**

| Field id        | Label              | Example placeholder                              |
|-----------------|--------------------|--------------------------------------------------|
| narr_course     | Course / Event     | LGMA Conference, Chainsaw cert                   |
| narr_provider   | Provider           | LGAQ, TAFE, University                           |
| narr_staff      | Staff Member       | J. Smith                                         |
| narr_dates      | Dates              | 15-17 May 2026                                   |
| narr_type       | Type               | Registration, accommodation, fees                |

**Pattern:**

```
{course} — {provider} for {staff} {dates} ({type})
```

**Example:**

```
LGMA Conference — LGAQ for J. Smith 15-17 May 2026 (Registration)
```

## 5. agency — Agency / Temp Labour

**Account:** 73214 (Temporary Labour)

**Fields:**

| Field id        | Label              | Example placeholder                              |
|-----------------|--------------------|--------------------------------------------------|
| narr_agency     | Agency             | Hays, Chandler Macleod, Adecco                   |
| narr_role       | Role               | Admin support, field officer                     |
| narr_period     | Period             | w/e 15 Mar 2026                                  |
| narr_section    | Section            | Natural Areas, Park Maintenance                  |

**Pattern:**

```
{agency} — {role} {period} {section} — agency temp labour
```

**Example:**

```
Hays — Admin support w/e 15 Mar 2026 Natural Areas — agency temp labour
```

## 6. plant — Plant / Equipment Hire

**Account:** 74123 (Plant Hire)

**Fields:**

| Field id        | Label              | Example placeholder                              |
|-----------------|--------------------|--------------------------------------------------|
| narr_equip      | Equipment          | 8t excavator, backhoe, water truck               |
| narr_supplier   | Supplier           | Tutt Bryant, Kennards                            |
| narr_period     | Hire Period        | 3 days, 1 week                                   |
| narr_site       | Site / Location    | Slacks Creek reserve                             |
| narr_svc        | Service Code       | 20451                                            |

**Pattern:**

```
{supplier} — {equip} hire {period} at {site}[ Svc {svc}]
```

**Example:**

```
Tutt Bryant — 8t excavator hire 3 days at Slacks Creek reserve Svc 20451
```

## 7. travel — Travel / Transport

**Account:** 73533 (Travel)

**Fields:**

| Field id        | Label              | Example placeholder                              |
|-----------------|--------------------|--------------------------------------------------|
| narr_dest       | Destination        | Melbourne, Cairns, Brisbane CBD                  |
| narr_purpose    | Purpose            | LGMA conference, site inspection                 |
| narr_mode       | Mode               | Flight, taxi, toll, accommodation                |
| narr_staff      | Staff              | K. Quinn                                         |
| narr_dates      | Dates              | 10-12 Apr 2026                                   |

**Pattern:**

```
{mode} — {dest} for {purpose} {staff} {dates}
```

**Example:**

```
Flight — Melbourne for LGMA conference K. Quinn 10-12 Apr 2026
```

## 8. cleaning — Cleaning / Waste / Sanitary

**Account:** 73121 (Cleaning Services)

**Fields:**

| Field id        | Label              | Example placeholder                              |
|-----------------|--------------------|--------------------------------------------------|
| narr_vendor     | Contractor         | Kachel, Cleanaway, ANS                           |
| narr_service    | Service Type       | Amenities cleaning, garbage                      |
| narr_zone       | Zone / Site        | Zone 1, Marsden depot                            |
| narr_period     | Period             | March 2026                                       |
| narr_po         | SO / DM Ref        | DM 16845001                                      |

**Pattern:**

```
{vendor} — {service} {zone} {period}[ Ref: {po}]
```

**Example:**

```
Kachel — Amenities cleaning Zone 1 March 2026 Ref: DM 16845001
```

## 9. general — General Invoice

**Account:** (none — picked at use time)

**Fields:**

| Field id        | Label              | Example placeholder                              |
|-----------------|--------------------|--------------------------------------------------|
| narr_vendor     | Vendor             | Bunnings, Officeworks                            |
| narr_goods      | Goods / Service    | Garden tools, office supplies                    |
| narr_purpose    | Purpose            | For depot workshop                               |
| narr_location   | Location           | Marsden depot                                    |
| narr_ref        | Invoice Ref        | INV-12345                                        |

**Pattern:**

```
{vendor} — {goods} for {purpose} at {location}[ Ref: {ref}]
```

**Example:**

```
Bunnings — Garden tools for For depot workshop at Marsden depot Ref: INV-12345
```

**Note:** "general" has no fixed account because it covers everything from supplies to subscriptions to one-off vendor charges. Account picked at code-review time using `lcc-coding-review` decision flow.

---

## Picking the right category

```
Is the invoice for landscaping / mowing / vegetation work?         → mowing
Is it a repair or maintenance fix on an asset?                     → maintenance
Is it food, drink, or a function?                                  → hospitality
Is it a course, conference, training session, or study?            → training
Is it temp labour from an agency?                                  → agency
Is it equipment / plant rental?                                    → plant
Is it travel-related (flight, taxi, accommodation, conference)?    → travel
Is it cleaning, waste, or sanitary services?                       → cleaning
None of the above?                                                 → general
```

If two categories could apply (e.g. travel for a training event), pick the dominant one — the line item that drives the cost. A flight to a training course usually goes under `travel` if it's the line item (account 73533); the registration fee goes under `training` (account 73544). Two categories, two lines on the journal.

## Cross-reference to chart of accounts

The accounts named here resolve in `full_chart_of_accounts.json` (also at `_shared/lcc_chart_of_accounts.json`). Verify the account name and any restrictions before using:

* 73126 Landscapers & Gardeners — no restrictions; standard mowing/landscaping account.
* 73123 Maintenance Services — exclude security (73124), exclude landscaping (73126), exclude electrical (73127).
* 73512 Entertainment & Hospitality Non-FBT — Reason A or G typically; alcohol → 73511 instead.
* 73544 Training & Development — registration / accommodation / fees.
* 73214 Temporary Labour — distinct from contractor consultancies (73211/73212).
* 74123 Plant Hire — distinct from purchases (72311-72315).
* 73533 Travel — taxi, flight, accommodation, tolls.
* 73121 Cleaning Services — amenities cleaning, sanitary, garbage.
