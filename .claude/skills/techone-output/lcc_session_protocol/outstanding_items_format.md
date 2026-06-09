# Outstanding Items Format

Numbered, persistent, never renumbered. The structure that holds dozens of in-flight queries without losing any of them across 34+ sessions.

## Structure

```
OUTSTANDING ITEMS
-----------------
* = send to {Finance contacts} — batch all starred into one email, do not drip-feed

{N}    {context tag}    {one-line description with all references and dollar amounts}
{N}*   {context tag}    {one-line description — starred for Finance batch}
```

## Numbering rules

1. **Numbers are permanent identifiers.** Item 33 is item 33 forever, even after it closes.
2. **Closed items move to the closed log keeping their number.** They do not get renumbered, do not collapse the gap.
3. **New items take the next unused number.** Don't fill gaps left by closed items.
4. **Sub-numbering with letters is allowed for closely-related sub-issues.** Item 7 / 7a / 7b for three Farmcraft lines under the same vendor query.

## Starring convention

`*` after the number marks an item destined for the next batched Finance email. The rule is one-email-per-session for Finance, never drip-feed. At session end:
- Compile every starred item into a single message to Amy Forgione and Owen Jensen
- Send one email with all the items
- Do not star and send mid-session

Items can be starred at any session. They stay starred until they close.

## Context tag column

A short identifier between item number and description. Used for grep/filtering. Common values:

- A natural account code: `73124`, `72112`, `7B411`
- A workstream tag: `maps`, `misc`, `housekeeping`
- A document reference: `DM 17802475`, `PO 702713`

## Worked examples (from NA Analysis v9_s34)

```
1*   73124     FY2024 nine missing months. QLDPSI Sep-Nov 2023 in 73124 ($48,513). Dec 2023-Jun 2024 not here — confirm where posted.
3*   73212     GJ credits -$762k FY2025 — request journal detail to confirm what these reverse.
4*   73130     source invoice behind $6,263 FY2024 — journal confirmed, vendor invoice not sighted.
5*   73128     source invoices for svc 20671 refs 2957 ($5,180) and 2995 ($1,500) FY2025.
6    73131     insurance premium zero FY2024 — request listing.
7    72112     Farmcraft three lines outstanding (4-1207173 $400, 40015840 $41, 40020033 $70 svc 20322).
7a   72112     SI-00106646 $700 and SI-00106647 $1,300 Greenway — contractor spray, possible miscoding to 73128/73211.
7b   72112     SI-00091774 $65 N-Lift annotated "DO NOT USE" — confirm approved.
```

Note item 2 is missing — it was closed and moved to the closed log keeping its number 2. Item 7 has 7a and 7b sub-items grouped under the same vendor.

## What a good item line contains

Every item line should be self-sufficient enough that someone reading it cold next session can act on it without re-deriving context.

Required elements:
- Account code or other primary identifier
- Period or year if relevant (FY2024, P10, etc.)
- Dollar amount where known
- Vendor or counterparty where known
- Document reference where known (DM number, PO, invoice ref)
- The specific question or action

Anti-pattern: vague items like "73128 — investigate" or "follow up on the Farmcraft thing." Every such item costs the next session a re-investigation.

## What is NOT in outstanding items

- Findings. Those live in workbook col P or the report.
- Discussion or speculation. The session log is for narrative.
- Items resolved this session. Those go to the closed log.
- Operational housekeeping that doesn't block another item. Just do it.

## Lifecycle

```
New observation surfaces   →   Becomes an outstanding item with next available number
Blocker on Finance         →   Star it, will go in next batched email
Listing arrives            →   Item progresses to investigation
Investigation completes    →   Item closes, moves to closed log keeping number
                              workbook col P updated with finding
```

## Maintenance

Once an outstanding-items list exceeds ~80 items (which it will, given recurrence), the temptation is to renumber or "clean up." Do not. The session log entries reference items by number. Renumbering breaks every backwards reference. Live with the gaps.
