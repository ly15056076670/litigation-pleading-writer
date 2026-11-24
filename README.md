# 律稿续写

律稿续写是面向中国民事诉讼的 Agent Skill。从现有案卷和律师已明确的策略起草二审答辩状、再审答辩状和再审申请书，贯通材料对应、提纲确认、纯文本及 Word 排版。

## 它解决什么问题

| 文书 | 起草时重点对应 |
| --- | --- |
| 二审答辩状 | 当前上诉理由、一审裁判及我方历审观点，说明相关判项为何应当维持 |
| 再审答辩状 | 对方提出的再审事由、生效裁判和案卷页码，区分事实争执与启动再审条件 |
| 再审申请书 | 压缩交代历审案情、争点和处理结果，从生效裁判中定位所选错误并解释对判项的影响 |

同一套案卷按拟制时点开放。起草二审答辩时，后来形成的二审判决从本轮排除。分析先将争点全部对齐，随后由律师在提纲中决定写入、合并和保留哪些争点。引文区分原件印刷页、PDF 物理页和证据册页码。Word 使用确认的正文及指定模板，也支持单独查看审阅稿版式。

## 安装

将本仓库下载或克隆到本地。使用 Codex 时，在仓库上一级目录执行下列命令，将整个 Skill 放入用户目录。

```bash
mkdir -p "$HOME/.agents/skills"
cp -R litigation-pleading-writer "$HOME/.agents/skills/"
```

也可直接在仓库目录打开 Codex，在任务中指定读取 [SKILL.md](SKILL.md) 及其链接的参考文件。其他支持 Agent Skills 的环境可按该环境的安装约定放置整个目录。首次打开时可用 `$litigation-pleading-writer` 显式调用。

## 首次使用

1. 提供本轮要写的文书类型、我方当事人及可用案卷。答辩稿的本阶段案号、受文法院以实际信息为准。
2. 先看材料及争点分析。明确哪些争点写、合并、暂留或删除，并确认各项请求的范围。
3. 确认纯文本后安排 Word 排版。也可以直接指定明确范围并批准下一步，或仅看当前稿的排版。

> 用 $litigation-pleading-writer 为我方写民事二审答辩状。先按拟制时点整理材料，逐项对应上诉理由、一审裁判与我方一审观点。单列对方的新说法、庭审承认及可核的页码。给我分析后等我确认。

[完整合成试用](examples/retrial-application.md)含案卷、对话顺序、关键检查项和可生成 Word 的示例。需要使用自己的团队风格时，在对话中指定已生成的团队 Skill 或通用风格文档。有关读入范围和修订回流，见[风格衔接](references/style-handoff.md)。

## 可选命令行工具

核心 Skill 由 Markdown 指令和参考文档组成。随附的本地脚本需要 Python 3.10 或更高版本。Word 生成用 `python-docx`，精确引文筛查用 `pypdf`。

```bash
python3 -m venv .venv
. .venv/bin/activate
python3 -m pip install python-docx pypdf
python3 scripts/build_word.py examples/retrial-application.json retrial-preview.docx --confirmed-text
```

使用 Word 或 WPS 预览生成文稿。可选渲染脚本接受已有的兼容 `render_docx.py`，按[排版与复核](references/word-format.md)配置。对有文字层的 PDF，可按[材料接收](references/material-intake.md)准备包含物理页的引用清单，再运行 `python3 scripts/check_quote_pages.py quotes.json`。以原页和所在语境为最终核对依据。

## 许可

[MIT](LICENSE)。示例案卷和文稿均为合成材料。
