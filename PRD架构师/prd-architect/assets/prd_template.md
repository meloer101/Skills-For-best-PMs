# Product Requirements Document

> **Usage**: 按节填写；每个关键判断后加 `Evidence:` 或 `Assumption:`。空缺处留 `[TBD]` 并回填到 Open Questions。输出前跑 `references/requirements_checklist.md`。

---

## Feature Overview

- **Feature name**:
- **Owner**:
- **Date**:
- **Status**: Draft / In Review / Approved
- **Related docs**: *(上游 Problem Discovery Brief / Prioritized Roadmap / User Insight Report 链接)*

---

## 1. Problem Statement

> 为什么要做这个功能？用户今天怎么受苦？

- **Problem**:
- **Target user**:（角色 + 规模 + 使用频率）
- **Current behavior / workaround**:（用户今天怎么做）
- **Evidence / Assumption**:

---

## 2. Goals & Non-goals

> Non-goals 是 PRD 最有价值的部分——明确「这次不做什么」，防止范围蔓延和跨团队误解。

**Goals**
- User goal:
- Business goal:（growth / retention / revenue / cost / trust）

**Non-goals（本次明确不做）**
- NG1:（+ 一句为什么排除 / 何时再考虑）
- NG2:

**Scope 边界**
- In scope:
- Out of scope:

---

## 3. User Stories

> 格式：As a [user] / I want to [action] / So that [benefit]。每条 story 应能追溯到下面的功能需求。

- **US1** — As a ___, I want to ___, so that ___.
- **US2** — As a ___, I want to ___, so that ___.

---

## 4. Functional Requirements

> 用可测试的 shall/should 语句；每条 FR 挂 Acceptance Criteria（Given/When/Then）。避免不可验证的形容词（"快"、"友好"、"稳定"）。

### FR1: [需求标题]
- **Requirement**: The system **shall** ___.
- **Priority**: Must / Should / Could
- **Traces to**: US1
- **Acceptance Criteria**:
  - Given ___, When ___, Then ___.
  - Given ___, When ___, Then ___.
- **Evidence / Assumption**:

### FR2: [需求标题]
- **Requirement**: The system **shall** ___.
- **Priority**:
- **Traces to**:
- **Acceptance Criteria**:
  - Given ___, When ___, Then ___.

*(按需增加 FR3…)*

---

## 5. Edge Cases

> 用 `assets/edge_case_matrix_template.md` 的类别框架系统枚举，不要只列"invalid input"。把高风险边界的处理结论回填到这里。

| # | 类别 | 场景 | 预期行为 |
|---|------|------|----------|
| 1 | | | |

---

## 6. Non-Functional Requirements

> 每条 NFR 必须有可度量阈值。参考 `references/nfr_rubric.md`。

| # | 维度 | 需求（含阈值） | 度量方式 |
|---|------|----------------|----------|
| NFR1 | Performance | 例：核心接口 p95 < 200ms | APM 监控 |
| NFR2 | Reliability | | |
| NFR3 | Security/Privacy | | |

---

## 7. Dependencies & Risks

> 依赖别人 / 别人依赖你 / 会砸场子的风险。

| 类型 | 项 | 影响 | 应对 / Owner |
|------|----|------|--------------|
| Dependency | | | |
| Risk | | | |

---

## 8. Rollout Plan

> 怎么上、怎么灰度、怎么回滚。

- **Rollout 方式**:（全量 / 灰度百分比 / 按 segment / feature flag）
- **灰度阶段与门槛**:（例：先 5% 内部 → 监控 X 指标 → 50% → 100%）
- **回滚触发条件**:（例：错误率 > 1% 或核心指标下跌 > 5%）
- **Kill switch**: 有 / 无

---

## 9. Success Metrics

> 指标 + 目标值 + 数据来源 + 置信度。详见 `assets/metrics_table_template.csv`。

| 指标 | 定义 | 目标值 & 时限 | 数据来源 | Confidence |
|------|------|---------------|----------|------------|
| | | | | L / M / H |

---

## 10. Open Questions

> 未决问题。不要假装已解决——显式列出并指派。

- **Q1**:（+ 谁来回答 / 何时需要答案）
- **Q2**:

---

## 11. Assumptions Log

> 所有 `Assumption:` 汇总于此，便于后续验证或推翻。

| # | 假设 | 若为假的影响 | 如何验证 |
|---|------|--------------|----------|
| A1 | | | |
