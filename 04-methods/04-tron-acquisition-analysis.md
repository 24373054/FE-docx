---
document_id: M-TRON-001
title: TRON采集、执行与TRC-20分析方法
version: 0.2.0
status: 受控草案
document_type: 技术方法
owner: TRON方法负责人
approver: 质量负责人（未签批）
effective_date: 尚未生效
review_cycle: 每6个月或java-tron、网络、API、TVM、Token标准重大变化时
classification: 内部受控
---

# TRON采集、执行与TRC-20分析方法

## 1. 文件目的

定义TRON网络交易本体、执行结果、资源消耗、日志、内部调用、地址编码和TRC-20变化的候选采集与分析规则。

本方法严格区分“已上链”“已固化/确认”“执行成功”“产生Token事件”和“现实主体控制”。

当前没有TRON冻结样本包、获批真值、自建节点、独立复算、工具验证或方法批准；本文件只作为V0研发设计。

## 2. 适用范围与排除

### 2.1 当前候选范围

- 经登记的TRON主网或测试网；
- FullNode与SolidityNode查询结果；
- Transaction及`raw_data`、签名、合约参数；
- TransactionInfo、结果、费用、Energy、Bandwidth、日志和内部调用；
- TRX与TRC-20整数变化候选；
- Base58Check与hex地址表示转换；
- 固化状态和多节点差异。

### 2.2 明确排除

- 创建、签名或广播真实交易；
- 获取或处理客户私钥、助记词、API密钥；
- 只凭TronGrid扩展索引或浏览器展示形成P0事实；
- 把Ethereum地址去/加`41`前缀当作跨链同一主体证明；
- 只凭`Transfer`事件断言全部Token变化；
- 未验证的账户聚类、主体身份、违法属性或资产处置结论。

## 3. 对象与来源分层

|层级|来源|允许用途|限制|
|---|---|---|---|
|DS1|自建且受控的java-tron节点|P0候选与复算|当前为0|
|DS2|第二独立节点/实现|交叉验证|当前为0|
|DS3|托管FullNode/SolidityNode接口|采集候选|供应商、限流和历史能力需核验|
|DS4|TronGrid扩展索引|发现账户/Token候选|不是标准节点原始对象|
|DS5|区块浏览器/社区页面|线索和人工导航|不得单独支持P0|

每个来源必须登记端点、接口族、`visible`参数、节点类型、版本/声明、观察时间、区块高度和原始响应哈希。

## 4. 角色与前置门

|角色|职责|
|---|---|
|TRON方法负责人|维护网络、协议对象、字段语义和验证范围|
|节点负责人|证明FullNode/SolidityNode能力、版本、同步和数据保留|
|执行人员|保存请求、响应、编码、对象哈希和错误|
|独立复核人员|从冻结对象复算地址、交易ID、字段和状态|
|质量负责人|审查真值、偏差、数据源、工具和结论措辞|

执行前需具名授权、批准方法/工具、数据源审查和任务范围。当前均未满足。

## 5. 详细控制要求

