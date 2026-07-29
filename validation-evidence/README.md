# 公开验证证据区

本目录只保存可以进入版本库的公开、无敏感信息验证记录，用于证明“实际做过什么、看到了什么、为什么通过或停止”。它不保存真实案件材料、个人信息、私钥、令牌、受限节点凭据或大体量链数据。

## 边界

- `public/`：公开网络、公开规范和公开实现形成的研究或验证记录；
- 每个运行目录必须包含范围、环境、来源、捕获、比较、复核、`manifest.json`和`hashes.sha256`；
- `manifest.json`不自包含哈希，避免循环依赖；
- `hashes.sha256`和`root_hash`覆盖manifest中列出的证据对象，不覆盖manifest自身；
- 未具备GT1至GT4真值、独立复核和批准证据时，不得把公开端点比较写成方法通过；
- 大体量原始数据、真实案件证据和受限数据继续由`.gitignore`中的`evidence/`、`case-data/`或外部受控证据库承载。

## 根哈希算法

当前算法标识：`sha256-sorted-path-lines-v1`。

1. 对manifest中每个对象的精确UTF-8文件字节计算SHA-256和字节数；
2. 按POSIX相对路径升序排列；
3. 每行写为`<sha256>  <size_bytes>  <path>\n`；
4. 对全部行拼接后的UTF-8字节计算SHA-256，得到`root_hash`。

该算法只验证版本库内对象的一致性，不替代数字签名、可信时间戳、访问审计或司法保管链。

## 当前公开包

|包|性质|状态|明确不代表|
|---|---|---|---|
|[`VAL-METHOD-T1-PROBE-001`](./public/VAL-METHOD-T1-PROBE-001/)|公共端点探索与冲突记录|blocked|方法通过或数据源批准|
|[`GT-BTC-GENESIS-001-V1`](./public/GT-BTC-GENESIS-001-V1/)|Bitcoin创世区块原始字节独立计算|truth_prepared|已批准真值或T1方法通过|
