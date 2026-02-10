# Repository Map (Scaffolding)

This document describes why each major folder exists and what future content belongs there.

## `templates/`
Section-based letter skeletons with neutral placeholders (no final engineering determinations).

## `instructions/primitives/`
Reusable language primitives for assumptions, limitations, scope boundaries, and disclaimer patterns.

## `instructions/guardrails/`
Rules constraining LLM behavior and clarifying PE-required review checkpoints.

## `scenarios/modules/`
Scenario packs for narrowly scoped contexts (e.g., retrofit observation follow-up, non-prescriptive detail support). Modules should provide context, not conclusions.

## `prompts/`
Prompt blueprints and system contracts for structured LLM workflows.

## `schemas/letter-parameters/`
Parameter catalogs and validation rules used to construct draft outputs consistently.

## `data/training/`
Future ingestion location for real-world letter corpora and metadata.

## `docs/architecture/engineer-letter-faq.md`
Contributor-facing FAQ for high-level repository usage and boundaries.

## `data/references/`
Metadata-first intake for external jurisdiction/process guides (provenance, licensing, review status).
