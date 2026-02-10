# Engineer Letter FAQ (Repository Orientation)

This FAQ is informational and repository-focused. It is not engineering advice.

## 1) Does this repository generate final engineer letters?
No. It provides scaffolding (templates, parameters, prompts, and guardrails) for draft support only.

## 2) Who is responsible for final technical conclusions?
A licensed Professional Engineer with authority in the relevant jurisdiction is responsible for final conclusions and release.

## 3) Will this repository include real-world training letters later?
Yes. Future phases are expected to ingest curated corpora into `data/training/` with provenance and permission controls.

## 4) Why separate templates, scenarios, primitives, and prompts?
To keep language structure modular, reduce duplication, and improve traceability during PE review.

## 5) Can contributors add jurisdiction-specific compliance conclusions?
Not in this scaffolding phase. Contributions should remain neutral and avoid final compliance determinations.

## 6) What should contributors add now?
- Structure definitions
- Parameter schemas
- Guardrail improvements
- Documentation clarity

## 7) Where should domain-specific patterns go later?
- Template structure: `templates/`
- Reusable language blocks: `instructions/primitives/`
- Situation-specific context: `scenarios/modules/`
- LLM orchestration patterns: `prompts/`
