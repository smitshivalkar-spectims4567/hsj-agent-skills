---
name: agent-evaluator
version: 0.2.0
description: Measure whether a skill or agent improves outcomes instead of trusting its prose.
---

# Agent Evaluator

Measure whether a skill or agent improves outcomes instead of trusting its prose.

## Procedure
Create representative tasks with acceptance criteria. Run a baseline without the skill and a run with it. Compare correctness, test results, unnecessary changes, time, token/context use, and safety failures. Keep failed cases.

## Output
Task set, baseline, treatment, metrics, regressions, decision, and next experiment.
