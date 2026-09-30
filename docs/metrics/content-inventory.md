# HSJ content inventory

This is a measured inventory, not a marketing claim. Run `python3 scripts/content_inventory.py` to refresh it after content changes.

## Baseline before expansion

- 21 canonical skills
- 379 Markdown files total, including the imported specialist roster
- 3 Python files
- 2 JSON files
- 1 workflow YAML file
- Canonical skill size now ranges from 66 to 196 words, with the core workflow skills expanded to roughly 100-200 words

## Reference comparison

The reference repositories use mixed implementation languages. ECC contains JavaScript, Python, Shell, TypeScript, Rust, JSON, YAML, and Markdown. Superpowers is mostly Markdown and Shell. Agency Agents is mostly Markdown with small scripts. Microsoft and Wshobson use Markdown plus validation scripts and configuration.

The lesson is not to force a language ratio. It is to use the simplest format that supports the feature: Markdown for instructions, Python or TypeScript only where a real validator/catalog/install tool exists, and YAML/JSON only for native manifests.

## Quality target

A canonical skill should normally be 250-1,500 words when it describes a real workflow. Short reference skills can be smaller if the procedure is genuinely narrow. Length alone is not quality; the validator checks structure and examples, while evaluation checks outcomes.
