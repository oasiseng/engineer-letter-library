# Letter Corpus Intake and Skill Packaging Workflow

This workflow is designed for turning a private corpus of engineer letters into a sanitized, reusable knowledge base and then packaging that material as a skill.

> [!IMPORTANT]
> Source letters may contain sensitive data. Keep raw files out of version control and only commit sanitized derivatives.

## 1) Intake Structure

Create a private local staging area (not committed):

```text
private/
  raw-letters/
  sanitized-letters/
  manifests/
```

- `raw-letters/`: original files with full provenance.
- `sanitized-letters/`: de-identified versions for extraction and clustering.
- `manifests/`: one metadata file per source letter documenting sanitization and review status.

## 2) Redaction Checklist (Per Letter)

Apply the repository redaction policy before any model processing:

- remove client/person names
- remove exact site addresses and parcel identifiers
- remove permit numbers that can re-identify a site
- remove contact details and signatures
- remove proprietary or confidential project references

Then replace retained context with placeholders:

- `{{PROJECT_NAME}}`
- `{{PROJECT_ADDRESS}}`
- `{{CLIENT_ROLE}}`
- `{{PERMIT_REFERENCE}}`
- `{{INSPECTION_DATE}}`

## 3) Synthesis Pass (LLM-Friendly)

For each sanitized letter, derive:

1. **Letter type** (e.g., condition observation, roof framing review, deferred submittal support)
2. **Discipline** (structural/civil/geotechnical/etc.)
3. **Scenario tags** (wind retrofit, foundation movement, water intrusion, etc.)
4. **Risk posture** (low/medium/high statement sensitivity)
5. **Reusable sections** (scope, assumptions, limitations, disclaimers, recommendation framing)
6. **Parameter candidates** (all variable fields needed to draft similar letters)

Write one synthesis record per letter using structured YAML or JSON.

## 4) Category Model for 50+ Letters

After per-letter synthesis, cluster into 6–12 practical categories. Suggested top-level taxonomy:

- **Site/Context Verification Letters**
- **Observed Condition Summary Letters**
- **Repair/Remediation Recommendation Letters**
- **Permit/Authority Support Letters**
- **Inspection Follow-Up Letters**
- **Scope Limitation / Partial Observation Letters**

Each category should include:

- intent and non-intent boundaries
- required parameters
- optional parameters
- common assumptions
- common limitations
- prohibited over-claims

## 5) Tips Library Extraction

Build a concise “tips” block for each category:

- best-practice phrasing patterns
- language to avoid (absolute guarantees, code-interpretation claims without review)
- typical missing inputs to request
- quality checklist before PE review

Store these tips in markdown files under a new category folder (for example, `scenarios/modules/`).

## 6) Skill Packaging Plan (for Clawbot/Clawdhub)

When the categories are stable:

1. Create a single skill entrypoint that:
   - accepts sanitized parameters,
   - selects the correct category pack,
   - composes draft sections,
   - enforces guardrail/disclaimer injection,
   - requires PE review acknowledgment.
2. Keep legal/safety boundaries explicit in skill instructions.
3. Include examples with placeholders only (no real project data).
4. Version the skill and changelog as category logic evolves.

## 7) Suggested Immediate Next Steps

1. Add your 50 letters to a private `private/raw-letters/` folder outside git tracking.
2. Produce sanitized derivatives and manifests.
3. Generate first-pass category clusters and tips.
4. Promote only de-identified reusable patterns into this repository’s `templates/`, `instructions/`, and `scenarios/` folders.
5. Package the resulting orchestrator as a skill once category quality is consistent.
