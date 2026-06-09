"""
techone_loader.py

Canonical TechOne "Ledger Accounts Transactions Table" .xlsx loader.
Materialised from the calamine loader pattern defined in lcc-na-analysis.
Bundled here so every skill that references this loader resolves it
within the package (previously the reference pointed at a path that did
not exist anywhere in the library).

Use the calamine engine, roughly 9x faster than openpyxl on large
multi-account exports, with single-pass header detection that avoids
re-reading the file. Falls back to the default engine automatically if
python-calamine is not installed.

    from techone_loader import load_techone_export
    df = load_techone_export("P10_export.xlsx")

All GL amounts in the result are ex-GST. Multiply by 1.1 for
incl-GST invoice reconciliation. Read the Details narration on every
RJ/GJ line, the dollar amount is meaningless without it.
"""
from __future__ import annotations

CANONICAL_COLUMNS = [
    "Short Description", "Account", "Period", "Reference", "Date",
    "Doc Type", "Details", "Transaction Amount", "Service Code",
    "Description", "Work Order",
]


def load_techone_export(path, header_token: str = "Short Description"):
    """
    Load a TechOne Ledger Accounts Transactions Table .xlsx.

    Exports arrive with parameter/title lines above the real header
    row. This finds the header row by token, slices once (no re-read),
    promotes it, and drops subtotal/rollup rows (those with no
    Reference value).

    Returns a pandas DataFrame. Raises ImportError if pandas is absent
    and ValueError if no header row containing `header_token` is found.
    """
    try:
        import pandas as pd
    except ImportError as e:  # pragma: no cover
        raise ImportError("pandas is required for load_techone_export") from e

    # calamine is ~9x faster on large exports; fall back transparently.
    try:
        raw = pd.read_excel(path, header=None, engine="calamine")
    except (ImportError, ValueError):
        raw = pd.read_excel(path, header=None)

    try:
        header_row = next(
            i for i, r in raw.iterrows()
            if any(header_token in str(v) for v in r.values)
        )
    except StopIteration as e:
        raise ValueError(
            f"no header row containing {header_token!r} found in {path}"
        ) from e

    df = raw.iloc[header_row + 1:].copy()
    df.columns = raw.iloc[header_row].tolist()
    if "Reference" in df.columns:
        df = df[df["Reference"].notna()]   # drop subtotal/rollup rows
    return df


def normalise_service_code(df, col: str = "Service Code"):
    """
    NaN-safe integer service code, never astype(float).astype(int)
    (that crashes on any missing service code). Returns the DataFrame
    with the column coerced to pandas Int64.
    """
    import pandas as pd
    df = df.copy()
    df[col] = pd.to_numeric(df[col], errors="coerce").astype("Int64")
    return df


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("usage: python techone_loader.py <export.xlsx>")
        raise SystemExit(2)
    out = load_techone_export(sys.argv[1])
    print(f"loaded {len(out)} transaction rows; columns: {list(out.columns)}")
