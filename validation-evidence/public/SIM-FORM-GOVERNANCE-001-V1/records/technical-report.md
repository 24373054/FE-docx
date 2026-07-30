# FRM-011 第一次演练记录

## 1. 报告身份

|字段|填写值|
|---|---|
|记录编号|FRM-011-RH-2026-001|
|案件或项目编号|PUBLIC-RND-SIM-BTC-GENESIS-001|
|记录状态|待复核|
|创建人|Codex workspace research session|
|创建时间|2026-07-30T02:55:00+08:00|
|报告编号|RPT-SIM-BTC-GENESIS-001|
|报告资格|内部公开数据模拟报告；不是司法鉴定意见、检验检测报告或客户报告|

## 2. 委托事项与边界

- 委托方：不适用；内部研发模拟。
- 技术问题：从冻结的Bitcoin创世区块hex复算字节数、交易计数、区块哈希、交易ID和Merkle一致性，并验证证据包完整性。
- 排除：地址控制人、资产权属、交易目的、违法性、主观故意、法律责任、公共端点普遍准确性。
- 发布范围：Git公开验证证据区内部研究引用；不得作为能力宣传或真实案件交付。

## 3. 材料与数据来源

|对象|引用|
|---|---|
|原始hex|SIM-E2E-BTC-GENESIS-001-V1/raw/block.hex|
|执行结果|SIM-E2E-BTC-GENESIS-001-V1/execution/powershell-reproduction.json|
|环境|SIM-E2E-BTC-GENESIS-001-V1/environment/environment.json|
|manifest|SHA-256 `971e7915bebc9b2b535b40b9f33062ab4c4c69d080156ee02daaa9f64497dbc0`|
|完整报告正文|SIM-E2E-BTC-GENESIS-001-V1/report/internal-simulation-report.md|

## 4. 方法与工具

- 方法：MTH-BTC-UTXO 0.2.0的T1确定性事实子集；状态为受控草案，未确认；
- 工具：PowerShell 7.6.4/.NET SHA-256；单样本技术结果通过，工具未验证；
- 包根：`sha256-sorted-path-lines-v1`；不是数字签名或可信时间戳；
- 独立性：Python与PowerShell为不同实现路径，但不是不同自然人。

## 5. 可验证技术事实

|事实|值|证据状态|
|---|---|---|
|原始区块字节数|285|从冻结hex解码|
|交易计数|1|CompactSize解析|
|区块哈希|`000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f`|80字节头双SHA-256|
|交易ID|`4a5e1e4baab89f3a32518a88c31bc87f618f76673e2cc77ab2127b7afdeda33b`|冻结交易字节双SHA-256|
|Merkle根|与交易ID一致|单交易规则|
|包对象完整性|13/13|对象哈希、字节数和根哈希|

## 6. 推断、无法判断与限制

- 规则推断：无主体归属、路径、聚类或标签推断；
- 统计推断：不适用；
- 无法判断：私钥控制、资产权属、交易法律属性、方法普遍准确性、工具生产适用性；
- 限制：单链、单区块、单交易、正常历史对象；无独立自然人、无公司批准、无真实案件。

## 7. 附件与复核

|附件|哈希/位置|
|---|---|
|原报告|`2636ca3fbe0b5c2599bde112df200b05f48cf4d538a3b0dcb1ccb6c66f1e324a`|
|父包manifest|`971e7915bebc9b2b535b40b9f33062ab4c4c69d080156ee02daaa9f64497dbc0`|

技术自检通过；独立复核、批准和对外发布均为`blocked`。

第一次演练发现模板需要`report_qualification`、`claim_class`、`evidence_status`、`publication_scope`和`release_state`，以防内部模拟报告被误标为司法鉴定或已发布报告。
