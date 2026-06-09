"""
ABN validator and supplier intelligence module for tax-invoice-compliance.

Three primary functions:
1. validate_checksum(abn): offline ATO checksum test, returns True/False
2. lookup_abr(abn): fetches the ABR public-register record, returns structured dict
3. lookup_asic_business_names(abn, business_name): fetches the ASIC Business Names
   register entry, returns structured dict

Plus assess_concerns(abr_record, asic_record, invoice_data) which runs the
red-flags catalogue against gathered data and returns a list of concern
objects ready for the verdict engine.

The ABR and ASIC fetchers use stdlib urllib only, so the script runs in
any Python 3.8+ environment without external dependencies. The HTML parsing
uses regex against the known table structure of the ABR and ASIC pages,
which is stable across years.

CLI usage:

    python abn_validator.py checksum 33078502894
    python abn_validator.py abr 33078502894
    python abn_validator.py asic 33078502894
    python abn_validator.py verify 33078502894 --supplier-name "Fire Management Training"
"""

import argparse
import json
import re
import sys
import urllib.request
import urllib.error
from datetime import date, datetime, timezone
from typing import Any


# 1.0 Checksum validation

ABN_WEIGHTS = [10, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19]


def _clean_abn(abn: str) -> str:
    """Strip whitespace and hyphens from a possibly-formatted ABN."""
    return re.sub(r"[\s\-]", "", abn or "")


def validate_checksum(abn: str) -> bool:
    """
    Test an ABN against the ATO checksum algorithm. Mathematical, offline.

    1. Strip whitespace and hyphens.
    2. Confirm exactly 11 digits.
    3. Subtract 1 from the first digit.
    4. Multiply each digit by the corresponding weight.
    5. Sum the weighted products.
    6. Valid if and only if sum mod 89 equals 0.
    """
    cleaned = _clean_abn(abn)
    if not cleaned.isdigit() or len(cleaned) != 11:
        return False
    digits = [int(d) for d in cleaned]
    digits[0] -= 1
    total = sum(d * w for d, w in zip(digits, ABN_WEIGHTS))
    return total % 89 == 0


# 2.0 ABR public-register fetch

ABR_VIEW_URL = "https://abr.business.gov.au/ABN/View?abn={abn}"
ABR_HISTORY_URL = "https://abr.business.gov.au/AbnHistory/View?id={abn}"

_DEFAULT_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (compatible; tax-invoice-compliance-skill/1.0; "
        "+https://logan.qld.gov.au)"
    )
}


def _fetch(url: str, timeout: int = 15) -> str:
    """Fetch a URL and return the response body decoded as UTF-8."""
    req = urllib.request.Request(url, headers=_DEFAULT_HEADERS)
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        raw = resp.read()
    try:
        return raw.decode("utf-8")
    except UnicodeDecodeError:
        return raw.decode("latin-1", errors="replace")


def _strip_tags(html: str) -> str:
    """Crude HTML-to-text. Strip tags, collapse whitespace."""
    text = re.sub(r"<[^>]+>", " ", html)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def _row_value(html: str, label: str) -> str | None:
    """
    Pull the value for a labelled row out of the ABR HTML.

    The ABR uses table rows with <th>Label:</th><td>Value</td>. The label
    has a trailing colon. The value cell can contain nested spans and
    divs with itemprop microdata attributes. We strip all tags and
    HTML entities (&nbsp;, &amp;) and collapse whitespace.
    """
    pattern = (
        r"<th[^>]*>\s*" + re.escape(label) +
        r"\s*:?\s*</th>\s*<td[^>]*>(.*?)</td>"
    )
    match = re.search(pattern, html, re.IGNORECASE | re.DOTALL)
    if not match:
        return None
    value = match.group(1)
    # Strip nested tags
    value = re.sub(r"<[^>]+>", " ", value)
    # Decode common HTML entities
    value = value.replace("&nbsp;", " ").replace("&amp;", "&")
    value = value.replace("&lt;", "<").replace("&gt;", ">")
    value = re.sub(r"\s+", " ", value)
    return value.strip() or None


