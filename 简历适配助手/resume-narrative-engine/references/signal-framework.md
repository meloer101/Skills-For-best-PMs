# Signal Framework

## Strong Signals (prioritize)

- **Product model inference** (UGC, marketplace, workflow, social graph, etc.)
- **User flow definition** (auth → create → feed → interaction, onboarding, retention loop)
- **Data model design** (schema choices, entities, relationships)
- **System interfaces** (API boundaries, service contracts, integration points)
- **Scalability/performance strategy** (caching, pagination, async jobs, queues)
- **AI/RAG/data pipeline** (retrieval, evaluation, latency controls, guardrails)
- **Architecture choices** (SSR/CSR, monolith vs services, infra constraints)

## Weak Signals (ignore unless JD explicitly asks)

- UI styling, layout tweaks, component refactors
- Basic CRUD endpoints with no product impact
- Library swaps without architectural trade-offs
- Cosmetic performance changes without evidence

## Evidence Rule

Every claim must map to observable evidence from code or artifacts:
schema files, routes, services, infrastructure config, README, tests, or diagrams.

## PM Translation Table

| Engineering Signal | PM Framing |
| --- | --- |
| Database schema | Data model design |
| API endpoints | System interface definition |
| Frontend state | User flow / interaction design |
| Auth system | Identity & access control strategy |
| Caching/perf | Scalability & performance strategy |
| Queue/worker | Reliability & throughput design |
| RAG pipeline | AI experience & knowledge delivery |

## Counterfactual Framing (allowed)

When metrics are missing, describe capability not outcome:

- ✅ “Designed a system capable of supporting high-frequency user interactions.”
- ✅ “Defined data model and API structure to enable scalable content flows.”
- ❌ “Improved engagement by 30%.”

## Signal Scoring Heuristic

`Priority Score = JD Priority × Signal Strength`

Use the top-scoring signals as the spine of the narrative.
