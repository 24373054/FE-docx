---
document_id: M-EVM-001
title: EVM链采集、执行重建与资产变化方法
version: 0.2.0
status: 受控草案
document_type: 技术方法
owner: EVM方法负责人
approver: 质量负责人（未签批）
effective_date: 尚未生效
review_cycle: 每6个月或网络升级、客户端、RPC、合约标准重大变化时
classification: 内部受控
---

# EVM链采集、执行重建与资产变化方法

## 1. 文件目的

定义EVM兼容链交易、收据、日志、调用轨迹、历史代码和资产变化的候选采集与重建规则。

本方法优先回答“指定网络、区块和交易在冻结来源中包含什么，以及批准算法能复算什么”，不以接口显示替代原始响应，不以事件或trace自动证明现实主体控制。

当前EVM样本、真值、归档节点、跨客户端复算、工具验证和方法批准均为0。本文件只用于研发与验证设计。

## 2. 适用范围与排除

### 2.1 当前候选范围

- 以太坊及经单独登记的EVM兼容网络；
- 区块、交易、交易收据和日志固定；
- 传统及类型化交易字段解析；
- 合约创建、调用轨迹、状态差异和资产变化候选；
- ERC-20、ERC-721、ERC-1155标准事件候选；
- 代理合约、历史代码、失败调用和账户抽象对象。

### 2.2 明确排除

- 未登记网络或把相同地址格式视为同一链；
- 用`latest`响应重建历史事实；
- 把debug/trace接口视为共识对象；
- 只根据`Transfer`事件断言完整资产变化；
- 只根据`from`、bundler、paymaster或事件地址认定真实签名人；
- 未经验证的MEV、意图、攻击者身份、获利或法律责任结论。

## 3. 输入对象与冻结单元

一个运行必须冻结：

|对象|最低字段|
|---|---|
|网络身份|规范名称、chain ID、创世区块哈希、网络配置来源|
|节点身份|执行客户端、版本、构建、节点模式、同步/裁剪状态、端点ID|
|区块锚点|区块号、区块哈希、父哈希、时间、状态标签、观察时间|
|交易|交易哈希、类型、完整RPC响应或可用原始封装、区块定位|
|收据|交易哈希、区块哈希、索引、status、gas、logs、原始响应|
|扩展对象|trace、state diff、代码、存储、ABI及各自接口和参数|
|运行环境|工具制品、依赖、配置、时区、开始/结束时间|

对象固定后不得覆盖；补采形成新对象并引用父对象。

## 4. 角色与前置门

|角色|职责|
|---|---|
|EVM方法负责人|登记网络、协议分叉、对象规则和验证范围|
|节点负责人|证明端点、客户端、同步、归档、trace和历史状态能力|
|执行人员|固定请求/响应、对象哈希、参数和异常|
|独立复核人员|按区块哈希重取或离线复算P0字段|
|质量负责人|审查样本、偏差、工具、授权和结论边界|

运行前必须同时满足任务授权、人员授权、方法版本、工具版本、数据源等级和最小必要性。当前这些运行门未满足。

## 5. 详细控制要求