|控制ID|主题|强制规则|最低证据|阻断条件|
|---|---|---|---|---|
|M-TRON-001-C001|网络与节点类型|记录网络、创世/检查点锚、节点接口族、节点类型和观察高度；相同地址格式不证明网络相同|网络与节点登记|网络或接口族不明|
|M-TRON-001-C002|FullNode|`/wallet/*`结果按最新可见链状态记录，不自动称为已确认；保存请求和返回区块锚|原始响应|把FullNode可见等同固化|
|M-TRON-001-C003|SolidityNode|`/walletsolidity/*`结果只按官方固化语义使用，并记录返回高度与观察时间|原始响应、节点状态|以名称代替实际响应核验|
|M-TRON-001-C004|交易本体|Transaction对象须与交易ID、区块定位和TransactionInfo分开保存并建立引用|交易对象、对象哈希|只有浏览器展示|
|M-TRON-001-C005|raw_data|保存`raw_data`结构及可用的原始序列化字节；任何重编码形成派生对象|原始/派生对象|JSON重排后声称原始字节|
|M-TRON-001-C006|签名|保留签名数组原值；只在序列化和签名规则经验证时恢复地址，不把签名地址等同自然人|签名原值、复算|规则或字节边界不明|
|M-TRON-001-C007|contract参数|按`type_url`和对应协议消息解码`contract`参数，保存原始value和`Permission_id`适用性|Protobuf依据、解码记录|未知类型被按转账解析|
|M-TRON-001-C008|TransactionInfo|TransactionInfo须与交易ID、blockNumber和交易本体闭合；缺失明确区分未找到、未执行或端点能力不足|原始响应|空响应被写成失败|
|M-TRON-001-C009|result|分别保存交易`ret.contractRet`及TransactionInfo receipt/result语义，不把字段名相似视为等价|字段对照|状态字段互相覆盖|
|M-TRON-001-C010|resMessage|保存原始值、编码和派生文本；无法解码时保持原值，不把缺失解释为无异常|原值、解码规则|乱码/空值被静默丢弃|
|M-TRON-001-C011|fee|费用使用整数SUN保存，并分解可得费用项；展示TRX值不得覆盖整数原值|TransactionInfo、分录|浮点数或单位不明|
|M-TRON-001-C012|energy_usage|分别记录当次和累计Energy字段、来源及单位，不把资源用量直接换算为固定货币价值|receipt原值|字段/单位混用|
|M-TRON-001-C013|net_usage|记录Bandwidth/net_usage及相关费用字段，区分资源消耗和支付金额|receipt原值|缺字段被填0|
|M-TRON-001-C014|blockNumber|blockNumber与区块ID、时间、交易位置和节点观察高度闭合|区块/交易对象|仅凭扩展索引高度|
|M-TRON-001-C015|log事件|日志保留address、topics、data、顺序和原始编码；ABI/TRC-20解码形成派生对象|日志原值、ABI依据|只保存解码展示|
|M-TRON-001-C016|internal_transactions|记录每条内部调用/转值及`rejected`字段的接口差异；不得称为独立共识交易|TransactionInfo原值|忽略rejected或失败父交易|
|M-TRON-001-C017|TRC-20 decimals|decimals须从目标合约、目标高度可复核来源取得并版本化；整数原值始终保留|调用响应、代码/ABI|用聚合器元数据覆盖|
|M-TRON-001-C018|地址编码|地址保存网络、21字节hex表示、Base58Check表示和校验状态；不得截断原值|地址对象|长度、前缀或校验失败|
|M-TRON-001-C019|Base58与hex转换|转换须验证`41`前缀、Base58Check校验和和往返一致；Ethereum式20字节另存派生值|测试向量、复算|只做字符串替换|
|M-TRON-001-C020|确认语义|确认必须以固化接口/区块状态和观察时间证明；确认状态属于F3动态事实|SolidityNode响应|把确认写成永久属性|
|M-TRON-001-C021|失败交易|区分纳入区块、固化和TVM执行结果；失败交易仍保留费用、资源和可观察错误|交易、TransactionInfo|以已上链替代执行成功|
|M-TRON-001-C022|链上时间|保存区块时间原始整数、单位依据、UTC派生值和观察时间；不以本机时间覆盖|区块对象、转换记录|单位未验证|
|M-TRON-001-C023|多节点复核|P0字段由第二节点/实现或离线规则复核，完整保留节点差异和延迟|差异表|通过多数投票消除冲突|

## 6. 标准工作流程

### 6.1 T0 运行登记

登记网络、交易/区块ID、技术问题、输出边界、数据源、接口族和停止条件。

### 6.2 T1 网络与节点确认

核对网络锚、FullNode/SolidityNode类型、版本、同步高度、托管服务身份和观察时间。

### 6.3 T2 交易本体固定

从明确接口获取Transaction，保存完整请求、响应、HTTP元数据、错误、重试和SHA-256。

### 6.4 T3 执行结果固定

