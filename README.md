# 区块链电子数据司法取证与关联分析研发体系

> 当前受控版本：**v3.0.0（生产单一权威版本）**  
> 生效日期：2026-07-27  
> 适用主体：研发、质量、合规、实验室建设与合作试点团队  
> 仓库状态：生产交付基线；旧版 11—16 平行目录已由 Git 历史保留，不再作为现行文件。

## 1. 仓库目标

本仓库用于指导团队建设面向公开链及经授权电子数据的证据级采集、固定、验证、关联分析和电子数据司法鉴定准备能力。仓库不是宣传材料，也不以文件数量或行数代表能力；每项生产要求必须能追踪到控制、测试和记录证据。

当前优先方向：

1. 0301 电子数据存在性鉴定相关技术准备：网络数据提取、固定、形成过程与内容关联分析；
2. 0302 电子数据真实性鉴定相关技术准备：完整性、一致性、修改情况和多源核验；
3. Bitcoin、Ethereum/EVM、TRON 三类代表性链的证据级方法；
4. 跨链桥、DeFi、混币、聚类和标签作为受限制的特色分析能力；
5. CMA、CNAS、司法鉴定机构和人员登记的差距评估与证据准备。

## 2. 法律与结论边界

- 未取得司法鉴定机构和司法鉴定人登记前，仅开展研发、技术辅助、方法共建和合作试点，不以本机构名义出具司法鉴定意见。
- 未取得相应 CMA 或 CNAS 能力前，不使用相关标志，不宣传已获认可或已具备法定能力。
- CMA、CNAS、司法行政登记和诉讼证据审查是不同制度，不能相互替代。
- 链上技术事实不能单独证明自然人身份、主观故意、资金违法属性或法律责任。
- 标签、聚类、跨链和混币分析必须区分可验证事实、规则推断、统计推断、主体归属意见和法律判断。
- 第三方 RPC、区块浏览器和商业标签库只能作为辅助来源；关键事实需要自建节点、独立客户端、原始区块解析或密码学证明复核。
- AI/Agent 只能执行受控检索、候选生成、证据索引和一致性检查，不得独立形成最终技术结论。

## 3. 单一权威目录

|目录|定位|主要读者|
|---|---|---|
|`00-governance/`|项目章程、治理、文档层级、变更、质量目标和发布基线|管理层、项目、质量|
|`01-regulatory/`|CMA、CNAS、司法鉴定、北京路径、电子证据与数据合规|合规、质量、管理层|
|`02-product/`|用户、用例、功能、案件状态、证据包、报告和验收|产品、研发、测试|
|`03-architecture/`|系统、证据、血缘、节点、安全、灾备和接口|架构、研发、安全|
|`04-methods/`|BTC、EVM、TRON、跨链、DeFi、混币、聚类、标签和AI方法|方法、分析、测试|
|`05-quality/`|质量手册、方法工具验证、人员、设备、CAPA、审核和供应商|质量、实验室、管理层|
|`06-operations/`|受理、采集、分析、报告、存储、节点、发布、事件和质证SOP|运行、分析、支持|
|`07-organization/`|组织边界、岗位、能力、授权、独立性和人员计划|管理层、人力、质量|
|`08-planning/`|24个月路线、WBS、预算、实验室、试点、风险和标准化|项目、财务、管理层|
|`09-templates/`|16份可直接填写的受控记录模板|全部执行角色|
|`10-reference/`|官方来源、术语、索引、追踪、交付检查和发布说明|全部人员|
|`catalogs/`|需求、控制、测试和追踪矩阵|研发、测试、质量|
|`schemas/`|机器可读证据、案件、来源和工具Schema|研发、数据、验证|
|`scripts/`|索引、质量、追踪和链接检查|维护者、CI|

## 4. 推荐阅读路径

### 管理层
1. [`00-governance/01-program-charter.md`](00-governance/01-program-charter.md)
2. [`01-regulatory/01-regulatory-map.md`](01-regulatory/01-regulatory-map.md)
3. [`08-planning/01-24-month-roadmap.md`](08-planning/01-24-month-roadmap.md)
4. [`10-reference/05-production-readiness-checklist.md`](10-reference/05-production-readiness-checklist.md)

### 研发与架构
1. [`02-product/03-functional-requirements.md`](02-product/03-functional-requirements.md)
2. [`03-architecture/04-evidence-data-model.md`](03-architecture/04-evidence-data-model.md)
3. [`03-architecture/05-provenance-chain-of-custody.md`](03-architecture/05-provenance-chain-of-custody.md)
4. [`04-methods/01-general-method-framework.md`](04-methods/01-general-method-framework.md)
5. [`catalogs/traceability.csv`](catalogs/traceability.csv)

### 方法与分析
1. [`04-methods/01-general-method-framework.md`](04-methods/01-general-method-framework.md)
2. 对应链或场景方法
3. [`05-quality/03-method-validation.md`](05-quality/03-method-validation.md)
4. [`06-operations/03-analysis-review.md`](06-operations/03-analysis-review.md)
5. [`09-templates/06-analysis-hypothesis-log.md`](09-templates/06-analysis-hypothesis-log.md)

### 质量与准入
1. [`05-quality/01-quality-manual.md`](05-quality/01-quality-manual.md)
2. [`01-regulatory/02-cma-one-list-one-library.md`](01-regulatory/02-cma-one-list-one-library.md)
3. [`01-regulatory/03-cnas-accreditation.md`](01-regulatory/03-cnas-accreditation.md)
4. [`01-regulatory/04-judicial-appraisal-registration.md`](01-regulatory/04-judicial-appraisal-registration.md)
5. [`10-reference/05-production-readiness-checklist.md`](10-reference/05-production-readiness-checklist.md)

## 5. 强制质量门

每次 Pull Request 和 `main` 推送执行：

```bash
python scripts/build_document_index.py --check
python scripts/repo_quality_check.py
python scripts/validate_traceability.py
python scripts/validate_internal_links.py
```

质量门检查：

- 受控文档元数据完整、编号唯一、状态有效；
- 00—10 是唯一现行目录，11—16 平行目录不存在；
- 不存在 `TODO`、`TBD`、占位文本、空壳模板或失效内部链接；
- 方法、SOP、政策和模板达到各自最低内容结构；
- 模板包含可填写字段、填写说明、示例、复核和附件索引；
- 需求、控制和测试具有双向追踪；
- 官方监管来源使用受控登记，不以搜索摘要替代正式文本；
- 禁止性宣传和越界结论措辞被自动扫描；
- JSON Schema 可解析且示例通过基本校验；
- 文档索引与实际仓库一致。

## 6. 变更规则

任何人不得直接修改生产基线后绕过评审。变更必须：

1. 创建变更记录；
2. 完成监管、技术、数据、安全、人员和历史案件影响分析；
3. 更新关联需求、方法、测试、模板和培训；
4. 通过全部质量门；
5. 由文件责任人、技术/方法复核人和质量负责人批准；
6. 以 Pull Request 合并并保留完整 Git 历史。

## 7. 当前生产限制

本仓库定义的是可执行的研发与质量体系，不等于已经获得任何行政许可或认可。正式申报、签约、对外宣传、案件受理和报告发布前，必须核验最新官方规则、主管机关书面意见、人员资格、场所设备和实际运行证据。
