# Source Prefix Glossary

Every TechOne transaction reference starts with a two-character prefix that identifies the source. Reading the prefix tells you what kind of transaction it is, which workflow created it, and what evidence to expect.

## The prefixes

| Prefix | Source | What it is | Evidence to expect |
|---|---|---|---|
| `AP` | Accounts Payable creditor invoice | Vendor invoice processed through AP workflow with a creditor invoice number | Tax invoice (PDF in TechOne or hard copy) |
| `TE` | P-Card cardholder transaction | Credit card charge by a Council cardholder, batched per-card | Tax invoice + cover slip with cardholder signature, requesting officer, account, business purpose |
| `GJ` | General Journal | Manual or batch journal posted by Finance | Journal narration plus any underlying source document referenced |
| `IJ` | Internal Invoice / Internal Journal | Cross-branch internal charge | Signed internal agreement OR email confirmation from charging branch |
| `RJ` | Reversing Journal | EOM accrual or reversal journal | Reverses on the next period boundary; the narration names the underlying contract or event |
| `TC` | Timesheet to Cost | Payroll-to-GL interface entry | Payroll system trail; usually no per-line documentation |
| `PW` | Payroll | Direct payroll posting | Payroll batch reference |
| `IN` | Inventory issue | ALLSTORE / CHAMBERS stores issue | Stores issue slip naming requester and cost centre |
| `PJ` | Project Journal | Capital or project-specific journal | Project file in TechOne; CO/COP capital codes often appear |
| `MI` | Mobile / Inventory | Subscription or recurring device-related billing | Subscription master record, ABN |
| `DM` | Document Management reference | Refers to a TechOne DM (DocSet) record, not a journal source itself | The DM record itself, which holds the underlying contract or accrual basis |
| `PUR` | Purchase order reference | Invoice tied to a PO | The PO and its delegated approval |
| `CO` / `COP` | Capital project | Capital expenditure code, NOT operational | Should not appear in expense reviews unless miscoded (capitalisation issue) |

## Common combined references

A single line in a listing may show multiple references separated by spaces or slashes. Read each:

- `AP003576` followed by an invoice number — AP creditor invoice
- `GJ078805` followed by a narration referencing `INV-157860` — Finance journal moving an AP-paid amount between cost centres
- `RJ013015` followed by `DM 17802492` — EOM accrual referencing a contract held in a DocSet
- `IJ072068` referencing `RCM` (Reactive Cyclone Management) — internal cross-branch charge

## What each prefix means for review

### AP (creditor invoice)
**Reviewing rule:** Tier 1 evidence available. Pull the tax invoice. Check the vendor matches the work, the amount matches, and the account is correct per the chart.

### TE (P-Card)
**Reviewing rule:** Both halves needed for Tier 1 — invoice AND cover slip. Cover slip alone is Tier 2. Invoice alone is Tier 2. The cover slip provides the cardholder signature, the requesting officer, and the business purpose. The invoice provides the vendor and amount.

### GJ (general journal)
**Reviewing rule:** Read the narration first. The dollar amount is meaningless without it. Many GJs are Finance batch processing (50/50 FBT, recodes, accruals) — check whether the GJ is part of a known batch before flagging individual lines as miscodes.

### IJ (internal invoice / journal)
**Reviewing rule:** Cross-branch charges. Trace back to the issuing branch's signed agreement or email. 7B and 7C account ranges are typical destinations.

### RJ (reversing journal)
**Reviewing rule:** EOM accruals. Will reverse on the next period boundary so the net effect across two periods is zero. Don't treat a single-period RJ as final spend — read both periods.

### TC / PW (payroll)
**Reviewing rule:** Generally not investigated at transaction level. Payroll-to-GL interface is a separate audit. If 71000 carries a balance for >2 periods, it's an interface failure that needs HR/Finance escalation.

### IN (inventory)
**Reviewing rule:** ALLSTORE/CHAMBERS issues hit 72-series materials accounts. The marsden_stores_inventory.csv (in `_shared/` if present) maps inventory codes to descriptions. PFS-restricted destinations (74181-188) are a recurring miscode trap.

### DM (DocSet reference)
**Reviewing rule:** Not a journal source on its own — points at a TechOne document (contract, agreement, narration block). Pull the DM to understand the underlying obligation.

## Prefix-driven evidence tier mapping

| Prefix | Tier 1 evidence path |
|---|---|
| AP | Pull tax invoice from TechOne or AP file |
| TE | Pull both invoice and cover slip |
| GJ | Read narration; pull source DM if referenced; trace original AP/TE if a recode |
| IJ | Pull issuing-branch agreement or confirmation email |
| RJ | Read narration; cross-check against the underlying contract or event |
| IN | Pull stores issue slip |
| TC/PW | Payroll trail (rarely Tier 1 at transaction level) |
| DM | Pull the DM record itself |

## Cross-reference

For the GENJNL upload format (PK ledger vs SL ledger), see `worked_examples.md` and `pk_validator.py`.

For the systemic miscoding patterns these references surface (e.g. PFS-restricted accounts misused, training catch-all 73544), see `lcc-coding-review/systemic_miscodes.json`.
