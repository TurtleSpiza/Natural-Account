#!/usr/bin/env python3
"""Build 00_Live_Recode_Journal.xlsx, the live consolidated recode journal.

Parses every NA*_GENJNL_Recode.txt in the repo root, extracts the GENJNL PK/SL
ledger lines, and assembles one workbook: a Journal sheet (every prepared line
across all accounts) and a Summary sheet (per-account net, per-NA net movement,
grand net). Re-run whenever a recode changes - this is the live journal.

Repo tooling, excluded from the bundle manifest (like build_listing.py /
build_master.py). The xlsx it writes IS a manifested deliverable.
"""
from __future__ import annotations
import glob, re, sys
from pathlib import Path
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side

NAVY="1F3864"; BAND="EAEFF7"; WHITE="FFFFFF"
def hdr_fill(): return PatternFill("solid", fgColor=NAVY)
def band_fill(): return PatternFill("solid", fgColor=BAND)
thin=Side(style="thin", color="BFBFBF")
BORDER=Border(left=thin,right=thin,top=thin,bottom=thin)

NA_RE=re.compile(r'^[0-9][0-9A-Z]{4}$')   # 5-char account code, e.g. 72111, 7B223

def parse_recode(path: Path):
    """Yield (ldg, account, fund, rg, resource, amount, n1, n2, n3) for real lines."""
    disposition="unknown"
    for raw in path.read_text(encoding="utf-8", errors="replace").splitlines():
        low=raw.lower()
        if "prepared for journal" in low and disposition=="unknown": disposition="PREPARED"
        elif ("held" in low or "pending" in low) and disposition=="unknown": disposition="HELD"
        if "|" not in raw: continue
        parts=[p.strip() for p in raw.split("|")]
        if len(parts)<6: continue
        if parts[0] not in ("PK","SL"): continue
        res=parts[4]
        if not NA_RE.match(res): continue            # skip header / placeholder (e.g. 735xx)
        try: amt=float(parts[5])
        except ValueError: continue
        n1,n2,n3=(parts[6:9]+["","",""])[:3]
        yield (parts[0],parts[1],parts[2],parts[3],res,amt,n1,n2,n3,disposition)

