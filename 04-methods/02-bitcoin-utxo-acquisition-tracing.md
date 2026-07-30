---
document_id: M-BTC-001
title: Bitcoin对象提取与UTXO确定性事实重建方法
version: 0.2.0
status: 受控草案
document_type: 技术方法
owner: Bitcoin方法负责人
approver: 项目发起人（未签批）
effective_date: 尚未生效
review_cycle: 每6个月或协议、客户端、数据源、规则、用途变化时
classification: 内部受控
---

# Bitcoin对象提取与UTXO确定性事实重建方法

## 1. 文件目的

本方法规定Bitcoin主网区块、交易、输入、输出和UTXO确定性字段的获取、固定、解析、计算、冲突处理和复核。

当前状态：

- 仅为受控草案；
- 只允许公开或批准的模拟样本研发；
- `M-BTC-T1`对象提取与固定尚未完成正式验证；
- `M-BTC-T2`确定性交易事实重建尚未完成正式验证；
- 创世区块候选GT2达到`truth_prepared`但未由公司指定人员复核；
- 找零、聚类、CoinJoin、路径分配、身份归属和法律结论不在当前方法范围。

本文件不授权真实案件操作或对外出具司法鉴定意见。

## 2. 方法身份与范围

### 2.1 方法单元

|method_id|名称|输入|输出|当前状态|
|---|---|---|---|---|
|M-BTC-T1|Bitcoin对象提取与固定|网络、区块/交易ID、批准来源|原始对象、来源记录、哈希、确定性头字段|planned|
|M-BTC-T2|UTXO确定性事实重建|冻结原始区块/交易|输入输出、原始整数、手续费、脚本分类候选、字段血缘|planned|

### 2.2 当前纳入

- Bitcoin主网；
- 已最终确认或固定历史对象；
- 区块头和区块哈希；
- 原始区块与交易序列化字节；
- txid及在适用时的wtxid；
- 输入outpoint和输出索引；
- 输出原始satoshi值；
- coinbase结构；
- 非coinbase交易手续费的确定性计算；
- 指定观察时点的UTXO与确认状态，但必须带来源和时点。

### 2.3 当前排除

- 测试网、signet和regtest对外结论；
- mempool对象作为最终事实；
- 闪电网络、侧链和托管平台内部账；
- 脚本执行有效性全面验证；
- 地址控制人、受益人或自然人身份；
- 找零识别、多输入聚类、CoinJoin识别；
- FIFO、LIFO、haircut、poison等资金路径分配；
- 交易目的、违法性、权属或法律责任；
- 冻结、解冻、签名、广播、兑换和资产处置。

任何排除项只能作为后续独立方法立项，不得以“分析备注”绕过验证。

## 3. 输出分层

|层级|示例|当前允许|
|---|---|---|
|F1原始事实|原始字节、对象ID、输入输出、satoshi、区块高度|允许研发|
|F2协议计算|区块哈希、txid、wtxid、手续费、Merkle检查|允许研发|
|F3观察状态|确认数、UTXO是否已花费、mempool/RBF状态|只允许带观察时点和来源|
|I1规则推断|脚本类型、候选找零、CoinJoin候选|仅候选研究 不进入当前结论|
|I2统计/主体推断|聚类、身份、控制关系、风险标签|禁止当前方法输出|
|L法律判断|权属、违法性、责任、证据能力|禁止|

输出字段必须携带`fact_level`，不能把F3或I1显示为永久链上事实。

## 4. 角色与前置授权

|角色|职责|
|---|---|
|方法负责人|维护规则、范围、P0字段和停止门|
|获取执行人|确认网络和来源并固定原始对象|
|解析执行人|按冻结版本解析与计算|
|样本/真值负责人|建立GT1至GT4|
|独立复核人|从原始字节重算P0字段|
|质量负责人|检查运行、偏离、差异和状态|
|批准人|批准方法、工具、人员、环境和用途|

运行前必须具备：

- 合法用途和对象范围；
- 方法版本与哈希；
- 批准的工具/环境版本；
- 网络身份和来源策略；
- 样本或案件对象的授权记录；
- 执行人与独立复核人；
- 证据包位置和访问控制；
- 预期、P0门和停止条件。

缺少任一项，正式运行`blocked`。

## 5. 详细控制要求