def lookup_abr(abn: str) -> dict[str, Any]:
    """
    Fetch the ABR public-register record for an ABN.

    Returns a dict with keys: abn, entity_name, abn_status, abn_status_from,
    entity_type, gst_status, gst_from, business_location_state,
    business_location_postcode, business_names, trading_names, source_url,
    fetched_at, fetch_error.
    """
    cleaned = _clean_abn(abn)
    result: dict[str, Any] = {
        "abn": cleaned,
        "source_url": ABR_VIEW_URL.format(abn=cleaned),
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "fetch_error": None,
    }
    try:
        html = _fetch(result["source_url"])
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as e:
        result["fetch_error"] = str(e)
        return result

    result["entity_name"] = _row_value(html, "Entity name")
    result["abn_status"] = _row_value(html, "ABN status")
    result["entity_type"] = _row_value(html, "Entity type")
    result["gst_status"] = _row_value(html, "Goods &amp; Services Tax (GST)")
    if result["gst_status"] is None:
        result["gst_status"] = _row_value(html, "Goods & Services Tax (GST)")
    result["business_location_state"] = _row_value(html, "Main business location")

    # Business names and trading names appear in tables further down the page.
    # Each row has two <td> cells: name (which may include an external-link
    # icon <img>) and the "From" date. We extract the first <td> of each
    # row and strip all nested tags.
    def _extract_names_from_section(section_html: str) -> list[str]:
        names: list[str] = []
        # Match each <tr> that contains exactly two <td> cells.
        # Exclude rows where the first <td> uses colspan (the intro paragraph)
        # by requiring the first <td> tag to NOT contain 'colspan'.
        rows = re.finditer(
            r"<tr[^>]*>\s*<td(?![^>]*colspan)[^>]*>(.*?)</td>\s*"
            r"<td[^>]*>.*?</td>\s*</tr>",
            section_html, re.DOTALL | re.IGNORECASE
        )
        for r in rows:
            raw = r.group(1)
            text = re.sub(r"<[^>]+>", " ", raw)
            text = text.replace("&nbsp;", " ").replace("&amp;", "&")
            text = text.replace("&lt;", "<").replace("&gt;", ">")
            text = re.sub(r"\s+", " ", text).strip()
            if not text or text in names:
                continue
            # Skip rows that are pure dates
            if re.match(r"^\d{1,2}\s+\w{3,9}\s+\d{4}$", text):
                continue
            # Skip overly long rows (intro paragraphs, not names)
            if len(text) > 150:
                continue
            names.append(text)
        return names

    business_names_block = re.search(
        r"Business name\(s\)(.*?)(?:Trading name\(s\)|Deductible gift|ABN Lookup)",
        html, re.IGNORECASE | re.DOTALL
    )
    result["business_names"] = (
        _extract_names_from_section(business_names_block.group(1))
        if business_names_block else []
    )

    trading_names_block = re.search(
        r"Trading name\(s\)(.*?)(?:Deductible gift|ABN Lookup|</body>|$)",
        html, re.IGNORECASE | re.DOTALL
    )
    result["trading_names"] = (
        _extract_names_from_section(trading_names_block.group(1))
        if trading_names_block else []
    )

    return result


# 3.0 ASIC Business Names register fetch

ASIC_BUSINESS_NAMES_URL = (
    "https://connectonline.asic.gov.au/RegistrySearch/faces/landing/"
    "ProfessionalRegisters.jspx?_adf.ctrl-state={abn}"
)


def lookup_asic_business_names(business_name: str) -> dict[str, Any]:
    """
    The ASIC Business Names register does not expose a clean public JSON
    or GET-fetchable URL keyed by ABN. The user-facing search at
    connectonline.asic.gov.au is an interactive JSF application that
    requires session state and a POST.

    For practical use inside the tax-invoice-compliance skill, this
    function returns a placeholder structure flagging that the ASIC
    check requires either:

    (a) the user supplying the ASIC Business Name extract directly
        (as the user did in the worked example), or
    (b) the skill operator using the web_fetch tool against
        connectonline.asic.gov.au with the business name as the query

    If a future ASIC public API becomes available, this function should
    be the integration point.
    """
    return {
        "business_name": business_name,
        "lookup_method": "manual",
        "instructions": (
            "Go to connectonline.asic.gov.au, choose Business names register, "
            "search by name '" + business_name + "', confirm Status is "
            "Registered, confirm the Holder ABN matches the invoice ABN, "
            "confirm Principal place of business is plausible. Or use the "
            "ABR's listed business names from lookup_abr, which mirrors "
            "the ASIC register for ABR-listed business names."
        ),
    }


# 4.0 Red flags scan

