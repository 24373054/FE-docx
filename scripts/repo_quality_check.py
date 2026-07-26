from pathlib import Path
import json,re,sys
r=Path(__file__).resolve().parents[1];fs=[p for p in r.rglob("*") if p.is_file() and ".git" not in p.parts and p.suffix in {".md",".py",".json",".yml",".yaml"}];n=sum(len(p.read_text(encoding="utf-8").splitlines()) for p in fs);e=[];ids={}
for p in fs:
 t=p.read_text(encoding="utf-8")
 if p.suffix==".json":
  try:json.loads(t)
  except Exception as x:e.append(f"JSON {p}:{x}")
 if p.suffix==".md" and p.name not in {"README.md","CONTRIBUTING.md"}:
  m=re.search(r"^document_id: (\S+)",t,re.M)
  if not m:e.append(f"missing id {p}")
  elif m.group(1) in ids:e.append(f"duplicate {m.group(1)}")
  else:ids[m.group(1)]=p
if len(fs)<20:e.append(f"files {len(fs)}<20")
if n<8000:e.append(f"lines {n}<8000")
print(f"Text files: {len(fs)}\nTotal text lines: {n}\nDocument IDs: {len(ids)}")
if e:print("QUALITY GATE FAILED\n"+"\n".join(e));sys.exit(1)
print("QUALITY GATE PASSED")
