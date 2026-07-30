# GT-BTC-GENESIS-001-V1 独立计算规则

## 1. 输入

- 读取`raw/block.hex`；
- 只允许小写十六进制字符和文件末尾换行；
- 去除末尾换行后进行十六进制解码；
- 预期得到285字节；
- 对解码字节计算SHA-256并与两个来源记录比较。

## 2. 区块头

取字节区间`[0,80)`：

|字段|区间|解码|
|---|---|---|
|version|0..4|4字节little-endian有符号整数|
|previous block|4..36|32字节；显示时反转|
|merkle root|36..68|32字节；显示时反转|
|timestamp|68..72|4字节little-endian无符号整数|
|bits|72..76|4字节little-endian无符号整数|
|nonce|76..80|4字节little-endian无符号整数|

区块哈希计算：

1. `h1 = SHA256(header_bytes)`；
2. `h2 = SHA256(h1)`；
3. 内部字节为`h2`；
4. 常用显示区块哈希为`reverse(h2)`的十六进制。

不得对显示字符串本身计算哈希。

## 3. CompactSize

从字节80读取交易数量：

- 首字节小于`0xfd`时该字节就是数值；
- `0xfd`后读取2字节little-endian；
- `0xfe`后读取4字节little-endian；
- `0xff`后读取8字节little-endian。

本对象字节80为`0x01`，因此交易数为1，交易从偏移81开始。

## 4. 交易解析

按非SegWit序列化顺序：

1. version：4字节little-endian；
2. vin count：CompactSize；
3. 每个输入：previous txid 32字节、vout 4字节、script length、script、sequence 4字节；
4. vout count：CompactSize；
5. 每个输出：value 8字节little-endian、script length、script；
6. locktime：4字节little-endian。

交易ID：

1. 对偏移`[81,285)`的204字节交易计算两次SHA-256；
2. 常用显示交易ID为第二次摘要反转后的十六进制。

解析必须在偏移285结束且无尾随字节。

## 5. Merkle检查

本区块只有一笔交易，因此Merkle树只有一个叶子，Merkle根的显示值必须等于该交易ID。该规则只用于单交易区块；不得推广为多交易Merkle计算规则。

## 6. 官方常量比较

将计算结果与Bitcoin Core固定提交`7e5952b0aa04429c88d8ad990f35862421c4fa9d`中：

- 创世区块哈希断言；
- Merkle根断言；
- 时间、nonce、bits、version和50 COIN构造参数；
- `vtx=1`注释；

逐项比较。官方源记录复用前一包中哈希为`675bec03106240b50ea6c844b44a8b949983d7f6aa68bcb54a42a511018191b9`的对象。

## 7. 独立性限制

计算只使用通用SHA-256、字节切片和整数端序规则，不调用Bitcoin Core、区块浏览器解析结果或链分析工具。

但本次计算仍由同一研究会话执行，尚未由不同人员、不同实现或不同环境复验；因此结果只到`truth_prepared`。
