from __future__ import annotations
import argparse
import hashlib
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "10-reference/03-document-index.md"
CONTROL_ROOTS = [f"{i:02d}-" for i in range(11)]

def controlled_markdown():
    docs=[]
    for p in ROOT.rglob("*.md"):
        rel=p.relative_to(ROOT)
        if rel.as_posix() in {"README.md","CONTRIBUTING.md","SECURITY.md","LICENSE.md","catalogs/README.md"}:
            continue
        if rel.parts and any(rel.parts[0].startswith(x) for x in CONTROL_ROOTS):
            docs.append(p)
    return sorted(docs)

def meta(text,key):
    m=re.search(rf"^{re.escape(key)}:\s*(.+?)\s*$", text, re.M)
    return m.group(1).strip() if m else ""

def render():
    rows=[]
    for p in controlled_markdown():
        if p == OUT:
            continue
        text=p.read_text(encoding="utf-8")
        rows.append((p.relative_to(ROOT).as_posix(), meta(text,"document_id"), meta(text,"title"),
                     meta(text,"document_type"), meta(text,"owner"), len(text.splitlines()),
                     hashlib.sha256(text.encode()).hexdigest()[:16]))
    lines=["---","document_id: REF-003","title: 受控文档索引","version: 3.0.0","status: 受控基线",
           "document_type: 参考索引","owner: 配置管理员","approver: 质量负责人",
           "effective_date: 2026-07-27","review_cycle: 每次合并自动更新","classification: 内部受控",
           "---","","# 受控文档索引","",
           f"本索引由脚本生成，共登记 **{len(rows)}** 份受控文档。SHA-256前16位用于发现非预期变化，不能替代完整制品签名。","",
           "|路径|文档ID|标题|类型|责任人|行数|SHA-256前16位|","|---|---|---|---|---|---:|---|"]
    for row in rows:
        lines.append("|`{}`|{}|{}|{}|{}|{}|`{}`|".format(*row))
    lines += ["","## 维护规则","",
              "- 索引不得手工编辑；运行 `python scripts/build_document_index.py` 更新。",
              "- CI使用 `--check` 比较生成结果，发现未同步时拒绝合并。",
              "- 文件移动、编号、标题、类型或责任人变化必须同步评估追踪矩阵和培训材料。",""]
    return "\n".join(lines)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--check",action="store_true")
    args=ap.parse_args()
    expected=render()
    if args.check:
        actual=OUT.read_text(encoding="utf-8") if OUT.exists() else ""
        if actual != expected:
            raise SystemExit("document index is stale; run python scripts/build_document_index.py")
        print("DOCUMENT INDEX PASSED")
    else:
        OUT.parent.mkdir(parents=True,exist_ok=True)
        OUT.write_text(expected,encoding="utf-8")
        print(f"wrote {OUT.relative_to(ROOT)}")
if __name__=="__main__":
    main()
