---
name: systematic-debugging
version: 0.3.0
description: Reproduce a failure, isolate its root cause, and verify a focused fix instead of patching symptoms.
---
# Systematic Debugging

Use for bugs, failed tests, regressions, and confusing behavior.

## Procedure

1. Capture the exact failure, environment, command, and expected behavior.
2. Reproduce it before editing whenever possible.
3. Trace the data flow and all relevant callers.
4. Form one falsifiable root-cause hypothesis and test it with the smallest diagnostic.
5. Apply the smallest fix at the shared cause.
6. Add or update one regression check, then run the original reproduction and relevant suite.

## Escalation

After three materially different failed approaches, stop repeating attempts. Return evidence, hypotheses rejected, and a focused question.

## Output

Reproduction, root cause, fix, regression evidence, commands/results, and remaining uncertainty.
