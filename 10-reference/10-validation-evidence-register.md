---
document_id: REF-010
title: 验证证据与运行登记册
version: 0.1.5
status: 研究底稿
document_type: 参考登记
owner: 质量负责人
approver: 项目发起人（未签批）
effective_date: 2026-07-30
review_cycle: 每次验证运行及每两周汇总
classification: 内部受控
---

# 验证证据与运行登记册

## 1. 文件目的

本登记册记录实际执行过的验证运行、适用范围、输入版本、结果和证据限制。

关键规则：

- “计划”不登记为运行；
- “测试标题存在”不登记为执行；
- “命令退出码为0”只支持该命令定义的检查；
- 文档质量检查不能证明区块链方法、工具、人员或生产能力；
- 失败、阻断和不适用与通过记录同等保留；
- 每个通过状态必须指向可复核输入、步骤、实际结果和执行环境。

## 2. 状态

|状态|含义|
|---|---|
|not_executed|已有计划但没有实际运行|
|running|已经开始且结果尚未冻结|
|passed|定义范围内达到预先判定|
|failed|运行完成但没有达到预先判定|
|blocked|因前置条件、环境、数据、权限或未解释差异无法判定|
|withdrawn|原结果因缺陷、版本变化或证据问题被撤回|

## 3. 运行总表

|运行ID|对象|版本/提交|执行时间|结果|直接支持|明确不支持|
|---|---|---|---|---|---|---|
|VAL-DOC-20260730-001|文档结构、目录生命周期和内部链接|Git `d0cbfe88fb4689549fbc10d081ccde40f40cffd4`|2026-07-30T00:16:48+08:00|passed|索引一致、元数据与状态规则、追踪ID闭合、内部相对链接存在|法律正确、外部链接现行、方法有效、工具正确、人员胜任、生产就绪|
|VAL-METHOD-T1-PROBE-001|三条主网创世区块公共端点探针；Bitcoin证据固化复跑|初始Git `61a75d1d1370fdc893839a6952cbc3e248172f41`；固化基线`2d3f9bb8525a9b7e4c33607b8b7ea8967185aac6`|2026-07-30T00:29:20+08:00；00:32:53至00:33:38复跑|blocked|发现数据源失败和字段冲突；形成首个可校验公开证据包|不支持T1方法通过，不支持任一公共端点作为关键事实唯一来源|
|VAL-GT-BTC-20260730-001|Bitcoin创世区块原始字节GT2准备|Git `69f530b68ae3273d52be1749f2d416b03d01272f`|2026-07-30T00:58:28+08:00至01:00:20+08:00|passed|两个来源字节一致；独立重算区块哈希 交易数 交易ID和Merkle根；支持truth_prepared|不支持真值批准 T1方法通过 工具验证或生产使用|
|SIM-FORM-BTC-CONFLICT-001-V1|六份模板第二次冲突场景演练|Git `055429f34f961c533c2c179e55a72f26be5ccbc6`|2026-07-30T02:15:00+08:00至02:20:00+08:00|expected_conflict_detected_governance_blocked|父包再摄取、P0冲突停止、11对象完整性和第二场景填写|不支持独立复核、跨包Schema闭合、模板批准或方法/工具批准|
|VAL-METHOD-T1-001|公开链对象提取与固定正式运行|未冻结|未执行|not_executed|无|无方法通过结论|
|VAL-METHOD-T2-001|确定性交易事实重建|未冻结|未执行|not_executed|无|无方法通过结论|
|VAL-METHOD-T3-001|多源一致性与离线验证包|未冻结|未执行|not_executed|无|无方法通过结论|

## 4. VAL-DOC-20260730-001

### 4.1 范围

- 受控文档索引与当前文件内容一致；
- 文档元数据、ID、最低结构、状态生命周期和禁止表述检查；
- requirements、controls、tests和traceability中的ID引用闭合；
- Markdown内部相对链接目标存在；
- 工作树在运行开始时无未提交变更。

### 4.2 输入

