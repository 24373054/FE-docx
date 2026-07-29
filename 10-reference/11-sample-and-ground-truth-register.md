---
document_id: REF-011
title: 首批样本与真值候选登记册
version: 0.1.0
status: 研究底稿
document_type: 参考登记
owner: 样本与真值负责人
approver: 项目发起人（未签批）
effective_date: 2026-07-30
review_cycle: 每次样本状态变化及每两周汇总
classification: 内部受控
---

# 首批样本与真值候选登记册

## 1. 文件目的

本登记册在执行正式验证之前冻结首批候选场景，防止看到工具结果后再选择有利样本。它只证明候选设计存在，不证明：

- 已取得样本对象；
- 已建立真值；
- 已执行测试；
- 90个候选具有统计代表性；
- 任一方法、工具或人员已获授权。

样本治理规则见[`样本、黄金数据与真实值管理`](../05-quality/05-sampling-ground-truth.md)，执行规则见[`首批方法验证总计划`](../08-planning/09-validation-master-plan.md)。

## 2. 登记状态

|状态|含义|
|---|---|
|candidate_design|只有场景设计，尚未选定或固定对象|
|candidate_acquired|原始对象已取得并记录哈希，真值未冻结|
|truth_prepared|真值已建立，等待独立复核|
|truth_disputed|来源或重算冲突，停止用于正式判定|
|approved_for_validation|样本、真值、许可和复核均已批准|
|retired|不再用于新运行，保留历史|

除非有具名批准证据，本表不得使用`approved_for_validation`。

## 3. 计数规则

- 本表登记的是候选验证案例，不是市场统计样本；
- 同一底层对象可用于不同错误模式，但不得在统计推断中伪装为独立观测；
- 三个网站展示同一对象不构成三个样本；
- 重试和重复响应不增加样本数量；
- 每个案例进入验证前须补全固定对象、来源、字节数、哈希、GT对象和复核人；
- `target_GT`只是目标，不表示已经达到该等级；
- 当前`BTC-T1-N-001`与`BTC-T3-C-001`复用的创世区块对象已形成原始字节GT2准备包，两个案例状态均为`truth_prepared`但未独立复核。

## 4. Bitcoin候选案例（30）

