# FRM-014 第一次演练记录

## 1. 候选身份

|字段|填写值|
|---|---|
|记录编号|FRM-014-RH-2026-001|
|案件或项目编号|FE-DOCX-RND-2026-001|
|记录状态|待复核|
|记录用途|岗位授权缺口计划，不是已完成人员培训记录|
|人员编号|PERSON-PENDING-001；公司尚未指定自然人|
|目标岗位/角色|Bitcoin公开对象采集与确定性事实复算执行人|
|能力差距|公司身份/劳动关系、电子数据取证能力、Bitcoin协议、证据保全、质量体系、隐私与合规、独立性声明均未建立|

## 2. 培训与考核状态

|字段|填写值|
|---|---|
|培训课程|待设计：监管边界、采集SOP、BTC方法、证据包、异常/CAPA、报告边界|
|讲师、日期和材料版本|未指定/未执行|
|监督实践|可使用SIM-E2E-BTC-GENESIS-001-V1和SIM-FORM-BTC-CONFLICT-001-V1；导师未指定|
|书面考核|not_executed|
|实操考核|not_executed|
|盲样结果|not_executed|
|口头答辩|not_executed|
|授权范围|none|
|授权有效期|不适用：未授权|
|监督要求|首次所有活动必须由合格导师监督；当前无导师|
|暂停/撤销条件|不适用：尚未授权；若未来授权，方法/工具变更、差错、离岗或利益冲突触发暂停|
|批准人|待公司任命质量负责人或授权委员会|

## 3. 判定

|能力门|状态|
|---|---|
|具名自然人|blocked|
|培训完成|not_executed|
|考核通过|not_executed|
|独立性声明|not_executed|
|方法/工具范围冻结|blocked|
|人员授权|not_authorized|

第一次演练证明“培训计划”“考核记录”和“授权决定”不应挤在同一状态字段。模板需增加`record_purpose`、`candidate_status`、`prerequisite_gate`、`authorization_state`和`authorization_evidence_id`；人员未指定时只能建立岗位缺口计划，不能生成空壳授权。
