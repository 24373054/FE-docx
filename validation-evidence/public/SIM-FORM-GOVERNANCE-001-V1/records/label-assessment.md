# FRM-007 第一次演练记录

## 1. 候选标签

|字段|填写值|
|---|---|
|记录编号|FRM-007-RH-2026-001|
|案件或项目编号|PUBLIC-RND-BTC-GENESIS-001|
|记录状态|待复核|
|创建人|Codex workspace research session|
|创建时间|2026-07-30T02:52:00+08:00|
|标签记录ID|LABEL-CAND-BTC-1A1Z-001|
|链与地址|Bitcoin mainnet；`1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa`|
|标签内容|候选描述：“创世交易输出的常见浏览器显示地址”|
|来源类型|第三方公共区块浏览器响应|
|原始来源URL/文件|VAL-METHOD-T1-PROBE-001/capture/public-endpoint-captures.json|
|来源获取时间|父包2026-07-30T00:32:53+08:00至00:33:38+08:00|
|合法性依据|公开来源研究；未取得主体授权或法定调取|
|证据等级|未批准；按当前事实最多为GT5/L0候选|
|独立核验|原始脚本为P2PK输出，浏览器的地址展示不等于链上脚本直接声明实体身份|
|冲突标签|无其他实体标签被采纳；“Satoshi Nakamoto控制”未被验证|
|实体范围|仅描述浏览器如何显示创世交易输出；不归属自然人、机构或现时控制方|
|有效期/复核日|仅适用于冻结父包；任何对外引用前重新复核|
|允许用途|数据源显示行为和标签风险演示|
|禁止用途|不得证明Satoshi Nakamoto身份、私钥控制、资产权属、可支配性、违法性或自然人归属|

## 2. 结论

|判定|结果|
|---|---|
|地址字符串存在于冻结公共响应|known|
|它是原始输出脚本中的直接地址字段|not_supported|
|它与“创世交易输出”存在浏览器展示关联|limited_candidate|
|它证明某自然人或实体控制|rejected|
|可进入对外主体归属意见|blocked|

第一次演练暴露两类混淆：地址/脚本表示与实体标签不同，历史控制与当前控制不同。模板需增加`assertion_type`、`subject_level`、`derivation_method`、`control_time`和`disposition`，并允许“拒绝标签但保留来源观察”。
