---
document_id: REF-010
title: 验证证据与运行登记册
version: 0.1.1
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
|VAL-METHOD-T1-PROBE-001|三条主网创世区块公共端点探针|Git `61a75d1d1370fdc893839a6952cbc3e248172f41`；curl 8.21.0|2026-07-30T00:29:20+08:00|blocked|发现数据源失败和字段冲突；验证停止门可触发|不支持T1方法通过，不支持任一公共端点作为关键事实唯一来源|
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
2. 没有将原始HTTP响应保存到受控证据包；
3. 没有保存响应头、TLS证书、出口网络和端点客户端版本；
4. Bitcoin出现未关闭的交易数字段冲突；
5. Ethereum只有一个成功来源；
6. TRON只有一个来源且字段缺失原因未解释；
7. 未由第二名人员独立复验；
8. 公共端点的底层节点和相互独立性未评估；
9. 当前执行人不是经公司授权的方法执行人员。

### 5.7 后续动作

- 将Bitcoin创世区块加入冲突与回归样本；
- 在自控Bitcoin Core或保存的原始区块上重建GT2真值；
- 将BlockCypher该字段异常登记为数据源缺陷候选；
- 为Ethereum部署或取得两个不同客户端的受控端点；
- 为TRON使用java-tron自控节点和第二独立路径；
- 冻结原始响应文件、响应头、请求、时间和哈希；
- 由具名第二人员复验；
- 保持T1正式运行not_executed，直至上述前置条件满足。

## 6. 区块链方法运行入口

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

## 7. 证据位置规则

- 大体量原始区块、节点数据和日志不直接提交公共Git仓库；
- Git只保存无敏感信息的manifest、哈希、方法、结果摘要和证据位置；
- 真实案件材料不得进入本仓库；
- 外部证据库必须有访问控制、备份、审计和保存期限；
- 文件名、路径和日志不得泄露个人信息、案件秘密、私钥或令牌；
- 证据删除或迁移后保留授权、时间、范围和校验记录。

## 8. 运行前检查

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

## 9. 当前验证结论

截至2026年7月30日：

- 文档结构质量检查在提交`d0cbfe8`范围内通过；
- 已完成一个公共端点探索探针并因来源冲突、缺失和证据包不完整而阻断；
- 没有任何区块链专项方法达到V1；
- 没有任何工具版本被验证；
- 没有任何人员获得方法执行授权；
- 没有任何真实案件试点；
- 项目仍处于V0验证设计。

## 10. 版本记录

|版本|日期|变更|状态|
|---|---|---|---|
|0.1.1|2026-07-30|登记三条主网创世区块公共端点探针及阻断原因|研究底稿|
|0.1.0|2026-07-30|登记首个可复核文档质量运行，并建立区块链方法运行入口|研究底稿|
