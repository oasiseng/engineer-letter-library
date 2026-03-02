# Template Cleanup Playbook (for Uploaded Letter Examples)

Use this when a batch of new letter examples is dropped into `templates/`.

## Goal

Convert raw examples into safe, reusable, LLM-friendly templates.

## 1) Place Files in a Staging Folder

Use this structure:

```text
templates/
  _incoming/
    <uploaded-files>.md
```

Do not move files into `templates/civil/` or `templates/structural/` until cleanup is complete.

## 2) Remove Sensitive Data

For each file, replace project/client specifics with placeholders:

- names → `{{CLIENT_ROLE}}`
- addresses → `{{PROJECT_ADDRESS}}`
- permit IDs → `{{PERMIT_REFERENCE}}`
- inspection date → `{{INSPECTION_DATE}}`
- project name → `{{PROJECT_NAME}}`

## 3) Normalize into Reusable Sections

Reshape each template into consistent blocks:

1. Purpose
2. Scope of review
3. Inputs reviewed
4. Observations
5. Assumptions
6. Limitations
7. PE review required note

## 4) Run Automated Audit

Run:

```bash
python scripts/template_cleanup_audit.py templates
```

Expected behavior:
- exits `0` with no obvious privacy leaks or placeholder drift
- exits `1` and reports suspect lines if cleanup is still needed

## 5) Categorize for Retrieval

Move cleaned files to domain folders and map each to one category in `templates/categories/`:

- site-context-verification
- observed-condition-summary
- repair-remediation-recommendation
- permit-authority-support
- inspection-follow-up
- scope-limitation-partial-observation

## 6) Add a Quick Tips Block per Category

Each category should include:

- drafting intent
- required parameters
- common assumptions
- common limitations
- over-claim language to avoid

