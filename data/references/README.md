# External References Intake

This directory is for **reference materials** that inform template and instruction design.

It is separate from `data/training/` because references may include public guidance,
blogs, agency pages, and other non-letter artifacts used for context only.

## Why this exists

External guides (for example, county inspection requirement explainers) can be very useful,
but they must be handled with provenance, licensing, and review controls.

## Intake Rules

1. Do not copy proprietary content into this repository without permission.
2. Prefer storing metadata + URL + summary over full text.
3. Track publication date and last-reviewed date.
4. Mark jurisdiction and topic tags explicitly.
5. Treat extracted points as draft context, not binding determinations.
6. Require PE/legal review before converting reference ideas into reusable language primitives.

## Recommended Structure

- `jurisdiction-guides/` for local/regional guidance sources
- one YAML manifest per source
- optional notes markdown for reviewer synthesis
