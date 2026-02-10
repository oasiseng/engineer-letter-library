# Engineer Letter Library

A conservative, open-source framework for structuring **engineering letter artifacts** and **LLM instruction workflows**.

> [!IMPORTANT]
> This repository does **not** provide engineering advice, code interpretation, or final engineering determinations.
> All final conclusions, certifications, and stamped deliverables must be made by a licensed Professional Engineer (PE) with authority in the relevant jurisdiction.

## Purpose (Phase 1: Scaffolding)

This phase establishes a durable architecture so future contributors can add:
- Letter templates (language structure only)
- Reusable instruction primitives
- Scenario/situation modules
- Prompt blueprints for LLM-assisted drafting support

This phase intentionally excludes final opinion language, engineering calculations, and compliance determinations.

## Repository Architecture

```text
.
├── data/
│   ├── references/
│   │   ├── README.md
│   │   └── jurisdiction-guides/
│   │       ├── README.md
│   │       └── us-fl-lee-county-residential-inspections-source.example.yaml
│   └── training/
│       └── README.md
├── docs/
│   ├── architecture/
│   │   ├── engineer-letter-faq.md
│   │   └── repository-map.md
│   └── governance/
│       ├── contribution-policy.md
│       └── legal-boundaries.md
├── instructions/
│   ├── guardrails/
│   │   ├── llm-safety-boundaries.md
│   │   └── pe-review-requirement.md
│   └── primitives/
│       ├── assumptions.md
│       ├── limitations.md
│       ├── scope-definition.md
│       └── standard-disclaimers.md
├── prompts/
│   ├── blueprints/
│   │   ├── compose-letter-draft.md
│   │   ├── extract-parameters.md
│   │   └── validate-boundaries.md
│   └── system/
│       └── system-contract.md
├── scenarios/
│   └── modules/
│       ├── README.md
│       └── module-template.md
├── schemas/
│   └── letter-parameters/
│       ├── parameter-catalog.md
│       ├── parameter-schema.example.yaml
│       └── validation-rules.md
├── templates/
│   ├── README.md
│   ├── _shared/
│   │   └── section-blocks.md
│   ├── civil/
│   │   └── README.md
│   └── structural/
│       └── README.md
├── what-is-an-engineer-letter.md
└── README.md
```


## Orientation Documents

- `what-is-an-engineer-letter.md`: concise definition and repository boundary framing.
- `docs/architecture/engineer-letter-faq.md`: practical FAQ for contributors and users.

## Design Principles

1. **PE authority is non-delegable**
   - LLM outputs are drafting aids only.
2. **Conservative legal posture**
   - Avoid definitive compliance claims in reusable scaffolds.
3. **Composable building blocks**
   - Separate template structure, scenario context, and instruction logic.
4. **Parameter-first authoring**
   - Letters are assembled from validated parameters, not ad-hoc prose.
5. **Traceability and reviewability**
   - Inputs, assumptions, and limitations are explicit and reviewable.

## Parameterization Model (Core)

Future letters should be defined by explicit parameters (non-exhaustive):
- `jurisdiction`: state/province/local authority context
- `discipline`: structural/civil/geotechnical/etc.
- `letter_type`: observation summary, deferred submittal support, etc.
- `project_metadata`: project name, address, permit reference
- `inspection_context`: date, method, observed areas, access limits
- `scope_of_review`: what is and is not included
- `assumptions`: declared assumptions used in draft language
- `limitations`: constraints, exclusions, and data limitations
- `requested_by`: party requesting the document
- `pe_reviewer`: responsible engineer metadata (placeholder only)

See `schemas/letter-parameters/` for scaffold files.

## Naming Conventions

- Use lowercase kebab-case for file and folder names.
- Keep scenario modules short, specific, and reusable.
- Keep template files content-neutral and section-oriented.
- Prefer `.md` for instruction documents and `.yaml` for structured parameter examples.

## External Guide Intake (e.g., Lee County, Florida)

Yes—external guides can be loaded as **reference metadata** under `data/references/` using source manifests.

Use this flow:
1. Add source metadata YAML (URL, publisher, jurisdiction, date, license status).
2. Keep full-text storage disabled unless permissions are explicitly documented.
3. Run PE/legal review before converting insights into reusable scaffolding.

## How This Repository Evolves

When real-world training letters are added later:
1. Place source corpora under `data/training/` with provenance metadata.
2. Extract recurring structural patterns into `templates/`.
3. Extract reusable logic and caveat language into `instructions/primitives/`.
4. Add scenario-specific context packs under `scenarios/modules/`.
5. Update prompt blueprints to orchestrate retrieval + parameter validation + boundary checks.

## Current Status

This repository currently contains scaffolding only. It is ready for phased population with curated, reviewable source material and PE-supervised workflows.
