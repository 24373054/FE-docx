# FRM-004 第二次演练记录

## 1. 记录身份

|字段|填写值|
|---|---|
|记录编号|FRM-004-RH-2026-002|
|案件或项目编号|PUBLIC-RND-SIM-BTC-CONFLICT-001|
|记录状态|待复核|
|创建人|Codex workspace research session|
|创建时间|2026-07-30T02:18:00+08:00|
|包ID与Schema版本|SIM-FORM-BTC-CONFLICT-001-V1；3.0.0|
|根哈希算法|`sha256-sorted-path-lines-v1`|
|保密级别|公开|
|存储等级|Git受控；不是WORM|
|访问角色|项目研究人员；对外使用仍需批准|
|留存期限|按项目记录控制决定；当前不得销毁|

## 2. 逻辑对象登记

|证据对象ID|对象类型|文件名或对象键|来源类型|来源记录ID|父对象|值状态|格式/MIME|完整性|
|---|---|---|---|---|---|---|---|---|
|OBJ-CONFLICT-SOURCE-001|记录|source/source-package-reference.json|既有冻结包|VAL-METHOD-T1-PROBE-001|外部父包root_hash|known|application/json|见本包manifest|
|OBJ-CONFLICT-CMP-001|派生|comparison/conflict-selection.csv|字段摘录|OBJ-T1P1-COMPARISON-001|OBJ-CONFLICT-SOURCE-001|conflicted|text/csv|见本包manifest|
|OBJ-CONFLICT-ACQ-001|记录|records/acquisition.md|模板演练|FRM-003-RH-2026-002|OBJ-CONFLICT-SOURCE-001|known|text/markdown|见本包manifest|
|OBJ-CONFLICT-MVAL-001|记录|records/method-validation.md|模板演练|FRM-008-RH-2026-002|OBJ-CONFLICT-CMP-001|known|text/markdown|见本包manifest|
|OBJ-CONFLICT-REV-001|记录|records/review.md|模板演练|FRM-010-RH-2026-002|OBJ-CONFLICT-MVAL-001|known|text/markdown|见本包manifest|

其余对象见本包manifest；manifest和`hashes.sha256`不进入对象清单，以避免自哈希循环。

## 3. 跨包血缘限制

现有Schema只允许`parent_ids`字符串，但没有定义跨包命名、父包root hash、依赖是否随包交付或依赖可用性。因此：

- 本包manifest不把父包对象ID直接写入`parent_ids`，避免将外部引用误判为包内可解析父节点；
- 通过`OBJ-CONFLICT-SOURCE-001`建立包内代理对象；
- 代理对象记录父包ID、manifest SHA-256、root hash和选定对象；
- 离线完整复核必须同时取得父包，本包单独恢复只能证明表单记录自身完整性。

## 4. 完整性与审批

|项目|状态|
|---|---|
|逻辑对象与文件对象映射|passed|
|值状态`conflicted`表达|passed|
|包内父对象闭合|passed|
|跨包依赖可机器强制|failed；Schema缺少正式字段|
|独立复核|not_executed|
|批准|blocked|

模板结果为`partial_pass`。第二次演练发现新的跨包血缘缺口，必须增加`parent_package_id`、`parent_root_hash`、`external_parent_object_id`和`dependency_mode`。
