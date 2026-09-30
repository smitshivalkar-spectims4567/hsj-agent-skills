---
name: subagent-driven-development
version: 0.3.0
description: Execute an approved plan with bounded specialists, fresh-context review, and explicit handoffs.
---
# Subagent-Driven Development

Use for multi-step work where separate contexts reduce noise or independent tasks can run safely.

## Procedure

1. Confirm the approved plan and assign one owner per task or file region.
2. Give each worker a small handoff: task, relevant paths, constraints, acceptance criteria, and return format.
3. Workers inspect before editing, implement only their task, run focused checks, and return evidence.
4. Integrate changes in dependency order. Resolve conflicts from repository evidence, not preference.
5. Run a fresh-context code review and security review after implementation.
6. Stop after repeated failure or scope expansion and escalate with a failure history.

## Rules

Do not parallelize tightly coupled edits. Do not preload the full agency roster. Do not treat a worker's “done” claim as verification.

## Output

Handoffs, task results, conflicts, tests, review findings, unresolved risks, and final gate status.
