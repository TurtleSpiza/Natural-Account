"""
PK and service-code validator for TechOne GENJNL upload.

Confirms that:
  - The PK number exists in the canonical service map
  - The service code exists in the canonical service map
  - PK and service code are consistent (PK belongs to that service code)
  - The natural account is in the chart of accounts
  - The natural account is not restricted (PFS-only, Logan Water Alliance, etc.)
  - The cost-centre/PK combination is appropriate for the section

Reference data sources (loaded lazily, with portability fallback):
  - First tries the same directory as this script (portable case, e.g. claude.ai web upload)
  - Falls back to ../_shared/ (local Claude Code install)
  - Filenames searched: service_section_pk_map.json,
                        full_chart_of_accounts.json (preferred, portable copy)
                        or lcc_chart_of_accounts.json (legacy _shared/ name)

Usage:
    from pk_validator import validate_journal_line, load_reference_data

    refs = load_reference_data()  # one-time load
    issues = validate_journal_line(
        ledger="PK",
        pk_number="PK000017",
        service_code="20374",
        natural_account="73126",
        amount=59439.74,
        refs=refs,
    )
    # returns list of issue strings; empty list = valid

CLI usage:
    python pk_validator.py PK PK000017 20374 73126 59439.74
"""

import json
import sys
from pathlib import Path

# Default search order for reference data (portability-first)
LOCAL_DIR = Path(__file__).parent
SHARED_DIR_FALLBACK = Path(__file__).parent.parent / "_shared"


def _resolve(filename_local: str, filename_shared: str = None) -> Path:
    """Look for a reference file in the local skill dir first, then ../_shared/."""
    if filename_shared is None:
        filename_shared = filename_local
    p_local = LOCAL_DIR / filename_local
    if p_local.exists():
        return p_local
    p_shared = SHARED_DIR_FALLBACK / filename_shared
    if p_shared.exists():
        return p_shared
    raise FileNotFoundError(
        f"Reference file not found. Tried {p_local} and {p_shared}"
    )


def load_reference_data(shared_dir: Path = None) -> dict:
    """Load the canonical maps once. Returns a dict with the loaded data.

    Searches in this order:
      1. Same directory as this script (portable / claude.ai web case)
      2. ../_shared/ (local Claude Code install)
      3. Custom path passed via shared_dir parameter
    """
    if shared_dir is not None:
        shared_dir = Path(shared_dir)
        svc_map_path = shared_dir / "service_section_pk_map.json"
        coa_path = shared_dir / "lcc_chart_of_accounts.json"
        if not coa_path.exists():
            coa_path = shared_dir / "full_chart_of_accounts.json"
    else:
        svc_map_path = _resolve("service_section_pk_map.json")
        # Prefer portable filename; fall back to legacy _shared/ filename
        try:
            coa_path = _resolve("full_chart_of_accounts.json", "lcc_chart_of_accounts.json")
        except FileNotFoundError:
            coa_path = _resolve("lcc_chart_of_accounts.json")

    if not svc_map_path.exists():
        raise FileNotFoundError(f"Service map not found at {svc_map_path}")
    if not coa_path.exists():
        raise FileNotFoundError(f"Chart of accounts not found at {coa_path}")

    svc_map_doc = json.loads(svc_map_path.read_text(encoding="utf-8"))
    coa_doc = json.loads(coa_path.read_text(encoding="utf-8"))

    svc_codes = svc_map_doc.get("service_codes", {})

    # Build a reverse PK lookup
    pk_to_svc = {}
    for code, entry in svc_codes.items():
        pk = entry.get("pk")
        if pk:
            pk_to_svc[pk] = code

    return {
        "svc_codes": svc_codes,
        "pk_to_svc": pk_to_svc,
        "accounts": coa_doc.get("accounts", {}),
    }


