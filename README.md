# 区块链电子数据司法取证与关联分析研发体系

> 当前受控版本：**v2.0.0**  
> v1基线日期：2026-07-25  
> v2深化日期：2026-07-26  
> 仓库定位：面向虚拟资产链上数据提取、固定、验证、关联分析及电子数据司法鉴定准备的研发与质量体系。

## 1. 项目目标

本仓库用于指导团队集中研发投入，并把产品、算法、数据、实验室、质量体系和准入准备放入同一套可追踪框架。目标不是制作一份宣传材料，而是形成：

1. 可从结论追溯至原始数据、工具版本、方法参数和操作记录的证据链；
2. 可由独立人员在隔离环境中复现的采集与分析流程；
3. 对BTC、EVM、TRON、跨链桥、DeFi、混币、聚类、标签和实体归属分别验证的方法体系；
4. 为CMA、CNAS和司法鉴定机构/人员登记准备服务的受控记录；
5. 在证据不足、来源冲突或方法超界时主动拒绝确定性结论的产品机制。

## 2. 法律与业务边界

- 未取得司法鉴定机构和司法鉴定人登记前，只开展研发、技术辅助、方法共建和合作试点，不以本机构名义出具司法鉴定意见。
- 未取得相应CMA或CNAS能力前，不使用相关标志，不宣传已经具备获证能力。
- CMA、CNAS、司法行政登记和诉讼证据审查属于不同制度，不能相互替代。
- 链上技术事实不能单独证明自然人身份、主观故意、资金违法属性或法律责任。
- 标签、聚类、跨链和混币分析必须区分确定性事实、规则推断、统计推断、主体归属意见和法律判断。
- 第三方RPC、区块浏览器和商业标签库只能作为辅助来源；关键事实需要自建节点、独立客户端、原始区块解析或密码学证明复核。
- AI/Agent只能执行受控检索、候选生成、证据索引和一致性检查，不得独立形成最终技术结论。
- 涉及个人信息、案件秘密、商业秘密、跨境数据或受限制数据源时，先完成合法性、最小必要性和授权审查。

## 3. 推荐阅读路径

### 决策层

1. [`11-v2-foundation/01-v2-program-charter.md`](11-v2-foundation/01-v2-program-charter.md)
2. [`11-v2-foundation/02-scope-claims-and-exclusions.md`](11-v2-foundation/02-scope-claims-and-exclusions.md)
3. [`15-implementation/01-24-month-integrated-roadmap.md`](15-implementation/01-24-month-integrated-roadmap.md)
4. [`15-implementation/04-budget-and-procurement-plan.md`](15-implementation/04-budget-and-procurement-plan.md)
5. [`15-implementation/07-risk-register-and-contingency-plan.md`](15-implementation/07-risk-register-and-contingency-plan.md)

### 监管、质量与实验室负责人

1. [`12-research/01-cma-one-list-one-library-dossier.md`](12-research/01-cma-one-list-one-library-dossier.md)
2. [`12-research/02-cnas-forensic-accreditation-dossier.md`](12-research/02-cnas-forensic-accreditation-dossier.md)
3. [`12-research/03-beijing-licensing-and-laboratory-dossier.md`](12-research/03-beijing-licensing-and-laboratory-dossier.md)
4. [`12-research/04-electronic-evidence-law-dossier.md`](12-research/04-electronic-evidence-law-dossier.md)
5. [`15-implementation/06-regulator-engagement-plan.md`](15-implementation/06-regulator-engagement-plan.md)

### 产品、平台与安全负责人

1. [`13-system/01-reference-architecture-v2.md`](13-system/01-reference-architecture-v2.md)
2. [`13-system/02-evidence-object-and-manifest-model.md`](13-system/02-evidence-object-and-manifest-model.md)
3. [`13-system/03-provenance-chain-of-custody.md`](13-system/03-provenance-chain-of-custody.md)
4. [`13-system/04-security-threat-model.md`](13-system/04-security-threat-model.md)
5. [`13-system/05-node-and-data-source-governance.md`](13-system/05-node-and-data-source-governance.md)
6. [`13-system/06-ai-agent-control-plane.md`](13-system/06-ai-agent-control-plane.md)

### 协议、算法和测试负责人

