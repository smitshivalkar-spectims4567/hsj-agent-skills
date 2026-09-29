#!/usr/bin/env python3
"""List and search HSJ's specialist agency without loading every prompt."""
from pathlib import Path
import argparse
import re

ROOT = Path(__file__).resolve().parents[1] / "agency"

def metadata(path):
    text = path.read_text(errors="replace")
    block = re.search(r"\A---\n(.*?)\n---\n", text, re.S)
    data = {}
    if block:
        for line in block.group(1).splitlines():
            key, sep, value = line.partition(":")
            if sep:
                data[key.strip()] = value.strip().strip('"')
    return data, text

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("list")
    search = sub.add_parser("search")
    search.add_argument("query")
    search.add_argument("--division")
    inspect = sub.add_parser("inspect")
    inspect.add_argument("path")
    args = parser.parse_args()
    files = sorted(ROOT.glob("**/*.md"))
    files = [p for p in files if p.name not in {"README.md", "AGENCY-LICENSE.txt"}]
    if args.command == "list":
        print(f"{len(files)} agency specialists")
        for path in files:
            data, _ = metadata(path)
            print(f"{path.relative_to(ROOT)}\t{data.get('name', path.stem)}\t{data.get('description', '')}")
    elif args.command == "search":
        query = args.query.lower()
        division = args.division.lower() if args.division else None
        hits = []
        for path in files:
            if division and path.relative_to(ROOT).parts[0].lower() != division:
                continue
            data, text = metadata(path)
            haystack = " ".join([str(data), text]).lower()
            if all(term in haystack for term in query.split()):
                hits.append((path, data))
        print(f"{len(hits)} matches")
        for path, data in hits:
            print(f"{path.relative_to(ROOT)}\t{data.get('name', path.stem)}\t{data.get('description', '')}")
    else:
        path = (ROOT / args.path).resolve()
        if ROOT not in path.parents or not path.is_file():
            raise SystemExit("agent not found inside agency/")
        print(path.read_text())

if __name__ == "__main__":
    main()
