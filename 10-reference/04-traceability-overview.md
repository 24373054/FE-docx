---
document_id: REF-004
title: 需求、控制、测试与证据追踪说明
version: 0.2.0
status: 受控草案
document_type: 参考说明
owner: 测试负责人
approver: 质量负责人（未签批）
effective_date: 尚未生效
review_cycle: 每次需求、控制、测试、Schema或证据接口变化时
classification: 内部受控
---

# 需求、控制、测试与证据追踪说明

## 1. 当前规模

|对象|数量|状态|
|---|---:|---|
|requirements.csv|1639|1151 reviewed；488 generated_unreviewed|
|controls.csv|1639|1639 not_implemented|
|tests.csv|1639|1639 not_executed|
|traceability.csv|1639|1639条映射闭合|

目录数量只证明追踪结构，不证明要求正确、控制有效或测试通过。

## 2. 追踪链

标准链：

`受控文件主题 → requirement → control → test → evidence template → actual record → review/approval`

|对象|回答的问题|
|---|---|
|Requirement|必须达到什么结果|
|Control|如何预防、发现或纠正失败|
|Test|用什么正向与反向操作验证|
|Template|记录需要哪些字段和签名|
|Actual record|实际做了什么、输入输出和结果|
|Review/approval|谁在什么权限和证据下接受|

缺少actual record时，控制和测试不得升级。

## 3. 生命周期

### 3.1 Requirement

- `generated_unreviewed`：历史生成，仅作线索；
- `reviewed`：已与正文逐项实质核对；
- `approved`：有权人员批准进入实现/验收；
- `rejected`：不再采用但保留历史。

### 3.2 Control

- `not_implemented`；
- `implemented`；
- `verified`；
- `retired`。

### 3.3 Test

- `not_executed`；
- `passed`；
- `failed`；
- `blocked`。

`reviewed requirement`不自动改变控制或测试状态。

## 4. ID规则

- 需求：`REQ-<DOCUMENT>-NNN`；
- 控制：`<DOCUMENT>-CNNN`；
- 测试：`TST-<DOCUMENT>-NNN`；
- 文件：frontmatter中的`document_id`；
- 实际运行/证据：由相应SOP/manifest分配唯一ID。

ID不可复用。废止时保留原ID、替代项、最后适用版本和历史影响。

## 5. 内容同步

正文控制主题、目录topic、requirement和expected须语义一致。

变更时：

1. 更新正文及版本；
2. 更新requirement文本和状态；
3. 更新control主题/责任/证据模板；
4. 更新test正向、反向和预期；
5. 检查traceability路径；
6. 评估模板、样本、培训和历史运行；
7. 重建索引并执行全部检查；
8. 在发布记录中说明计数与未升级状态。

## 6. 测试预期

每个测试至少包含：

- 正向输入、前置条件和可观察结果；
- 反向/边界输入；
- 明确阻断、拒绝、隔离或告警；
- 对象、日志和证据位置；
- 方法/工具/环境版本；
- 复核人与差异处置。

通用占位预期不能标记为passed。

## 7. 证据状态

|证据|可支持|不能支持|
|---|---|---|
|文档正文|设计规则|实际实施|
|目录行|生命周期登记|运行结果|
|自动检查|结构/路径/ID一致|业务正确|
|Git提交|内容版本和时间顺序|公司批准|
|模拟证据包|实际模拟步骤和完整性|真实案件能力|
|签批记录|批准主体、范围和日期|超出范围能力|

## 8. 自动检查

```text
python scripts/build_document_index.py --check
python scripts/repo_quality_check.py
python scripts/validate_traceability.py
python scripts/validate_internal_links.py
git diff --check
```

当前检查覆盖：

- 119份受控目录文档及唯一ID；
- 1639组需求/控制/测试/追踪；
- 元数据、状态、最低结构和禁止表述；
- 内部相对链接；
- JSON语法；
- 空白和换行问题。

## 9. 抽样复核

自动通过后仍须人工抽样：

- requirement是否忠实概括正文；
- control是否能实际降低风险；
- test是否能区分通过/失败；
- evidence template是否有必要字段；
- owner是否具备职责和授权；
- 状态是否有直接证据；
- 已通过测试是否包含失败尝试和环境；
- 历史影响是否闭合。

## 10. 删除、合并与拆分

- 删除前检索文档、报告、模板、样本和历史记录引用；
- 合并保留旧ID到新ID的映射；
- 拆分定义每个新项的范围和原项状态；
- 不得为了减少未完成数删除失败或未实施项；
- traceability行与历史基线一并归档。

## 11. 验收检查

- [ ] 四个目录数量和ID一一闭合；
- [ ] 正文控制ID全部存在于controls.csv；
- [ ] requirement/control/test主题和责任一致；
- [ ] reviewed/implemented/verified/passed均有对应证据；
- [ ] 废止、合并和拆分保留历史映射；
- [ ] 全部自动检查通过；
- [ ] 人工抽样未发现状态提前升级；
- [ ] 发布记录说明计数、范围和限制。

## 12. 版本记录

|版本|日期|变更|状态|
|---|---|---|---|
|0.2.0|2026-07-30|修复历史乱码，更新1639条追踪规模、生命周期、同步和证据解释|受控草案，未签批|
|3.0.0-draft|2026-07-27|历史生成稿；曾错误声称全部approved|已由本版替代|
