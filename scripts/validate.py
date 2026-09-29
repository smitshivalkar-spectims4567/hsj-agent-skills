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
        if name != path.parent.name:
            errors.append(f"{path}: frontmatter name does not match directory")
    if not re.search(r"^version:\s*.+$", text, re.MULTILINE):
        errors.append(f"{path}: missing version")
    if not re.search(r"^description:\s*.+$", text, re.MULTILINE):
        errors.append(f"{path}: missing description")
    if len(text.split()) < 40:
        errors.append(f"{path}: skill is too short to be operational")

for directory in ("agents", "workflows"):
    if not any((ROOT / directory).glob("*.md")):
        errors.append(f"{directory}: no markdown files")

for required in ("AGENTS.md", "CLAUDE.md", "GEMINI.md", ".hermes/README.md", ".openclaw/README.md", ".opencode/README.md", ".claude-plugin/plugin.json", ".codex-plugin/plugin.json", "adapters/README.md", "rules/common.md"):
    if not (ROOT / required).exists():
        errors.append(f"missing adapter or policy file: {required}")

agency_divisions = {"academic", "design", "engineering", "finance", "game-development", "gis", "healthcare", "marketing", "paid-media", "product", "project-management", "research", "sales", "security", "spatial-computing", "specialized", "support", "testing"}
agency_files = sorted((ROOT / "agency").glob("**/*.md"))
for path in agency_files:
    relative = path.relative_to(ROOT / "agency")
    if not relative.parts or relative.parts[0] not in agency_divisions:
        continue
    text = path.read_text(errors="replace")
    if not text.startswith("---\n") or "\n---\n" not in text[4:]:
        errors.append(f"{path}: agency agent missing frontmatter")
        continue
    for field in ("name", "description"):
        if not re.search(rf"^{field}:\s*.+$", text, re.MULTILINE):
            errors.append(f"{path}: agency agent missing {field}")

if errors:
    print("HSJ validation failed")
    print("\n".join(f"- {e}" for e in errors))
    raise SystemExit(1)

print(f"HSJ validation passed: {len(skills)} skills, {len(list((ROOT / 'agents').glob('*.md')))} agents, {len(list((ROOT / 'workflows').glob('*.md')))} workflows")
