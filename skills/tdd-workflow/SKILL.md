---
name: tdd-workflow
version: 0.2.0
description: Drive a feature or bug fix through a focused red-green-refactor loop.
---

# Tdd Workflow

Drive a feature or bug fix through a focused red-green-refactor loop.

## Procedure
1. Define one observable behavior.
2. Add a failing test that demonstrates it.
3. Implement the smallest change that passes.
4. Refactor only while tests remain green.
5. Run the broader relevant suite and report exact commands.

Do not force TDD where the repository has no test harness; instead create the smallest runnable verification and document the limitation.