获取TransactionInfo，并核对交易ID、blockNumber、result/receipt、费用、资源、日志和内部调用。

### 6.5 T4 固化状态复核

使用SolidityNode接口查询同一交易/区块，记录是否可得和返回锚点；不对尚未固化对象提前升级。

### 6.6 T5 字段与编码解析

按协议消息类型解析`raw_data.contract`，验证地址往返、整数单位和时间单位。

### 6.7 T6 TRX/TRC-20变化

分别记录顶层TRX、合约内部转值、TRC-20日志候选、费用和资源。无法闭合时输出分量而非净额。

### 6.8 T7 第二来源复核

用第二节点、不同接口或离线实现复算P0字段；扩展索引只能辅助发现，不作投票。

### 6.9 T8 复核与输出

冻结事实、派生值、冲突、未知和限制，绑定方法/工具/节点版本与运行ID。

## 7. 交易与执行状态

### 7.1 三个不同问题

|问题|所需证据|允许表述|
|---|---|---|
|是否可被节点查询|对应接口原始响应|在观察时点由该节点返回|
|是否已固化|SolidityNode/固化区块证据|在观察时点处于固化状态|
|是否执行成功|相应交易结果字段|该合约执行结果字段为成功|

三个问题不得相互替代。

### 7.2 系统合约与智能合约

不同交易类型的成功判定字段可能不同。方法实现必须先确定`type_url`，再选择规则；不得用一个全局`result`字段处理所有交易。

### 7.3 内部调用

`internal_transactions`是执行信息中的记录，不具有独立交易ID语义。HTTP与gRPC对成功记录的`rejected`字段展示可能不同，必须登记接口并把缺失与`false`区分。

## 8. 地址、金额与Token

### 8.1 地址

内部标准对象同时保存：

- `address_hex_21`：含网络前缀的21字节表示；
- `address_base58check`；
- `address_payload_20`：仅作明确标注的派生值；
- `network_id`；
- `checksum_valid`；
- 转换工具、版本和测试向量。

### 8.2 金额

TRX金额以整数SUN为原值。Token金额以合约事件/状态中的整数为原值；`decimals`只用于展示换算。

### 8.3 TRC-20候选

一个`Transfer`解码至少需要：

- 目标合约地址；
- 事件topic与data原值；
- 交易执行状态；
- 合约代码/接口证据；
- `from`、`to`、整数`value`；
- decimals来源与高度；
- 非标准行为和Token税限制。

事件候选不能单独证明余额净变化或资产价值。

## 9. 错误、冲突与停止

必须停止强结论：

- 网络或节点类型不能确认；
- Transaction与TransactionInfo的交易ID/区块不能闭合；
- FullNode与SolidityNode状态被混用；
- 原始序列化边界不明却需要交易ID/签名复算；
- 地址校验和或往返转换失败；
- 合约类型、执行状态或decimals来源未知；
- 内部调用被裁剪或`rejected`语义不明；
- 第二节点P0字段冲突；
- 任务要求自然人控制、意图或法律判断。

停止时保留所有原值、端点错误、节点高度和差异。

## 10. 输出字段最低集

```text
run_id
network_id / network_anchor
node_id / node_type / client_version / observed_height
api_family / endpoint_id / visible
transaction_id / transaction_object_id
contract_type_url / contract_parameter_raw
block_number / block_id / block_timestamp_raw / block_time_utc
solid_status / solid_observed_at
contract_ret / receipt_result / res_message_raw
fee_sun / energy_usage / energy_usage_total / net_usage
log_index / contract_address / topics / data
internal_index / internal_rejected / internal_value
address_hex_21 / address_base58check / checksum_valid
token_contract / amount_integer / decimals / amount_display
fact_level / value_status / method_version / tool_id
input_object_ids / review_status / limitation
```

## 11. 记录与关联接口

