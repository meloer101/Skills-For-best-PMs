# Product Performance Insight Report

> **Usage**: 每个结论必须带 `Evidence:`（引用具体指标/切片）和 `Confidence: L/M/H`。归因前先按 `references/anomaly_heuristics.md` 排除噪声与埋点变更。

---

## Key Metrics Overview

- **Primary metrics（含分子/分母绝对值，不只百分比）**:
- **Baseline period**:
- **对比方式**: 环比 / 同比 / vs 目标
- **Data gaps**:（缺哪些数据 + 如何获取）

---

## Trend Analysis

> 每条趋势先过噪声护栏：分母够吗？超出历史波动带吗？持续 3+ 周期吗？

### T1: [趋势标题]
- **Observation**:（变化方向 + 幅度 + 分母）
- **是否超出日常波动带**: 是 / 否（历史波动范围：___）
- **Evidence**:（指标 + 时间窗 + 切片）
- **Confidence**: L / M / H —（理由：样本量 / 持续时长 / 复现性）

*(按需增加 T2、T3)*

---

## Funnel Analysis

- **Primary funnel steps**:
- **Drop-off points**:（哪一步 + 绝对转化变化）
- **Evidence**:

---

## Retention Impact

- **Cohort retention changes**:（用 cohort，不用全量；区分新奇效应与稳态采用）
- **Key drivers**:
- **Evidence**:
- **Confidence**:

---

## Unexpected Signals

- **Positive surprises**:
- **Negative surprises**:
- **反例 / 与主结论冲突的信号**:（显式记录，别只挑支持性证据）

---

## Hypotheses

> Observation → Hypothesis → Supporting signals。同时记入 `assets/hypothesis_log_template.csv`。

### H1
- **Observation**:
- **Hypothesis**:
- **Supporting signals**:
- **What would disconfirm it**:（什么证据会推翻它）
- **Confidence**: L / M / H

*(H2、H3…)*

---

## Recommended Experiments

> 用最小实验降低最大不确定性。参考 `references/experiment_catalog.md`。

| # | 实验 | 针对的假设 | 目标 segment | 成功指标 & 阈值 | 预期变化的指标 |
|---|------|-----------|--------------|-----------------|----------------|
| 1 | | | | | |
| 2 | | | | | |

---

## Data Gaps & Next Steps

- **本报告受限于**:（哪些结论因数据不足只能标 Low confidence）
- **建议补充**:（查询 / 埋点 / 调研）
