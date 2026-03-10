# Uncertainty Toolkit

Use these techniques when data is missing or weak.

## Ranges and Sensitivity

- Capture min / most-likely / max for Reach, Impact, or Effort.
- Compute best-case and worst-case scores.
- If ranking flips under small changes, flag as unstable.

## Confidence Labels

- High: strong quantitative data or repeated signals
- Medium: mixed evidence or small samples
- Low: mostly assumptions or one-off anecdotes

## Assumption Log

For each feature, list assumptions that could invalidate the ranking.
Example:
- Assumption: 30% of active users will adopt within 30 days.
- Risk: onboarding friction limits adoption.

## Fastest Experiment

Recommend one of:
- Prototype test (qualitative)
- Concierge or manual workflow test
- A/B test or holdout
- Data replay or backtest

Pick the smallest test that reduces the highest uncertainty first.

