---
name: project-intelligence
description: Analyzes any codebase and generates a deep Project Intelligence Report — revealing system architecture, core modules, data flows, business logic, and complexity areas. Goes far beyond README generation. Use when a user wants to understand a new codebase, onboard to a project, explore system architecture, trace request flows, analyze dependencies, understand how a project really works, or needs to explain a system to developers or PMs.
---

# Project Intelligence

Generates a **Project Intelligence Report** — a deep system comprehension document that reveals invisible structures: who orchestrates what, how data flows, where complexity lives, and what the code means in product terms.

This is not a README generator. It is a **Project Comprehension Engine**.

**Success standard**: a new engineer can start modifying code after reading the report for 10 minutes.

## Output (required)

Produce a `Project Intelligence Report` using the structure defined in `assets/project_intelligence_report_template.md`.

## Operating Rules

- Concrete over generic: name actual files, not "the service layer"
- Evidence-first: every Core Module claim must cite evidence (call count, dependencies, business logic present)
- Translate code to roles: every module gets a system role (Orchestrator, Gatekeeper, Async Processor, Data Layer, API Gateway)
- Narratives over diagrams alone: add a human-readable scenario for each key flow
- Business lens: explain what code does in product terms, not just technical terms

## Workflow (4 stages)

### Stage 1 — Explore

Read broadly before writing. Prioritize:

1. **Entry points** — `main.ts`, `server.ts`, `app.py`, `index.js`, `cmd/`
2. **Directory structure** — top-level, then key subdirectories
3. **Dependency manifest** — `package.json`, `requirements.txt`, `go.mod`
4. **Config / infra** — `.env.example`, `docker-compose.yml`, CI configs
5. **Data models** — `schema.prisma`, `models/`, `entities/`, `migrations/`
6. **Most-imported files** — high import count = likely core module
7. **Routing layer** — `routes/`, `controllers/`, `handlers/`

For very large codebases: focus on entry points → routing → core business logic → data models.

Exit criteria: you can describe what the system does in one paragraph.

### Stage 2 — Identify core modules

For each candidate core module, collect evidence:
- How many files import it?
- How many downstream modules does it call?
- Does it contain primary business logic?

Assign a **system role** to each. See `references/analysis_guide.md` for role definitions and signal patterns.

### Stage 3 — Trace key flows

Pick 2–4 critical user actions. For each, trace the full path from UI to database.
Note which files are touched and what each does at that step.

### Stage 4 — Generate report

Fill the template from `assets/project_intelligence_report_template.md`.

Optionally generate role-specific views if requested:

| View | Emphasis |
|------|----------|
| Developer View | Modules, dependencies, complexity, onboarding path |
| PM View | Features, user flows, business scenarios, data models in product terms |
| Architecture View | Layers, services, data flow, tech choices, patterns |

## Resources

- Report template: `assets/project_intelligence_report_template.md`
- Analysis methodology: `references/analysis_guide.md`
