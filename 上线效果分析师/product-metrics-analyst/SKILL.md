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

