# Data Sanitization Policy

This repository should only store **de-identified training artifacts** and **neutral templates**.

## Redact Before Ingestion

Remove or replace the following from source letters:
- owner/client names
- street addresses and parcel numbers
- permit numbers that can identify a specific property
- phone numbers, email addresses, signatures, and license IDs not required for template logic
- contractor/subconsultant names when not essential to the reusable pattern
- any notes marked confidential/proprietary

## Replace With Placeholders

Use reusable placeholders instead of project-specific facts:
- `{{PROJECT_NAME}}`
- `{{PROJECT_ADDRESS}}`
- `{{CLIENT_ROLE}}`
- `{{PERMIT_REFERENCE}}`
- `{{INSPECTION_DATE}}`

## Minimum Metadata for Sanitized Artifacts

Each ingested artifact should include:
- `source_id`
- `sanitization_status` (`pending` | `complete`)
- `sanitized_by`
- `sanitized_at_utc`
- `pii_removed` (`true` | `false`)
- `confidential_removed` (`true` | `false`)

## Review Gate

No source-derived text can be promoted into templates until:
1. sanitization is marked `complete`, and
2. a maintainer confirms no client/site-specific content remains.