|sample_id|任务|场景族|候选场景|target_GT|P0或关键判定|当前状态|进入验证前阻断项|
|---|---|---|---|---|---|---|---|
|BTC-T1-N-001|T1|正常|固定主网创世区块对象|GT2+GT3|区块哈希 高度 版本 时间 bits nonce Merkle根 交易数|truth_prepared|GT2机器计算完成 待第二人员复核和批准|
|BTC-T1-N-002|T1|正常|早期非SegWit普通区块|GT2+GT3|头字段 交易数 原始字节|candidate_design|未选对象 未部署独立节点|
|BTC-T2-N-003|T2|正常|P2PKH多输入多输出交易|GT1+GT2|输入输出 outpoint 金额 手续费|candidate_design|未选对象 未冻结计算规则|
|BTC-T2-N-004|T2|正常|P2SH多签花费交易|GT1+GT2|脚本类型 输入输出 金额|candidate_design|未选对象 未定义脚本解释范围|
|BTC-T2-N-005|T2|正常|SegWit v0交易|GT1+GT2|txid wtxid witness 金额 手续费|candidate_design|未选对象 未冻结端序和ID规则|
|BTC-T1-B-006|T1|边界|创世区块前序哈希表示|GT2+GT4|null与全零的等价或差异|candidate_acquired|归一化规则和复核未批准|
|BTC-T2-B-007|T2|边界|coinbase输入与普通outpoint区分|GT1+GT2|coinbase标记 prevout sequence|candidate_design|未选对象 未建负向对照|
|BTC-T2-B-008|T2|边界|历史零手续费交易|GT2+GT3|输入和减输出 手续费为零|candidate_design|未选对象 未冻结金额整数规则|
|BTC-T1-B-009|T1|边界|接近批准容量上限的区块或交易|GT1+GT2|完整获取 分页 截断 资源|candidate_design|容量门和对象未批准|
|BTC-T2-B-010|T2|边界|Taproot witness v1交易|GT1+GT2|脚本类型 witness txid wtxid|candidate_design|未选对象 未批准协议范围|
|BTC-T1-X-011|T1|负向|少于32字节的交易ID|GT4|invalid_input且无外部查询|candidate_design|未固定接口编码规则|
|BTC-T1-X-012|T1|负向|包含非十六进制字符的对象ID|GT4|invalid_input|candidate_design|未固定错误分类|
|BTC-T1-X-013|T1|负向|格式正确但不存在的对象ID|GT1+GT3|not_found不等于source_unavailable|candidate_design|需在自控节点证明不存在|
|BTC-T1-X-014|T1|负向|在错误网络查询已知对象|GT1+GT3|network_mismatch或not_found|candidate_design|未部署主网与测试网隔离环境|
|BTC-T1-X-015|T1|负向|剪枝节点请求不可得历史对象|GT1+GT3|source_incomplete不等于对象不存在|candidate_design|未部署剪枝和全量对照节点|
|BTC-T3-C-001|T3|冲突|创世区块公共API交易数0与1冲突|GT2+GT3|source_conflict并停止|truth_prepared|GT2已从原始字节得到1 待第二人员和第二客户端复核|
|BTC-T3-C-002|T3|冲突|previousblockhash返回null与全零|GT2+GT4|归一化前保留原值|candidate_acquired|等价规则未批准|
|BTC-T3-C-003|T3|冲突|confirmations或depth随观察时点变化|GT2+GT3|动态字段带观察时间且不作固定真值|candidate_design|未冻结观察窗口|
|BTC-T3-C-004|T3|冲突|区块total与交易输出或手续费语义差异|GT2+GT4|字段定义和单位不混用|candidate_design|未完成供应商字段语义核验|
|BTC-T3-C-005|T3|冲突|内部字节序与显示哈希方向|GT1+GT2|转换可逆且原始字节保留|candidate_design|未建立独立解析对照|
|BTC-T1-M-001|T1|恶意|截断的原始区块字节|GT1+GT4|invalid_input且不产生部分真值|candidate_design|未生成隔离样本|
|BTC-T1-M-002|T1|恶意|非规范CompactSize编码|GT1+GT4|拒绝或按批准规则明确处理|candidate_design|未冻结客户端版本行为|
|BTC-T2-M-003|T2|恶意|离线构造重复输入交易|GT1+GT4|检测重复且不归集双倍金额|candidate_design|未生成样本和预期|
|BTC-T1-M-004|T1|恶意|离线变异Merkle根与交易不一致区块|GT1+GT2|完整性失败并停止|candidate_design|未生成原始对象和独立重算|
|BTC-T1-M-005|T1|恶意|超大脚本或资源消耗输入|GT1|达到资源门时明确blocked|candidate_design|资源上限和隔离环境未批准|
|BTC-T1-R-001|T1|回归|SegWit激活边界前后对象|GT2+GT3|解析分支和字段完整|candidate_design|未选固定高度和客户端|
|BTC-T2-R-002|T2|回归|Taproot激活边界前后交易|GT2+GT3|witness版本和脚本类型|candidate_design|未选对象和独立实现|
|BTC-T2-R-003|T2|回归|区块高度写入coinbase的历史边界|GT2+GT3|coinbase高度解析和适用时期|candidate_design|未选对象和规则版本|
|BTC-T3-R-004|T3|回归|保存响应后公共来源不可用|GT1|离线包仍可校验和复核|candidate_design|未建立完整离线恢复包|
|BTC-T3-R-005|T3|回归|创世交易数冲突缺陷关闭后重放|GT2+GT3|P0差异关闭且旧失败仍保留|candidate_design|缺陷尚未关闭|

## 5. EVM候选案例（30）

