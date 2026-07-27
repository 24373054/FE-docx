from __future__ import annotations
import csv
import re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def read_csv(name):
    with (ROOT/"catalogs"/name).open(encoding="utf-8",newline="") as f:
        return list(csv.DictReader(f))

def main():
    req=read_csv("requirements.csv"); ctr=read_csv("controls.csv"); tst=read_csv("tests.csv"); tr=read_csv("traceability.csv")
    errors=[]
    req_ids={r["requirement_id"] for r in req}; ctr_ids={r["control_id"] for r in ctr}; tst_ids={r["test_id"] for r in tst}
    if len(req_ids)!=len(req): errors.append("duplicate requirement IDs")
    if len(ctr_ids)!=len(ctr): errors.append("duplicate control IDs")
    if len(tst_ids)!=len(tst): errors.append("duplicate test IDs")
    seen_req=set(); seen_ctr=set(); seen_tst=set()
    for row in tr:
        if row["requirement_id"] not in req_ids: errors.append(f"unknown requirement {row['requirement_id']}")
        if row["control_id"] not in ctr_ids: errors.append(f"unknown control {row['control_id']}")
        if row["test_id"] not in tst_ids: errors.append(f"unknown test {row['test_id']}")
        if not (ROOT/row["document_path"]).is_file(): errors.append(f"missing document {row['document_path']}")
        seen_req.add(row["requirement_id"]); seen_ctr.add(row["control_id"]); seen_tst.add(row["test_id"])
    for label,all_ids,seen in [("requirement",req_ids,seen_req),("control",ctr_ids,seen_ctr),("test",tst_ids,seen_tst)]:
        missing=sorted(all_ids-seen)
        if missing: errors.append(f"untraced {label}s: {missing[:10]}")
    # every documented control heading must appear in controls.csv
    documented=set()
    for p in ROOT.glob("[0-8][0-9]-*/*.md"):
        text=p.read_text(encoding="utf-8")
        documented.update(re.findall(r"^###\s+([A-Z0-9-]+-C\d{3})｜",text,re.M))
    missing_catalog=sorted(documented-ctr_ids)
    if missing_catalog: errors.append(f"documented controls absent from catalog: {missing_catalog[:10]}")
    if errors:
        print("TRACEABILITY FAILED")
        for e in errors: print("-",e)
        raise SystemExit(1)
    print(f"TRACEABILITY PASSED: requirements={len(req)} controls={len(ctr)} tests={len(tst)} links={len(tr)}")
if __name__=="__main__":
    main()
