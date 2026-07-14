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
- **Testable language**: requirements must be verifiable. 禁止不可验证的形容词，改写成有阈值/有判定的语句：
  - ❌ "系统应快速响应" → ✅ "核心接口 p95 < 200ms"
  - ❌ "错误提示应友好" → ✅ "输入非法时在 100ms 内在字段下方展示具体原因，不清空已填内容"
  - 每条功能需求都要能写成一个通过/失败明确的 Acceptance Criteria（Given/When/Then）。
- **Non-goals first**: 定义功能时同步写明"本次不做什么"，这是 PRD 防范围蔓延最有价值的部分。

## 交互模式（提问经济学）

- **轮次上限**：最多 2–3 轮提问，每轮 3–5 题；到上限后带**显式假设**（`Assumption:`）直接产出 PRD 草稿，不再无限追问。
- **两档模式**：
  - `Express（lite）`：用户说"快点/先出草稿/lite"时，用一轮问答补齐最关键的 target user + 核心 FR，其余用 `Assumption:` 标注后直接出草稿。
  - `Full`（默认）：走完整 6 个 Stage。
- 允许用户回答"不知道"，把它转成 Open Questions，而不是卡住流程。

## Upstream Inputs（串联上游）

如果存在上游产出物，先读取并继承，不要从零重问：
- **Prioritized Feature Roadmap**（功能排序引擎）：取头号功能项的 Key Driver / Main Risk 作为 Problem 与 Risks 输入。
- **Problem Discovery Brief**（问题澄清引擎）：继承 Target User / JTBD / Success criteria，直接填入 Stage 1–2。
- **User Insight Report**（用户洞察提炼）：Pain Points 作为 Problem 证据，Opportunity 作为范围参考。
- 无上游时正常从 Stage 1 采集。

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
- Worked example: `examples/example_prd.md`