|sample_id|任务|场景族|候选场景|target_GT|P0或关键判定|当前状态|进入验证前阻断项|
|---|---|---|---|---|---|---|---|
|EVM-T1-N-001|T1|正常|固定Ethereum主网区块0|GT2+GT3|区块哈希 高度 父哈希 时间 交易数|candidate_acquired|仅一个公共RPC成功且无原始对象包|
|EVM-T2-N-002|T2|正常|legacy简单价值转移|GT1+GT2|from to value nonce gas fee status|candidate_design|未选对象 未冻结费用规则|
|EVM-T2-N-003|T2|正常|动态费用类型交易|GT1+GT2|type maxFee effectiveGasPrice 实付费|candidate_design|未选对象 未冻结字段来源|
|EVM-T2-N-004|T2|正常|合约创建交易|GT1+GT2|to为空 contractAddress status code存在性|candidate_design|未选对象 未定义执行后状态|
|EVM-T2-N-005|T2|正常|代币Transfer日志交易|GT1+GT2|合约 日志topic data index receipt状态|candidate_design|未选对象且不允许只读浏览器标签|
|EVM-T1-B-006|T1|边界|创世区块父哈希和时间为零|GT2+GT3|零值编码与显示|candidate_design|无第二客户端|
|EVM-T1-B-007|T1|边界|无交易区块|GT2+GT3|空数组不等于查询失败|candidate_design|未选固定对象|
|EVM-T2-B-008|T2|边界|零value但有calldata交易|GT1+GT2|价值转移与合约调用分离|candidate_design|未选对象和调用分类规则|
|EVM-T1-B-009|T1|边界|JSON-RPC quantity最小值0x0|GT4|0x0合法且0x00不被混同|candidate_design|官方示例和负向请求未冻结|
|EVM-T2-B-010|T2|边界|协议升级前后费用字段变化|GT2+GT3|字段存在性和不适用表达|candidate_design|升级边界和客户端版本未选|
|EVM-T1-X-011|T1|负向|长度错误的区块或交易哈希|GT4|invalid_params且无模糊修复|candidate_design|错误映射未冻结|
|EVM-T1-X-012|T1|负向|格式正确但不存在的交易哈希|GT1+GT3|not_found不等于RPC失败|candidate_design|需自控节点和冻结状态|
|EVM-T1-X-013|T1|负向|错误chain ID或网络端点|GT1+GT3|network_mismatch并停止|candidate_design|多网络隔离环境未建|
|EVM-T2-X-014|T2|负向|执行revert的合约交易|GT1+GT2|交易入块与执行失败分离|candidate_design|未生成已知revert样本|
|EVM-T1-X-015|T1|负向|pending或非最终对象被当固定证据|GT1+GT3|状态明确且不冻结为最终对象|candidate_design|最终性和确认门未批准|
|EVM-T3-C-001|T3|冲突|区块0公共RPC一成功一内部错误|GT2+GT3|source_unavailable与对象存在分离|candidate_acquired|未形成应用层证据包和第二客户端|
|EVM-T3-C-002|T3|冲突|quantity编码0x0与0x00|GT4|保留原值并按规范判定合法性|candidate_design|负向样本未执行|
|EVM-T3-C-003|T3|冲突|十六进制时间和十进制显示转换|GT1+GT2|整数无精度损失且时区不改变原值|candidate_design|转换规则未冻结|
|EVM-T3-C-004|T3|冲突|交易体与receipt字段混用|GT1+GT2|status gasUsed logs来源正确|candidate_design|对象模型和字段血缘未批准|
|EVM-T3-C-005|T3|冲突|日志顺序 transactionIndex与logIndex|GT1+GT2|稳定排序且原索引保留|candidate_design|未选多日志对象|
|EVM-T1-M-001|T1|恶意|离线构造畸形RLP对象|GT1+GT4|解析拒绝且不输出部分对象|candidate_design|样本生成和隔离未完成|
|EVM-T2-M-002|T2|恶意|事件签名相同但非目标合约的伪标签|GT1|不因topic相同推断资产或主体|candidate_design|合约白名单和反例未建立|
|EVM-T2-M-003|T2|恶意|代理合约升级造成实现变化|GT1+GT2|代理 实现 观察区块分层|candidate_design|历史状态和实现解析未冻结|
|EVM-T2-M-004|T2|恶意|内部调用不在基础交易对象中|GT1+GT3|无trace时明确不可得|candidate_design|trace来源和方法范围未批准|
|EVM-T1-M-005|T1|恶意|超大trace或日志响应触发截断|GT1|分页 资源门和incomplete明确|candidate_design|容量环境和阈值未批准|
|EVM-T1-R-001|T1|回归|区块0字段解析|GT2+GT3|创世零值和空交易稳定|candidate_design|原始对象和第二客户端缺失|
|EVM-T2-R-002|T2|回归|receipt状态字段历史边界|GT2+GT3|旧新receipt差异不误判|candidate_design|边界对象和规则未冻结|
|EVM-T2-R-003|T2|回归|基础费用字段引入边界|GT2+GT3|字段缺失与零值分离|candidate_design|边界对象未选|
|EVM-T3-R-004|T3|回归|执行层与共识层对象边界|GT2+GT3|数据来源和最终性声明准确|candidate_design|双层客户端环境未建|
|EVM-T3-R-005|T3|回归|后续批准协议升级的前后对象|GT2+GT3|变更字段和旧样本均可重放|candidate_design|具体升级和版本待阶段门批准|

## 6. TRON候选案例（30）