1. [`14-method-validation/01-general-method-validation-master-plan.md`](14-method-validation/01-general-method-validation-master-plan.md)
2. [`14-method-validation/02-bitcoin-validation-profile.md`](14-method-validation/02-bitcoin-validation-profile.md)
3. [`14-method-validation/03-evm-validation-profile.md`](14-method-validation/03-evm-validation-profile.md)
4. [`14-method-validation/04-tron-validation-profile.md`](14-method-validation/04-tron-validation-profile.md)
5. [`14-method-validation/05-cross-chain-bridge-validation-profile.md`](14-method-validation/05-cross-chain-bridge-validation-profile.md)
6. [`14-method-validation/06-defi-economic-flow-validation-profile.md`](14-method-validation/06-defi-economic-flow-validation-profile.md)
7. [`14-method-validation/07-mixer-and-clustering-validation-profile.md`](14-method-validation/07-mixer-and-clustering-validation-profile.md)
8. [`14-method-validation/08-label-and-entity-attribution-validation-profile.md`](14-method-validation/08-label-and-entity-attribution-validation-profile.md)

### 案件流程、复核和技术解释人员

1. [`16-operational-playbooks/01-case-intake-and-technical-question-playbook.md`](16-operational-playbooks/01-case-intake-and-technical-question-playbook.md)
2. [`16-operational-playbooks/02-acquisition-session-playbook.md`](16-operational-playbooks/02-acquisition-session-playbook.md)
3. [`16-operational-playbooks/03-analysis-review-and-report-playbook.md`](16-operational-playbooks/03-analysis-review-and-report-playbook.md)
4. [`16-operational-playbooks/04-release-change-and-incident-playbook.md`](16-operational-playbooks/04-release-change-and-incident-playbook.md)
5. [`16-operational-playbooks/05-expert-review-and-court-explanation-playbook.md`](16-operational-playbooks/05-expert-review-and-court-explanation-playbook.md)

## 4. 文档结构

|目录|用途|
|---|---|
|`00-governance`|项目章程、决策和文档控制|
|`01-regulatory`|v1监管地图和结论边界|
|`02-product`|产品定义、流程和阶段门|
|`03-architecture`|v1证据、数据、安全和连续性架构|
|`04-methods`|v1逐链及关联方法基线|
|`05-quality`|质量体系、方法和工具验证|
|`06-operations`|案件、节点、发布和事件运行要求|
|`07-organization`|角色、能力和授权|
|`08-planning`|v1路线、预算、风险和采购|
|`09-templates`|受控记录模板|
|`10-reference`|官方来源、统计和变更验收记录|
|`11-v2-foundation`|v2章程、范围和决策登记|
|`12-research`|CMA、CNAS、北京准入、证据法、数据合规和虚拟资产业务边界|
|`13-system`|v2参考架构、证据对象、保管链、安全、数据源和Agent控制|
|`14-method-validation`|逐链及复杂场景验证画像|
|`15-implementation`|24个月计划、WBS、人才、预算、合作、监管沟通和风险|
|`16-operational-playbooks`|从受理到技术解释的操作手册|
|`catalogs`|控制、需求和测试用例目录|
|`schemas`|机器可读证据清单结构|
|`scripts`|仓库质量检查脚本|

## 5. 当前研发优先级

- **P0：证据级采集与固定。** 先完成BTC、Ethereum和TRON的自建节点、多源核验、原始响应固定、证据清单和离线验证。
- **P0：质量体系前置。** 方法、工具、数据集、人员、设备和变更记录从研发第一天受控，不在申请前补材料。
- **P1：确定性资金路径和统一经济语义。** 先证明资产变化，再发展跨链、DeFi、混币和聚类推断。
- **P1：方法验证与拒绝机制。** 每项能力必须有正常、边界、冲突、恶意和历史回归样本。
- **P2：实验室和准入投入。** 以人员路径、场所可行性、能力项目库查询和主管机关书面沟通结果为阶段门。

## 6. 质量门

本地执行：

```bash
python scripts/repo_quality_check.py
```

永久GitHub Actions工作流会在涉及Markdown、JSON、Python或质量工作流的推送和PR中自动检查：

- 文本文件和总行数下限；
- Markdown文档编号存在性和唯一性；
- JSON有效性；
- v2六个目录完整性；
- v2受控文档不少于35份；
- v2主题内容不少于22,000行；
- README版本标识和一次性bootstrap材料清理状态。

## 7. 规模与验收记录

- v1基线提交：15,309行新增；
- v2深化PR：36个文件、23,314行新增、0行删除；
- v2受控主题文档：35份、23,244行；
- 详细文件哈希见 [`10-reference/03-v2-change-statistics.md`](10-reference/03-v2-change-statistics.md)。

规模只证明文档建设量，不证明任何行政许可、认可或司法采信状态。正式申报、签约或对外宣传前，必须重新核验官方来源并取得必要书面意见。