|输入|SHA-256|
|---|---|
|`scripts/build_document_index.py`|`8a1f811b4f03ce2c9d00fa07b3156a2af414c89bdf8c129f6bae33247b679017`|
|`scripts/repo_quality_check.py`|`21567b4e2bdcdbb87ced9b02531027281e3fef910d140975f405f4e799cd6e1c`|
|`scripts/validate_traceability.py`|`2470b37c6e097c635ba6ad0955cb4e8dd48afc7ebcca148cdfbb2ed1d15b0490`|
|`scripts/validate_internal_links.py`|`c883f14692091aa13187e8183b8986109cd3eeadbd1164c27056ce5451e077cd`|
|`catalogs/requirements.csv`|`3b716b8996fe6a4493f596c41586ccfaa54674ce10560e05b1afbf5f7784a5d9`|
|`catalogs/controls.csv`|`bd9a1aee4b3683eea7f68d3ad06068fed5caa880ec7f38836f45f65068f3b1ac`|
|`catalogs/tests.csv`|`0dac8f146776bb86063bc3e182a0d3b10a4235514975bec3adef175125f08d91`|
|`catalogs/traceability.csv`|`6ee05925faa4c1e1dbfafbf02f672f1cb11482ecf05b48e316057f4dfc2990db`|

### 4.3 执行命令与实际结果

|顺序|命令|实际结果|
|---:|---|---|
|1|`python scripts/build_document_index.py --check`|`DOCUMENT INDEX PASSED`|
|2|`python scripts/repo_quality_check.py`|`QUALITY GATE PASSED`；113份受控文档、113个文档ID|
|3|`python scripts/validate_traceability.py`|`TRACEABILITY PASSED`；requirements=1639、controls=1639、tests=1639、links=1639|
|4|`python scripts/validate_internal_links.py`|`INTERNAL LINKS PASSED: 449`|
|5|`git status --porcelain`|无输出，工作树干净|

### 4.4 状态分布

|状态|数量|
|---|---:|
|历史生成稿（待重构）|88|
|模板草案（待实测）|16|
|研究底稿|6|
|待签批治理提案|1|
|受控草案|1|
|自动生成索引|1|
|合计|113|

该分布是提交`d0cbfe8`运行时快照，后续提交会变化。

### 4.5 目录状态

|目录|数量|生命周期状态|
|---|---:|---|
|requirements|1639|原1631项为generated_unreviewed；GOV-008新增8项为reviewed|
|controls|1639|全部not_implemented|
|tests|1639|全部not_executed|
|traceability|1639|ID映射闭合，不含执行通过含义|

### 4.6 判定

结果为passed，限于4.1定义的结构检查。

这个结果不能升级：

- 原历史生成稿的成熟度；
- GOV-008的签批状态；
- 任何测试目录项的not_executed状态；
- 任何方法、工具或人员状态；
- REF-005生产、试点或申报就绪门。

### 4.7 已知限制

- 内部链接检查只验证路径存在，不验证锚点、语义或外部URL；
- 最低行数不能证明内容质量；
- 追踪检查只验证ID引用，不验证控制实施和证据存在；
- JSON检查只验证可解析，不等于Schema设计适用；
- 状态规则依赖文件元数据，尚未接入具名电子批准；
- Git提交证明内容版本，不证明公司批准；
- 本轮没有第二名人员独立重复执行。

## 5. VAL-METHOD-T1-PROBE-001

### 5.1 目的

在正式样本、真值和证据包冻结前，对Bitcoin、Ethereum和TRON主网创世区块进行只读公共端点探针，验证：

- 公共端点是否可用；
- 稳定对象的核心标识是否一致；
- 是否会出现字段语义或内容冲突；
- 现有环境是否足以直接进入T1正式验证。

本运行在执行前被定义为probe，不是方法确认。

### 5.2 环境

|字段|值|
|---|---|
|Git提交|`61a75d1d1370fdc893839a6952cbc3e248172f41`|
|执行时间|2026-07-30T00:29:20+08:00|
|时区|Asia/Shanghai，UTC+08:00|
|操作系统|Windows工作区环境|
|PowerShell|7.6.4|
|HTTP客户端|curl 8.21.0，Schannel|
|网络|当前项目工作站外网；未记录出口IP和代理|
|执行人|项目接管代理；尚无公司人员授权|
|独立复核|未执行|

### 5.3 Bitcoin观察

查询对象：Bitcoin mainnet block height 0。

