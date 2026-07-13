---
name: resume-narrative-engine
description: Transform project codebases and artifacts plus a target job description into PM-style resume narratives, bullets, and gap diagnostics. Use when a user wants to translate engineering work into product-manager framing, select an appropriate narrative (e.g., 0→1, system thinker, AI/data), prioritize signals based on a JD, and produce evidence-backed resume bullets without fabricating metrics.
---

# Resume Narrative Engine

## Overview

Translate code into credible PM resume narratives by extracting reality, ranking signals against the JD, and constructing bullets that prove a PM persona without inventing metrics.

## Inputs to Request (if missing)

- Codebase path or artifact list (README, architecture docs, schemas, major modules)
- Target JD or role description
- Target role level (intern/entry/mid/senior) and function focus (growth/platform/AI/etc.)
- Output language and bullet count per project
- Any real metrics or outcomes the user can claim

## Workflow (Two-Pass, Mandatory)

### Pass 0 — Guardrails (do before analysis)

- Do not fabricate metrics, users, or outcomes.
- Allow counterfactual framing: describe capabilities the system enables when metrics are missing.
- Require evidence: every claim must map to observable code or artifacts.
- Keep PM lens: emphasize decisions, user problems, trade-offs, and system thinking.

### Pass 1 — Mapping (no final bullets)

1. **Reality Extraction**  
   Infer product model, users, use-cases, and system shape from code and docs. Capture evidence notes.

2. **JD → Ideal PM Persona**  
   Convert the JD into a concise “ideal PM persona” list (top priorities and vocabulary).

3. **Signal Ranking**  
   Rank evidence by `JD Priority × Signal Strength`. Use strong/weak signal taxonomy and translation table in `references/signal-framework.md`.

4. **Narrative Selection**  
   Choose a primary narrative strategy and optional secondary. Use `references/narrative-strategies.md`.

5. **Claim Map**  
   Draft 3–5 candidate claims per project with: claim → evidence → PM framing → JD match.  
   Mark missing signals (gaps) explicitly.

6. **Project Positioning**  
   Classify project as toy / portfolio / production-like and tune tone accordingly.

**Output of Pass 1:**  
Produce a **Mapping Summary** section (persona, narrative, top signals, claim map, gaps). Do not write final bullets yet.

### Pass 2 — Narrative Construction

- Convert claim map into bullets using PM framing templates in `references/output-schema.md`.
- Prefer “decision + user problem + system impact” over engineering tasks.
- If outcomes are unknown, use counterfactual capability framing (see `references/signal-framework.md`).
- Ensure each bullet aligns to a JD priority and is supported by evidence.

## Output Format (default)

1. **Mapping Summary**  
   - Ideal PM persona (from JD)  
   - Chosen narrative strategy  
   - Top 3–5 strong signals with evidence  
   - Claim map (claim → evidence → PM framing)  
2. **Resume Bullets** (3–5 bullets per project)
3. **Missing Signals** (gap detection + suggested info to provide)
4. **Assumptions** (only if required)

## Quality Checks (must pass)

- No fabricated metrics or users.
- Every bullet links to evidence from code or artifacts.
- Weak signals are excluded unless JD explicitly requires them.
- PM lens is visible: decisions, trade-offs, user problems, system thinking.
- Tone matches project positioning (toy/portfolio/production-like).

## References

- `references/signal-framework.md` for signal taxonomy, PM translation table, and counterfactual framing rules.
- `references/narrative-strategies.md` for narrative selection logic and bullet composition strategy.
- `references/output-schema.md` for mapping summary and bullet templates.
