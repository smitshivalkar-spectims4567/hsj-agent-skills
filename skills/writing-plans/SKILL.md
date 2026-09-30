---
name: writing-plans
version: 0.3.0
description: Write an implementation plan that a focused engineer can execute without guessing.
---
# Writing Plans

Use after the design gate for multi-file or architectural work.

## Procedure

1. Read repository rules, the approved design, relevant files, callers, tests, and package configuration.
2. Break work into small ordered tasks with one clear outcome each.
3. For every task list exact files or symbols, implementation logic, dependencies, edge cases, and verification.
4. Mark parallel work only when tasks do not overlap or depend on the same changing state.
5. Identify migrations, rollback, secrets, external effects, and human approvals.
6. Keep the plan specific enough for a junior engineer with no conversation context.

## Output

Goal, non-goals, assumptions, tasks, dependencies, tests, risks, approval gates, and completion definition. Do not implement while writing the plan.
