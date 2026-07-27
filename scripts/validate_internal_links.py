from __future__ import annotations
import re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
LINK=re.compile(r"\[[^\]]+\]\(([^)]+)\)")
def main():
    errors=[]; checked=0
    for p in ROOT.rglob("*.md"):
        text=p.read_text(encoding="utf-8")
        for target in LINK.findall(text):
            if target.startswith(("https://","http://","#","mailto:")): continue
            target=target.split("#",1)[0]
            if not target: continue
            dest=(p.parent/target).resolve()
            checked+=1
            if ROOT not in dest.parents and dest!=ROOT:
                errors.append(f"unsafe link {p.relative_to(ROOT)} -> {target}")
            elif not dest.exists():
                errors.append(f"broken link {p.relative_to(ROOT)} -> {target}")
    if errors:
        print("INTERNAL LINKS FAILED")
        for e in errors: print("-",e)
        raise SystemExit(1)
    print(f"INTERNAL LINKS PASSED: {checked}")
if __name__=="__main__":
    main()
