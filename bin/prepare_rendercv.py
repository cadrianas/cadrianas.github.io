#!/usr/bin/env python3
"""Convert the site's CV data into the stricter RenderCV input schema."""

from __future__ import annotations

import argparse
import copy
from pathlib import Path
from typing import Any

import yaml


def prepare_document(document: dict[str, Any]) -> dict[str, Any]:
    output = copy.deepcopy(document)
    cv = output["cv"]

    # al-folio uses these fields on the website; RenderCV calls the role a headline
    # and accepts profile text as a regular text section.
    label = cv.pop("label", None)
    if label:
        cv["headline"] = label

    summary = cv.pop("summary", None)
    sections = cv["sections"]
    if summary:
        cv["sections"] = {"Profile": [summary], **sections}
        sections = cv["sections"]

    degree_labels = {
        "Master of Science": "MSc",
        "Master of Science (Course-Based)": "MSc",
        "Bachelor of Science (Honours)": "BSc",
    }
    for entry in sections.get("Education", []):
        entry["degree"] = degree_labels.get(entry.get("degree"), entry.get("degree"))

    sections["Publications"] = [
        {
            key: value
            for key, value in {
                "title": entry["title"],
                "authors": entry["authors"],
                "journal": entry.get("journal", entry.get("publisher")),
                "date": entry.get("date"),
                "doi": entry.get("doi"),
                "url": entry.get("url"),
            }.items()
            if value is not None
        }
        for entry in sections.get("Publications", [])
    ]

    sections["Skills"] = [
        {
            "label": entry["name"],
            "details": ", ".join(entry.get("keywords", [])),
        }
        for entry in sections.get("Skills", [])
    ]

    sections["Awards"] = [
        {
            key: value
            for key, value in {
                "name": entry["title"],
                "date": entry.get("date"),
                "summary": entry.get("awarder"),
            }.items()
            if value is not None
        }
        for entry in sections.get("Awards", [])
    ]

    return output


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("destination", type=Path)
    args = parser.parse_args()

    document = yaml.safe_load(args.source.read_text(encoding="utf-8"))
    prepared = prepare_document(document)
    args.destination.write_text(
        yaml.safe_dump(prepared, sort_keys=False, allow_unicode=True),
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
