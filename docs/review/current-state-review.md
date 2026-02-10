# Current State Review and Improvement Priorities

## Executive Assessment

The project foundation is strong: it clearly enforces PE authority, avoids over-claiming legal/compliance outcomes, and frames LLM output as drafting support only.

The highest-value next step is to convert that philosophy into repeatable operational controls so contributors can add letters safely at scale.

## What Is Working Well

1. **Safety posture is clear**
   - Current docs explicitly prevent misuse as engineering advice.
2. **Scaffold-first strategy is correct**
   - Building structure before loading source letters will reduce chaos later.
3. **Parameter-first direction is practical**
   - This will make validation, retrieval, and quality checks easier over time.

## Gaps to Close Before Data Ingestion

1. **No canonical intake contract yet**
   - Need one required metadata format for every incoming letter (discipline, scope, jurisdiction, limitations, provenance).
2. **No acceptance checklist for publishable templates**
   - Need a go/no-go gate before template release.
3. **No field-reality guardrails**
   - Need language patterns for uncertain access, incomplete records, changed site conditions, and contractor substitutions.
4. **No contribution workflow for sensitive content**
   - Need explicit rules for redaction, anonymization, and source license verification.

## Recommended Near-Term Plan (Practical + Field-Grounded)

### Phase A: Governance Hardening (Now)
- Publish contribution policy and legal boundaries.
- Add lightweight review checklist for PE/legal/repository maintainers.

### Phase B: Intake Discipline (Before loading database)
- Require per-letter metadata manifests.
- Add schema validation rules and minimum required fields.
- Enforce provenance + jurisdiction tagging from day one.

### Phase C: Drafting Safety Controls
- Add reusable assumption/limitation primitives.
- Add boundary-validation prompt before any draft is emitted.
- Ban absolute language unless explicitly justified and PE-approved.

### Phase D: Field Reality Modules
- Add scenario modules for:
  - Partial access inspections
  - Existing-condition uncertainty
  - Deferred submittal dependencies
  - Repair-in-kind vs redesign scope boundaries

## Guiding Principle

**Be conservative in conclusions and precise in scope.**

Strong engineering letters are less about sounding definitive and more about being explicit: what was reviewed, what was not reviewed, what assumptions were required, and what decisions remain with the AHJ and responsible PE.
