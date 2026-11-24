#!/usr/bin/env python3
"""Screen exact quotations on explicitly selected pages of local PDFs."""

from __future__ import annotations

import argparse
from collections import Counter
from functools import lru_cache
import json
import logging
from pathlib import Path
import re

from pypdf import PdfReader


ID_PATTERN = re.compile(r"[A-Za-z0-9][A-Za-z0-9_.:-]{0,63}")


def without_whitespace(text: str) -> str:
    return "".join(character for character in text if not character.isspace())


@lru_cache(maxsize=32)
def selected_page_text(path: Path, physical_page: int) -> tuple[str | None, str]:
    try:
        with path.open("rb") as source:
            reader = PdfReader(source)
            if reader.is_encrypted and not reader.decrypt(""):
                return None, "encrypted-pdf"
            if physical_page > len(reader.pages):
                return None, "page-out-of-range"
            try:
                extracted = reader.pages[physical_page - 1].extract_text()
            except Exception:
                return None, "page-extraction-failed"
    except FileNotFoundError:
        return None, "source-missing"
    except OSError:
        return None, "source-unreadable"
    except Exception:
        return None, "invalid-or-unreadable-pdf"

    text = without_whitespace(extracted or "")
    if not text:
        return None, "no-readable-text-layer"
    if "\ufffd" in text or "\x00" in text or not any(character.isalnum() for character in text):
        return None, "unreadable-text-layer"
    return text, ""


def check_entry(entry: dict, base: Path) -> dict:
    physical_page = entry.get("physical_page")
    valid_page = type(physical_page) is int and physical_page >= 1
    result = {
        "id": entry["id"],
        "physical_page": physical_page if valid_page else None,
        "status": "unverifiable",
    }

    path_value = entry.get("path")
    label = entry.get("citation_label")
    quote = entry.get("quote")
    if not valid_page:
        return {**result, "reason": "explicit-positive-physical-page-required"}
    if not isinstance(label, str) or not label.strip():
        return {**result, "reason": "citation-label-required"}
    if not isinstance(quote, str) or not without_whitespace(quote):
        return {**result, "reason": "nonempty-quotation-required"}
    if not isinstance(path_value, str) or not path_value.strip() or "\x00" in path_value:
        return {**result, "reason": "local-source-path-required"}
    path = base / path_value
    if path.suffix.lower() != ".pdf":
        return {**result, "reason": "unsupported-source-format"}
    text, reason = selected_page_text(path, physical_page)
    if text is None:
        return {**result, "reason": reason}
    if without_whitespace(quote) in text:
        return {**result, "status": "match", "reason": "text-found-on-selected-page"}
    return {**result, "status": "mismatch", "reason": "text-not-found-on-selected-page"}


def load_entries(path: Path) -> list[dict]:
    spec = json.loads(path.read_text(encoding="utf-8-sig"))
    entries = spec.get("quotes") if isinstance(spec, dict) else None
    if not isinstance(entries, list) or not entries:
        raise ValueError("Manifest must contain a non-empty quotes list")
    seen = set()
    for entry in entries:
        entry_id = entry.get("id") if isinstance(entry, dict) else None
        if not isinstance(entry_id, str) or not ID_PATTERN.fullmatch(entry_id):
            raise ValueError("Each quotation must have a short opaque id")
        if entry_id in seen:
            raise ValueError("Quotation ids must be unique")
        seen.add(entry_id)
    return entries


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path, help="JSON manifest with a quotes list")
    args = parser.parse_args()
    # Third-party extraction diagnostics can include source data. Return status codes instead.
    logging.getLogger("pypdf").setLevel(logging.CRITICAL + 1)
    try:
        entries = load_entries(args.manifest)
    except (OSError, UnicodeError, json.JSONDecodeError):
        parser.error("Manifest could not be read as UTF-8 JSON")
    except ValueError as error:
        parser.error(str(error))
    results = [check_entry(entry, args.manifest.parent) for entry in entries]
    counts = Counter(row["status"] for row in results)
    print(json.dumps({
        "summary": {status: counts[status] for status in ("match", "mismatch", "unverifiable")},
        "results": results,
        "review_note": "Text matches are candidates. Confirm the citation label, source page and context visually.",
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
