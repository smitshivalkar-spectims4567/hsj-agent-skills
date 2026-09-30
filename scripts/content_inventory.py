#!/usr/bin/env python3
"""Report HSJ file types and canonical skill sizes."""
from collections import Counter
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
files = [p for p in ROOT.rglob('*') if p.is_file() and '.git' not in p.parts]
counts = Counter(p.suffix.lower() or '[no extension]' for p in files)
print('Files by extension:')
for suffix, count in counts.most_common(): print(f'{suffix}	{count}')
skills = sorted((ROOT / 'skills').glob('*/SKILL.md'))
print(f'Canonical skills: {len(skills)}')
for path in sorted(skills, key=lambda p: len(p.read_text().split())):
    print(f'{len(path.read_text().split())}	{path.relative_to(ROOT)}')
