#!/usr/bin/env python3
"""Small structural validator for the HSJ content repository."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
errors = []

skills = sorted((ROOT / "skills").glob("*/SKILL.md"))
names = []
for path in skills:
    text = path.read_text()
    if not text.startswith("---\n") or "\n---\n" not in text[4:]:
        errors.append(f"{path}: missing YAML frontmatter")
    match = re.search(r"^name:\s*(.+)$", text, re.MULTILINE)
    if not match:
        errors.append(f"{path}: missing name")
    else:
        name = match.group(1).strip()
        if name in names:
            errors.append(f"duplicate skill name: {name}")
        names.append(name)
    if not re.search(r"^description:\s*.+$", text, re.MULTILINE):
        errors.append(f"{path}: missing description")

for directory in ("agents", "workflows"):
    if not any((ROOT / directory).glob("*.md")):
        errors.append(f"{directory}: no markdown files")

if errors:
    print("HSJ validation failed")
    print("\n".join(f"- {e}" for e in errors))
    raise SystemExit(1)

print(f"HSJ validation passed: {len(skills)} skills, {len(list((ROOT / 'agents').glob('*.md')))} agents, {len(list((ROOT / 'workflows').glob('*.md')))} workflows")
