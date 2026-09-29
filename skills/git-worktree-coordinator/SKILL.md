---
name: git-worktree-coordinator
version: 0.2.0
description: Coordinate independent agent work without overlapping edits.
---

# Git Worktree Coordinator

Coordinate independent agent work without overlapping edits.

## Procedure
Use separate worktrees or branches for genuinely independent tasks. Assign one owner per file region. Require each worker to return a focused diff, tests, and conflicts. Integrate only after review. Do not parallelize tightly coupled edits or create worktrees for trivial changes.
