# Templates

This folder will contain reusable **letter structure templates**.

## Rules for Template Content
- Keep content neutral and structural.
- Use placeholders for all fact-specific fields.
- Do not include final engineering determinations.
- Keep sections explicitly separable for composition.

## Suggested Section Pattern
1. Document metadata
2. Scope of review
3. Inputs reviewed
4. Observations (if applicable)
5. Assumptions
6. Limitations
7. PE review/signature block placeholder


## Placeholder Standard
Use the shared placeholder naming guidance in `templates/_shared/placeholder-conventions.md`.

## Batch Cleanup Workflow

If you upload a batch of example letters, run the cleanup playbook before promotion:

- `docs/workflows/template-cleanup-playbook.md`
- `python scripts/template_cleanup_audit.py templates`

Only move files out of `templates/_incoming/` after they pass sanitization and placeholder normalization.
