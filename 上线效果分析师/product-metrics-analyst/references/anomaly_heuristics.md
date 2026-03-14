# Anomaly Heuristics

Use simple rules to flag potential issues.

## Trend Flags

- Change > 15% week-over-week in a core metric
- Sudden drop after a specific version release
- Segment-specific deviation from overall trend
- Funnel step conversion change > 10% absolute

## Triage Questions

1. Is the anomaly global or segment-specific?
2. Did instrumentation or definitions change?
3. Is the anomaly correlated with a release or campaign?

