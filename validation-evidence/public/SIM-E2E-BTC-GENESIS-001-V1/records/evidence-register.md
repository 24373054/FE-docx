# FRM-004 证据项登记表——第一次演练记录

记录编号：`FRM-004-SIM-20260730-001`

模板版本：`3.0.0-draft`

案件或项目编号：`PUBLIC-RND-SIM-BTC-GENESIS-001`

记录状态：`assembled_pending_independent_review`

## 对象登记

|对象ID|类型|相对路径|字节数|SHA-256|来源/父对象|
|---|---|---|---:|---|---|
|OBJ-SIM-BTC-ENV-001|record|environment/environment.json|780|`2d7f4db2c54b06b6872502183366791c72f5703fc13b8dde6b5bedf88a1c57b8`|本地环境记录|
|OBJ-SIM-BTC-RUN-001|derived|execution/powershell-reproduction.json|910|`4461dc91a3011556f1361f03e78b4b78bfd7732259935bb5ca6f497090cf97b0`|OBJ-SIM-BTC-RAW-001、OBJ-SIM-BTC-ENV-001|
|OBJ-SIM-BTC-RAW-001|raw|raw/block.hex|571|`6f91a7dde963795146048aef2e347d02214edf6e0f841fc72950759c891e32bb`|GT-BTC-GENESIS-001-V1|
|OBJ-SIM-BTC-ACQ-001|record|records/acquisition.md|2142|`a9b3eeadd35e724540785021d3d899487e7cef9bb3213df6f9051719321fb0ae`|OBJ-SIM-BTC-RAW-001|
|OBJ-SIM-BTC-AUTH-001|record|records/authorization.md|1694|`9ca46feadcd0277dd64a5bd5df4771861ac5f0b34d212e8886ed9a3540cc246d`|scope.md|
|OBJ-SIM-BTC-MVAL-001|record|records/method-validation.md|2112|`37400fd5a08ffa459b0996e6d556a3f185b989177f0aec8b54cb5383e25b0bed`|OBJ-SIM-BTC-RUN-001|
|OBJ-SIM-BTC-REV-001|record|records/review.md|2063|`a3bcdb1f092fd9900a34c2fe89dde4ef49923320b9473dd01d630c04d0a99d12`|本包P0对象|
|OBJ-SIM-BTC-TRR-001|record|records/template-rehearsal-results.md|1475|`e534b65c6992ec389e43bb79ef91c1d315cb74a0b18d243c9584ce339be6ef06`|六份演练记录|
|OBJ-SIM-BTC-TVAL-001|record|records/tool-validation.md|1657|`a32ffde7e20b5435261f48c681dfb263447fea86caa4a001a1d50973f7f994ec`|OBJ-SIM-BTC-RUN-001|
|OBJ-SIM-BTC-RPT-001|report|report/internal-simulation-report.md|3204|`2636ca3fbe0b5c2599bde112df200b05f48cf4d538a3b0dcb1ccb6c66f1e324a`|OBJ-SIM-BTC-RUN-001、复核与限制记录|
|OBJ-SIM-BTC-SCOPE-001|record|scope.md|2376|`e0bc269f2c426a8fc3db71304e6adc8f899cdab5382c96f19d0ac3c1bb7f290a`|项目模拟计划|

本登记表自身作为`OBJ-SIM-BTC-EREG-001`登记在`manifest.json`中，不在正文写入自身哈希以避免自引用。

## 公共字段

|字段|值|
|---|---|
|格式/MIME|按扩展名；文本均为UTF-8|
|存储等级|Git公开验证区；不等于WORM或生产证据库|
|保密级别|public|
|访问角色|公开读取；修改受版本库权限约束|
|留存期限|随研究仓库保留；正式期限未批准|
|完整性复核日期|2026-07-30|

## 复核与批准

- 对象字节数和SHA-256由当前研究会话实际计算；
- manifest生成后将再次做全量机器校验；
- 独立自然人复核缺失；
- 具名批准缺失。

模板第一次演练结果：`partial_pass`。发现逻辑对象与文件对象可能不是一一对应，模板需增加`package_id`、`root_hash_algorithm`、`value_status`以及自引用处理规则。
