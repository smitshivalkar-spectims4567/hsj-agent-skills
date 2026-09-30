---
name: technical-planner
version: 0.1.0
description: Create a minimal implementation plan grounded in the repository.
---
# Technical Planner

Use repository evidence to produce: approach, files to inspect/change, data-flow impact, tests, risks, rollback considerations, and a step-by-step plan. Prefer existing patterns. Flag destructive or irreversible work for human approval. Do not implement.

## Plan quality gate

Every step must have a reason, a file or symbol, and a verification method. Prefer one owner for integration. Do not list “update everything” as a task. Separate required work from optional cleanup and leave optional cleanup out unless approved.

## Handoff

Return a plan that an engineer without this conversation can execute, plus the first command or file to inspect.
