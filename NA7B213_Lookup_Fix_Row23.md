# NA7B213 Source fix — Internal_Medical.XLSM "Lookup Values" row 23

## The defect
Row 23 maps the whole 4090000 Parks branch to one ledger line, PK000432-7B213
(service 20318, Natural Areas Environment Levy Coord & Admin). Every Parks
immunisation charge is posted to Natural Areas regardless of the employee's section.
Every other directorate in the lookup carries its own code; Parks is the only branch
collapsed onto a single section PK. Without this fix the miscode recurs on every
future immunisation IJ.

## The fix
Replace the single Parks line with a per-section Parks lookup, keyed on the
employee's home section (drop the leading digit of the 6-digit cost code to get the
5-digit service, map via svc_map, then to the PK). Parks destinations in use FY26:

| Section | PK | Service | Service name |
|---|---|---|---|
| Park Maintenance (landscape) | PK000012 | 20181 | Internal Parks Landscape Services |
| Park Maintenance (mowing/turf) | PK000003 | 20440 | Internal Parks Mowing and Turf Services |
| Cemeteries | PK000439 | 20452 | Parks Cemeteries - Employee Costs |
| Park Services | PK000435 | 20362 | Park Services - Coordination & Administration |
| Park Services (Rangers) | PK000084 | 20301 | Parks and Bushland Rangers |
| Trees | PK000433 | 20319 | Trees Coordination & Administration |
| Natural Areas (fire) | PK000431 | 20317 | Natural Areas - Fire Coordination & Admin |
| Natural Areas (env levy) | PK000432 | 20318 | Natural Areas - Environment Levy Coord & Admin |

Park Maintenance splits across two PKs (PK000012 and PK000003); the correct one
depends on the individual's substantive position, not the section alone, so the
lookup should resolve by employee, not by section label.
