---
name: product-metrics-analyst
description: Post-launch metrics analysis workflow that converts usage data into actionable Product Performance Insight Reports. Use when a feature has shipped and the team needs to assess adoption, retention, funnels, anomalies, behavioral signals, generate hypotheses, and recommend experiments with explicit evidence tagging and data gaps.
---

# Product Metrics Analyst

Turn post-launch metrics into actionable insights with clear hypotheses and experiments.

## Output (required)

Produce a `Product Performance Insight Report` using `assets/insight_report_template.md`.
Use `assets/metrics_snapshot_table.csv` and `assets/hypothesis_log_template.csv` as supporting artifacts.

## Operating Rules

- Evidence first: every conclusion must cite a metric or signal.
- No dashboard recitation: summarize meaning, not raw numbers.
- Tag data gaps: explicitly list missing data and how to obtain it.
- Keep it concise: short bullets, clear actions.
- **先判噪声再归因**：下任何结论前，先过 `references/anomaly_heuristics.md` 的噪声护栏——分母够不够、有没有超出历史波动带、是否持续 3+ 周期。落在日常波动带内的变化按噪声处理，不强行讲故事。
- **先排除仪器变更**：把观察归因到用户行为之前，先排除埋点/口径/数据管道变更。
- **标注置信度**：每个结论带 `Confidence: L/M/H`，Low confidence 的结论不驱动重决策，只驱动"再取数/做实验"。

## 交互模式（提问经济学）

- **轮次上限**：最多 2–3 轮提问，每轮 3–5 题；到上限后带显式假设直接产出报告草稿。
- **两档模式**：
  - `Express（lite）`：用户直接甩来一份指标截图/表格时，先出"趋势 + 疑似异常 + 待验证假设"的快报，缺的上下文用 `Assumption:` 标注。
  - `Full`（默认）：走完整 6 个 Stage。

## Upstream Inputs（串联上游）

- **PRD（PRD 架构师）的 Success Metrics**：直接作为本次分析的北极星指标与基线目标，不用重新问"什么算成功"。
- **Prioritized Roadmap / Problem Brief**：功能当初要解决的问题 = 现在要验证有没有解决。
- 无上游时从 Stage 1 采集产品目标与主指标。

## Workflow (6 stages)

Each stage outputs a brief summary and updates the report.

### Stage 1 - Metric Context

Goal: align on product goals and primary metrics.

Output:
- Product goal
- Primary success metrics
- Target user segments

Use questions from `references/question_bank.md#stage-1`.

### Stage 2 - Data Intake

Goal: collect the metrics and slices needed for analysis.

Output:
- Metrics snapshot (current vs baseline)
- Segment, cohort, version, and channel slices

Use questions from `references/question_bank.md#stage-2`.

### Stage 3 - Trend Detection

Goal: detect growth, decline, and anomalies.

Output:
- Notable trends (up/down/stable)
- Anomalies and potential drivers

Use `references/anomaly_heuristics.md`.

### Stage 4 - Behavioral Analysis

Goal: understand user paths and value realization.

Output:
- Funnel performance
- Activation and feature usage patterns
- Drop-off points

Use questions from `references/question_bank.md#stage-4`.

### Stage 5 - Hypothesis Generation

Goal: explain observations with testable hypotheses.

Output format:
- Observation -> Hypothesis -> Supporting signals

Log hypotheses in `assets/hypothesis_log_template.csv`.

### Stage 6 - Experiment Recommendation

Goal: propose experiments to validate hypotheses.

Output:
- Recommended experiments
- Success criteria and expected signal

Use `references/experiment_catalog.md`.

## Completeness Check

Before final output, run the checklist in `references/analysis_checklist.md`.

## Resources

- Question prompts: `references/question_bank.md`
- Analysis checklist: `references/analysis_checklist.md`
- Anomaly heuristics: `references/anomaly_heuristics.md`
- Experiment catalog: `references/experiment_catalog.md`
- Report template: `assets/insight_report_template.md`
- Metrics snapshot: `assets/metrics_snapshot_table.csv`
- Hypothesis log: `assets/hypothesis_log_template.csv`
- Worked example: `examples/example_insight_report.md`

