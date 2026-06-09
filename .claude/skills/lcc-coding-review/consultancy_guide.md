# LCC Consultancy Guide

Source: Chart of Accounts PDF, page 71 (Consultancy Guide).

Consultants are a type of contractor that LCC defines separately for reporting purposes. This guide identifies which transactions belong in the five 73600-series consultancy accounts versus the broader contractor accounts (73211, 73212, 73214, 73699, 73606).

## Council's definition of a "Consultant"

For reporting purposes a service provider can be categorised as a **"consultant"** (which may be an individual or an organisation) if **all of the following four elements are present**:

1. Provides expert knowledge to analyse information, draw conclusions and make recommendations in form of a written report or an intellectual product for future action which Council must then decide upon or take.
2. The nature of the output is not necessarily predictable, but tends to be open ended and is more complex (for example, a range of recommendations are presented for Council to consider).
3. Develops a new concept or process and where Council requires critical judgement to consider the recommended course of action.
4. Is engaged for a fixed period of time at an agreed payment rate, work which is not directly supervised by Council.

**All four** must be present. Miss one (e.g. the engagement is supervised, or the output is a known deliverable rather than analysis) and the supplier is a contractor, not a consultant.

## Consultant vs Contractor

Contractors differ from Employees because they are engaged under different legal arrangements. Contractors for professional services is generally where confusion may occur when categorising consultants and contractors.

**Contractor** — implements an existing process to deliver a known product or outcome.

**Consultant** — develops a new concept or process; Council exercises critical judgement on the recommendations.

Council has two types of contractor:

### Contractors for non-professional services
Trade services (plumbers, painters), cleaning services, construction works, and temporary staff (agency personnel) who are engaged to relieve vacant LCC employee positions.

### Independent contractor (professional services)
An "entity" engaged for services to be provided. An independent contractor relationship is defined as a **contract for service** and in this context an independent contractor is therefore contracted to achieve a specific result. Such engagement will have a start and end date in place, and will be temporary in nature and may not exceed 12 months in totality without approval from the Chief Executive Officer.

### Temporary agency personnel
An individual employed by an agency, engaged to provide services to Council. Such engagement will have a start and end date in place, and will be temporary in nature and may not exceed 12 months in totality without approval from the Chief Executive Officer. **Code to 73214 (Agency Personnel Costs), not the 73600-series.**

## The five consultancy account categories

| Account | Title | Description | GST |
|---------|-------|-------------|-----|
| **73601** | Management Consultancies | Includes business planning, business redesign, organisational change management, organisational strategic planning, organisational resource planning and organisational cultural project management. Also: consultants providing advice on the impact of interest rate changes. | C |
| **73603** | Planning & Environment Consultancies | Includes land use planning, urban design, environmental planning and climate change. | C |
| **73605** | Information Technology (IT) Consultancies | Includes software/hardware tendering, and software/hardware analysis. | C |
| **73607** | Engineering Consultancies | Includes expenditure on engineering advice or analysis for civil engineering, environmental engineering and electrical engineering (infrastructure focus). | C |
| **73609** | Other Consultancies | Anything that does not specifically fall into the above categories but is a consultancy service provided to Council. That is, more of an ad-hoc or business arising during the financial year. | C |

## Restricted: 73602 Alliance Consultancies

**73602 Alliance Consultancies** is reserved for the Logan Water Alliance (LWA). Restricted use — do **not** code general management or engineering consultancies here. Consultancies for non-Alliance work go to 73601, 73603, 73605, 73607, or 73609 per the table above.

## Common confusion pairs

| Confusable pair | Distinguish by |
|-----------------|----------------|
| 73601 (Mgmt Consultancy) vs 73214 (Agency Personnel) | If supervised and filling a vacant role → 73214. If delivering recommendations → 73601. |
| 73607 (Engineering Consultancy) vs 73113 (Engineering Services) | 73113 is engineering services where the deliverable is known (a survey, a design, a report on a known scope). 73607 is consultancy where Council exercises judgement on the output. |
| 73603 (Planning & Environment Consultancy) vs 73111 (Property-based Professional Services) | 73111 is property-related professional services with a known deliverable (valuation, conveyancing). 73603 is consultancy on planning, environment, climate. |
| 73605 (IT Consultancy) vs 73564 / 73566 (IT Equipment, Software Licences) | Goods and recurring licences are 73564/73566. Advisory work on IT decisions is 73605. |
| 73609 (Other Consultancy) vs 73128 (Other Services) | 73128 is non-consulting services that don't fit elsewhere. 73609 is consultancy that doesn't fit the other four 73600-series buckets. |
| 73211 / 73212 (Contractors operating / major operating) vs 73600-series | Contractors deliver a known scope; consultants deliver analysis and recommendations. Test against the four-element definition above. |
| 73699 (Contractors Recovery) vs 73600-series | 73699 is the recovery/clearing account for operational (non-capital) contractor cost; 73600-series is the consultancy reporting bucket. Different purposes. |
| 73606 (Contractors Capital Recovery) vs 73600-series | 73606 is contractors providing services for capital projects (CWIP). Consultancies stay in the 73600-series even on capital work. |

## Operational rules

1. **The four-element test is binding.** If even one element is missing, code as contractor.
2. **Agency personnel filling a Council role go to 73214**, never the 73600-series, regardless of the work content. Hays, Chandler Macleod, Adecco, Programmed → 73214.
3. **Restricted accounts.** 73602 (Alliance) requires CEO approval and is reserved for LWA work.
4. **GST.** All five consultancy categories carry GST code C.
5. **Capital vs operational.** Consultancy services on capital projects still go to the 73600-series; the capital-vs-operational distinction does not move consultancies into 73606.

## Cross-references

- `accts.json` and `full_chart_of_accounts.json` — full descriptions of 73601, 73602, 73603, 73605, 73606, 73607, 73609, 73699, 73214, 73211, 73212.
- `confusion_pairs.json` — formalised side-by-side good/bad examples.
- `vendor_lookup.json` — known vendor → suggested account mappings.
