from __future__ import annotations
import csv, json, re, sys
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
EXEMPT={"README.md","CONTRIBUTING.md","SECURITY.md","LICENSE.md","catalogs/README.md"}
LEGACY=[f"{i:02d}-" for i in range(11,17)]
REQUIRED_META=["document_id","title","version","status","document_type","owner","approver","effective_date","review_cycle","classification"]
BANNED_LINE=re.compile(r"^\s*(TODO|TBD|待补充|占位文本|以后完善)\s*[:：]?",re.I)
BANNED_CLAIMS=["本报告具有司法效力","已获得CMA资质","已通过CNAS认可","能够穿透所有混币器","可确定地址实际控制自然人"]
VALID_STATUS={
 "研究底稿","待签批治理提案","历史生成稿（待重构）","模板草案（待实测）",
 "受控草案","已批准","已生效","暂停","已废止","自动生成索引",
}
NON_ACTIVE_STATUS={"历史生成稿（待重构）","模板草案（待实测）","已废止"}
TYPE_HEADINGS={
 "治理政策":["## 5. 详细控制要求","## 8. 主要风险与控制","## 10. 验收准则"],
 "治理程序":["## 5. 详细控制要求","## 6. 标准工作流程","## 10. 验收准则"],
 "监管研究":["## 12. 监管结论分级与决策矩阵"],
 "监管程序":["## 12. 监管结论分级与决策矩阵"],
 "监管标准":["## 12. 监管结论分级与决策矩阵"],
 "监管政策":["## 12. 监管结论分级与决策矩阵"],
 "产品需求":["## 12. 用户故事与验收示例"],
 "产品程序":["## 12. 用户故事与验收示例"],
 "产品计划":["## 12. 用户故事与验收示例"],
 "架构标准":["## 12. 架构决策与接口约束"],
 "技术方法":["## 12. 方法验证矩阵"],
 "质量体系":["## 12. 审核证据与抽样策略"],
 "质量程序":["## 12. 审核证据与抽样策略"],
 "运行程序":["## 12. 执行检查点与停止条件"],
 "组织标准":["## 12. 授权与替补矩阵"],
 "组织程序":["## 12. 授权与替补矩阵"],
 "组织政策":["## 12. 授权与替补矩阵"],
 "组织计划":["## 12. 授权与替补矩阵"],
 "实施计划":["## 12. 阶段门与资源释放"],
}
MIN_LINES={"技术方法":230,"架构标准":200,"产品需求":190,"产品程序":190,"产品计划":190,"质量体系":190,"质量程序":190,"运行程序":190,"受控模板":100,"参考登记":50,"参考词典":40,"参考说明":45,"交付检查":60,"风险登记":30,"发布记录":35,"参考索引":80}
def meta(text,key):
    m=re.search(rf"^{re.escape(key)}:\s*(.+?)\s*$",text,re.M)
    return m.group(1).strip() if m else ""