|控制ID|主题|本版强制要求|当前实施|
|---|---|---|---|
|M-BTC-001-C001|网络与链身份|记录网络、创世哈希、节点链参数和对象所属网络|not_implemented|
|M-BTC-001-C002|节点版本|记录客户端、构建、配置、同步和索引状态|not_implemented|
|M-BTC-001-C003|区块头|从原始80字节按端序解析六个头字段|truth_prepared仅创世样本|
|M-BTC-001-C004|区块哈希|对头字节双SHA-256并保留内部与显示形式|truth_prepared仅创世样本|
|M-BTC-001-C005|前序区块|保留原始32字节和显示值；创世对象单独标记|truth_prepared仅创世样本|
|M-BTC-001-C006|Merkle根|从头提取并在验证范围内由交易重算|truth_prepared仅单交易创世样本|
|M-BTC-001-C007|交易原始字节|保存序列化字节、边界、字节数和哈希|truth_prepared仅创世交易|
|M-BTC-001-C008|txid与wtxid|按是否含witness分别计算；不得混用|not_implemented|
|M-BTC-001-C009|输入引用|保存previous txid、vout、script、sequence和coinbase例外|truth_prepared仅创世coinbase|
|M-BTC-001-C010|输出索引|保持区块/交易顺序和零基索引|truth_prepared仅创世输出0|
|M-BTC-001-C011|脚本类型|只按批准规则输出类型候选并保留原始script|not_implemented|
|M-BTC-001-C012|金额单位|原始整数使用satoshi；显示换算不覆盖原值|truth_prepared仅5000000000|
|M-BTC-001-C013|coinbase|按全零prev txid与`0xffffffff` vout识别结构|truth_prepared仅创世样本|
|M-BTC-001-C014|手续费|非coinbase为输入原值和减输出原值和；缺输入即不可得|not_implemented|
|M-BTC-001-C015|UTXO状态|必须限定观察时点、链尖、节点和索引状态|not_implemented|
|M-BTC-001-C016|确认数|作为动态观察字段保存高度、链尖和时间|not_implemented|
|M-BTC-001-C017|链重组|检测对象是否仍在最佳链并保留前后状态|not_implemented|
|M-BTC-001-C018|RBF|仅描述交易信号和观察状态 不判断最终替代目的|not_implemented|
|M-BTC-001-C019|找零候选|当前禁止输出|excluded_unvalidated|
|M-BTC-001-C020|多输入启发式|当前禁止聚类或共同控制结论|excluded_unvalidated|
|M-BTC-001-C021|CoinJoin识别|当前禁止确定识别 仅可另立候选研究|excluded_unvalidated|
|M-BTC-001-C022|路径分配模型|当前禁止选择或暗示唯一资金路径|excluded_unvalidated|
|M-BTC-001-C023|拒绝主体归属|没有链下授权证据时必须拒绝主体归属|mandatory|

表内`truth_prepared`只描述一个公开样本的证据成熟度，不表示控制已实施。正式状态仍以`catalogs/controls.csv`为准。

## 6. 标准工作流程

### 6.1 B0 运行登记

分配：

- `validation_run_id`或`case_run_id`；
- `method_id`与版本；
- `sample_id`或授权对象ID；
- 执行人和复核人；
- 输入来源与预期输出；
- 环境和工具ID。

### 6.2 B1 网络确认

至少核对：

- 网络名称；
- 创世区块哈希；
- 节点报告链；
- 端口/端点所属环境；
- 查询对象是否可能来自另一网络；
- 当前链尖、高度和同步状态。

公共API无法报告底层客户端时标为`source_client_unknown`，不得假定为Bitcoin Core。

### 6.3 B2 对象定位

优先使用固定区块哈希或交易ID。按高度查询时：

- 保存查询高度和返回哈希；
- 对仍可能重组的对象不得视为最终；
- 多个候选时全部记录；
- 动态`latest`只用于定位，不用于冻结真值。

### 6.4 B3 原始对象获取

保存：

- 请求方法、URL/RPC方法和参数；
- 起止时间、响应状态和头；
- 原始二进制或无损十六进制；
- 字节数、编码和SHA-256；
- 来源、重试、切源和失败；
- TLS/出口/客户端信息的可得程度。

只保存浏览器JSON字段而不保存原始对象时，不能进入P0重算。

### 6.5 B4 完整性与对象身份

对区块：

1. 读取前80字节；
2. 计算区块哈希；
3. 与请求ID和来源返回ID比较；
4. 解析交易数量；
5. 确认解析消耗全部字节。

对交易：

