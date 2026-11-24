#!/usr/bin/env python3
"""Apply the approved civil-pleading layout to confirmed text."""

from __future__ import annotations

import argparse
from io import BytesIO
import json
from pathlib import Path

from docx import Document
from docx.enum.style import WD_STYLE_TYPE
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor


MODES = {
    "second-defense": "二审答辩状",
    "retrial-defense": "再审答辩状",
    "retrial-application": "再审申请书",
}
ALIGNMENTS = {
    "left": WD_ALIGN_PARAGRAPH.LEFT,
    "center": WD_ALIGN_PARAGRAPH.CENTER,
    "right": WD_ALIGN_PARAGRAPH.RIGHT,
    "justify": WD_ALIGN_PARAGRAPH.JUSTIFY,
}
BODY_FONT = "宋体"
# font, bold, before/after in hundredths of a line, indent in hundredths of a character, alignment
FORMATS = {
    "title": ("黑体", True, 100, 0, "center"),
    "case-number": (BODY_FONT, False, 0, 0, "right"),
    "party": (BODY_FONT, False, 0, 200, "justify"),
    "heading-1": ("黑体", True, 50, 200, "justify"),
    "heading-2": ("楷体", True, 50, 200, "justify"),
    "heading-3": (BODY_FONT, True, 0, 200, "justify"),
    "heading-4": (BODY_FONT, False, 0, 200, "justify"),
    "body": (BODY_FONT, False, 0, 200, "justify"),
    "court-address": (BODY_FONT, False, 0, 0, "left"),
    "signature": (BODY_FONT, False, 0, 0, "right"),
    "date": (BODY_FONT, False, 0, 0, "right"),
    "pagination": (BODY_FONT, False, 0, 0, "center"),
}
METADATA_ALIGNABLE = {"case-number", "party", "court-address", "signature", "date"}


def make_styles(document, preview_font: str | None) -> None:
    for kind, (chinese_font, bold, lines, indent, align) in FORMATS.items():
        style = document.styles.add_style(f"Litigation {kind}", WD_STYLE_TYPE.PARAGRAPH)
        style.font.name = "Times New Roman"
        style.font.size = Pt(22 if kind == "title" else 10.5 if kind == "pagination" else 14)
        style.font.bold = bold
        style.font.color.rgb = RGBColor(0, 0, 0)
        fonts = style.element.get_or_add_rPr().rFonts
        fonts.set(qn("w:eastAsia"), preview_font or chinese_font)
        fonts.set(qn("w:cs"), "Times New Roman")
        paragraph = style.paragraph_format
        paragraph.alignment = ALIGNMENTS[align]
        paragraph.line_spacing = Pt(26)
        paragraph.line_spacing_rule = WD_LINE_SPACING.EXACTLY
        paragraph.space_before = Pt(26 * lines / 100)
        paragraph.space_after = Pt(26 * lines / 100)
        paragraph.first_line_indent = Pt(14 * indent / 100)
        paragraph.widow_control = True
        style.element.pPr.spacing.set(qn("w:beforeLines"), str(lines))
        style.element.pPr.spacing.set(qn("w:afterLines"), str(lines))
        style.element.pPr.ind.set(qn("w:firstLineChars"), str(indent))
        if kind == "title" or kind.startswith("heading-"):
            paragraph.keep_with_next = True
            paragraph.keep_together = True
        if kind.startswith("heading-"):
            outline = OxmlElement("w:outlineLvl")
            outline.set(qn("w:val"), str(int(kind[-1]) - 1))
            style.element.pPr.append(outline)


def append_field(paragraph, code: str) -> None:
    field = OxmlElement("w:fldSimple")
    field.set(qn("w:instr"), code)
    cached_run = OxmlElement("w:r")
    value = OxmlElement("w:t")
    value.text = "1"
    cached_run.append(value)
    field.append(cached_run)
    paragraph._p.append(field)


def build(spec: dict, preview_font: str | None = None):
    mode = spec.get("mode") if isinstance(spec, dict) else None
    if not isinstance(mode, str) or mode not in MODES:
        raise ValueError("Use mode second-defense, retrial-defense, or retrial-application")
    title = spec.get("title", MODES[mode])
    if not isinstance(title, str) or not title.strip() or "\n" in title or "\r" in title:
        raise ValueError("title must be one non-empty line")
    blocks = spec.get("blocks")
    if not isinstance(blocks, list) or not blocks:
        raise ValueError("blocks must contain the confirmed paragraphs")

    document = Document()
    document.core_properties.title = title
    document.core_properties.author = ""
    document.core_properties.last_modified_by = ""
    document.core_properties.comments = ""
    section = document.sections[0]
    section.page_width, section.page_height = Cm(21), Cm(29.7)
    section.top_margin = section.bottom_margin = Cm(2.6)
    section.left_margin = section.right_margin = Cm(2.8)
    section.header_distance, section.footer_distance = Cm(1.5), Cm(1.75)
    make_styles(document, preview_font)
    document.add_paragraph(title, style="Litigation title")
    previous_kind = ""
    previous_paragraph = None
    closing_kinds = {"court-address", "signature", "date"}
    for number, block in enumerate(blocks, start=1):
        if not isinstance(block, dict):
            raise ValueError(f"Block {number} must be an object")
        kind, value, align = block.get("kind"), block.get("text"), block.get("align")
        if not isinstance(kind, str) or kind not in FORMATS or kind in {"title", "pagination"}:
            raise ValueError(f"Block {number} has an unsupported kind")
        if not isinstance(value, str) or not value.strip() or "\n" in value or "\r" in value:
            raise ValueError(f"Block {number} must contain one non-empty paragraph")
        paragraph = document.add_paragraph(value, style=f"Litigation {kind}")
        if previous_kind in closing_kinds and kind in closing_kinds:
            previous_paragraph.paragraph_format.keep_with_next = True
        if align is not None:
            if kind not in METADATA_ALIGNABLE or not isinstance(align, str) or align not in ALIGNMENTS:
                raise ValueError(f"Block {number} has an unsupported alignment override")
            paragraph.alignment = ALIGNMENTS[align]
        previous_kind, previous_paragraph = kind, paragraph

    footer = section.footer.paragraphs[0]
    footer.style = "Litigation pagination"
    append_field(footer, "PAGE")
    footer.add_run(" / ")
    append_field(footer, "NUMPAGES")
    return document


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("spec", type=Path, help="JSON with mode, optional title, and blocks")
    parser.add_argument("output", type=Path, help="new DOCX output path")
    parser.add_argument("--confirmed-text", action="store_true", help="confirm the input text is approved for formatting")
    parser.add_argument("--preview-cjk-font", help="substitute fonts for a preview-*.docx copy")
    args = parser.parse_args()
    if not args.confirmed_text:
        parser.error("Use --confirmed-text after the text has been confirmed")
    if args.output.suffix.lower() != ".docx":
        parser.error("Output must use the .docx extension")
    if args.preview_cjk_font and "preview" not in args.output.stem.lower():
        parser.error("Font substitution requires preview in the output file name")
    try:
        spec = json.loads(args.spec.read_text(encoding="utf-8-sig"))
        document = build(spec, args.preview_cjk_font)
        data = BytesIO()
        document.save(data)
        with args.output.open("xb") as handle:
            handle.write(data.getbuffer())
    except (OSError, ValueError) as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()