|sample_id|任务|场景族|候选场景|target_GT|P0或关键判定|当前状态|进入验证前阻断项|
|---|---|---|---|---|---|---|---|
|TRON-T1-N-001|T1|正常|固定TRON主网区块0|GT2+GT3|blockID header 交易数 父哈希|candidate_acquired|仅TronGrid来源且字段缺失原因未解释|
|TRON-T2-N-002|T2|正常|原生TRX转账|GT1+GT2|owner to amount txID result|candidate_design|未选对象和java-tron真值|
|TRON-T2-N-003|T2|正常|TRC20 Transfer日志|GT1+GT2|contract topics data index receipt|candidate_design|未选对象且标签不可作真值|
|TRON-T2-N-004|T2|正常|TriggerSmartContract交易|GT1+GT2|交易体 参数 receipt result 能量|candidate_design|未选对象和执行状态规则|
|TRON-T2-N-005|T2|正常|账户创建相关交易|GT1+GT2|账户状态与交易结果观察时点|candidate_design|未选对象和状态快照|
|TRON-T1-B-006|T1|边界|创世header缺少常规number或timestamp显示|GT2+GT3|缺失 零值和接口省略分离|candidate_acquired|无自控节点和原始protobuf|
|TRON-T1-B-007|T1|边界|单区块含多个交易对象|GT2+GT3|交易数 顺序 txID完整|candidate_design|未选固定区块|
|TRON-T2-B-008|T2|边界|零或最小允许金额参数|GT1+GT4|合法性与执行失败分离|candidate_design|需隔离网络生成|
|TRON-T2-B-009|T2|边界|带宽与能量资源边界|GT1+GT2|资源消耗 fee和receipt字段|candidate_design|费用与资源规则未冻结|
|TRON-T2-B-010|T2|边界|交易体与TransactionInfo分离|GT1+GT4|入块事实不等于执行成功|candidate_design|对象映射样本未选|
|TRON-T1-X-011|T1|负向|长度或字符错误的txID|GT4|invalid_input|candidate_design|错误分类未冻结|
|TRON-T1-X-012|T1|负向|格式正确但不存在的txID|GT1+GT3|not_found不等于source_failure|candidate_design|需自控节点证明查询条件|
|TRON-T1-X-013|T1|负向|错误网络或地址前缀|GT1+GT3|network_or_address_mismatch|candidate_design|网络隔离环境未建|
|TRON-T2-X-014|T2|负向|过期或时间窗口无效交易|GT1|失败原因和未入块状态明确|candidate_design|需隔离网络生成|
|TRON-T2-X-015|T2|负向|合约执行失败交易|GT1+GT2|入块 结果 receipt错误分层|candidate_design|未选已知失败对象|
|TRON-T3-C-001|T3|冲突|创世区块只有单一公共来源|GT2+GT3|冗余不足时blocked|candidate_acquired|无第二java-tron路径|
|TRON-T3-C-002|T3|冲突|blockID与header字段计算关系|GT2+GT3|对象ID可独立重算|candidate_design|原始protobuf和规则未冻结|
|TRON-T3-C-003|T3|冲突|visible参数下Base58与十六进制地址|GT1+GT4|转换可逆且网络前缀保留|candidate_design|官方编码样本未冻结|
|TRON-T3-C-004|T3|冲突|交易体返回存在但TransactionInfo缺失|GT1+GT3|未确认 不存在 来源失败分离|candidate_design|观察窗口和节点类型未批准|
|TRON-T3-C-005|T3|冲突|FullNode与SolidityNode确认视图差异|GT2+GT3|节点角色和观察时点明确|candidate_design|双节点环境未建|
|TRON-T2-M-001|T2|恶意|非目标合约伪造相同Transfer事件|GT1|不因事件签名推断代币真实性|candidate_design|隔离合约与反例未生成|
|TRON-T2-M-002|T2|恶意|代理或可升级合约实现变化|GT1+GT2|代理 实现 区块高度分层|candidate_design|历史实现规则未定义|
|TRON-T1-M-003|T1|恶意|高资源消耗合约响应|GT1|资源门 超时和incomplete明确|candidate_design|隔离环境和容量门未建|
|TRON-T2-M-004|T2|恶意|重复或异常日志顺序|GT1|原索引保留且不重复归集|candidate_design|变异样本未生成|
|TRON-T1-M-005|T1|恶意|畸形或截断protobuf对象|GT1+GT4|解析拒绝且不产生部分事实|candidate_design|官方模式版本和样本未冻结|
|TRON-T1-R-001|T1|回归|创世区块字段解析|GT2+GT3|blockID 父哈希和交易数稳定|candidate_design|原始protobuf和第二实现缺失|
|TRON-T2-R-002|T2|回归|TVM规则升级前后对象|GT2+GT3|执行字段和费用规则按时期适用|candidate_design|具体升级边界未选|
|TRON-T3-R-003|T3|回归|地址前缀与显示格式转换|GT1+GT4|Base58 十六进制和网络前缀稳定|candidate_design|官方样本和负向集未建|
|TRON-T2-R-004|T2|回归|资源费用字段规则变化前后|GT2+GT3|原始整数 单位和时期保留|candidate_design|边界对象和规则未冻结|
|TRON-T3-R-005|T3|回归|公共来源不可用后的离线复核|GT1|保存包可恢复且来源失败不改历史事实|candidate_design|完整离线证据包未建|