|来源|端点|结果|
|---|---|---|
|Blockstream公共API|`https://blockstream.info/api/block-height/0`|返回哈希`000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f`|
|mempool.space公共API|`https://mempool.space/api/block-height/0`|TLS/传输失败，未获得可用响应|
|BlockCypher公共API|`https://api.blockcypher.com/v1/btc/main/blocks/0`|哈希、高度、时间、nonce、merkle root等与其他来源一致；返回`n_tx: 0`和空`txids`|
|Blockchain.com公共API|`https://blockchain.info/block-height/0?format=json`|同一哈希；返回`n_tx: 1`并包含创世交易|
|Bitcoin Core源代码|[bitcoin/bitcoin `src/kernel/chainparams.cpp`](https://github.com/bitcoin/bitcoin/blob/master/src/kernel/chainparams.cpp)|注释与构造显示创世区块`vtx=1`，交易哈希为merkle root|

一致字段：

- block hash；
- height 0；
- previous block全零；
- merkle root `4a5e1e4baab89f3a32518a88c31bc87f618f76673e2cc77ab2127b7afdeda33b`；
- timestamp `1231006505`；
- bits `486604799`/`1d00ffff`；
- nonce `2083236893`；
- size `285`。

冲突字段：

- BlockCypher返回交易数0；
- Blockchain.com和Bitcoin Core源代码表明创世区块有1笔交易。

探针结论：

- 区块哈希具有多源一致信号；
- 公共API即使返回HTTP成功，也可能在字段或索引语义上产生错误；
- BlockCypher的交易数量和交易清单在该样本上不能作为真值；
- 正式运行必须保存原始响应、响应头、检索时间和端点身份，并按协议/节点建立独立真值。

### 5.3.1 Bitcoin证据固化复跑

在初始探针发现差异后，以Git `2d3f9bb8525a9b7e4c33607b8b7ea8967185aac6`为执行基线进行了只读复跑，证据位置为[`validation-evidence/public/VAL-METHOD-T1-PROBE-001`](../validation-evidence/public/VAL-METHOD-T1-PROBE-001/)。

已冻结：

- 五个公开HTTP请求的请求URL、起止时间、响应状态、响应头和正文；
- 每个响应正文的UTF-8字节数和SHA-256；
- Bitcoin Core固定提交`7e5952b0aa04429c88d8ad990f35862421c4fa9d`、远程源码正文哈希和相关行；
- 执行环境、字段级比较、停止结论和未执行的独立复核状态；
- 六个证据对象的manifest、对象哈希、字节数和根哈希。

完整性校验结果：

|项目|结果|
|---|---|
|evidence-manifest Schema|passed|
|manifest对象数|6|
|HTTP正文数|5|
|正文哈希与字节数|5/5一致|
|对象哈希与字节数|6/6一致|
|root_hash|`8dc903d11c4206bc682caf6bba0dcfa9313f609df1699e1dae22e19882a7d35c`|

该复跑提高了“本次看到了什么”的可复核性，但没有改变`blocked`状态。HTTP正文由应用层客户端读取后保存，未保存传输层原始报文和TLS会话；完整远程Bitcoin Core源码也只保存其固定URL、正文哈希、字节数和摘录。

### 5.4 Ethereum观察

查询对象：Ethereum mainnet block parameter `0x0`，方法`eth_getBlockByNumber`，`full transaction objects=false`。

|来源|结果|
|---|---|
|Cloudflare Ethereum Gateway|返回JSON-RPC错误`code=-32603, message=Internal error`|
|PublicNode Ethereum RPC|返回block 0对象|

PublicNode选定字段：

|字段|值|
|---|---|
|hash|`0xd4e56740f876aef8c010b86a40d5f56745a118d0906a34e69aec8c0db1cb8fa3`|
|number|`0x0`|
|parentHash|64个十六进制零|
|timestamp|`0x0`|
|transactions|空数组|
|gasUsed|`0x0`|
|gasLimit|`0x1388`|

探针结论：

- 同一标准JSON-RPC方法在公共端点间存在可用性差异；
- 只有一个成功来源，不能达到多源一致性判定；
- Cloudflare错误不能解释为“区块不存在”；
- 正式运行必须加入客户端身份、chain ID、原始响应、重试政策和第二实现。

Ethereum官方JSON-RPC说明quantity和data编码不同，并要求查询状态时明确block parameter；本探针遵守`0x0`固定参数，没有使用动态`latest`。

### 5.5 TRON观察

查询对象：TRON mainnet `wallet/getblockbynum`，请求`{"num":0}`。

TronGrid返回：

|字段|值|
|---|---|
|blockID|`00000000000000001ebf88508a03865c71d452e25f4d51194196a1d22b6653dc`|
|transactions|3个交易对象|
|header raw_data|包含txTrieRoot、parentHash和witness_address|
|number/timestamp|响应中的创世raw_data未显式返回这两个字段|

探针结论：

- 单一TronGrid响应可用于发现对象结构；
- 本轮没有第二个独立TRON节点或实现，不能形成一致性结论；
- 字段缺失可能来自创世对象编码、接口映射或节点实现，尚未解释；
- 正式运行需要java-tron自控节点、配置/网络标识和独立解析。

TRON官方接口文档提醒交易体和执行回执属于不同对象；本探针只查询区块，不能推导交易执行状态。

### 5.6 阻断原因

本运行状态为blocked，原因：

1. 运行前没有冻结正式sample_id和GT等级；
2. 初始三链运行没有将HTTP响应保存到证据包；后续只对Bitcoin进行了应用层证据固化复跑；
3. Bitcoin复跑保存了响应头和正文，但没有保存TLS证书、TLS会话、出口网络或服务端节点/客户端版本；
4. Bitcoin出现未关闭的交易数字段冲突；
5. Ethereum只有一个成功来源；
6. TRON只有一个来源且字段缺失原因未解释；
7. 未由第二名人员独立复验；
8. 公共端点的底层节点和相互独立性未评估；
9. 当前执行人不是经公司授权的方法执行人员。

### 5.7 后续动作

- 将Bitcoin创世区块加入冲突与回归样本；
- 已从保存的原始区块字节建立候选GT2；下一步由具名第二人员独立重算和批准；
- 将BlockCypher该字段异常登记为数据源缺陷候选；
- 为Ethereum部署或取得两个不同客户端的受控端点；
- 为TRON使用java-tron自控节点和第二独立路径；
- 冻结原始响应文件、响应头、请求、时间和哈希；
- 由具名第二人员复验；
- 保持T1正式运行not_executed，直至上述前置条件满足。

## 6. VAL-GT-BTC-20260730-001

### 6.1 范围

本运行只从冻结的Bitcoin主网创世区块序列化字节建立候选GT2，不执行T1方法确认。

证据包：[`GT-BTC-GENESIS-001-V1`](../validation-evidence/public/GT-BTC-GENESIS-001-V1/)。

预先判定：

- 两条来源路径解码后的原始字节完全一致；
- 原始区块为285字节；
- 80字节头双SHA-256反转显示后等于官方固定区块哈希；
- 字节80的CompactSize交易数为1；
- 单笔交易解析恰好消耗剩余204字节；
- 交易ID等于头内Merkle根；
- 任一不满足则状态不通过并将真值标为`truth_disputed`。

### 6.2 输入与来源

|输入|观察|
|---|---|
|Blockstream Esplora raw|返回`application/octet-stream` 285字节|
|Blockchain.com rawblock hex|返回570个十六进制字符 解码为285字节|
|两个解码对象SHA-256|`5299fac924b5a2fc19a88876a0042c19ac4d11fe69c3f66e47516e26185f9e99`|
|Bitcoin Core固定提交|`7e5952b0aa04429c88d8ad990f35862421c4fa9d`|
|备用mempool.space路径|TLS意外EOF 未取得正文 不参与真值|

来源失败被保留为负面记录，未解释为对象不存在。

### 6.3 独立计算

计算不调用Bitcoin Core或区块浏览器字段解析，只使用：

- 原始字节切片；
- little-endian整数转换；
- CompactSize规则；
- 两次SHA-256；
- 显示哈希字节反转；
- 单交易Merkle根规则。

|字段|计算结果|
|---|---|
|version|1|
|previous block|64个十六进制零|
|timestamp|1231006505|
|bits|486604799 / `1d00ffff`|
|nonce|2083236893|
|block hash|`000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f`|
|transaction count|1|
|transaction size|204字节|
|value|5000000000 satoshi|
|transaction ID|`4a5e1e4baab89f3a32518a88c31bc87f618f76673e2cc77ab2127b7afdeda33b`|
|Merkle root|与transaction ID一致|
|parse end|偏移285 无尾随字节|

计算结果与Bitcoin Core固定提交中的区块哈希、Merkle根、构造参数和`vtx=1`一致。

### 6.4 证据完整性

|项目|结果|
|---|---|
|evidence-manifest Schema|passed|
|manifest对象数|10|
|对象哈希与字节数|10/10一致|
|原始区块解码|285字节|
|root_hash|`fd1911a139f4876ed6c170fdbd500d0a7f80ba9951adc4dd2fa849f37b2620c3`|

### 6.5 判定与限制

运行在“原始字节一致与独立计算”范围内为`passed`，真值状态为`truth_prepared`。

未执行：

- 具名第二人员独立重算；
- 不同客户端或独立环境GT3复验；
- 公司批准；
- 正式方法、工具或人员验证。

因此`VAL-METHOD-T1-001`仍为`not_executed`。本运行也不批准Blockstream或Blockchain.com作为关键事实的唯一来源。

## 7. 端到端记录链与模板第一次演练

### 7.1 运行标识

|字段|值|
|---|---|
|运行ID|SIM-E2E-BTC-GENESIS-001-V1|
|输入包|GT-BTC-GENESIS-001-V1|
|执行实现|PowerShell 7.6.4 / .NET SHA256|
|对象数|13|
|根哈希算法|`sha256-sorted-path-lines-v1`|
|root_hash|`f89512f8be22191f1b92fad07598f1630a5c69bb225254773ee8d476d18277bd`|
|状态|`technical_reproduction_passed_governance_blocked`|
|证据位置|[`SIM-E2E-BTC-GENESIS-001-V1`](../validation-evidence/public/SIM-E2E-BTC-GENESIS-001-V1/)|

### 7.2 实际执行

- 以既有公开真值准备包的原始hex为输入；
- 使用PowerShell/.NET而非原Python实现；
- 重算285字节、1笔交易、区块哈希、交易ID和单交易Merkle一致性；
- 实际填写FRM-002、FRM-003、FRM-004、FRM-008、FRM-009和FRM-010；
- 从新建空目录恢复整包；
- 对manifest Schema、13个对象的路径/字节数/SHA-256、哈希清单和包根哈希做全量校验；
- 清理前核对恢复目录位于工作区`tmp/`；环境策略拒绝自动递归删除后，改为按已核验固定路径逐文件清理，恢复副本未进入版本控制或证据包。

### 7.3 结果

|检查|结果|
|---|---|
|manifest Schema|passed|
|对象存在、字节数和SHA-256|13/13 passed|
|hashes.sha256与manifest|passed|
|包根哈希|passed|
|P0跨实现复算|passed|
|离线恢复|passed|
|独立自然人复核|blocked|
|方法确认|not_validated|
|工具验证|not_validated|
|模板升级|blocked；仅第一次演练|

演练中首次人工复制hex出现字节差异，SHA-256和字节数在manifest生成前将其拦截；错误及修复过程保留在采集记录。该事件支持完整性控制必要性，但不计作正式负向测试，因为错误对象未作为冻结测试输入进入manifest。

### 7.4 模板发现

|模板|发现|
|---|---|
|FRM-002|需增加授权类型、证据位置/哈希和独立授权状态|
|FRM-003|需结构化关联错误对象、发现控制、修复对象和影响|
|FRM-004|需增加包ID、根哈希算法、值状态和自引用规则|
|FRM-008|技术运行结果与方法确认结论必须分层|
|FRM-009|制品哈希失败原因、覆盖缺口和整体批准必须分层|
|FRM-010|独立性和P0差异应是阻断门|

六份模板已形成0.2.0候选修订，但仍保持`模板草案（待实测）`，等待第二次不同场景和不同自然人角色的演练。

## 8. 六份模板第二次冲突场景演练

### 8.1 运行标识

|字段|值|
|---|---|
|运行ID|SIM-FORM-BTC-CONFLICT-001-V1|
|父包|VAL-METHOD-T1-PROBE-001|
|父包manifest SHA-256|`3e5b21df87d192489e8f7bf469fdc5c16b3f2cedbde413e0da374b013197e106`|
|父包root_hash|`8dc903d11c4206bc682caf6bba0dcfa9313f609df1699e1dae22e19882a7d35c`|
|本包对象数|11|
|本包root_hash|`da6acdc3ebe0a9a6bda6d5619ddd5ef27901f12d4985904d36baff18001ee13a`|
|状态|`expected_conflict_detected_governance_blocked`|
|证据位置|[`SIM-FORM-BTC-CONFLICT-001-V1`](../validation-evidence/public/SIM-FORM-BTC-CONFLICT-001-V1/)|

### 8.2 实际执行

- 未重新访问公共端点，只读再摄取已冻结父包；
- 复核父包manifest SHA-256、6个对象和父包根哈希；
- 摘录`transaction_count`、`transaction_ids`和`previous_block`差异；
- 保持P0冲突为open，并验证停止门按预先规则触发；
- 用0.2.0候选再次填写FRM-002、003、004、008、009、010；
- 生成11对象manifest和哈希清单并完成全量校验；
- 将六份模板修订为0.3.0候选，但未升级生命周期状态。

### 8.3 结果与新缺口

|项目|结果|
|---|---|
|manifest Schema|passed|
|对象存在、字节数和SHA-256|11/11 passed|
|包内父对象引用|passed|
|hashes.sha256与root_hash|passed|
|P0冲突发现和停止控制|passed|
|源方法运行|blocked；符合预期|
|跨包父对象机器表达|failed；Schema 3.0.0缺字段|
|独立自然人复核|not_executed|
|模板升级|blocked|

新发现：

- 再摄取需要父包ID、父包manifest哈希、父包根哈希和新数据产生标志；
- Schema需要跨包父对象、依赖模式和恢复要求；
- 方法记录需要分开“源运行阻断”“停止控制通过”和“方法未确认”；
- 工具记录需要分开客户端、运行时、数据源和服务后端；
- 复核记录需要分开预期阻断与复核失败。

两次演练均由同一研究会话编制和自检。因为没有公司具名人员完成角色分离演练，六份模板继续保持`模板草案（待实测）`。

## 9. 区块链方法运行入口

未来每次方法运行新增：

|字段|要求|
|---|---|
|运行ID|全局唯一，不复用|
|方法|ID、版本、范围和状态|
|样本|sample_id、类型、链、网络和真值等级|
|工具|名称、版本、制品哈希和环境|
|数据源|节点、客户端、网络、同步和观察时点|
|输入|对象ID和文件哈希|
|步骤|实际执行步骤和偏离|
|预期|运行前冻结的字段与判定|
|实际|机器可读输出和人读摘要|
|差异|字段级差异、分类和缺陷ID|
|复核|独立复核范围、人员、时间和结果|
|状态|passed/failed/blocked/withdrawn|
|限制|不得推导的结论|

运行使用的候选案例、目标GT和真值状态必须先在[`首批样本与真值候选登记册`](./11-sample-and-ground-truth-register.md)登记；案例处于`candidate_design`或`truth_disputed`时不得形成通过结论。

## 10. 证据位置规则

- 大体量原始区块、节点数据和日志不直接提交公共Git仓库；
- Git只保存无敏感信息的manifest、哈希、方法、结果摘要和证据位置；
- 真实案件材料不得进入本仓库；
- 外部证据库必须有访问控制、备份、审计和保存期限；
- 文件名、路径和日志不得泄露个人信息、案件秘密、私钥或令牌；
- 证据删除或迁移后保留授权、时间、范围和校验记录。

## 11. 运行前检查

- [ ] 方法和版本已经冻结；
- [ ] 样本真值在运行前冻结；
- [ ] 数据来源和使用授权明确；
- [ ] 环境、工具和依赖记录完整；
- [ ] 执行人与复核人职责分离；
- [ ] 预期、通过门和停止条件预先登记；
- [ ] 证据存储位置和访问权限已验证；
- [ ] 失败结果不会被自动覆盖；
- [ ] 不涉及未经批准的真实案件或资产控制；
- [ ] 运行结束后更新本登记册。

## 12. 当前验证结论

截至2026年7月30日：

- 文档结构质量检查在提交`d0cbfe8`范围内通过；
- 已完成一个公共端点探索探针并因来源冲突、缺失和证据包不完整而阻断；
- 已完成一个Bitcoin原始字节GT2准备运行；机器计算通过但未独立复核批准；
- 已完成一次13对象端到端记录链和模板第一次演练；跨实现与恢复通过但组织独立性阻断；
- 已完成一次11对象冲突场景和六份模板第二次演练；停止门通过但跨包Schema和组织独立性阻断；
- 没有任何区块链专项方法达到V1；
- 没有任何工具版本被验证；
- 没有任何人员获得方法执行授权；
- 没有任何真实案件试点；
- 项目仍处于V0验证设计。

## 13. 版本记录

|版本|日期|变更|状态|
|---|---|---|---|
|0.1.5|2026-07-30|登记六份模板第二次冲突场景演练、11对象依赖包及跨包Schema缺口|研究底稿|
|0.1.4|2026-07-30|登记端到端记录链、六份模板第一次实测、跨实现复算和恢复结果|研究底稿|
|0.1.3|2026-07-30|登记Bitcoin创世区块原始字节GT2准备运行及truth_prepared限制|研究底稿|
|0.1.2|2026-07-30|固化Bitcoin探针公开证据包，登记manifest、对象哈希和根哈希校验结果|研究底稿|
|0.1.1|2026-07-30|登记三条主网创世区块公共端点探针及阻断原因|研究底稿|
|0.1.0|2026-07-30|登记首个可复核文档质量运行，并建立区块链方法运行入口|研究底稿|