|记录|最低内容|
|---|---|
|网络/节点登记|网络锚、节点类型、接口、版本、同步和端点|
|采集记录|请求、响应、`visible`、错误、时间和对象哈希|
|交易解析|type_url、raw_data、签名、参数和整数字段|
|执行解析|result、费用、资源、日志、内部调用和失败|
|编码复算|Base58Check/hex测试向量和往返结果|
|固化复核|FullNode/SolidityNode差异和观察高度|
|技术复核|第二节点/实现结果、差异和处置|

关联：

- [`ARC-006`](../03-architecture/06-node-data-source-governance.md)
- [`SOP-002`](../06-operations/02-acquisition-session.md)
- [`SOP-003`](../06-operations/03-analysis-review.md)
- [`MTH-001`](./01-general-method-framework.md)
- [`M-AUTH-001`](./10-authenticity-integrity.md)

## 12. 方法验证矩阵

|维度|正向样本|反向/边界样本|接受原则|当前状态|
|---|---|---|---|---|
|网络/节点|登记网络的FullNode与SolidityNode|错误网络、节点类型伪报|身份错误必须阻断|未执行|
|交易对象|TRX、系统合约、智能合约|未知type_url、畸形raw_data|原值保留且不误解析|未执行|
|状态|已上链、固化、成功|未固化、执行失败、空响应|三种状态不混用|未执行|
|费用资源|有/无资源抵扣场景|字段缺失、极值|整数与单位正确|未执行|
|日志/internal|标准TRC-20和内部调用|伪事件、rejected、失败父交易|候选不过度解释|未执行|
|地址|已知Base58Check/hex向量|错前缀、错校验和、错长度|无效地址拒绝|未执行|
|时间|已知区块时间|单位错误、未来值|原值与UTC可复算|未执行|
|多节点|同高度一致响应|高度差、字段冲突、裁剪|差异保留并停止|未执行|
|复现性|冻结响应离线复算|不同工具/环境|P0无未解释差异|未执行|

## 13. 当前证据与限制

- TRON样本目前仅为候选设计；
- 原始交易、TransactionInfo和固化响应包数量为0；
- 地址转换获批测试向量数量为0；
- TRC-20、失败交易和内部调用真值数量为0；
- 自建FullNode/SolidityNode数量为0；
- 第二节点/实现复核数量为0；
- 方法、工具和人员批准数量为0。

## 14. 生效前检查

- [ ] 网络锚和节点接口登记获批；
- [ ] FullNode与SolidityNode能力实测；
- [ ] Transaction/raw_data原始对象冻结规则验证；
- [ ] 系统合约和智能合约状态规则验证；
- [ ] 费用、Energy、Bandwidth整数规则验证；
- [ ] 日志、内部调用和失败交易反例通过；
- [ ] Base58Check/hex转换测试向量通过；
- [ ] TRC-20 decimals与非标准Token边界验证；
- [ ] 第二节点或独立实现复算；
- [ ] 工具、人员、方法和用途获批。

## 15. 外部依据

- [TRON Transactions](https://developers.tron.network/docs/tron-protocol-transaction)
- [TRON Accounts and address formats](https://developers.tron.network/docs/account)
- [FullNode HTTP API Overview](https://developers.tron.network/reference/full-node-api-overview)
- [TRON Transaction Info](https://developers.tron.network/docs/transaction-info)
- [GetTransactionInfoById](https://developers.tron.network/reference/gettransactioninfobyid-1)
- [TRC-20 Protocol Interface](https://developers.tron.network/docs/trc20-protocol-interface)
- [TRC-20 Contract Interaction](https://developers.tron.network/docs/trc20-contract-interaction)
- [Parameter Encoding and Decoding](https://developers.tron.network/docs/parameter-encoding-and-decoding)

这些页面属于外部动态资料。方法批准、签约或重大版本发布前须重新核验、记录更新时间并保存适用快照。

## 16. 版本记录

|版本|日期|变更|状态|
|---|---|---|---|
|0.2.0|2026-07-30|重建节点类型、交易/执行状态、资源、地址、TRC-20和固化复核规则|受控草案，未签批|
|3.0.0-draft|2026-07-27|历史结构化生成稿；生产声明已撤销|已由本版替代|