## 7. 数量与成熟度汇总

### 7.1 候选数量

|链|正常|边界|负向|冲突|恶意|回归|合计|
|---|---:|---:|---:|---:|---:|---:|---:|
|Bitcoin|5|5|5|5|5|5|30|
|EVM|5|5|5|5|5|5|30|
|TRON|5|5|5|5|5|5|30|
|总计|15|15|15|15|15|15|90|

### 7.2 当前状态

|状态|数量|说明|
|---|---:|---|
|candidate_design|81|只有场景设计|
|candidate_acquired|7|已有探针观察但证据或真值不足|
|truth_disputed|0|当前无；后续复核发现差异时恢复该状态|
|truth_prepared|2|复用Bitcoin创世对象的正常与冲突案例已形成候选GT2|
|approved_for_validation|0|无|

`candidate_acquired`包括Bitcoin前序哈希表示、Ethereum区块0、TRON区块0及两项相应冲突/缺失观察；它们可能复用同一底层对象，不能在统计分析中视为独立样本。

## 8. 样本进入验证的字段门

每个案例从`candidate_design`前进时补全：

|字段|要求|
|---|---|
|base_object_id|固定区块 交易 文件或生成对象|
|chain_network|链 网络 chain ID或创世哈希|
|source_record|来源主体 端点/文件 许可 时间|
|raw_object|路径 字节数 SHA-256|
|ground_truth_id|GT对象唯一ID和版本|
|target_GT_actual|实际达到的GT1至GT4或GT5辅助|
|expected_fields|值 类型 单位 允许差异和unknown|
|builder_reviewer|不同人员及其重算证据|
|method_tool_env|批准的方法 工具 环境版本|
|blind_access|输入包和答案库权限|
|acceptance|P0门 失败和停止条件|
|evidence_location|manifest 根哈希和保存位置|

缺失任一P0必需字段，验证运行只能`blocked`或`not_executed`。

## 9. 与现有证据的映射

|证据ID|关联案例|结论|
|---|---|---|
|VAL-METHOD-T1-PROBE-001|BTC-T1-N-001 BTC-T1-B-006 BTC-T3-C-001 BTC-T3-C-002|公开端点字段冲突和表示差异；运行blocked|
|GT-BTC-GENESIS-001-V1|BTC-T1-N-001 BTC-T1-B-006 BTC-T3-C-001 BTC-T3-C-002|两个来源原始字节一致；独立计算得到交易数1；truth_prepared|
|VAL-METHOD-T1-PROBE-001摘要中的Ethereum观察|EVM-T1-N-001 EVM-T3-C-001|一个端点成功 一个内部错误；未成独立包|
|VAL-METHOD-T1-PROBE-001摘要中的TRON观察|TRON-T1-N-001 TRON-T1-B-006 TRON-T3-C-001|单一来源且字段缺失；未成独立包|

公开Bitcoin探针包见[`VAL-METHOD-T1-PROBE-001`](../validation-evidence/public/VAL-METHOD-T1-PROBE-001/)，原始字节GT2准备包见[`GT-BTC-GENESIS-001-V1`](../validation-evidence/public/GT-BTC-GENESIS-001-V1/)。

## 10. 近期动作

1. 指定第二人员从冻结原始字节独立复核Bitcoin GT2；
2. 部署或取得第二个实质独立的Bitcoin客户端路径以准备GT3；
3. 固定EVM两个不同客户端的区块0响应和原始对象；
4. 固定java-tron自控节点与第二路径的创世对象；
5. 从每条链先选择一个正常、一个负向、一个冲突案例完成真值演练；
6. 指定样本建立人、真值复核人和质量负责人；
7. 其余84个设计案例在G1范围冻结后才投入获取成本。

## 11. 禁止表述

- “已经有90个黄金样本”；
- “三链验证集已完成”；
- “公共链公开所以无需数据合规”；
- “两个工具一致即可视为真值”；
- “没有查询结果就是负样本”；
- “样本通过代表方法在所有对象上正确”。

## 12. 版本记录

|版本|日期|变更|状态|
|---|---|---|---|
|0.1.0|2026-07-30|建立三链 六场景族共90个候选案例和状态门|研究底稿|