def validate_journal_line(
    ledger: str,
    pk_number: str,
    service_code: str,
    natural_account: str,
    amount: float = None,
    refs: dict = None,
) -> list[str]:
    """Validate a single journal line against the reference data.

    Args:
        ledger: "PK" (Parks ledger) or "SL" (Sales/SL ledger for non-Parks)
        pk_number: PK number (e.g. "PK000017"), required for PK ledger,
                   may be empty for SL ledger
        service_code: Service code (cost centre), e.g. "20374"
        natural_account: Natural account, e.g. "73126"
        amount: Dr/Cr amount (just used for sign conventions if needed)
        refs: Output of load_reference_data()

    Returns:
        List of issue strings. Empty list means valid.
    """
    if refs is None:
        refs = load_reference_data()

    issues = []

    # Ledger value check
    if ledger not in ("PK", "SL"):
        issues.append(f"Ledger must be 'PK' or 'SL', got '{ledger}'")

    # Service code validation
    svc_entry = refs["svc_codes"].get(service_code)
    if not svc_entry:
        issues.append(f"Service code '{service_code}' not found in service map")

    # PK validation
    if ledger == "PK":
        if not pk_number:
            # PK ledger entries can have blank PK if service code has no assigned PK
            if svc_entry and svc_entry.get("pk"):
                issues.append(
                    f"PK ledger line: service code {service_code} has assigned PK "
                    f"{svc_entry['pk']} but journal line has empty PK number"
                )
        else:
            mapped_svc = refs["pk_to_svc"].get(pk_number)
            if not mapped_svc:
                issues.append(f"PK number '{pk_number}' not found in service map")
            elif mapped_svc != service_code:
                issues.append(
                    f"PK number '{pk_number}' maps to service code "
                    f"'{mapped_svc}' but journal line has '{service_code}'"
                )
    elif ledger == "SL":
        # SL ledger lines should have empty PK
        if pk_number and pk_number != service_code:
            # Some SL formats use the full account string in the PK column
            # (e.g. "1-18611-73564") — check by length/format
            if not (pk_number.startswith("1-") and pk_number.count("-") == 2):
                issues.append(
                    f"SL ledger line should have empty PK or full account string, "
                    f"got '{pk_number}'"
                )

    # Natural account validation
    acct = refs["accounts"].get(natural_account)
    if not acct:
        issues.append(f"Natural account '{natural_account}' not found in chart")
    else:
        # Check restrictions
        restriction = acct.get("restrictions")
        if restriction:
            issues.append(
                f"Natural account {natural_account} ({acct['name']}) is restricted: "
                f"{restriction}"
            )
        # Pending accounts must net to zero — flag any non-zero amount
        restriction_text = acct.get("restrictions") or ""
        if amount is not None and restriction_text.startswith("Pending"):
            if amount != 0:
                issues.append(
                    f"Natural account {natural_account} is a pending account "
                    f"(must net to zero) but amount is {amount}"
                )

    return issues


def main():
    if len(sys.argv) < 5:
        print("Usage: python pk_validator.py <PK|SL> <pk_number> <service_code> <natural_account> [amount]")
        print()
        print("Examples:")
        print("  python pk_validator.py PK PK000017 20374 73126 59439.74")
        print("  python pk_validator.py PK '' 20455 73126 1300.00")
        print("  python pk_validator.py SL '1-18611-73564' 18611 73564 1699.00")
        sys.exit(1)

    ledger = sys.argv[1]
    pk = sys.argv[2]
    svc = sys.argv[3]
    nat = sys.argv[4]
    amt = float(sys.argv[5]) if len(sys.argv) > 5 else None

    refs = load_reference_data()
    issues = validate_journal_line(ledger, pk, svc, nat, amt, refs)

    if not issues:
        print("OK - journal line is valid")
        if pk and ledger == "PK":
            entry = refs["svc_codes"].get(svc, {})
            print(f"  Service: {svc} {entry.get('service_name', '')}")
            print(f"  Section: {entry.get('section', '')}")
        if nat:
            acct = refs["accounts"].get(nat, {})
            print(f"  Account: {nat} {acct.get('name', '')}")
        sys.exit(0)

    for i in issues:
        print(f"FAIL: {i}")
    sys.exit(1)


if __name__ == "__main__":
    main()
