---
name: prd-architect
description: Structured PRD authoring workflow that turns a decided feature into a concise, engineer-ready Product Requirements Document. Use when a team must translate product decisions into clear problem context, user stories, functional requirements, edge cases, non-functional requirements, and success metrics, with completeness checks and explicit assumptions.
---

# PRD Architect

Turn a decided feature into a concise, executable PRD that aligns PM, design, and engineering.

## Output (required)

Produce a `Product Requirements Document` using `assets/prd_template.md`.
Use `assets/edge_case_matrix_template.md` and `assets/metrics_table_template.csv` as supporting artifacts when needed.

## Operating Rules

- Avoid verbosity: focus on system behavior, not narrative history.
- Evidence tagging: mark assumptions and evidence for key claims.
- Completeness check: ensure all core sections are filled.
- Testable language: requirements must be verifiable.

## Workflow (6 stages)

Each stage outputs a short summary and updates the PRD.

### Stage 1 - Context Intake

Goal: capture why this feature exists and what success means.

Output:
- Feature context (problem, target user, success signal)

Use questions from `references/question_bank.md#stage-1`.

### Stage 2 - User Story Construction

Goal: bind the feature to user value.

Output format:
```
As a [user]
I want to [action]
So that [benefit]
```

Use questions from `references/question_bank.md#stage-2`.

### Stage 3 - Functional Requirements

Goal: express system behaviors in testable terms.

Output:
- Functional requirements list (shall/should statements)
- Acceptance criteria per key requirement

Use questions from `references/question_bank.md#stage-3`.

### Stage 4 - Edge Case Discovery

Goal: enumerate failure modes, limits, and exceptions.

Output:
- Edge case matrix (scenario -> expected behavior)

Use questions from `references/question_bank.md#stage-4`.

### Stage 5 - Non-Functional Requirements

Goal: define performance, security, reliability, and constraints.

Output:
- NFR list with measurable thresholds

Use `references/nfr_rubric.md`.

### Stage 6 - Success Metrics

Goal: define how success is measured.

Output:
- Metrics table (definition, target, data source)

Use questions from `references/question_bank.md#stage-6`.

## Completeness and Consistency

Before final output, run the checklist in `references/requirements_checklist.md`.

## Resources

- Question prompts: `references/question_bank.md`
- Completeness checklist: `references/requirements_checklist.md`
- NFR guidance: `references/nfr_rubric.md`
- PRD template: `assets/prd_template.md`
- Edge case matrix: `assets/edge_case_matrix_template.md`
- Metrics table: `assets/metrics_table_template.csv`