|控制ID|主题|强制规则|最低证据|阻断条件|
|---|---|---|---|---|
|M-EVM-001-C001|Chain ID|调用`eth_chainId`并与任务登记和创世锚点共同确认网络；chain ID不能单独证明网络身份|请求响应、登记表|三者不一致|
|M-EVM-001-C002|创世区块|保存高度0完整响应及区块哈希；无法提供创世历史的端点降级|创世对象、哈希|只凭端点名称认链|
|M-EVM-001-C003|客户端版本|记录客户端名称、版本、构建、端点、同步/归档能力；`web3_clientVersion`仅是声明|节点快照|版本或能力不可核验|
|M-EVM-001-C004|区块标签safe/finalized|记录实际请求标签、返回区块号/哈希和观察时间；不支持时不得伪造等价标签|原始RPC响应|标签语义未知或被`latest`替代|
|M-EVM-001-C005|区块头|按网络规则保存区块哈希、父哈希、状态根、交易根、收据根、时间和分叉相关字段|区块对象|字段缺失且影响复算|
|M-EVM-001-C006|交易类型|保留类型字节/字段和完整交易对象；未知类型输出`unsupported`而非按legacy解析|交易对象、解析记录|类型被默认覆盖|
|M-EVM-001-C007|交易签名|只在对应交易类型和签名规则已验证时恢复发送地址；保留签名原值和链域|原值、复算结果|签名规则/链域不明|
|M-EVM-001-C008|nonce|nonce按无符号整数保存，并区分交易nonce、账户观察值及账户抽象nonce|字段映射|不同nonce语义混用|
|M-EVM-001-C009|gas字段|gasLimit、gasPrice、maxFee、priorityFee、gasUsed、effectiveGasPrice等保持原始整数与字段适用性|交易/收据对照|浮点换算覆盖原值|
|M-EVM-001-C010|交易收据|收据必须与交易哈希、区块哈希、区块号和交易索引闭合；pending时明确不可得|收据原始响应|区块或交易身份冲突|
|M-EVM-001-C011|status|`status`只表示执行成功/失败语义；成功不证明业务目的达成，失败仍可产生费用和可观察对象|收据、说明|以收据存在替代成功|
|M-EVM-001-C012|logs|按`logIndex`保留地址、topics、data、removed和区块/交易锚点；ABI解码为派生对象|日志对象|只保存解码展示|
|M-EVM-001-C013|logsBloom|bloom只按已验证算法用于候选筛选；阳性须回到日志，阴性适用性须单独验证|bloom原值、测试|将bloom命中当事件证明|
|M-EVM-001-C014|合约创建|以`to`适用性、收据`contractAddress`和执行结果共同记录创建；CREATE/CREATE2内部创建依赖trace|交易、收据、trace|只从地址有代码反推创建交易|
|M-EVM-001-C015|内部调用轨迹|trace必须登记接口、客户端、tracer、参数和错误；不得称为共识交易或“内部交易”事实|trace原始响应|接口语义不明或裁剪|
|M-EVM-001-C016|状态差异|state diff绑定前后区块/交易边界、客户端和归档能力；缺历史状态时输出不可验证|diff与锚点|用当前状态代替历史状态|
|M-EVM-001-C017|原生币变化|按顶层value、内部调用、费用和适用协议项分项重建；无法闭合时不输出净变化强结论|分录、平衡检查|只看顶层value|
|M-EVM-001-C018|ERC-20事件|标准`Transfer`事件只形成代币变化候选；核对合约、topic、data、status、代码版本和异常语义|日志、ABI依据|把任意同topic日志当标准转账|
|M-EVM-001-C019|NFT事件|区分ERC-721和ERC-1155、单笔/批量、token ID和数量；接口识别失败时保持未知|日志、接口证据|标准或字段混用|
|M-EVM-001-C020|代理合约|按区块高度解析代理、实现、存储槽和升级事件；报告同时保留代理与实现地址|历史存储/代码|以当前实现解释历史调用|
|M-EVM-001-C021|历史代码|`eth_getCode`必须指定区块；保存字节码哈希、获取高度和端点历史能力|代码对象|用最新代码覆盖历史代码|
|M-EVM-001-C022|revert原因|revert data和解码只作派生信息，注明来源、ABI和可能缺失/截断|原始返回、解码|把缺失原因写成无错误|
|M-EVM-001-C023|自毁与重建|按网络分叉和交易时点解释SELFDESTRUCT/代码变化，不沿用单一历史语义|分叉依据、前后状态|协议版本未确定|
|M-EVM-001-C024|Account Abstraction|分别记录顶层交易、EntryPoint/UserOperation、sender、bundler、factory、paymaster和签名验证范围|事件/调用/协议版本|把bundler或paymaster认定为控制人|
|M-EVM-001-C025|跨客户端差异|P0字段至少用第二实现或离线规则复核；trace等非标准输出按实现比较并保留差异|差异表|差异被多数投票掩盖|

## 6. 标准工作流程

### 6.1 E0 运行登记

登记任务、问题、网络、对象、时间范围、允许输出、数据源和停止条件。

### 6.2 E1 网络与节点确认

固定chain ID、创世锚点、客户端版本、同步高度、归档/trace能力和观察时间。

### 6.3 E2 区块锚定

优先以明确区块哈希或区块号加返回哈希工作。记录`safe`、`finalized`或其他标签的原始请求，不在后续以`latest`重放。

