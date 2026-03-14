#!/usr/bin/env python3
"""
Minimal skill validator (no external deps).

Validates:
- SKILL.md exists
- YAML frontmatter exists and contains name + description
- name is hyphen-case (lowercase letters, digits, hyphens)
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


NAME_RE = re.compile(r"^[a-z0-9-]+$")


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        raise ValueError("No YAML frontmatter start ('---') found.")

    end = text.find("\n---\n", 4)
    if end == -1:
        raise ValueError("No YAML frontmatter end ('---') found.")

    block = text[4:end]
    data: dict[str, str] = {}

    current_key: str | None = None
    for raw_line in block.splitlines():
        line = raw_line.rstrip("\n")
        if not line.strip():
            continue

        if re.match(r"^[A-Za-z0-9_-]+:\s*", line):
            key, value = line.split(":", 1)
            current_key = key.strip()
            data[current_key] = value.strip()
            continue

        # Support simple continuation lines (indented)
        if current_key and (line.startswith("  ") or line.startswith("\t")):
            data[current_key] = (data[current_key] + " " + line.strip()).strip()
            continue

        raise ValueError(f"Unrecognized frontmatter line: {raw_line}")

    return data


def main() -> int:
    skill_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        print("SKILL.md not found")
        return 1

    text = skill_md.read_text(encoding="utf-8")
    try:
        fm = parse_frontmatter(text)
    except ValueError as e:
        print(str(e))
        return 1

    name = (fm.get("name") or "").strip()
    desc = (fm.get("description") or "").strip()
    if not name:
        print("Missing 'name' in frontmatter")
        return 1
    if not desc:
        print("Missing 'description' in frontmatter")
        return 1

    if not NAME_RE.match(name):
        print("Invalid name: must match ^[a-z0-9-]+$")
        return 1
    if name.startswith("-") or name.endswith("-") or "--" in name:
        print("Invalid name: cannot start/end with '-' or contain '--'")
        return 1
    if len(name) > 64:
        print("Invalid name: length must be <= 64")
        return 1

    if "<" in desc or ">" in desc:
        print("Invalid description: cannot contain '<' or '>'")
        return 1
    if len(desc) > 1024:
        print("Invalid description: length must be <= 1024")
        return 1

    print("Skill looks valid (minimal checks passed).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

