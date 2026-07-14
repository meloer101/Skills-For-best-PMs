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
- **Verify before you quantify（防幻觉）**: 写「Called by N files」这类具体数字前，必须实际 grep 计数；没核实的量化断言标为 estimate，不要编造精确数字。引用文件/函数/字段前先确认其真实存在。详见 `references/analysis_guide.md#anti-hallucination-rule`。
- Translate code to roles: every module gets a system role (Orchestrator, Gatekeeper, Async Processor, Data Layer, API Gateway)
- Narratives over diagrams alone: add a human-readable scenario for each key flow
- Business lens: explain what code does in product terms, not just technical terms
- **Degrade explicitly on large codebases**: 库过大读不完时，采样高优先级区域并在报告里声明覆盖范围，不假装通读。见 `references/analysis_guide.md#大代码库降级策略`。

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

### Stage 3.5 — Impact & Evolution

- **Impact Analysis**: 对 2–3 个最高风险核心模块，用依赖关系（谁调用它）列出改动波及面（直接调用方 + 二阶波及 + blast radius）。回答"改这里会不会炸"。
- **System Evolution**: 若有 git 历史，用 `git log` 统计最常改动文件，区分活跃区 / 稳定区，标出既高频又高复杂度的 hotspot。无 git 历史则标 N/A。

### Stage 4 — Generate report

Fill the template from `assets/project_intelligence_report_template.md`.

Optionally generate role-specific views if requested:

| View | Emphasis |
|------|----------|
| Developer View | Modules, dependencies, complexity, onboarding path |
| PM View | Features, user flows, business scenarios, data models in product terms |
| Architecture View | Layers, services, data flow, tech choices, patterns |

## Upstream Inputs（串联位置）

本 Skill 是**独立入口**，无需上游产出物。其输出可作为下游 Skill 的证据源：
- **Resume Narrative Engine / PM Interview Defense System** 会把本报告的 Core Modules / Data Models / Business Scenarios 作为简历与面试的证据来源。

## 交互模式

- 本 Skill 以自主分析代码为主，提问少。需要用户澄清时（如目标视角、关注的子系统）**一次问清**，不超过 1 轮。
- **两档模式**：`Express` = 只出 System Overview + Core Modules + 1 条关键 Flow；`Full`（默认）= 完整报告 11 节。

## Resources

- Report template: `assets/project_intelligence_report_template.md`
- Analysis methodology: `references/analysis_guide.md`
- Worked example: `examples/example_report_excerpt.md`
