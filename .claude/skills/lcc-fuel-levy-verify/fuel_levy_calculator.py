"""
LCC Fuel Levy Verifier
======================
Decisive verification of supplier fuel levy surcharges against the Council
stepped and capped fuel levy model, per Fact Sheet DM19338551.

Formula
-------
    Levy ($) = Work_ex_GST x Fuel_Component_% x Fuel_Escalation_%

Where:
- Work_ex_GST       = invoice subtotal ex GST, EXCLUDING the levy line itself
- Fuel_Component_%  = contractually agreed fuel share (per supplier, locked)
- Fuel_Escalation_% = stepped band selected by Brisbane Diesel TGP on the work date

Bands (Fact Sheet Stepped Surcharge Table):
    1.70 - 1.86  ->  0%
    1.87 - 2.03  ->  5%
    2.04 - 2.20  -> 10%
    2.21 - 2.37  -> 15%
    2.38 - 2.54  -> 20%
    2.55 - 2.71  -> 25%
    2.72 - 2.88  -> 30%
    2.89 - 3.05  -> 35%
    3.06 - 3.22  -> 40%
    3.23 - 3.39  -> 45%
    3.40 - 3.56  -> 50%
    3.57 - 3.73  -> 55%
    3.74 - 3.90  -> 60%
    3.91 - 4.00  -> 65% (cap)
    > 4.00       -> 65% (cap, no further increase)
    < 1.70       -> 0% (below baseline)

Usage
-----
CLI:
    python fuel_levy_calculator.py verify \\
        --supplier "Vinton Tree Services" \\
        --contract PAR/329E/2021 \\
        --work-date 2026-05-06 \\
        --work-ex-gst 1262.50 \\
        --charged-levy 37.31

    python fuel_levy_calculator.py reverse \\
        --supplier "Vinton Tree Services" \\
        --work-ex-gst 1262.50 \\
        --charged-levy 37.31

Programmatic:
    from fuel_levy_calculator import FuelLevyVerifier
    v = FuelLevyVerifier()
    result = v.verify(
        supplier="Vinton Tree Services",
        contract="PAR/329E/2021",
        work_date="2026-05-06",
        work_ex_gst=1262.50,
        charged_levy=37.31,
    )
    print(result.verdict, result.max_levy, result.variance)
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import sys
from dataclasses import dataclass, field, asdict
from datetime import date, datetime, timedelta
from typing import Optional

# ----- Constants from the Fact Sheet ----------------------------------------

BASELINE_TGP = 1.70
CAP_TGP = 4.00
CAP_ESCALATION = 0.65
BAND_WIDTH = 0.17  # ($ per litre, per band)
STEP = 0.05        # (escalation increment per band)

# Stale-TGP behaviour: warn at 5 business days, refuse at 15 business days
STALE_WARN_DAYS = 5
STALE_REFUSE_DAYS = 15

# Bands, generated from the Fact Sheet constants. Inclusive at both ends.
BANDS = []
for i in range(14):  # 14 bands from baseline through to cap
    lo = round(BASELINE_TGP + (i * BAND_WIDTH), 2)
    hi = round(lo + BAND_WIDTH - 0.01, 2)
    esc = round(i * STEP, 2)
    BANDS.append((lo, hi, esc))
# Manually correct the final cap band to end exactly at 4.00 and esc 0.65
BANDS[-1] = (3.91, 4.00, 0.65)

# ----- Data files -----------------------------------------------------------

SKILL_DIR = os.path.dirname(os.path.abspath(__file__))
FUEL_COMPONENTS_PATH = os.path.join(SKILL_DIR, "fuel_components_register.json")
BRANCH_PROPOSALS_PATH = os.path.join(SKILL_DIR, "branch_fuel_levy_proposals.json")
TGP_SERIES_PATH = os.path.join(SKILL_DIR, "brisbane_diesel_tgp.csv")

# ----- Status taxonomy ------------------------------------------------------
# Decisive verdicts. Each one maps to exactly one operational next step.

STATUS_OK_EXACT = "OK_EXACT_MATCH"            # pay at face value
STATUS_OK_UNDER = "OK_SUPPLIER_UNDER_CLAIM"   # pay at face value, optionally note
STATUS_OVER_REJECT = "OVER_CLAIM_REJECT"      # supplier exceeded ceiling, cap or reject
STATUS_OK_NO_LEVY = "OK_NO_LEVY_BELOW_BASELINE"  # TGP below baseline, supplier should not have charged
STATUS_BLOCK_NO_FUEL_COMPONENT = "BLOCK_SUPPLIER_NOT_IN_REGISTER"
STATUS_BLOCK_BRANCH_PROPOSAL_ONLY = "BLOCK_BRANCH_PROPOSAL_NO_VARIATION"
STATUS_BLOCK_NO_TGP = "BLOCK_NO_TGP_FOR_WORK_DATE"
STATUS_BLOCK_TGP_STALE = "BLOCK_TGP_SERIES_TOO_STALE"

# Match/mismatch tolerance in dollars. The levy lines are reported to the cent
# by suppliers, so anything within 1 cent is treated as an exact match.
TOLERANCE = 0.01


# ----- Dataclasses ----------------------------------------------------------

@dataclass
class TGPLookup:
    """Result of looking up the TGP for a work date."""
    work_date: date
    source_date: Optional[date]
    cents_per_litre_incl_gst: Optional[float]
    dollars_per_litre_incl_gst: Optional[float]
    days_stale: Optional[int]  # business days between source and work
    band_low: Optional[float]
    band_high: Optional[float]
    escalation: Optional[float]
    available: bool
    stale_warning: bool
    stale_refusal: bool
    note: str = ""


@dataclass
class VerificationResult:
    """Decisive verdict for a single invoice line."""
    status: str
    verdict: str
    action: str
    max_levy: Optional[float]
    variance: Optional[float]  # charged minus max, +ve = supplier over, -ve = under
    inputs: dict = field(default_factory=dict)

    def to_dict(self) -> dict:
        return asdict(self)

    def pretty(self) -> str:
        lines = [
            f"Status:    {self.status}",
            f"Verdict:   {self.verdict}",
            f"Action:    {self.action}",
        ]
        if self.max_levy is not None:
            lines.append(f"Max levy:  ${self.max_levy:,.2f}")
        if self.variance is not None:
            sign = "+" if self.variance >= 0 else ""
            lines.append(f"Variance:  {sign}${self.variance:,.2f}  (charged - max)")
        if self.inputs:
            lines.append("Inputs used:")
            for k, v in self.inputs.items():
                lines.append(f"  {k}: {v}")
        return "\n".join(lines)


# ----- The verifier ---------------------------------------------------------

class FuelLevyVerifier:
    """
    Loads the Fuel Components register and Brisbane Diesel TGP series, then
    verifies a supplier-charged levy against the Council formula. Returns a
    decisive verdict with a defined next action.
    """

    def __init__(
        self,
        components_path: str = FUEL_COMPONENTS_PATH,
        tgp_series_path: str = TGP_SERIES_PATH,
        proposals_path: str = BRANCH_PROPOSALS_PATH,
    ):
        self.components_path = components_path
        self.tgp_series_path = tgp_series_path
        self.proposals_path = proposals_path
        self.components = self._load_components()
        self.proposals = self._load_proposals()
        self.tgp = self._load_tgp_series()

    # -- Loaders --

    def _load_components(self) -> dict:
        with open(self.components_path, "r") as f:
            data = json.load(f)
        # Normalise supplier names to lowercase for matching
        return {entry["supplier"].lower(): entry for entry in data["suppliers"]}

    def _load_proposals(self) -> dict:
        """Load the Branch fuel levy proposals register, if present.

        Returns a dict keyed by lowercased supplier name. Returns an empty
        dict if the file is missing; the contract-variations register is the
        authoritative source and the proposals register only enriches the
        BLOCK verdict text.
        """
        if not os.path.exists(self.proposals_path):
            return {}
        with open(self.proposals_path, "r") as f:
            data = json.load(f)
        return {entry["supplier"].lower(): entry for entry in data.get("suppliers", [])}

    def _load_tgp_series(self) -> dict:
        """Returns {date: cents_per_litre_incl_gst}."""
        tgp = {}
        with open(self.tgp_series_path, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                d = datetime.strptime(row["date"], "%Y-%m-%d").date()
                tgp[d] = float(row["cents_per_litre_incl_gst"])
        return tgp

    # -- Public API --

    def verify(
        self,
        supplier: str,
        contract: str,
        work_date,  # date or "YYYY-MM-DD" str
        work_ex_gst: float,
        charged_levy: float,
        multi_day_convention: str = "earliest",
    ) -> VerificationResult:
        """
        Decisively verify a single invoice line.

        Args:
            supplier: supplier name (case-insensitive lookup)
            contract: contract reference (for the audit log; not used in maths)
            work_date: date of work (the levy is selected by the TGP on this day)
            work_ex_gst: invoice subtotal ex GST, EXCLUDING the levy line itself
            charged_levy: the supplier's levy line ex GST
            multi_day_convention: 'earliest', 'latest' (for cross-day works)

        Returns:
            VerificationResult with status, verdict, action, max_levy, variance.
        """
        if isinstance(work_date, str):
            work_date = datetime.strptime(work_date, "%Y-%m-%d").date()

        inputs = {
            "supplier": supplier,
            "contract": contract,
            "work_date": work_date.isoformat(),
            "work_ex_gst": round(work_ex_gst, 2),
            "charged_levy": round(charged_levy, 2),
        }

        # Step 1: resolve Fuel Component from the contract-variations register
        comp_entry = self.components.get(supplier.lower())
        if comp_entry is None:
            # Not in the authoritative register. Check the proposals register
            # so the BLOCK verdict can name the proposed rate and sense-check
            # the charged levy against it.
            proposal = self.proposals.get(supplier.lower())
            if proposal is not None:
                inputs["branch_proposal"] = {
                    "contract": proposal.get("contract"),
                    "proposed_rate_text": proposal.get("proposed_rate_text"),
                    "proposed_flat_rate_pct": proposal.get("proposed_flat_rate_pct"),
                    "model_type": proposal.get("model_type"),
                    "source_document": proposal.get("source_document"),
                    "status": proposal.get("status"),
                }
                proposed_pct = proposal.get("proposed_flat_rate_pct")
                if proposed_pct is not None and work_ex_gst > 0:
                    proposed_amount = round(work_ex_gst * proposed_pct, 2)
                    inputs["sense_check_vs_proposal"] = {
                        "proposed_flat_rate_pct": proposed_pct,
                        "proposed_amount": proposed_amount,
                        "variance_vs_proposed": round(charged_levy - proposed_amount, 2),
                        "effective_rate_pct": round(charged_levy / work_ex_gst * 100, 4),
                    }
                verdict_text = (
                    f"Supplier '{supplier}' is in the Branch fuel levy proposals "
                    f"register at '{proposal.get('proposed_rate_text')}' under "
                    f"{proposal.get('contract')}, but no Council-issued contract "
                    f"variation letter is on file. A Branch proposal does not "
                    f"authorise payment of a levy line; only a sighted contract "
                    f"variation does."
                )
                if str(proposal.get("model_type", "")).startswith("flat"):
                    verdict_text += (
                        " The proposal is a flat-percentage model, which deviates "
                        "from the Fact Sheet stepped formula and would require "
                        "Procurement to confirm the deviation is authorised."
                    )
                return VerificationResult(
                    status=STATUS_BLOCK_BRANCH_PROPOSAL_ONLY,
                    verdict=verdict_text,
                    action=(
                        f"Block the levy line. Hold pending the Council-issued "
                        f"contract variation under {proposal.get('contract')}. "
                        f"Once received, add the supplier to "
                        f"fuel_components_register.json with the locked Fuel "
                        f"Component % and the variation letter as "
                        f"source_document, then re-run."
                    ),
                    max_levy=None,
                    variance=None,
                    inputs=inputs,
                )
            return VerificationResult(
                status=STATUS_BLOCK_NO_FUEL_COMPONENT,
                verdict=(
                    f"Supplier '{supplier}' is in neither the Fuel Components "
                    f"register nor the Branch fuel levy proposals register."
                ),
                action=(
                    "Block payment. Locate the contract variation letter or "
                    "schedule that defines the supplier's Fuel Component %, "
                    "add the supplier to fuel_components_register.json with a "
                    "source document reference, then re-run."
                ),
                max_levy=None,
                variance=None,
                inputs=inputs,
            )
        fuel_component = comp_entry["fuel_component_pct"]
        inputs["fuel_component_pct"] = fuel_component
        inputs["fuel_component_source"] = comp_entry.get("source_document", "")

        # Step 2: look up the TGP for the work date
        lookup = self.get_tgp(work_date)
        inputs["tgp_lookup"] = {
            "source_date": lookup.source_date.isoformat() if lookup.source_date else None,
            "cents_per_litre_incl_gst": lookup.cents_per_litre_incl_gst,
            "dollars_per_litre_incl_gst": lookup.dollars_per_litre_incl_gst,
            "days_stale": lookup.days_stale,
            "band_low": lookup.band_low,
            "band_high": lookup.band_high,
            "escalation_pct": lookup.escalation,
            "note": lookup.note,
        }

        if not lookup.available:
            return VerificationResult(
                status=STATUS_BLOCK_NO_TGP,
                verdict=(
                    f"No Brisbane Diesel TGP available on or before "
                    f"{work_date.isoformat()}. The TGP series in "
                    f"brisbane_diesel_tgp.csv is too short for this work date."
                ),
                action=(
                    "Block payment. Refresh brisbane_diesel_tgp.csv from the AIP "
                    "Brisbane Diesel terminal gate price series "
                    "(https://www.aip.com.au/pricing/terminal-gate-prices), "
                    "include the work date, then re-run."
                ),
                max_levy=None,
                variance=None,
                inputs=inputs,
            )

        if lookup.stale_refusal:
            return VerificationResult(
                status=STATUS_BLOCK_TGP_STALE,
                verdict=(
                    f"Latest TGP in series is from {lookup.source_date.isoformat()}, "
                    f"which is {lookup.days_stale} business days before the work "
                    f"date. This exceeds the {STALE_REFUSE_DAYS}-business-day "
                    f"refusal threshold."
                ),
                action=(
                    "Block payment. Refresh brisbane_diesel_tgp.csv from AIP "
                    "with the actual TGP for the work date, then re-run. "
                    "Do not extrapolate or guess the TGP."
                ),
                max_levy=None,
                variance=None,
                inputs=inputs,
            )

        # Step 3: compute the maximum permitted levy
        max_levy = round(work_ex_gst * fuel_component * lookup.escalation, 2)
        variance = round(charged_levy - max_levy, 2)
        inputs["max_levy"] = max_levy
        inputs["variance"] = variance
        if lookup.stale_warning:
            inputs["stale_warning"] = (
                f"TGP source date is {lookup.days_stale} business days before "
                f"the work date (warn threshold {STALE_WARN_DAYS}). Result is "
                f"calculated, however refreshing the TGP series is advised "
                f"before formally clearing."
            )

        # Step 4: classify
        # If TGP is below baseline, escalation is 0 and no levy applies
        if lookup.escalation == 0:
            if charged_levy <= TOLERANCE:
                return VerificationResult(
                    status=STATUS_OK_EXACT,
                    verdict=(
                        f"TGP ${lookup.dollars_per_litre_incl_gst:.3f}/L is at or "
                        f"below the $1.70/L baseline. No levy applies and none "
                        f"was charged."
                    ),
                    action="Pay invoice at face value.",
                    max_levy=0.00,
                    variance=0.00,
                    inputs=inputs,
                )
            return VerificationResult(
                status=STATUS_OVER_REJECT,
                verdict=(
                    f"TGP ${lookup.dollars_per_litre_incl_gst:.3f}/L is at or "
                    f"below the $1.70/L baseline, so no levy is permitted. "
                    f"Supplier has charged ${charged_levy:,.2f}."
                ),
                action=(
                    f"Reject the levy line. Request the supplier remove the "
                    f"${charged_levy:,.2f} levy and reissue, or cap the levy at "
                    f"$0.00 per the Fact Sheet 'lower of' rule."
                ),
                max_levy=0.00,
                variance=variance,
                inputs=inputs,
            )

        # TGP is in a banded zone, normal verification
        if abs(variance) <= TOLERANCE:
            return VerificationResult(
                status=STATUS_OK_EXACT,
                verdict=(
                    f"Charged levy ${charged_levy:,.2f} matches the maximum "
                    f"permitted ${max_levy:,.2f} to the cent. TGP "
                    f"${lookup.dollars_per_litre_incl_gst:.3f}/L sits in band "
                    f"${lookup.band_low:.2f}-${lookup.band_high:.2f} "
                    f"(escalation {lookup.escalation*100:.0f}%)."
                ),
                action="Pay invoice at face value.",
                max_levy=max_levy,
                variance=variance,
                inputs=inputs,
            )

        if variance < 0:
            return VerificationResult(
                status=STATUS_OK_UNDER,
                verdict=(
                    f"Charged levy ${charged_levy:,.2f} is under the maximum "
                    f"permitted ${max_levy:,.2f} by ${-variance:,.2f}. The Fact "
                    f"Sheet 'lower of' rule applies."
                ),
                action=(
                    f"Pay invoice at face value (${charged_levy:,.2f}). Council "
                    f"benefits from the supplier under-claim. Optionally note "
                    f"the discrepancy back to the supplier so they can correct "
                    f"the rate prospectively."
                ),
                max_levy=max_levy,
                variance=variance,
                inputs=inputs,
            )

        # variance > 0: supplier has over-charged
        return VerificationResult(
            status=STATUS_OVER_REJECT,
            verdict=(
                f"Charged levy ${charged_levy:,.2f} exceeds the maximum "
                f"permitted ${max_levy:,.2f} by ${variance:,.2f}. TGP "
                f"${lookup.dollars_per_litre_incl_gst:.3f}/L sits in band "
                f"${lookup.band_low:.2f}-${lookup.band_high:.2f} "
                f"(escalation {lookup.escalation*100:.0f}%)."
            ),
            action=(
                f"Reject the levy line as charged. Either request the supplier "
                f"reissue with the levy capped at ${max_levy:,.2f} per the "
                f"'lower of' rule, or pay the work value and process the "
                f"${variance:,.2f} excess separately as a creditor adjustment."
            ),
            max_levy=max_levy,
            variance=variance,
            inputs=inputs,
        )

    def reverse_engineer(
        self,
        work_ex_gst: float,
        charged_levy: float,
        supplier: Optional[str] = None,
    ) -> dict:
        """
        Given a work value and a charged levy, infer what TGP band and Fuel
        Component the supplier used. If a supplier is provided, the Fuel
        Component is taken from the register (locked) and only the escalation
        is inferred. If no supplier, all band x component splits are returned.

        Returns:
            dict with combined_rate, candidates (list of {esc%, fuel_comp%}),
            and best_match (the candidate with the cleanest match to a known
            band, given the supplier's locked Fuel Component if available).
        """
        if work_ex_gst <= 0:
            raise ValueError("work_ex_gst must be positive")
        combined_rate = charged_levy / work_ex_gst

        result = {
            "work_ex_gst": round(work_ex_gst, 2),
            "charged_levy": round(charged_levy, 2),
            "combined_rate_pct": round(combined_rate * 100, 4),
        }

        if supplier:
            comp_entry = self.components.get(supplier.lower())
            if comp_entry is None:
                result["error"] = (
                    f"Supplier '{supplier}' not in register. Re-run without "
                    f"the supplier argument to see all candidate splits."
                )
                return result
            fuel_component = comp_entry["fuel_component_pct"]
            implied_esc = combined_rate / fuel_component
            # Snap to nearest 5% band
            rounded_esc = round(implied_esc * 20) / 20
            band = _band_for_escalation(rounded_esc)
            result["fuel_component_pct"] = fuel_component
            result["fuel_component_source"] = comp_entry.get("source_document", "")
            result["implied_escalation_pct"] = round(implied_esc * 100, 4)
            result["nearest_band_escalation_pct"] = round(rounded_esc * 100, 2)
            result["nearest_band_tgp_range"] = (
                f"${band[0]:.2f}-${band[1]:.2f}/L" if band else "out of range"
            )
            result["clean_band_match"] = abs(implied_esc - rounded_esc) < 0.001
        else:
            # Try all standard escalations; report the Fuel Component each implies
            candidates = []
            for i in range(14):
                esc = round(i * STEP, 2)
                if esc == 0:
                    continue
                implied_fc = combined_rate / esc
                if 0 < implied_fc < 1:  # plausible range
                    band = _band_for_escalation(esc)
                    candidates.append({
                        "escalation_pct": round(esc * 100, 2),
                        "tgp_range": f"${band[0]:.2f}-${band[1]:.2f}/L" if band else "",
                        "implied_fuel_component_pct": round(implied_fc * 100, 4),
                    })
            result["candidates"] = candidates
        return result

    def get_tgp(self, work_date: date) -> TGPLookup:
        """Look up the TGP on or last-before the work date."""
        if not self.tgp:
            return TGPLookup(
                work_date=work_date, source_date=None,
                cents_per_litre_incl_gst=None, dollars_per_litre_incl_gst=None,
                days_stale=None, band_low=None, band_high=None,
                escalation=None, available=False,
                stale_warning=False, stale_refusal=False,
                note="TGP series is empty."
            )
        # Exact match, or last before
        if work_date in self.tgp:
            source_date = work_date
            note = "Exact TGP available for work date."
        else:
            candidates = [d for d in self.tgp if d <= work_date]
            if not candidates:
                return TGPLookup(
                    work_date=work_date, source_date=None,
                    cents_per_litre_incl_gst=None, dollars_per_litre_incl_gst=None,
                    days_stale=None, band_low=None, band_high=None,
                    escalation=None, available=False,
                    stale_warning=False, stale_refusal=False,
                    note=f"No TGP entry on or before {work_date.isoformat()}."
                )
            source_date = max(candidates)
            note = f"No exact TGP for work date; using last-before {source_date.isoformat()}."
        cents = self.tgp[source_date]
        dollars = cents / 100
        days_stale = _business_days_between(source_date, work_date)
        band = _band_for_tgp(dollars)
        return TGPLookup(
            work_date=work_date,
            source_date=source_date,
            cents_per_litre_incl_gst=round(cents, 2),
            dollars_per_litre_incl_gst=round(dollars, 4),
            days_stale=days_stale,
            band_low=band[0] if band else None,
            band_high=band[1] if band else None,
            escalation=band[2] if band else None,
            available=True,
            stale_warning=days_stale > STALE_WARN_DAYS and days_stale <= STALE_REFUSE_DAYS,
            stale_refusal=days_stale > STALE_REFUSE_DAYS,
            note=note,
        )


# ----- Band helpers ---------------------------------------------------------

def _band_for_tgp(tgp_dollars: float):
    """Return (lo, hi, escalation) for the band containing tgp_dollars."""
    t = round(tgp_dollars, 2)
    if t > CAP_TGP:
        return (3.91, 4.00, CAP_ESCALATION)  # cap
    if t < BASELINE_TGP:
        return (0.0, BASELINE_TGP - 0.01, 0.0)  # below baseline
    for lo, hi, esc in BANDS:
        if lo <= t <= hi:
            return (lo, hi, esc)
    return None


def _band_for_escalation(esc: float):
    """Return (lo, hi) of the TGP band that produces this escalation."""
    for lo, hi, e in BANDS:
        if abs(e - esc) < 0.001:
            return (lo, hi)
    return None


def _business_days_between(start: date, end: date) -> int:
    """Count business days (Mon to Fri) between start and end, inclusive of end."""
    if end <= start:
        return 0
    days = 0
    d = start + timedelta(days=1)
    while d <= end:
        if d.weekday() < 5:
            days += 1
        d += timedelta(days=1)
    return days


# ----- CLI ------------------------------------------------------------------

def _cli():
    p = argparse.ArgumentParser(
        description="LCC Fuel Levy Verifier",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    sub = p.add_subparsers(dest="cmd", required=True)

    v = sub.add_parser("verify", help="Verify a charged levy against the Council ceiling.")
    v.add_argument("--supplier", required=True)
    v.add_argument("--contract", required=True)
    v.add_argument("--work-date", required=True, help="YYYY-MM-DD")
    v.add_argument("--work-ex-gst", required=True, type=float,
                   help="Invoice subtotal ex GST, EXCLUDING the levy line itself.")
    v.add_argument("--charged-levy", required=True, type=float)
    v.add_argument("--convention", default="earliest", choices=["earliest", "latest"],
                   help="For cross-day works (default: earliest, most conservative).")
    v.add_argument("--json", action="store_true", help="Output JSON instead of pretty text.")

    r = sub.add_parser("reverse", help="Reverse-engineer the band/component split.")
    r.add_argument("--supplier", required=False,
                   help="If given, Fuel Component is locked from the register.")
    r.add_argument("--work-ex-gst", required=True, type=float)
    r.add_argument("--charged-levy", required=True, type=float)
    r.add_argument("--json", action="store_true")

    t = sub.add_parser("tgp", help="Look up the TGP and band for a date.")
    t.add_argument("--date", required=True, help="YYYY-MM-DD")

    sub.add_parser("bands", help="Print the full stepped band table.")

    args = p.parse_args()
    v_obj = FuelLevyVerifier()

    if args.cmd == "verify":
        result = v_obj.verify(
            supplier=args.supplier, contract=args.contract,
            work_date=args.work_date, work_ex_gst=args.work_ex_gst,
            charged_levy=args.charged_levy, multi_day_convention=args.convention,
        )
        if args.json:
            print(json.dumps(result.to_dict(), indent=2, default=str))
        else:
            print(result.pretty())

    elif args.cmd == "reverse":
        result = v_obj.reverse_engineer(
            work_ex_gst=args.work_ex_gst, charged_levy=args.charged_levy,
            supplier=args.supplier,
        )
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            for k, v in result.items():
                if isinstance(v, list):
                    print(f"{k}:")
                    for item in v:
                        print(f"  {item}")
                else:
                    print(f"{k}: {v}")

    elif args.cmd == "tgp":
        d = datetime.strptime(args.date, "%Y-%m-%d").date()
        lookup = v_obj.get_tgp(d)
        print(json.dumps(asdict(lookup), indent=2, default=str))

    elif args.cmd == "bands":
        print(f"{'TGP $/L':<16} {'Escalation %':>12}")
        print("-" * 30)
        print(f"{'< $1.70':<16} {0:>11}%")
        for lo, hi, esc in BANDS:
            print(f"${lo:.2f} - ${hi:.2f}    {int(esc*100):>10}%")
        print(f"{'> $4.00':<16} {65:>11}% (cap)")


if __name__ == "__main__":
    _cli()
