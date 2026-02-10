# Placeholder Conventions

Use double-curly placeholders for all project-specific fields:

- `{{PROJECT_NAME}}`
- `{{PROJECT_ADDRESS}}`
- `{{CLIENT_NAME_OR_ROLE}}`
- `{{PERMIT_REFERENCE}}`
- `{{JURISDICTION}}`
- `{{INSPECTION_DATE}}`
- `{{OBSERVED_AREA}}`

## Rules

1. Never commit real names, addresses, phone numbers, or emails into templates.
2. Prefer role-based placeholders (e.g., `{{REQUESTING_PARTY_ROLE}}`) over person names.
3. Keep placeholder names stable across templates and prompt blueprints.
4. If a value is optional, annotate as optional in template notes.
