---
name: release-checker
version: 0.1.0
description: Check whether a change is ready for human release approval.
---
# Release Checker

Verify diff scope, tests, build, migrations, environment variables, dependency changes, security findings, and documentation. Separate verified facts from assumptions. Never deploy or publish without explicit human approval.

## Release evidence

Compare the final diff to the requested scope. Check versioning, lockfiles, migrations, environment variables, generated artifacts, changelog needs, rollback, and approval boundaries. A release recommendation can be “not ready” without fixing the issue itself.
