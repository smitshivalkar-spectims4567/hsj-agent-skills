---
name: verification-loop
version: 0.3.0
description: Verify a change through targeted checks, review, and release evidence before calling it complete.
---
# Verification Loop

Use after implementation and before merge, release, or a completion claim.

## Procedure

1. Map acceptance criteria to checks.
2. Run the narrowest relevant tests, lint, type checks, build, and manual checks.
3. Inspect the complete diff and relevant callers.
4. Run security checks for trust boundaries, secrets, permissions, dependencies, and external effects.
5. Record exact commands, exit status, results, skipped checks, and limitations.
6. Escalate failures, data-loss risk, or unverified claims.

## Completion contract

A change is not verified because an agent says it is done. Return changed files, checks run, checks passed, checks not run, findings, known risks, and human approval needed.
