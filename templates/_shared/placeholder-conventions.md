# Placeholder Conventions

Use double-curly placeholders for all project-specific fields.

## Canonical Placeholders

- `{{PROJECT_NAME}}`
- `{{PROJECT_ADDRESS}}`
- `{{CLIENT_ROLE}}`
- `{{REQUESTING_PARTY_ROLE}}`
- `{{PERMIT_REFERENCE}}`
- `{{JURISDICTION}}`
- `{{INSPECTION_DATE}}`
- `{{OBSERVED_AREA}}`
- `{{DISCIPLINE}}`
- `{{LETTER_TYPE}}`

## Optional Placeholders

- `{{OBSERVATION_METHOD}}`
- `{{WEATHER_CONDITIONS}}`
- `{{REFERENCE_DOCUMENTS}}`
- `{{ASSUMPTION_LIST}}`
- `{{LIMITATION_LIST}}`
- `{{FOLLOW_UP_ACTIONS}}`

## Rules

1. Never commit real names, addresses, phone numbers, or emails into templates.
2. Prefer role-based placeholders over person names.
3. Keep placeholder names stable across templates and prompt blueprints.
4. If a value is optional, annotate as optional in template notes.
5. Do not embed numeric calculations or final compliance determinations in reusable templates.

## Legacy Alias Guidance

If existing drafts use `{{CLIENT_NAME_OR_ROLE}}`, convert it to `{{CLIENT_ROLE}}` during cleanup.