1. 识别legacy或SegWit序列化；
2. 确定交易边界；
3. 分别计算txid/wtxid；
4. 与区块交易清单和查询ID比较；
5. 保留原始字节。

任一P0不一致触发`source_conflict`或`integrity_failure`。

### 6.6 B5 字段解析

解析必须显式处理：

- little-endian整数；
- 内部哈希字节与显示顺序；
- CompactSize；
- 有/无witness；
- coinbase输入；
- 输入/输出顺序；
- script长度和原始字节；
- locktime与sequence原始值。

不支持的标志、版本或编码返回`unsupported`，不得猜测。

### 6.7 B6 确定性计算

允许：

- 区块哈希；
- 交易ID；
- wtxid；
- 输入outpoint清单；
- 输出索引和satoshi；
- 非coinbase手续费；
- 指定验证范围内的Merkle根；
- 指定观察时点的确认和UTXO状态。

手续费前置：

- 所有输入引用原值可得；
- 输入引用属于正确网络和对象；
- 使用整数satoshi；
- coinbase交易手续费记为`not_applicable`而不是0；
- 缺一项输入原值则手续费为`unknown`。

### 6.8 B7 多源比较

多源比较用于：

- 发现对象缺失；
- 发现字段语义差异；
- 发现数据滞后、截断和索引异常；
- 选择是否停止。

不得：

- 以多数投票代替GT；
- 静默从失败来源切到另一来源；
- 将空结果解释为不存在；
- 抹平`null`、全零、缺失和不适用；
- 把动态depth/confirmations当固定真值。

### 6.9 B8 复核

独立复核人：

1. 校验原始对象和manifest哈希；
2. 从字节重算区块哈希、txid/wtxid；
3. 抽查CompactSize和对象边界；
4. 重算输入、输出和手续费；
5. 核对coinbase和动态字段；
6. 检查未验证推断是否进入结果；
7. 记录差异和结论。

### 6.10 B9 输出

输出同时包含：

- 原始事实表；
- 计算事实表；
- 动态观察表；
- 来源和字段血缘；
- 失败、缺失、冲突和限制；
- 方法、工具、环境和时间；
- 复核状态；
- 不得推导的结论。

## 7. 区块对象规则

### 7.1 区块头

|字段|字节|解码|P0|
|---|---:|---|---|
|version|4|little-endian int32|是|
|previous block hash|32|内部字节 保留并提供反转显示|是|
|Merkle root|32|内部字节 保留并提供反转显示|是|
|timestamp|4|little-endian uint32 原始秒值|是|
|bits|4|little-endian uint32 同时保留十六进制|是|
|nonce|4|little-endian uint32|是|

区块高度不在区块头内。来源返回的height必须标记为索引/链上下文字段。

### 7.2 区块哈希

`display_hash = reverse(SHA256(SHA256(header_80_bytes)))`

记录：

- 原始80字节；
- 第一次和第二次摘要是否需要保留由计划决定；
- 内部摘要字节；
- 显示哈希；
- 与来源ID比较结果。

### 7.3 交易数量与边界

- 从偏移80读取CompactSize；
- 按交易格式逐项移动偏移；
- 解析结束必须等于原始区块字节数；
- 截断、尾随或交易数不符均为P0；
- 区块浏览器`n_tx`不参与原始交易数定义。

### 7.4 Merkle

当前只验证创世单交易样本：

- 单一交易的显示txid与显示Merkle根一致；
- 多交易Merkle树、奇数叶复制和witness commitment尚未验证；
- 在对应样本通过前不得宣称全面Merkle验证。

## 8. 交易与UTXO规则

### 8.1 交易身份

- legacy交易：txid为完整非witness序列化双SHA-256反转；
- SegWit交易：txid排除marker、flag和witness；wtxid包含完整witness序列化；
- 不支持格式返回`unsupported`；
- 显示ID和内部摘要不可混用。

### 8.2 输入

每个输入保存：

- input_index；
- previous txid原始与显示；
- previous vout；
- scriptSig原始字节；
- sequence；
- witness栈原始项；
- coinbase标记。

输入引用不证明同一主体控制。

### 8.3 输出

每个输出保存：

- output_index；
- value_satoshi；
- scriptPubKey原始字节；
- 脚本类型候选和规则版本；
- 地址显示如生成则标记为派生表示；
- 指定观察时点的spent/unspent状态及来源。

地址不是协议层主体身份。

### 8.4 金额与手续费