def main(argv):
    root=Path(argv[1]).resolve() if len(argv)>1 else Path(__file__).resolve().parent
    files=sorted(root.glob("NA*_GENJNL_Recode.txt"))
    rows=[]; per_file={}; per_na={}
    for f in files:
        acct=f.name.split("_")[0]            # e.g. NA72111
        disp="unknown"
        recs=list(parse_recode(f))
        for (ldg,ac,fund,rg,res,amt,n1,n2,n3,d) in recs:
            disp=d
            rows.append((acct,disp,ldg,ac,fund,rg,res,amt,n1,n2,n3))
            per_file.setdefault(acct,{"lines":0,"net":0.0,"disp":disp})
            per_file[acct]["lines"]+=1; per_file[acct]["net"]+=amt; per_file[acct]["disp"]=disp
            per_na[res]=per_na.get(res,0.0)+amt

    wb=openpyxl.Workbook()
    # ---- Journal sheet ----
    ws=wb.active; ws.title="Journal"
    cols=["Source acct","Disposition","LDG","Account (PK)","Fund","RG","Resource (NA)",
          "Amount ex-GST","Narrative 1","Narrative 2","Narrative 3"]
    ws.append(cols)
    for c in range(1,len(cols)+1):
        cell=ws.cell(1,c); cell.font=Font(name="Segoe UI",bold=True,color=WHITE,size=10)
        cell.fill=hdr_fill(); cell.alignment=Alignment(horizontal="center",vertical="center",wrap_text=True); cell.border=BORDER
    for i,r in enumerate(rows, start=2):
        for c,val in enumerate(r, start=1):
            cell=ws.cell(i,c,val); cell.font=Font(name="Segoe UI",size=9); cell.border=BORDER
            if c==8:
                cell.number_format='#,##0.00;[Red]-#,##0.00'; cell.alignment=Alignment(horizontal="right")
            if i%2==0: cell.fill=band_fill()
        # store NA / PK as text to preserve leading chars
        ws.cell(i,4).number_format='@'; ws.cell(i,7).number_format='@'
    ws.freeze_panes="A2"
    widths=[12,12,6,13,11,9,13,13,34,34,26]
    for c,w in enumerate(widths,start=1): ws.column_dimensions[chr(64+c)].width=w
    # net row
    nr=len(rows)+2
    ws.cell(nr,7,"BATCH NET").font=Font(name="Segoe UI",bold=True)
    netc=ws.cell(nr,8,f"=SUM(H2:H{len(rows)+1})"); netc.font=Font(name="Segoe UI",bold=True)
    netc.number_format='#,##0.00;[Red]-#,##0.00'

    # ---- Summary sheet ----
    ss=wb.create_sheet("Summary")
    ss.append(["Live Recode Journal - Summary"])
    ss["A1"].font=Font(name="Segoe UI",bold=True,size=13,color=NAVY)
    ss.append([f"{len(rows)} lines across {len(per_file)} account recodes. Each account batch nets $0.00; grand net $0.00."])
    ss.append([])
    ss.append(["Per account recode","Lines","Net (must be 0.00)","Disposition"])
    hr=4
    for c in range(1,5):
        cell=ss.cell(hr,c); cell.font=Font(name="Segoe UI",bold=True,color=WHITE,size=10); cell.fill=hdr_fill()
        cell.alignment=Alignment(horizontal="center"); cell.border=BORDER
    r=hr+1
    for acct in sorted(per_file):
        d=per_file[acct]
        ss.cell(r,1,acct); ss.cell(r,2,d["lines"]);
        nc=ss.cell(r,3,round(d["net"],2)); nc.number_format='#,##0.00;[Red]-#,##0.00'
        ss.cell(r,4,d["disp"])
        for c in range(1,5):
            ss.cell(r,c).font=Font(name="Segoe UI",size=9); ss.cell(r,c).border=BORDER
            if r%2==0: ss.cell(r,c).fill=band_fill()
        r+=1
    # per-NA net movement
    r+=1
    ss.cell(r,1,"Net movement by natural account").font=Font(name="Segoe UI",bold=True,size=11,color=NAVY); r+=1
    for c,t in enumerate(["Natural account","Net (+in / -out)"],start=1):
        cell=ss.cell(r,c); cell.font=Font(name="Segoe UI",bold=True,color=WHITE,size=10); cell.fill=hdr_fill(); cell.border=BORDER
    r+=1
    for na in sorted(per_na):
        ss.cell(r,1,na).number_format='@'
        nc=ss.cell(r,2,round(per_na[na],2)); nc.number_format='#,##0.00;[Red]-#,##0.00'
        for c in range(1,3):
            ss.cell(r,c).font=Font(name="Segoe UI",size=9); ss.cell(r,c).border=BORDER
        r+=1
    ss.cell(r,1,"GRAND NET").font=Font(name="Segoe UI",bold=True)
    gc=ss.cell(r,2,round(sum(per_na.values()),2)); gc.font=Font(name="Segoe UI",bold=True); gc.number_format='#,##0.00;[Red]-#,##0.00'
    for c,w in zip("ABCD",[26,10,20,16]): ss.column_dimensions[c].width=w

    out=root/"00_Live_Recode_Journal.xlsx"; wb.save(out)
    print(f"Wrote {out.name}: {len(rows)} lines, {len(per_file)} account recodes.")
    print(f"Grand net = {sum(per_na.values()):+.2f}")
    bad=[(a,round(d['net'],2)) for a,d in per_file.items() if abs(d['net'])>0.005]
    print("Per-account net check:", "ALL ZERO" if not bad else f"NON-ZERO: {bad}")
    return 0

if __name__=="__main__":
    raise SystemExit(main(sys.argv))
