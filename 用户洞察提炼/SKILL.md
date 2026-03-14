---
name: user-insight-synthesizer
description: Thematic analysis engine that transforms raw user data (interview transcripts, support tickets, app reviews, community posts, survey responses, behavior logs) into a structured User Insight Report with evidence-anchored insights. Use when a PM or researcher has collected user data and needs to extract behavior patterns, discover user archetypes, uncover hidden motivations, and identify ranked product opportunities. Prevents surface-level summarization by enforcing observation→insight layering and minority-voice tracking. 适用于：把大量原始用户声音压缩为可信的用户认知模型，输出可驱动产品决策的 User Insight Report。
---

# User Insight Synthesizer

把"混乱的用户声音 → 结构化用户认知模型 → 有证据支撑的产品机会"。

## Output (不可省略)

最终必须产出一份 `User Insight Report`（用 `assets/user_insight_report_template.md` 作为骨架）。**每条 insight 必须附 Evidence 行**（来源类型 + 数量 + 代表性引用）。

## Operating Rules (防止失控)

- **No bare summaries**：不允许只做摘要；每个 observation 都必须向上提炼到 insight 层（原因 / 模式 / 需求层）。
- **Evidence-anchored**：每条 insight 后附 `Evidence:`（例：`12/25 interviewees, 8 tickets, 3 App Store reviews`）。
- **Minority tracking**：主流观点旁必须记录反例或少数声音，防止确认偏误。
- **Signal vs Anecdote**：单人提及 = anecdote；3+ 独立来源 = signal；跨渠道重复 = strong signal。
- **No premature solutions**：Stage 1–4 中不提功能设计；Opportunity 方向只在 Stage 5 提出，且仅为"机会方向"，不涉及具体实现。
- **Small-batch questions**：每轮最多 5–8 个问题；优先问"能改变分析框架"的问题。

## Workflow (5 stages)

每个 Stage 都要输出一个小结，并写入 Report 对应章节。

### Stage 1 — Data Intake

**Goal**：理解数据结构，建立分析上下文，识别数据质量风险。

**Do**
- 询问数据来源类型、样本量、时间范围、用户类型
- 标注数据质量风险：代表性 / 新鲜度 / 收集偏差
- 建立 `Data Inventory`（见下方字段）

**Data Inventory fields**
- Source type (interview / ticket / review / community / survey / behavior log)
- Sample size
- User type (new / power / churned / etc.)
- Time range
- Known biases / collection method

**Exit criteria**
- 至少明确：1 个数据来源 + 样本量 + 数据覆盖的用户类型。

> 题库及方法细节见 `references/coding_guide.md#stage-1`.

---

### Stage 2 — Signal Extraction

**Goal**：把文本拆解为 atomic signals（最小可分析单元），并进行初步编码。

**Do**
- 把每段用户原话拆成独立的 signal
- 每个 signal 标注：极性（Positive / Negative / Neutral）、初始主题标签、来源引用
- 区分 signal（3+ 独立来源）和 anecdote（单人）

**Signal 格式**
```
[interview_03 | Neg] "onboarding is overwhelming" → #onboarding #cognitive-load
[ticket_142  | Neg] "can't find the export button" → #navigation #discoverability
[review_089  | Pos] "love the templates"           → #templates #ease-of-start
```

> 题库及编码规则见 `references/coding_guide.md#stage-2`.

---

### Stage 3 — Pattern Clustering

**Goal**：把 signals 聚合为 themes（主题模式）。

**Do**
- 按相似标签对 signals 聚类
- 为每个 cluster 命名 Theme（用名词短语，不用形容词）
- 记录每个 theme 的 signal count、代表性引用、以及 contradicting signals
- 尝试发现 User Archetypes（跨主题的行为人格）

**Cluster 格式**
```
Theme: Cognitive Overload During Onboarding
Signal count: 14 (interview ×8, review ×4, ticket ×2)
Representative quotes:
  - "too many options at once" (interview_02)
  - "I didn't know where to start" (review_089)
Contradicting signals: 1 ("onboarding was fine" — expert user, interview_11)
```

> 聚类方法论见 `references/coding_guide.md#stage-3`.

---

### Stage 4 — Insight Generation

**Goal**：从 observation 推导 insight，从表面现象挖掘深层需求 / 动机 / 心理模型。

**Insight 层级模型**
```
Level 1 — Observation:  用户在做什么 / 说什么（what）
Level 2 — Pattern:      多个用户的共同行为 / 反应（what × many）
Level 3 — Insight:      为什么会这样（why → mental model / motivation / constraint）
Level 4 — Implication:  对产品决策意味着什么（so what）
```

**每条 insight 的完整输出结构**
- Observation（Level 1–2）
- Insight（Level 3：深层原因 / 心理模型）
- Evidence（样本量 + 来源类型 + 代表性引用）
- Implication（Level 4：产品方向的一句话含义）
- Confidence (Low / Medium / High + 理由)

> 题库及推导方法见 `references/coding_guide.md#stage-4`.

---

### Stage 5 — Opportunity Detection

**Goal**：在 insights 中识别产品机会，按优先级排序。

**Scoring criteria（每项 1–5 分，加总）**
- **Frequency**：多少用户受影响？
- **Pain intensity**：有多痛？（阻断任务 vs 轻微不适）
- **Solution gap**：现有方案有多差？
- **Strategic fit**：与产品当前方向的对齐程度

**Output**
- Opportunity Areas（按总分降序排列）
- 每条附：supporting insights + evidence + Quick win / Strategic bet 标签
- 明确 `Data Gaps`（哪些问题还缺数据，建议下一步补什么）

> 题库见 `references/coding_guide.md#stage-5`.

---

## User Insight Report (artifact 生成规则)

按模板输出（见 `assets/user_insight_report_template.md`），并遵守：
- 每条 insight 后必须有 Evidence 行（来源 + 数量 + 引用）。
- Minority Views 区必须记录对立观点。
- Opportunity Areas 必须附 scoring 依据。
- 明确 `Data Gaps` 和 `Recommended Next Steps`。

## Optional tool hooks (更强版)

当用户授权或已有资料时，可接入：
- **Browser / Web research**：访问 App Store reviews 页、Reddit / 社区讨论、公开竞品反馈（使用 cursor-ide-browser MCP 抓取；记录来源 URL + 日期）
- **Document input**：访谈记录 / 调查问卷 / 客服 ticket（PDF、Notion 导出、Google Docs 链接）
- **Knowledge base**：与 Problem Discovery Brief 中的 Pain Points / JTBD 做交叉验证

只在能显著提升证据质量时才调用；否则优先推进"发现模式 + 输出 insight"。
