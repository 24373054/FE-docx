# FRM-006 第一次演练记录

## 1. 假设身份

|字段|填写值|
|---|---|
|记录编号|FRM-006-RH-2026-001|
|案件或项目编号|PUBLIC-RND-SIM-BTC-CONFLICT-001|
|记录状态|待复核|
|创建人|Codex workspace research session|
|创建时间|2026-07-30T02:50:00+08:00|
|假设ID|HYP-BTC-BLOCKCYPHER-NTX-001|
|问题表述|BlockCypher对Bitcoin创世区块返回`n_tx=0`是否可作为“该区块无交易”的可验证技术事实|

## 2. 证据与预测

|字段|填写值|
|---|---|
|初始依据|OBJ-T1P1-CAPTURE-001中BlockCypher响应`n_tx=0`、`txids=[]`|
|待验证预测|若假设成立，则冻结原始区块交易计数应为0，其他独立来源不应解析出创世交易|
|支持证据|只有BlockCypher单一GT5响应|
|反向证据|Blockstream返回1；Blockchain.com返回1及一笔交易；Bitcoin Core固定源码构造`vtx=1`；冻结原始字节CompactSize为1|
|替代解释|公共API索引策略、服务缺陷、创世交易特殊处理或字段映射错误|
|使用规则/模型|无统计或聚类模型；使用P0字段冲突停止规则|
|验证步骤|核对父包比较表；从GT2冻结原始字节读取交易计数；比较Bitcoin Core固定常量；保留服务差异|
|结果|不支持|
|置信与限制|足以否定“`n_tx=0`可直接作为该区块无交易事实”；不足以确定BlockCypher内部原因或推广到其他区块|
|复核意见|未由不同自然人复核|

## 3. 状态演进

|时间|状态|理由|
|---|---|---|
|父包初始探针|无法判断/blocked|当时无GT1至GT4冻结真值|
|GT2准备后|不支持|原始字节和固定实现均显示1笔交易|
|当前|保持不支持|不得回写父包历史状态；结论只适用于该字段和该样本|

第一次演练发现假设需要追加式状态历史、证据形成时间和“后续证据不得覆盖历史运行”的规则。模板需增加`status_history`、`evidence_cutoff`、`falsification_condition`和`scope_of_refutation`。
