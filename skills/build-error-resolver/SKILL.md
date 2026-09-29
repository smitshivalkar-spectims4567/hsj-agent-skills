---
name: build-error-resolver
version: 0.2.0
description: Resolve a build, type-check, or dependency failure without hiding the signal.
---

# Build Error Resolver

Resolve a build, type-check, or dependency failure without hiding the signal.

## Procedure
1. Capture the first meaningful error and exact command.
2. Check environment, package manager, lockfiles, generated artifacts, and recent diff.
3. Change one likely cause at a time.
4. Re-run the smallest failing check, then the relevant broader check.
5. Do not delete lockfiles or disable checks as a shortcut without evidence and approval.
