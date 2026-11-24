# Word 排版与复核

用户明确要求看格式时可排当前稿供审阅。正式拟提交的文件以经确认的正文、基本信息及适用的法院或团队格式为准。用户提供指定模板时优先依该模板，并检查原模板可能含有的案号、人员信息、批注及页眉。

## 通用可编辑样式

[Word 排版脚本](../scripts/build_word.py)使用 Python 及 python-docx。它以 A4、白底、黑字、首行两个汉字、固定26磅行距和动态页码排版。正文默认宋体14磅，标题黑体22磅，一级标题黑体14磅，二级标题楷体14磅。西文字体为 Times New Roman。这套格式供查看及编辑，具体提交样式以实际要求为准。字体由打开文档或渲染文档的环境提供。工具可以选用预览字体，不随项目分发字库。

```bash
python3 scripts/build_word.py examples/retrial-application.json retrial-preview.docx --confirmed-text
```

上例的输入已标明为合成排版示例。实际案件只有确认可以排版的文本才使用该确认参数。脚本接收 UTF-8 JSON，其输入包含 `mode`、可选 `title` 和按确认顺序列出的 `blocks`。三种 `mode` 为 `second-defense`、`retrial-defense` 和 `retrial-application`。每段用 `kind` 和 `text` 表达。每个 `text` 对应一个段落，法院落款的两行可分成两个段落。对案号、当事人、受文机关、签署和日期段，可用 `align` 覆盖默认对齐。适用文体和角色写法见[合成输入](../examples/retrial-application.json)。编号、日期、案号和引注直接用输入中的文本。需要处理内嵌表格、图片或真实脚注时，用文档编辑工具在确认稿上排版。

## 复核

通过 Word 或 WPS 导出 PDF 查看每页。若环境已有兼容的 `render_docx.py`，可选用 [render_word.py](../scripts/render_word.py) 调用。macOS 的渲染器如遗漏本机指定字体，该工具可临时补充字体目录。样式、字体、换页位置、标题是否与正文分离、页码、签名及盖章位置逐页查。

```bash
python3 scripts/render_word.py retrial-preview.docx visual-check --renderer /path/to/render_docx.py
```

文件文字复核独立于渲染。对照确认稿逐段检查当事人、角色、时期、金额、引文、申请请求及落款。PDF 原件短引可用 [check_quote_pages.py](../scripts/check_quote_pages.py) 核指定物理页，已匹配的文字仍应对照原页和上下文。缺号、缺页、字体缺失或证据尚未核实时标注状态再交用户处理。
