#!/usr/bin/env python3
"""Audit markdown templates for obvious privacy leaks and placeholder drift."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

PLACEHOLDER_RE = re.compile(r"\{\{[A-Z0-9_]+\}\}")
EMAIL_RE = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")
PHONE_RE = re.compile(r"\b(?:\+?1[-.\s]?)?(?:\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4})\b")
ADDRESS_RE = re.compile(
    r"\b\d{1,6}\s+(?:[A-Za-z0-9.'-]+\s+){1,5}"
    r"(?:Street|St|Avenue|Ave|Road|Rd|Boulevard|Blvd|Lane|Ln|Drive|Dr|Court|Ct)\b",
    re.IGNORECASE,
)

RECOMMENDED_PLACEHOLDERS = {
    "{{PROJECT_NAME}}",
    "{{PROJECT_ADDRESS}}",
    "{{CLIENT_ROLE}}",
    "{{PERMIT_REFERENCE}}",
    "{{INSPECTION_DATE}}",
    "{{JURISDICTION}}",
    "{{DISCIPLINE}}",
    "{{LETTER_TYPE}}",
    "{{CLIENT_NAME_OR_ROLE}}",
    "{{REQUESTING_PARTY_ROLE}}",
    "{{OBSERVED_AREA}}",
    "{{OBSERVATION_METHOD}}",
    "{{WEATHER_CONDITIONS}}",
    "{{REFERENCE_DOCUMENTS}}",
    "{{ASSUMPTION_LIST}}",
    "{{LIMITATION_LIST}}",
    "{{FOLLOW_UP_ACTIONS}}",
}


def scan_file(path: Path) -> list[str]:
    issues: list[str] = []
    text = path.read_text(encoding="utf-8", errors="ignore")

    for label, pattern in (
        ("possible email", EMAIL_RE),
        ("possible phone", PHONE_RE),
        ("possible street address", ADDRESS_RE),
    ):
        for match in pattern.finditer(text):
            snippet = match.group(0).strip()
            issues.append(f"{path}: {label}: '{snippet}'")

    placeholders = set(PLACEHOLDER_RE.findall(text))
    if placeholders:
        nonstandard = sorted(ph for ph in placeholders if ph not in RECOMMENDED_PLACEHOLDERS)
        if nonstandard:
            issues.append(
                f"{path}: non-standard placeholders detected: {', '.join(nonstandard)}"
            )
    return issues


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", default="templates", help="directory to scan")
    args = parser.parse_args()

    root = Path(args.root)
    if not root.exists():
        print(f"Path not found: {root}", file=sys.stderr)
        return 2

    files = sorted(p for p in root.rglob("*.md") if p.is_file())
    issues: list[str] = []
    for file in files:
        issues.extend(scan_file(file))

    if issues:
        print("TEMPLATE CLEANUP AUDIT: issues found")
        for item in issues:
            print(f"- {item}")
        return 1

    print(f"TEMPLATE CLEANUP AUDIT: no issues found in {len(files)} markdown file(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
