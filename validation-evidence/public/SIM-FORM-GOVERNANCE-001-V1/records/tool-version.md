# FRM-005 第一次演练记录

## 1. 工具登记

|字段|填写值|
|---|---|
|记录编号|FRM-005-RH-2026-001|
|案件或项目编号|FE-DOCX-RND-2026-001|
|记录状态|待复核|
|创建人|Codex workspace research session|
|创建时间|2026-07-30T02:48:00+08:00|
|工具ID|TOOL-RND-POWERSHELL-DOTNET-001|
|工具名称|PowerShell/.NET Bitcoin创世对象复算路径|
|版本|PowerShell 7.6.4；.NET运行时版本未单独冻结|
|制品SHA-256|`not_available`；系统安装组件未形成受控制品快照|
|来源|当前Windows工作区预装运行环境|
|预期用途|只用于公开Bitcoin创世对象的字节解码、双SHA-256和一致性复算；不得用于真实案件或主体归属|
|运行环境|Windows；PowerShell 7.6.4；环境详情见父包environment.json|
|依赖锁定文件|不存在|
|验证报告ID|SIM-E2E-BTC-GENESIS-001-V1；仅单样本技术复算，不是工具验证报告|
|已知限制|无制品哈希、SBOM、签名、构建来源、边界/恶意/性能/回归覆盖和独立人员复核|
|批准范围|无|
|批准日期|不适用：未批准|
|停用条件|任何结果差异、运行时更新、供应链异常或超出公开研发范围即停止|
|替代工具|Python历史实现和未来受控Bitcoin Core/独立解析器；均未批准|

## 2. 状态

|层级|结果|
|---|---|
|版本可识别|partial|
|单样本技术结果|passed|
|制品与供应链冻结|failed|
|工具验证|not_validated|
|生产批准|blocked|

第一次演练发现“版本”和“制品”必须支持组件级清单；一个逻辑工具可能由Shell、运行时、库和操作系统组成。模板还需增加`component_inventory`、`hash_status`、`validation_evidence_level`和`approval_state`，不能用一个验证报告ID替代证据范围。
