"""resolve_employee_pk: PK for a person-attributable Parks cost, date-aware for acting/TEV.
Lookup only. Every acting/TEV/override line returns AMBER: confirm with Parks Finance.
"""
import json, datetime, os
_DIR=os.path.dirname(__file__)
_MAP=json.load(open(os.path.join(_DIR,"employee_pk_map.json")))

def _date(s):
    return datetime.datetime.strptime(s,"%d-%b-%Y").date() if s else None

def resolve_employee_pk(emp_id, invoice_date):
    """invoice_date as 'D-Mon-YYYY' (e.g. 15-Jun-2026). Returns (pk, rag_note)."""
    e=_MAP["employees"].get(str(emp_id))
    if not e:
        return None, "RED: emp_id not in employee_pk_map"
    cut=_date(e["cutover"]); inv=_date(invoice_date) if invoice_date else None
    if cut and inv and e["current_pk"]!=e["revert_pk"]:
        pk=e["current_pk"] if inv<=cut else e["revert_pk"]
        side="current/acting" if inv<=cut else "revert/substantive"
        return pk, f"AMBER acting: {side} (cutover {e['cutover']}); confirm with Parks Finance"
    pk=e["current_pk"]
    if pk is None:
        return None, "RED: cost code does not crosswalk to a Parks PK"
    if e["temp_status"].startswith("override"):
        return pk, "AMBER: manual override on record; "+e["basis"]
    if e["pending_separation"]:
        return pk, "AMBER: pending separation; guard costs after exit date"
    return pk, "GREEN"
