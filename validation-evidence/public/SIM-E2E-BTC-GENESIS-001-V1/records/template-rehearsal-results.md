# 首批模板第一次演练结果

演练ID：`TRR-SIM-BTC-GENESIS-001`

## 结果

|模板|实际记录|第一次演练结论|发现|
|---|---|---|---|
|FRM-002 授权与范围|`records/authorization.md`|partial_pass|真实活动必须附书面授权；研究指令不能替代外部授权|
|FRM-003 采集记录|`records/acquisition.md`|partial_pass_with_field_gap|异常字段需关联错误对象、发现控制、修复对象和影响|
|FRM-004 证据项登记|`records/evidence-register.md`|待manifest后完成|需区分逻辑对象和文件对象并记录包根算法|
|FRM-008 方法确认|`records/method-validation.md`|partial_pass|技术结果与治理批准需要双层状态|
|FRM-009 工具验证|`records/tool-validation.md`|partial_pass|制品哈希失败原因和整体阻断应结构化|
|FRM-010 复核检查|`records/review.md`|partial_pass_with_required_changes|独立性必须是发布阻断门而非普通勾选项|

## 升级判定

项目治理要求模板至少完成两次演练后才可申请从`模板草案（待实测）`升级。本次是第一次，且存在字段缺口，因此六份模板全部保持原状态。

## 第二次演练必须覆盖

- 不同链/对象或至少一个负向、冲突样本；
- 真正不同的自然人复核角色；
- 批准记录和访问/交付双人角色；
- 存储、加密、恢复和接收回执；
- 根据本次发现修订后的模板版本；
- 字段级完成率和不可填写原因统计。