### 6.4 E3 交易与收据固定

保存JSON-RPC方法、参数、完整响应、HTTP/传输元数据、错误、重试、SHA-256和对象关系。

### 6.5 E4 字段解析

按交易类型解析数量和数据字段，保持十六进制原值，派生十进制值不覆盖原值。

### 6.6 E5 执行扩展

只有节点能力和工具验证允许时才采集trace、state diff、历史代码和存储；每种扩展单独声明非共识性质。

### 6.7 E6 资产变化重建

分别建立原生币、标准代币、NFT和费用分录。事件、调用和状态差异交叉核对，任何未闭合项保留。

### 6.8 E7 历史语义

解析代理实现、代码版本、网络分叉和协议规则在目标区块的有效状态。

### 6.9 E8 独立复核

复核人员从冻结响应或第二节点重新解析P0字段，不读取执行人员最终汇总后简单签字。

### 6.10 E9 输出

输出事实、派生、候选、冲突和未知；绑定运行ID、方法/工具版本、区块锚点和限制。

## 7. 交易、收据与执行规则

### 7.1 数量和数据编码

JSON-RPC `QUANTITY`与`DATA`必须分开验证。数量转十进制使用任意精度整数；地址、哈希、字节码和data保持定长/偶数位语义。

### 7.2 pending与区块内对象

pending交易没有稳定的区块哈希、区块号和收据。pending观察形成动态对象，不得与已纳入区块的交易合并为同一状态。

### 7.3 失败交易

失败交易至少可能保留：

- 交易已纳入区块的事实；
- 发送地址、nonce和输入data；
- `status=0`；
- gas使用和费用；
- trace或revert data（如可得）。

不得因为失败而删除交易，也不得因为有日志展示或供应商标签就覆盖收据状态。

### 7.4 日志

事件解码必须保存：

- 合约地址；
- topic原值与事件签名依据；
- indexed与非indexed参数位置；
- data原值；
- ABI/标准版本；
- 解码工具与结果；
- 标准偏离和反例。

## 8. 资产变化和功能边界

### 8.1 原生币

顶层`value`只是一个分量。若没有完整调用轨迹、费用规则和适用状态证据，输出“观察到顶层转值”而非“全部净变化”。

### 8.2 Token

Token名称、符号和decimals是合约返回的元数据，不证明资产性质、价值或合法性。金额同时保留整数原值、decimals来源和展示值。

### 8.3 代理与账户抽象

代理调用的代码身份依目标高度确定。账户抽象场景中“发起、提交、支付、验证、执行、受益”可能由不同对象承担，报告不得压缩成单一“发送人”。

## 9. 冲突、错误与停止条件

必须停止强结论：

- chain ID与创世锚点不一致；
- 交易、收据和区块哈希不能闭合；
- 同区块P0字段在两个可信实现间冲突；
- 节点裁剪但任务需要历史代码/状态；
- trace被截断、超时或实现语义未知；
- 代理历史或网络分叉无法确定；
- Token合约非标准且只有事件展示；
- 结果需要主体身份、意图或法律判断。

停止后仍保存原始响应、差异和允许的F1/F2事实。

## 10. 输出字段最低集

```text
run_id
network_id / chain_id / genesis_hash
node_id / client / version / capability
block_number / block_hash / block_status / observed_at
transaction_hash / transaction_type / transaction_index
receipt_status / gas_used / effective_gas_price
log_address / topics / data / log_index / removed
trace_provider / tracer / trace_status
code_address / implementation_address / code_hash / code_block
asset_contract / asset_standard / amount_integer / decimals / amount_display
fact_level / value_status / method_version / tool_id
input_object_ids / rule_id / review_status / limitation
```

空缺须使用明确状态，不得用0伪装未知。

## 11. 记录与关联接口

|记录|最低内容|
|---|---|
|网络登记|chain ID、创世哈希、官方依据、分叉和网络状态|
|节点记录|客户端、版本、端点、归档、trace、同步和裁剪|
|采集记录|请求、响应、重试、错误、对象哈希和时间|
|解析记录|交易类型、字段映射、整数转换和异常|
|资产分录|来源对象、规则、整数、decimals和未闭合项|
|复核记录|第二实现/规则、差异、处置和签名|

