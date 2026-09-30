# Agency roster

HSJ has two layers:

- `skills/` contains the canonical, provider-neutral procedures.
- `agency/` contains optional specialist personas organized by division.

Search first and load one specialist at a time:

```bash
python3 scripts/agency_catalog.py search "database performance"
python3 scripts/agency_catalog.py inspect engineering/engineering-database-optimizer.md
```

The roster is not automatically preloaded. A large prompt catalog is useful only when selection is lazy and the selected agent has a bounded deliverable.
