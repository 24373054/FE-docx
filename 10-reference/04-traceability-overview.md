---
document_id: REF-004
title: 需求、控制、测试与证据追踪说明
version: 3.0.0
status: 受控基线
document_type: 参考说明
owner: 测试负责人
approver: 质量负责人
effective_date: 2026-07-27
review_cycle: 每次需求、控制或测试变化时
classification: 内部受控
---

# 需求、控制、测试与证据追踪说明

## 1. 追踪规模

|对象|数量|文件|
|---|---:|---|
|生产需求|1631|`catalogs/requirements.csv`|
|控制项|1631|`catalogs/controls.csv`|
|测试用例|1631|`catalogs/tests.csv`|
|追踪链接|1631|`catalogs/traceability.csv`|

## 2. 追踪链

每一项生产要求必须形成以下闭环：

`受控文档主题 → REQ需求 → C控制 → TST测试 → FRM证据模板 → 实际记录`

- **REQ**说明系统、流程、方法或组织必须达到的结果。
- **C**说明预防、发现或纠正风险的控制。
- **TST**说明如何证明要求和控制有效。
- **FRM**提供形成客观证据的受控记录结构。
- 实际项目或案件记录必须使用唯一编号并引用相应ID。

## 3. 变更影响

修改文档中的控制主题、方法范围、接受标准、工具用途、模板字段或SOP步骤时：

1. 更新对应REQ、C和TST；
2. 检查相邻和下游追踪链接；
3. 更新验证样本、培训和授权；
4. 评估历史案件或发布版本；
5. 运行 `python scripts/validate_traceability.py`；
6. 在PR中说明新增、修改、废止的追踪ID。

## 4. 删除与废止

不得直接删除仍被追踪矩阵、报告、培训或历史记录引用的ID。废止时保留原ID和状态，记录替代项、最后适用版本和历史复现方式。当前v3目录中的所有条目状态均为 `approved`。