接口文件：

- [`ARC-006`](../03-architecture/06-node-data-source-governance.md)
- [`SOP-002`](../06-operations/02-acquisition-session.md)
- [`SOP-003`](../06-operations/03-analysis-review.md)
- [`MTH-001`](./01-general-method-framework.md)
- [`M-FUNC-001`](./11-smart-contract-functional-analysis.md)

## 12. 方法验证矩阵

|维度|正向样本|反向/边界样本|接受原则|当前状态|
|---|---|---|---|---|
|网络身份|主网与已登记测试网|相同chain ID声明、错误创世锚点|错误网络必须阻断|未执行|
|交易类型|legacy及获批类型化交易|未知类型、畸形字段|不误按其他类型解析|未执行|
|收据状态|成功与失败交易|pending、区块哈希冲突|状态与费用正确分层|未执行|
|日志|ERC-20/721/1155标准事件|伪topic、非标准合约、removed日志|原值保留且候选不过度解释|未执行|
|trace|至少两客户端支持的简单调用|超时、裁剪、不同tracer|差异显式且不冒充共识|未执行|
|历史状态|代理升级前后代码|非归档端点、同区块升级|按目标高度解释|未执行|
|资产变化|顶层与内部转值、费用|Token税、rebase、失败调用|分录闭合或明确未知|未执行|
|账户抽象|受控UserOperation场景|bundler/paymaster混淆|角色不被压缩|未执行|
|复现性|冻结响应离线复算|更换客户端和环境|P0无未解释差异|未执行|

## 13. 当前证据与限制

- EVM候选样本已在样本登记中设计，但没有冻结原始对象包；
- 没有GT1至GT4获批真值；
- 没有自建归档节点或获批第三方RPC；
- 没有第二客户端复算；
- 没有trace、state diff、代理历史或账户抽象验证包；
- 方法、工具、人员和报告模板均未批准。

因此，本方法当前只能作为V0验证设计，不得出具EVM技术结论。

## 14. 生效前检查

- [ ] 网络登记和创世锚点获批；
- [ ] 自建/第三方节点能力及许可审查完成；
- [ ] 正常、失败、pending、重组和历史状态样本获批；
- [ ] 交易类型、收据、日志和整数转换P0测试通过；
- [ ] 至少第二客户端或独立实现复算；
- [ ] trace与state diff的实现差异已量化；
- [ ] Token、代理、SELFDESTRUCT和账户抽象边界验证；
- [ ] 工具和环境验证通过；
- [ ] 独立人员复现并签名；
- [ ] 方法、人员和用途获批。

## 15. 外部依据

- [Ethereum JSON-RPC API](https://ethereum.org/developers/docs/apis/json-rpc/)
- [EIP-1474 Remote procedure call specification](https://eips.ethereum.org/EIPS/eip-1474)
- [EIP-2718 Typed Transaction Envelope](https://eips.ethereum.org/EIPS/eip-2718)
- [EIP-658 Transaction receipt status](https://eips.ethereum.org/EIPS/eip-658)
- [ERC-20 Token Standard](https://eips.ethereum.org/EIPS/eip-20)
- [ERC-721 Non-Fungible Token Standard](https://eips.ethereum.org/EIPS/eip-721)
- [ERC-1155 Multi Token Standard](https://eips.ethereum.org/EIPS/eip-1155)
- [ERC-1967 Proxy Storage Slots](https://eips.ethereum.org/EIPS/eip-1967)
- [ERC-4337 Account Abstraction](https://eips.ethereum.org/EIPS/eip-4337)
- [EIP-6780 SELFDESTRUCT only in same transaction](https://eips.ethereum.org/EIPS/eip-6780)

外部资料须在方法批准或重大版本发布前重新核验并保存快照；EIP状态及网络采用情况必须按目标区块另行确认。

## 16. 版本记录

|版本|日期|变更|状态|
|---|---|---|---|
|0.2.0|2026-07-30|重建网络锚定、交易/收据、trace、历史状态、资产变化和账户抽象规则|受控草案，未签批|
|3.0.0-draft|2026-07-27|历史结构化生成稿；生产声明已撤销|已由本版替代|