- 全部运算使用整数satoshi；
- BTC小数只作显示；
- 不使用浮点累计；
- 手续费不分配到单个输出；
- coinbase补贴、总输出和区块费用概念分离；
- 汇率和法币价值不属于本方法。

## 9. 动态状态规则

### 9.1 确认

确认数必须绑定：

- observed_at；
- best_block_hash；
- best_height；
- object_block_height；
- source_id；
- 节点同步状态。

报告可写“在观察时点处于最佳链某高度”，不得写成永久不变事实。

### 9.2 UTXO

`unspent`是指定节点和观察时点的状态。来源：

- 自控节点UTXO查询；
- 冻结链状态重建；
- 第三方索引辅助。

第三方索引为唯一来源时必须限制结论。

### 9.3 重组和mempool

- 未最终对象与已固定历史对象分开；
- 重组前后对象均保留；
- mempool接受不等于已确认；
- RBF信号不等于交易一定被替代；
- 冲突交易全部保留，不选“更可信”一笔隐藏其他。

## 10. 错误与停止条件

|错误|输出|是否停止P0|
|---|---|---|
|invalid_input|对象ID或字节格式错误|是|
|network_mismatch|网络与对象不一致|是|
|not_found|批准来源确认未找到|是|
|source_unavailable|端点或节点失败|是|
|source_incomplete|剪枝 截断 分页或历史不可得|是|
|source_conflict|关键字段或原始字节不一致|是|
|integrity_failure|计算ID与对象不一致|是|
|unsupported|版本 编码或脚本超范围|是|
|dynamic_state|只能给出观察时点状态|限制而非自动失败|
|not_applicable|字段不适用|不填0|
|unknown|证据不足|不得强填|

禁止自动降级为截图、缓存或单一浏览器后继续形成强结论。

## 11. 推断与报告边界

### 11.1 当前禁止

- “该输出是找零”；
- “这些输入由同一人控制”；
- “该交易是CoinJoin”；
- “资金从A流向B的唯一金额是X”；
- “该地址属于某自然人/机构”；
- “该资产属于某方”；
- “该行为违法或构成犯罪”。

### 11.2 允许的保守表达

- “交易字节显示输入引用以下outpoint”；
- “输出索引n记录原始值x satoshi”；
- “在观察时点和指定来源中该outpoint显示为未花费”；
- “来源之间存在以下冲突 因此未形成结论”；
- “当前方法不支持主体归属或唯一路径分配”。

### 11.3 链下材料

即使委托方提供KYC、交易所或设备材料，也必须：

- 独立登记来源、授权和完整性；
- 与链上事实分层；
- 评价材料时期和账户控制变化；
- 不把标签自动升级为自然人身份；
- 由另行批准的关联方法处理。

## 12. 方法验证矩阵

### 12.1 T1对象提取与固定

|场景|候选案例|目标GT|P0字段|当前|
|---|---|---|---|---|
|正常创世对象|BTC-T1-N-001|GT2+GT3|原始字节 区块哈希 头字段 交易数|truth_prepared GT2|
|创世前序表示|BTC-T1-B-006|GT2+GT4|null 全零 原始32字节|candidate_acquired|
|错误ID|BTC-T1-X-011至014|GT1/GT4|错误分类 不发外部模糊查询|candidate_design|
|来源冲突|BTC-T3-C-001至005|GT2+GT3|原始值 差异 停止|部分探针|
|畸形对象|BTC-T1-M-001至005|GT1/GT4|拒绝 完整性 资源门|candidate_design|
|历史升级|BTC-T1-R-001等|GT2+GT3|解析分支和离线恢复|candidate_design|

T1正式通过门：

- 批准样本集全部P0字段100%；
- 证据包对象完整率100%；
- 第二人员P0复验100%；
- 来源冲突均关闭或明确阻断；
- 不支持对象全部明确拒绝；
- 无未关闭P0缺陷。

### 12.2 T2确定性事实重建

|场景|候选案例|目标GT|P0字段|当前|
|---|---|---|---|---|
|P2PKH|BTC-T2-N-003|GT1+GT2|输入输出 金额 手续费|candidate_design|
|P2SH多签|BTC-T2-N-004|GT1+GT2|脚本原值 类型候选|candidate_design|
|SegWit v0|BTC-T2-N-005|GT1+GT2|txid wtxid witness|candidate_design|
|coinbase|BTC-T2-B-007|GT1+GT2|结构 不适用手续费|部分创世准备|
|零手续费|BTC-T2-B-008|GT2+GT3|整数输入输出和|candidate_design|
|Taproot|BTC-T2-B-010|GT1+GT2|witness版本 ID|candidate_design|

