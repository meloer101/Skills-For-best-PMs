---
name: pm-interview-defense-system
description: Build evidence-backed, multi-layer interview answer systems (surface/deep/follow-up) for PM/TPM/engineering interviews using project artifacts. Use when a user wants interview prep, needs defensible answers, wants to simulate follow-up questions, or needs to turn project work into decision-focused narratives with trade-offs and evidence mapping.
---

# PM Interview Defense System

## Overview
Convert project evidence into a three-layer answer system that can withstand follow-up pressure. Prioritize decision-making, trade-offs, and credibility over polished but fragile narratives.

## Workflow

### 1) Intake And Scope
- Gather the interview question(s), target role, and available project artifacts (codebase, PRDs, tickets, metrics, launch notes, demos, writeups).
- If evidence is missing, proceed with conservative assumptions and label them explicitly as assumptions.
- If multiple questions are provided, handle them one at a time.

### 2) Difficulty Selection Engine
Select a difficulty that demonstrates decision value, not just technical complexity. Use these criteria:
- Has real trade-offs and multiple viable options.
- Involves a decision or prioritization (not just debugging).
- Impacts user experience, system design, or product outcomes.
- Demonstrates PM thinking (problem framing, constraints, impact, iteration).

If a question is too shallow (e.g., “fixed a bug”), reframe it into a decision-oriented difficulty using the criteria above.

### 3) Evidence Extraction
- Identify concrete evidence from artifacts (architecture choices, data models, metrics, user feedback, release notes, backlog priorities).
- Build an evidence map that ties each claim to a source or marks it as an assumption.
- Avoid fabricating metrics or outcomes; use qualitative signals when hard data is missing.

### 4) Construct The Three-Layer Answer System
Always output three layers:
- **Layer 1 — Surface Answer (30–60 sec)**: concise, structured narrative focused on decision points and impact.
- **Layer 2 — Deep Breakdown (not necessarily spoken)**: facts, constraints, alternatives considered, trade-offs, failed attempts, and reasoning.
- **Layer 3 — Follow-up Defense**: 3–7 likely follow-up questions with credible responses grounded in evidence.

### 5) Compression Levels
Provide multiple lengths when useful:
- `30 sec version` (elevator)
- `2 min version` (standard)
- `Deep dive` (for follow-ups)

### 6) Imperfection Rule
Include at least one of the following in the deep breakdown or follow-ups:
- Failed attempt
- Uncertainty
- Trade-off regret

This prevents over-polished, non-credible answers.

### 7) Quality Gates
- Each claim must be mapped to evidence or explicitly labeled as an assumption.
- Focus on decisions and trade-offs, not implementation details.
- Summarize the lesson as a transferable capability (what you would do again and why).

## Output Format
Use this structure for each question:
- `Difficulty Selected` (1–2 lines)
- `Evidence Map` (claim → evidence/assumption)
- `Layer 1 — Surface Answer`
- `Layer 2 — Deep Breakdown`
- `Layer 3 — Follow-up Defense`
- `Compression Levels` (if requested)

## Reference Template
Use `/Users/m/Documents/Skills/pm-interview-defense-system/references/answer-system-template.md` for the canonical structure and checklists.
