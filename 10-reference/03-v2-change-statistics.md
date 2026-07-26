---
document_id: REF-003
title: v2深化变更统计与验收记录
version: 2.0.0
status: 受控草案
owner: 质量负责人
effective_date: 2026-07-26
review_cycle: 每次重大变更或至少每季度
---
# v2深化变更统计与验收记录

## 本轮规模

- v2独立受控文档：35份。
- v2主题文档行数：23244行。
- 本轮生成或替换文件（不含本统计文件）：35个。
- 本轮生成或替换文本行数（不含本统计文件）：23244行。
- 验收下限：增添及修改内容不少于8000行；本轮按v2主题文档行数计量。

## 验收原则

- 统计对象为UTF-8文本文件，行数按Python `splitlines()`口径计算。
- 行数不等于质量；合并前还必须通过文档编号唯一性、JSON解析、禁止性表述、范围边界和目录完整性检查。
- 法规、标准和主管机关信息以正式申报前最新官方文件及书面答复为准。

## 文件摘要

|文件|行数|SHA-256前16位|
|---|---:|---|
|`11-v2-foundation/01-v2-program-charter.md`|528|`60b73df0dea5da0e`|
|`11-v2-foundation/02-scope-claims-and-exclusions.md`|528|`6cbe0d8e1c9fb970`|
|`11-v2-foundation/03-decision-and-assumption-register.md`|527|`289b3530570e699e`|
|`12-research/01-cma-one-list-one-library-dossier.md`|629|`dc29c3d824568283`|
|`12-research/02-cnas-forensic-accreditation-dossier.md`|645|`98181ec825fa3a78`|
|`12-research/03-beijing-licensing-and-laboratory-dossier.md`|668|`a507b3006ebfba28`|
|`12-research/04-electronic-evidence-law-dossier.md`|686|`dd5fa984ed9e1003`|
|`12-research/05-data-security-and-privacy-dossier.md`|633|`ac489534591aa092`|
|`12-research/06-virtual-asset-policy-boundaries.md`|566|`74bb38cb634882a2`|
|`13-system/01-reference-architecture-v2.md`|683|`5619dbe3de1baf8b`|
|`13-system/02-evidence-object-and-manifest-model.md`|727|`4366571e6e2ec469`|
|`13-system/03-provenance-chain-of-custody.md`|630|`8c87047242d3c52f`|
|`13-system/04-security-threat-model.md`|702|`67d2ac39288d6ee4`|
|`13-system/05-node-and-data-source-governance.md`|690|`d1184f3e27a43386`|
|`13-system/06-ai-agent-control-plane.md`|633|`61f29019e3e51195`|
|`14-method-validation/01-general-method-validation-master-plan.md`|733|`d626d3c14f646986`|
|`14-method-validation/02-bitcoin-validation-profile.md`|756|`0ea65e1fd23233a3`|
|`14-method-validation/03-evm-validation-profile.md`|796|`ec1a6f9617194af4`|
|`14-method-validation/04-tron-validation-profile.md`|723|`559a58afdcdeda74`|
|`14-method-validation/05-cross-chain-bridge-validation-profile.md`|815|`db15afac464b13c5`|
|`14-method-validation/06-defi-economic-flow-validation-profile.md`|757|`a6d7e1d6122dcf21`|
|`14-method-validation/07-mixer-and-clustering-validation-profile.md`|778|`c878831707cc6cdc`|
|`14-method-validation/08-label-and-entity-attribution-validation-profile.md`|778|`1f986a02fefeddc4`|
|`15-implementation/01-24-month-integrated-roadmap.md`|673|`2735d0fb68f3851e`|
|`15-implementation/02-work-breakdown-structure.md`|786|`43306885cfffd029`|
|`15-implementation/03-team-competence-and-authorization-plan.md`|630|`5761ed902935dd7d`|
|`15-implementation/04-budget-and-procurement-plan.md`|665|`af2847d84c28d7b0`|
|`15-implementation/05-partner-pilot-and-case-simulation-plan.md`|600|`3567f85295ee2a39`|
|`15-implementation/06-regulator-engagement-plan.md`|562|`a7bc61ccfa47f1af`|
|`15-implementation/07-risk-register-and-contingency-plan.md`|657|`33fdfc65c1a6c5e8`|
|`16-operational-playbooks/01-case-intake-and-technical-question-playbook.md`|582|`da4e4718ba48382f`|
|`16-operational-playbooks/02-acquisition-session-playbook.md`|616|`5000405790236501`|
|`16-operational-playbooks/03-analysis-review-and-report-playbook.md`|648|`991e927b95d20ecc`|
|`16-operational-playbooks/04-release-change-and-incident-playbook.md`|632|`ddd49dba2ea05608`|
|`16-operational-playbooks/05-expert-review-and-court-explanation-playbook.md`|582|`a00327a2552939e3`|

## 质量门结果

- 生成器完成后必须运行 `python scripts/repo_quality_check.py`。
- 合并PR前必须核对GitHub compare统计，确认新增与修改行数不低于8000。
- 本记录仅证明仓库内容规模和内部检查结果，不证明任何行政许可、认可或司法采信状态。