# Loaded from red_flags.json at runtime
def _load_red_flags(path: str = "red_flags.json") -> list[dict[str, Any]]:
    import os
    full_path = os.path.join(os.path.dirname(__file__), path)
    try:
        with open(full_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def assess_concerns(
    abr_record: dict[str, Any],
    invoice_data: dict[str, Any] | None = None,
) -> list[dict[str, Any]]:
    """
    Run the red-flags catalogue against the gathered supplier data
    and the invoice data. Return a list of concern objects each with
    severity (BLOCK / FIXABLE / NOTE), code, and human-readable
    description.

    invoice_data is expected to be a dict with optional keys:
        supplier_name_on_invoice, gst_amount, total_inc_gst,
        invoice_date (ISO yyyy-mm-dd), buyer_identity_present (bool)
    """
    concerns: list[dict[str, Any]] = []
    inv = invoice_data or {}

    if abr_record.get("fetch_error"):
        concerns.append({
            "severity": "BLOCK",
            "code": "ABR_UNREACHABLE",
            "description": (
                "Could not reach the ABR public register: " +
                str(abr_record["fetch_error"]) +
                ". Retry when the register is available."
            ),
        })
        return concerns

    if abr_record.get("abn_status") and "active" not in abr_record["abn_status"].lower():
        concerns.append({
            "severity": "BLOCK",
            "code": "ABN_NOT_ACTIVE",
            "description": (
                "ABN status on the ABR is '" + abr_record["abn_status"] +
                "', not Active. The supplier is not entitled to charge GST "
                "on an inactive ABN."
            ),
        })

    gst_status = (abr_record.get("gst_status") or "").lower()
    # The ABR returns one of: "Registered from <date>", "Not currently
    # registered", "Cancelled from <date>", or similar. Anything that
    # does not start with "registered" and is non-empty means not currently
    # registered for GST.
    gst_not_registered = bool(gst_status) and not gst_status.startswith("registered")
    if inv.get("gst_amount") and float(inv.get("gst_amount") or 0) > 0:
        if gst_not_registered:
            concerns.append({
                "severity": "BLOCK",
                "code": "GST_CHARGED_WITHOUT_REGISTRATION",
                "description": (
                    "GST is charged on the invoice but the ABR shows the "
                    "supplier is not GST-registered (status: '" +
                    (abr_record.get("gst_status") or "unknown") + "'). "
                    "This is unlawful and forfeits the recipient's input "
                    "tax credit."
                ),
            })

    supplier_name = (inv.get("supplier_name_on_invoice") or "").strip().upper()
    if supplier_name:
        candidates = set()
        if abr_record.get("entity_name"):
            candidates.add(abr_record["entity_name"].strip().upper())
        for bn in abr_record.get("business_names") or []:
            candidates.add(bn.strip().upper())
        for tn in abr_record.get("trading_names") or []:
            candidates.add(tn.strip().upper())
        if not any(supplier_name in c or c in supplier_name for c in candidates):
            concerns.append({
                "severity": "BLOCK",
                "code": "SUPPLIER_NAME_NOT_RECONCILED",
                "description": (
                    "The supplier name on the invoice ('" + (inv.get("supplier_name_on_invoice") or "") +
                    "') does not match the ABR entity name, any registered "
                    "business name, or any trading name for this ABN. "
                    "Possible misrepresentation or fraud."
                ),
            })

    if inv.get("total_inc_gst"):
        try:
            total = float(inv["total_inc_gst"])
            if total >= 1000 and not inv.get("buyer_identity_present"):
                concerns.append({
                    "severity": "FIXABLE",
                    "code": "MISSING_BUYER_IDENTITY_OVER_1000",
                    "description": (
                        "Invoice total is $1,000 or more. ATO QC 22422 "
                        "requires the buyer's identity or ABN to be shown. "
                        "Request a reissue with the buyer details."
                    ),
                })
        except (TypeError, ValueError):
            pass

    if inv.get("invoice_date"):
        try:
            inv_date = date.fromisoformat(inv["invoice_date"])
            today = date.today()
            if inv_date > today:
                concerns.append({
                    "severity": "BLOCK",
                    "code": "FUTURE_DATED_INVOICE",
                    "description": (
                        "Invoice date is in the future. Future-dated "
                        "invoices are not valid tax invoices and may "
                        "indicate fraud."
                    ),
                })
            age_days = (today - inv_date).days
            if age_days > (365 * 3 + 180):
                concerns.append({
                    "severity": "NOTE",
                    "code": "APPROACHING_4_YEAR_CREDIT_LIMIT",
                    "description": (
                        "Invoice is more than three and a half years old. "
                        "The four-year credit time limit (MT 2024/1) may "
                        "be close to running out. Claim the GST credit "
                        "in the next BAS to preserve the entitlement."
                    ),
                })
        except (TypeError, ValueError):
            pass

    if inv.get("gst_amount") and inv.get("total_inc_gst"):
        try:
            gst = float(inv["gst_amount"])
            total = float(inv["total_inc_gst"])
            expected = round(total / 11, 2)
            if abs(gst - expected) > 0.02:
                concerns.append({
                    "severity": "FIXABLE",
                    "code": "GST_MATH_INCONSISTENT",
                    "description": (
                        "GST amount $" + format(gst, ".2f") +
                        " does not equal Total divided by 11 (expected $" +
                        format(expected, ".2f") + "). Possible "
                        "calculation error or mixed-supply breakdown. "
                        "Request a reissue with a clear breakdown."
                    ),
                })
        except (TypeError, ValueError):
            pass

    return concerns


# 5.0 CLI

def _cmd_checksum(args: argparse.Namespace) -> int:
    ok = validate_checksum(args.abn)
    print("VALID" if ok else "INVALID")
    return 0 if ok else 1


def _cmd_abr(args: argparse.Namespace) -> int:
    record = lookup_abr(args.abn)
    print(json.dumps(record, indent=2, default=str))
    return 0 if not record.get("fetch_error") else 1


def _cmd_asic(args: argparse.Namespace) -> int:
    if not args.business_name:
        print("--business-name is required for ASIC lookup", file=sys.stderr)
        return 2
    record = lookup_asic_business_names(args.business_name)
    print(json.dumps(record, indent=2, default=str))
    return 0


def _cmd_verify(args: argparse.Namespace) -> int:
    if not validate_checksum(args.abn):
        print(json.dumps({
            "verdict": "NON_COMPLIANT_BLOCK",
            "reason": "ABN_CHECKSUM_FAILED",
        }, indent=2))
        return 1
    abr = lookup_abr(args.abn)
    inv = {
        "supplier_name_on_invoice": args.supplier_name,
        "gst_amount": args.gst_amount,
        "total_inc_gst": args.total_inc_gst,
        "invoice_date": args.invoice_date,
        "buyer_identity_present": args.buyer_identity,
    }
    concerns = assess_concerns(abr, inv)
    severities = {c["severity"] for c in concerns}
    if "BLOCK" in severities:
        verdict = "NON_COMPLIANT_BLOCK"
    elif "FIXABLE" in severities:
        verdict = "NON_COMPLIANT_FIXABLE"
    elif "NOTE" in severities:
        verdict = "COMPLIANT_WITH_NOTE"
    else:
        verdict = "COMPLIANT"
    print(json.dumps({
        "verdict": verdict,
        "abn": _clean_abn(args.abn),
        "abr_record": abr,
        "concerns": concerns,
    }, indent=2, default=str))
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        prog="abn_validator",
        description="ABN checksum, ABR lookup, ASIC lookup, and concerns scan",
    )
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_checksum = sub.add_parser("checksum", help="Run the ATO checksum offline")
    p_checksum.add_argument("abn", help="ABN, with or without spaces")
    p_checksum.set_defaults(func=_cmd_checksum)

    p_abr = sub.add_parser("abr", help="Fetch the ABR public-register record")
    p_abr.add_argument("abn", help="ABN, with or without spaces")
    p_abr.set_defaults(func=_cmd_abr)

    p_asic = sub.add_parser("asic", help="ASIC Business Names lookup placeholder")
    p_asic.add_argument("abn", help="ABN, with or without spaces")
    p_asic.add_argument("--business-name", required=True)
    p_asic.set_defaults(func=_cmd_asic)

    p_verify = sub.add_parser("verify", help="End-to-end verification")
    p_verify.add_argument("abn")
    p_verify.add_argument("--supplier-name", default=None)
    p_verify.add_argument("--gst-amount", type=float, default=None)
    p_verify.add_argument("--total-inc-gst", type=float, default=None)
    p_verify.add_argument("--invoice-date", default=None,
                          help="ISO yyyy-mm-dd")
    p_verify.add_argument("--buyer-identity", action="store_true",
                          help="Buyer identity is shown on the invoice")
    p_verify.set_defaults(func=_cmd_verify)

    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
