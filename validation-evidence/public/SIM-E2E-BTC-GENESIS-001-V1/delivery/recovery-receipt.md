# 本地离线恢复与接收回执

回执ID：`RCPT-SIM-BTC-GENESIS-001`

包ID：`SIM-E2E-BTC-GENESIS-001-V1`

执行时间：2026-07-30T02:05:00+08:00

发送位置：工作区`validation-evidence/public/SIM-E2E-BTC-GENESIS-001-V1`

接收位置：操作系统临时目录中的新建空目录

接收主体：同一Codex研究会话（不满足独立人员要求）

## 执行步骤

1. 将完整包复制到新建空目录；
2. 解析`manifest.json`；
3. 检查Schema；
4. 对manifest中的全部对象检查包内相对路径；
5. 逐项比较文件存在性、字节数和SHA-256；
6. 按`sha256-sorted-path-lines-v1`从对象清单重建规范行；
7. 计算根哈希并与manifest比较；
8. 从恢复目录中的`raw/block.hex`重新解码和计算P0字段；
9. 比较区块哈希、交易数、交易ID和Merkle根。

## 结果

|检查|结果|
|---|---|
|对象存在性|passed|
|对象字节数|passed|
|对象SHA-256|passed|
|包根哈希|passed|
|原始hex解码|285字节|
|交易数|1|
|区块哈希|与接受准则一致|
|交易ID|与接受准则一致|
|Merkle一致性|passed|
|独立自然人|failed/not_available|

最终对象数和包根哈希以同目录`manifest.json`为唯一记录，避免回执自引用。

## 接收决定

`accepted_for_public_research_record_only`

本回执不批准方法、工具、模板、人员或生产存储。因为发送人与接收/复核主体是同一研究会话，组织独立性门保持`blocked`。