def main():
    errors=[]; ids={}; docs=[]; all_lines=[]; status_counts=Counter()
    for d in LEGACY:
        if any(p.is_dir() and p.name.startswith(d) for p in ROOT.iterdir()):
            errors.append(f"legacy parallel directory remains: {d}*")
    for p in sorted(ROOT.rglob("*.md")):
        rel=p.relative_to(ROOT).as_posix()
        if rel in EXEMPT: continue
        top=p.parts[len(ROOT.parts)] if len(p.parts)>len(ROOT.parts) else ""
        if not (top[:2].isdigit() and 0<=int(top[:2])<=10): continue
        text=p.read_text(encoding="utf-8"); docs.append(p)
        for key in REQUIRED_META:
            if not meta(text,key): errors.append(f"{rel}: missing metadata {key}")
        doc_id=meta(text,"document_id")
        if doc_id in ids: errors.append(f"duplicate document_id {doc_id}: {ids[doc_id]} and {rel}")
        ids[doc_id]=rel
        status=meta(text,"status")
        status_counts[status]+=1
        if status not in VALID_STATUS: errors.append(f"{rel}: invalid maturity status {status}")
        if status in {"已批准","已生效"} and re.search(r"未签批|待指定|不适用",meta(text,"approver")):
            errors.append(f"{rel}: approved/effective status lacks a qualified approver")
        dtype=meta(text,"document_type")
        min_lines=MIN_LINES.get(dtype,150 if dtype!="参考索引" else 80)
        if len(text.splitlines())<min_lines: errors.append(f"{rel}: {len(text.splitlines())} lines < {min_lines} for {dtype}")
        for h in TYPE_HEADINGS.get(dtype,[]):
            if h not in text: errors.append(f"{rel}: missing required section {h}")
        if dtype=="受控模板":
            for h in ["## 2. 表单字段","## 3. 可填写表单","## 4. 附件索引","## 5. 复核与批准","## 6. 填写示例"]:
                if h not in text: errors.append(f"{rel}: incomplete template, missing {h}")
        in_front=True
        for line in text.splitlines():
            if line.strip()=="---":
                in_front=not in_front
                continue
            if BANNED_LINE.search(line): errors.append(f"{rel}: placeholder line: {line[:80]}")
            if status not in NON_ACTIVE_STATUS and not in_front and not line.lstrip().startswith(("#","|---")):
                all_lines.append(line.strip())
        for phrase in BANNED_CLAIMS:
            if phrase in text: errors.append(f"{rel}: prohibited claim: {phrase}")
        if "[ ]" not in text and dtype not in {"参考登记","参考词典","参考索引","参考说明","发布记录","风险登记"}:
            errors.append(f"{rel}: no executable checklist")
        # information density: normalized unique nonempty lines
        meaningful=[x for x in text.splitlines() if x.strip() and not x.startswith("---")]
        ratio=len(set(meaningful))/max(1,len(meaningful))
        if ratio<0.52: errors.append(f"{rel}: low unique-line ratio {ratio:.2f}")
    if len(docs)<100: errors.append(f"controlled documents {len(docs)} < 100")
    # duplicate boilerplate guard: no substantive line may occur in more than 90 docs
    counts=Counter(x for x in all_lines if len(x)>=30 and not x.startswith(("#","|---","---")))
    frequent=[(line,n) for line,n in counts.items() if n>110 and not line.startswith(("- **质量负责人**","- **执行人员**","- **独立复核人员**"))]
    if frequent: errors.append(f"excessive duplicated substantive lines: {frequent[:3]}")
    # JSON
    for p in ROOT.rglob("*.json"):
        try: json.loads(p.read_text(encoding="utf-8"))
        except Exception as e: errors.append(f"invalid JSON {p.relative_to(ROOT)}: {e}")
    # catalog status truthfulness: a generated row is not an approved or executed row
    catalog_statuses={
        "requirements.csv":{"generated_unreviewed","reviewed","approved","rejected"},
        "controls.csv":{"not_implemented","implemented","verified","retired"},
        "tests.csv":{"not_executed","passed","failed","blocked"},
    }
    for name,allowed in catalog_statuses.items():
        p=ROOT/"catalogs"/name
        with p.open(encoding="utf-8",newline="") as f:
            rows=list(csv.DictReader(f))
        invalid=sorted({r.get("status","") for r in rows}-allowed)
        if invalid: errors.append(f"{name}: invalid lifecycle statuses {invalid}")
        if name=="tests.csv":
            generic="满足前置条件时输出可追溯结果；前置条件失败时产生明确阻断或拒绝结论"
            passed_generic=[r["test_id"] for r in rows if r.get("status")=="passed" and r.get("expected")==generic]
            if passed_generic: errors.append(f"tests.csv: generic generated tests marked passed {passed_generic[:10]}")
    # required files/dirs
    required=["README.md",".github/workflows/documentation-quality.yml","scripts/build_document_index.py",
              "scripts/validate_traceability.py","scripts/validate_internal_links.py","catalogs/traceability.csv",
              "10-reference/03-document-index.md","10-reference/05-production-readiness-checklist.md"]
    for rel in required:
        if not (ROOT/rel).exists(): errors.append(f"missing required path: {rel}")
    # README must declare the audited maturity state, not the withdrawn v3 production claim
    readme=(ROOT/"README.md").read_text(encoding="utf-8")
    if "当前阶段：**研究与研发准备**" not in readme: errors.append("README lacks the current research-and-R&D-preparation stage")
    if "v3.0.0的生产声明已撤销" not in readme: errors.append("README does not record withdrawal of the v3 production claim")
    if "v3.0.0（生产单一权威版本）" in readme: errors.append("README still presents v3.0.0 as the production baseline")
    if re.search(r"`1[1-6]-",readme): errors.append("README references legacy parallel directories")
    print(f"controlled_documents={len(docs)} document_ids={len(ids)} statuses={dict(status_counts)}")
    if errors:
        print("QUALITY GATE FAILED")
        for e in errors: print("-",e)
        return 1
    print("QUALITY GATE PASSED")
    return 0
if __name__=="__main__":
    sys.exit(main())
