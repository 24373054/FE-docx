# 贡献与变更规则

## 分支和PR

- 从 `main` 创建短期分支，命名为 `docs/`、`method/`、`quality/` 或 `fix/` 加简要主题。
- 每个PR只解决一个可审查主题；不得同时夹带无关格式化或批量重写。
- PR正文说明变更原因、影响文件、验证结果、历史案件影响和回退方案。
- 涉及监管、方法、工具、结论措辞、Schema或模板的变更必须由质量负责人审查。
- 不允许直接向 `main` 推送未经审查的生产内容。

## 编写要求

1. 使用UTF-8和中文主文；专业名词首次出现给出英文或协议原名。
2. 每份受控Markdown保留YAML元数据，并使用唯一 `document_id`。
3. 不使用 `TODO`、`TBD`、`待补充`、`占位`、`以后完善` 等未完成文本。
4. 不复制大段通用边界充当正文；文件内容必须针对本主题提供操作、证据、异常和验收细节。
5. 外部规则引用优先使用官方来源，记录发布日期、访问日期和适用范围。
6. 任何推断写明前提、反例、误差、限制和拒绝条件。
7. 表单必须能够实际填写，并提供字段属性、说明、附件、复核和示例。
8. 删除文件前确认是否有内部链接、追踪项、模板、培训或历史案件依赖。

## 本地验证

```bash
python scripts/build_document_index.py
python scripts/build_document_index.py --check
python scripts/repo_quality_check.py
python scripts/validate_traceability.py
python scripts/validate_internal_links.py
```

所有检查通过后再提交PR。由自动化生成的提交还应由仓库所有者或获授权维护者追加一次可审查提交，以确保永久质量工作流在受信任主体上下文中完成最终验证。
