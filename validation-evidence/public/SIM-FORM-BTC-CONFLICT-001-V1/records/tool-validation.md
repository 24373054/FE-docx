# FRM-009 第二次演练记录

## 1. 记录身份

|字段|填写值|
|---|---|
|记录编号|FRM-009-RH-2026-002|
|案件或项目编号|PUBLIC-RND-SIM-BTC-CONFLICT-001|
|记录状态|待复核|
|工具对象|父包采集客户端与三个第三方公共数据源；本次只读文件复核工具|
|测试人员|当前研究会话|
|独立复核人|未指定|
|批准范围|无|

## 2. 对象分层

|对象类别|对象|版本/身份可冻结性|制品哈希状态|技术结果|整体状态|
|---|---|---|---|---|---|
|采集客户端|System.Net.Http.HttpClient|父包仅记录名称，组件制品未冻结|not_available|历史响应已保存|blocked_not_validated|
|数据源|Blockstream公共API|后端节点/版本未知|not_applicable|部分字段与其他来源一致|blocked_not_validated|
|数据源|BlockCypher公共API|后端节点/版本未知|not_applicable|P0交易数量与清单冲突|failed_for_selected_fields|
|数据源|Blockchain.com公共API|后端节点/版本未知|not_applicable|与两条来源部分一致|blocked_not_validated|
|本次复核工具|PowerShell 7.6.4/.NET SHA256|运行时版本已记录，完整供应链未冻结|not_available|父包哈希复核通过|blocked_not_validated|

## 3. 覆盖缺口

|覆盖类型|状态|说明|
|---|---|---|
|正常|limited|仅创世区块|
|边界|limited|创世对象是特殊边界，但无系统边界集|
|冲突|passed_for_detection|交易数量/交易ID冲突被发现|
|恶意|not_executed|未构造篡改、注入或欺骗输入|
|性能|not_executed|无负载或容量数据|
|安全|not_executed|无供应链、权限或网络安全验证|
|回归|not_executed|无冻结版本和回归集|

## 4. 判定

- 技术测试：冲突检测控制在本样本上`passed`；
- BlockCypher选定字段：`failed_for_selected_fields`；
- 公共服务不是可执行制品，不能用空的“制品哈希”假装已固定版本；
- 采集客户端、数据源和复核工具必须分开批准；
- 工具整体状态：`blocked_not_validated`；
- 不得用于真实案件、生产或对外结论。

第二次演练发现模板还需强制区分`client_tool`、`runtime`、`data_source`和`service_backend`，并为在线服务记录运营方、端点、观察时点、后端身份可知性和依赖状态。
