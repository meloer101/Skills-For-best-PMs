---
name: feature-prioritization-engine
description: Structured feature prioritization workflow that converts a backlog of features/opportunities into a transparent, ranked roadmap with explicit scoring, assumptions, and trade-offs. Use when a team must decide execution order across multiple proposals, align on evaluation criteria, apply frameworks like RICE/ICE/MoSCoW/Impact-Effort, surface hidden assumptions, handle uncertainty, and produce a Prioritized Feature Roadmap artifact with reasoning.
---

# Feature Prioritization Engine

Turn a political, fuzzy backlog into a transparent decision system with repeatable scoring and explicit trade-offs.

## Output (required)

Produce a `Prioritized Feature Roadmap` using `assets/prioritized_feature_roadmap_template.md` and a `Feature Scoring Table` using `assets/feature_scoring_table_template.csv`.

## Operating Rules

- Freeze debate: enforce the same criteria for every item before any ranking.
- Evidence-first: label assumptions vs evidence; quantify confidence.
- No magic: every score must have a stated rationale.
- Small batches: 5 to 8 questions per round.
- Uncertainty-aware: if data is missing, use ranges and tag risks.

## Workflow (6 stages)

Each stage outputs a short summary and updates the scoring table.

### Stage 1 - Feature Intake

Goal: understand each feature before scoring.

Collect for each item:
- Target user
- Problem or opportunity
- Expected user value
- Business goal
- Success signal

Use questions from `references/question_bank.md#stage-1`.

Exit criteria:
- At least one clear user segment and one success signal per feature.

### Stage 2 - Evaluation Criteria Setup

Goal: define the decision framework and weights.

Default criteria:
- User Value
- Business Impact
- Strategic Alignment
- Effort
- Risk

Optional frameworks:
- RICE (Reach, Impact, Confidence, Effort)
- ICE (Impact, Confidence, Effort)
- MoSCoW (Must, Should, Could, Won't)
- Impact vs Effort

If the strategy is clear, set weights (sum to 1.0). Otherwise keep equal weights and document the uncertainty.

### Stage 3 - Scoring

Goal: score each feature consistently.

Default formula (weighted score):
```
Priority Score = sum(criterion_score * weight) - risk_penalty
```

RICE formula (when applicable):
```
RICE Score = (Reach * Impact * Confidence) / Effort
```

Guidance:
- Use numeric scales (1-5 or 1-10) for comparable criteria.
- Record the rationale and evidence level in the scoring table.
- If a value is unknown, use a range and mark confidence as Low.

See `references/scoring_rubrics.md`.

### Stage 4 - Trade-off Analysis

Goal: categorize items by value vs cost vs risk.

Classify:
- Quick wins (high value, low effort)
- Strategic bets (high value, high effort)
- Maintenance or debt paydown (low value, necessary)
- Defer or kill (low value, high effort or risk)

Call out the top 3 trade-offs explicitly.

### Stage 5 - Portfolio View

Goal: build a balanced roadmap, not only top scores.

Create a portfolio mix:
- 2 quick wins
- 1 strategic bet
- 1 reliability or infra improvement

Adjust based on constraints (capacity, deadlines, dependencies). Document any overrides.

### Stage 6 - Recommendation

Goal: publish the ranked roadmap with reasoning and uncertainty.

For each ranked item:
- Priority rank
- Key drivers
- Main risks
- Next validation step

Use the roadmap template and include a short rationale per item.

## Uncertainty Handling

When data is missing or weak:
- Use ranges (min/most-likely/max) and show sensitivity.
- Mark confidence (Low/Medium/High) and list what would change it.
- Recommend the smallest experiment that reduces the highest uncertainty first.

See `references/uncertainty_toolkit.md`.

## Resources

- Question prompts: `references/question_bank.md`
- Scoring guidance: `references/scoring_rubrics.md`
- Uncertainty toolkit: `references/uncertainty_toolkit.md`
- Roadmap template: `assets/prioritized_feature_roadmap_template.md`
- Scoring table template: `assets/feature_scoring_table_template.csv`

