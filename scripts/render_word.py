#!/usr/bin/env python3
"""Render a DOCX with the existing documents renderer and macOS fonts."""

from __future__ import annotations

import argparse
import os
from pathlib import Path
import subprocess
import sys
from tempfile import TemporaryDirectory
from xml.etree.ElementTree import Element, ElementTree, SubElement


def mac_font_config(directory: Path, additional: list[Path]) -> Path:
    config = Element("fontconfig")
    system_fonts = Path("/System/Library/Fonts")
    for fonts in (system_fonts, Path("/Library/Fonts"), Path.home() / "Library/Fonts", *additional):
        if fonts.is_dir():
            SubElement(config, "dir").text = str(fonts.resolve())
    SubElement(config, "cachedir").text = str(directory / "font-cache")
    path = directory / "fonts.conf"
    ElementTree(config).write(path, encoding="utf-8", xml_declaration=True)
    return path


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("docx", type=Path)
    parser.add_argument("output_dir", type=Path)
    parser.add_argument("--renderer", type=Path, required=True, help="path to documents skill's render_docx.py")
    parser.add_argument("--font-dir", action="append", type=Path, default=[], help="additional macOS font directory")
    parser.add_argument("--dpi", type=int, default=130)
    args = parser.parse_args()
    if not args.docx.is_file() or not args.renderer.is_file():
        parser.error("Provide existing DOCX and renderer files")
    if args.output_dir.exists():
        parser.error("Use a fresh output directory to avoid mixing preview versions")
    if args.dpi <= 0 or any(not directory.is_dir() for directory in args.font_dir):
        parser.error("Use a positive DPI and existing font directories")

    command = [
        sys.executable,
        str(args.renderer.resolve()),
        str(args.docx.resolve()),
        "--output_dir",
        str(args.output_dir.resolve()),
        "--dpi",
        str(args.dpi),
        "--emit_pdf",
    ]
    with TemporaryDirectory(prefix="litigation-fonts-") as scratch:
        environment = os.environ.copy()
        if sys.platform == "darwin":
            environment["FONTCONFIG_FILE"] = str(mac_font_config(Path(scratch), args.font_dir))
        elif args.font_dir:
            parser.error("--font-dir is supported on macOS")
        result = subprocess.run(command, env=environment, check=False)
    raise SystemExit(result.returncode)


if __name__ == "__main__":
    main()
