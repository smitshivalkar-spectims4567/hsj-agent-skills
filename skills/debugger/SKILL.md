---
name: debugger
version: 0.1.0
description: Reproduce failures and fix their root cause.
---
# Debugger

Reproduce the failure. Trace callers and the real data flow. Identify the root cause before editing. Make one focused fix at the shared cause where possible. Add one regression check. Record failed attempts and remaining uncertainty.

## Debugging evidence

Do not make a sequence of guesses without recording results. Narrow the failure with input reduction, boundary logging, or a failing regression test. Check whether the same cause affects sibling callers. A fix is incomplete if the original reproduction still fails.

## Failure report

Include the first failing command, root cause, rejected hypotheses, changed paths, and exact reproduction after the fix.
