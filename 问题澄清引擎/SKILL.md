---
name: problem-discovery-engine
description: Systematic product discovery workflow that turns a fuzzy idea/feature proposal into a structured, testable Problem Discovery Brief (Idea → Problem Definition). Use when PMs need to prevent solution-first misframing, discover hidden user problems, map User Situation + JTBD, perform root-cause analysis (Five Whys/Fishbone/constraints), identify opportunity areas, and convert findings into verifiable product hypotheses + validation plans. 适用于：需求/功能想法澄清、问题定义、产品 discovery 早期对话式追问与产出 Problem Brief。
---

# Problem Discovery Engine

把“模糊想法 → 结构化问题模型 → 可验证的产品假设”。

## Output (不可省略)

最终必须产出一份 `Problem Discovery Brief`（用 `assets/problem_discovery_brief_template.md` 作为骨架），并维护一份 `Hypothesis Ledger`（用 `assets/hypothesis_ledger_template.md`）。

## Operating Rules (防止失控)

- **Freeze solutions**：在 Stage 6 之前，不设计功能、不写 PRD、不讨论 UI 细节；一旦用户给 solution，先把它记录为“候选假设/干预手段”，然后继续问题探查。
- **Evidence-first**：每个关键断言都标注证据来源（用户访谈/数据/工单/观察/推断），推断必须显式写明。
- **Relentless why**：对“这是问题/需要/痛点”的陈述递归追问，直到出现可操作的 root cause 或关键约束。
- **Small-batch questions**：每轮最多 5–8 个问题；给出建议回答格式，降低用户负担。
- **Hypothesis management**：把不确定性都写进 ledger；用置信度驱动下一步研究，而不是争论。

## Workflow (6 stages)

每个 Stage 都要输出一个小结（可直接写入 Brief），并更新 Hypothesis Ledger。

### Stage 1 — Idea Intake (禁止直接跳方案)

**Goal**：把想法翻译成“需要澄清的上下文”，识别信息缺口。

**Do**
- 复述用户的 idea（用中性语言），拆出：目标用户候选、场景候选、期望结果候选、显性约束。
- 生成 `Initial Context Questions`（优先级从高到低）。

**Exit criteria**
- 至少明确 1 个目标用户画像候选 + 1 个场景候选 + 1 个可观察的失败/摩擦信号。

> 题库见 `references/question_bank.md#stage-1`.

### Stage 2 — User Situation Mapping

**Goal**：建立 `User Situation Model`：谁 / 在什么情境 / 被什么触发 / 想达成什么 / 受什么约束。

**Output fields**
- User
- Situation
- Trigger
- Goal
- Constraints

> 题库见 `references/question_bank.md#stage-2`.

### Stage 3 — Job To Be Done (JTBD)

**Goal**：把“想要功能”提炼为“想完成的任务”。

**Output format**
```
When ______
I want to ______
So I can ______
```

**Checks**
- “I want to …” 里避免具体实现（例如“自动总结”），改写为任务/结果（例如“快速抓住关键决策并同步给团队”）。

> 题库见 `references/question_bank.md#stage-3`.

### Stage 4 — Root Cause Analysis

**Goal**：找到“为什么这是问题”的根因与约束结构。

**Methods (按需选 1–2 个即可)**
- Five Whys（递归追问到可行动的机制/约束）
- Fishbone（人/流程/工具/信息/激励/环境）
- Constraint analysis（瓶颈在哪里？为什么不可绕过？）

**Output**
- Root causes（1–3 条，写成机制句：`Because ... therefore ...`）
- Non-causes（哪些看似原因但其实是症状/二阶效应）

> 题库见 `references/question_bank.md#stage-4`.

### Stage 5 — Opportunity Discovery

**Goal**：从现有解法与摩擦中抽取机会空间，而不是直接发明功能。

**Output**
- Current solutions（含替代品/手工 workaround/竞品/内部流程）
- Pain points（按频率×严重度×可替代性排序）
- Opportunity areas（可被改善的环节/信号/流程）

> 题库见 `references/question_bank.md#stage-5`.

### Stage 6 — Hypothesis Generation (允许进入方案，但仍以验证为中心)

**Goal**：把机会空间转成“可被验证/证伪”的产品假设，并明确验证方法。

**Output format (一条假设一行)**
- Hypothesis：`If we ... for [target user] in [situation], then [measurable outcome], because [root cause].`
- Validation method：最小验证（访谈/原型/实验/数据回放/concierge）
- Success criteria：阈值（例：≥30% 用户在 1 周内复用；或关键指标提升 X%）

同时把每条假设写入 `Hypothesis Ledger`，包含置信度与证据。

> 题库见 `references/question_bank.md#stage-6`.

## Problem Discovery Brief (artifact 生成规则)

按模板输出（见 `assets/problem_discovery_brief_template.md`），并遵守：
- 每段尽量 1–3 句，避免散文。
- 所有关键判断后加 `Evidence:`（例如：`Evidence: 3 interviews (2026-03-10), 12 support tickets, analytics query TBD`）。
- 明确 `Open Questions`（下一步需要补什么信息/数据）。

## Hypothesis Ledger (持续维护)

使用 `assets/hypothesis_ledger_template.md`：
- 记录 **Hypothesis / Evidence / Confidence / Test / Next step**。
- 置信度建议用 `Low/Medium/High`，并说明理由（样本量/代表性/反例）。

## Optional tool hooks (更强版)

当用户授权或已有资料时，可接入：
- **Web research**：竞品、行业基准、已知用户行为（记录来源与日期）
- **User data**：工单/反馈/埋点/漏斗（把查询需求写进 Open Questions）
- **Knowledge base**：访谈记录/产品文档/roadmap（用于证据与约束）

只在能显著提升证据质量时才调用；否则优先推进“问对问题 + 形成可验证假设”。