T2未执行，不得因创世样本通过部分字段而提前批准。

### 12.3 当前证据

|证据|结果|支持|不支持|
|---|---|---|---|
|[`VAL-METHOD-T1-PROBE-001`](../validation-evidence/public/VAL-METHOD-T1-PROBE-001/)|blocked|发现交易数冲突和停止门|方法通过|
|[`GT-BTC-GENESIS-001-V1`](../validation-evidence/public/GT-BTC-GENESIS-001-V1/)|truth_prepared|原始字节 区块哈希 交易数1 txid Merkle|GT批准或T1/T2通过|

## 13. 输出字段最低集

### 13.1 provenance

- object_id；
- object_type；
- network；
- source_id；
- acquired_at；
- raw_path、size、sha256；
- method_id/version；
- tool/environment；
- operator/reviewer；
- run status。

### 13.2 block

- block_hash_display/internal；
- version；
- previous_block_display/raw；
- merkle_root_display/raw；
- timestamp_raw；
- bits_decimal/hex；
- nonce；
- transaction_count；
- parse_end/trailing；
- height与来源；
- best_chain观察状态。

### 13.3 transaction

- txid、wtxid与适用性；
- raw bytes path/hash；
- version、locktime；
- input/output counts；
- 输入outpoint；
- 输出index、value_satoshi、script raw；
- coinbase；
- fee_satoshi或unknown/not_applicable；
- block inclusion；
- dynamic status observation。

## 14. 证据包与记录

每次运行保存：

```text
run/
  manifest.json
  scope.md
  source/
  raw/
  parsed/
  calculation/
  comparison/
  review/
  defects/
  hashes.sha256
```

要求：

- 原始二进制可用无损hex保存但必须记录解码哈希；
- 解析结果不能覆盖原始对象；
- 字段级血缘指向字节区间或来源字段；
- 失败来源和重试保留；
- manifest不自包含哈希；
- 根哈希算法在运行前固定；
- 真实案件不得进入公开版本库。

## 15. 复核与质量监控

### 15.1 复核清单

- [ ] 网络和创世哈希正确；
- [ ] 原始对象字节与来源记录一致；
- [ ] 区块/交易ID从字节独立重算；
- [ ] CompactSize和对象边界正确；
- [ ] txid/wtxid适用性正确；
- [ ] coinbase未按普通输入处理；
- [ ] 金额均为整数satoshi；
- [ ] 手续费输入完整或明确unknown；
- [ ] 动态状态带观察时点；
- [ ] 来源冲突未被多数投票隐藏；
- [ ] 找零 聚类 CoinJoin 路径和身份未越界；
- [ ] manifest和对象哈希重新校验。

### 15.2 监控

后续如获授权，监控：

- P0解析差异；
- 不支持率和拒绝率；
- 节点同步/索引异常；
- 公共来源字段变化；
- 重组和动态状态改判；
- 工具/依赖升级；
- 人工复核改判；
- 报告更正与投诉。

## 16. 生效前门

- [ ] 项目发起人批准本方法范围和禁止项；
- [ ] M-BTC-T1与M-BTC-T2分别形成验证计划；
- [ ] Bitcoin客户端、解析工具和环境制品冻结；
- [ ] 90个候选中批准实际Bitcoin样本子集；
- [ ] GT2由第二人员复核且GT3路径建立；
- [ ] SegWit、Taproot、多交易Merkle和手续费样本完成；
- [ ] 正常 边界 负向 冲突 恶意 回归均执行；
- [ ] P0差异为零或保持阻断；
- [ ] 工具和人员单独授权；
- [ ] 模拟报告通过范围审查；
- [ ] 真实案件数据隔离和记录控制已验证；
- [ ] 质量负责人确认没有把truth_prepared写成approved。

任一项未完成，方法保持`受控草案/planned`。

## 17. 版本记录

|版本|日期|变更|状态|
|---|---|---|---|
|0.2.0|2026-07-30|将范围收窄为对象提取和UTXO确定性事实 重构字节级规则 停止门和验证矩阵|受控草案|
|3.0.0-draft|2026-07-29|历史批量生成稿包含未验证追踪推断|已被本版替代 未曾生效|
