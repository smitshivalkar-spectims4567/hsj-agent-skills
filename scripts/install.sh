#!/usr/bin/env bash
set -euo pipefail

# Copy a selected HSJ surface into a project; never touches global credentials or permissions.
TARGET="${1:-.}"
mkdir -p "$TARGET/.hsj"
cp -R AGENTS.md skills agents workflows rules commands "$TARGET/.hsj/"
printf 'HSJ content copied to %s/.hsj\n' "$TARGET"
printf 'Review the files before enabling them in your agent.\n'
