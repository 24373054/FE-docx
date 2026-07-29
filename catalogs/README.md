# 追踪目录

本目录保存原v3.0.0生成的需求、控制、测试和证据模板候选映射。

当前1631组记录只证明ID能够对应，不证明需求已经批准、控制已经实施、测试已经执行或证据已经产生。

|文件|行数（不含表头）|当前状态|用途|
|---|---:|---|---|
|`requirements.csv`|1631|`generated_unreviewed`|待评审需求候选及责任、优先级|
|`controls.csv`|1631|`not_implemented`|待重构和实施的控制候选|
|`tests.csv`|1631|`not_executed`|测试标题和通用预期占位，不能作为测试规程|
|`traceability.csv`|1631|无执行状态|候选需求—控制—测试—模板—文档映射|

状态升级要求：

- 需求变为`reviewed`或`approved`前，必须完成去重、来源核验、可测试性检查和具名评审；
- 控制变为`implemented`或`verified`前，必须明确实施对象、责任人、频次和实际记录；
- 测试变为`passed`、`failed`或`blocked`前，必须有具体输入、步骤、判定、实际结果、执行人、时间和证据位置；
- `evidence_template`只表示候选记录模板，不是实际证据记录。

修改文档中的控制主题时，同步更新目录并运行：

```bash
python scripts/validate_traceability.py
```
