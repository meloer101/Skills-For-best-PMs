# Coding Guide — User Insight Synthesizer

分析方法论参考 + 各阶段追问题库。

使用原则：每轮最多 5–8 题；优先问"能改变分析框架"的问题；允许"不知道"，但把它变成 `Data Gaps` 和下一步行动。

---

## Table of Contents

1. [Stage 1 — Data Intake](#stage-1)
2. [Stage 2 — Signal Extraction](#stage-2)
3. [Stage 3 — Pattern Clustering](#stage-3)
4. [Stage 4 — Insight Generation](#stage-4)
5. [Stage 5 — Opportunity Detection](#stage-5)
6. [Appendix: Thematic Analysis Primer](#appendix)

---

## Stage 1

### 题库

1. 数据来自哪些渠道？（访谈 / 客服 ticket / App Store 评价 / 社区 / 问卷 / 行为日志）
2. 总共有多少条 / 多少人？样本是如何被选择的？
3. 这些用户是哪类用户？（新用户 / 活跃用户 / 流失用户 / 付费用户 / 特定 Persona）
4. 数据收集的时间范围是？有没有明显的外部事件（版本更新 / 促销 / 竞品变化）影响这段时间的反馈？
5. 数据的收集方式是什么？（结构化问卷 vs 开放访谈 vs 被动评论）——会影响偏差方向。
6. 你已知的"期望结论"是什么？（帮助识别确认偏误风险）
7. 有没有你明确不想分析的内容 / 范围？（边界设定）

### 数据质量风险清单

| 风险类型 | 表现 | 应对方式 |
|---------|------|---------|
| 选样偏差 | 只有投诉用户发声，沉默用户缺席 | 标注 "vocal minority" 风险；建议补充满意用户访谈 |
| 时效偏差 | 数据来自旧版本，产品已变化 | 标注日期范围；旧数据仅作参考 |
| 渠道偏差 | 只有 App Store（高情绪）无客服 ticket（具体问题） | 建议补充其他渠道 |
| 代理人偏差 | 数据来自销售 / CS 转述，非用户直接声音 | 降低 confidence；标注来源为二手 |
| 语言 / 地区偏差 | 只有英文评价，产品主力用户在其他市场 | 明确适用范围 |

---

## Stage 2

### 题库

1. 这句话里有几个独立的意思？（常见错误：把多层意思压在一个 signal 里）
2. 这是用户在描述"行为"、"感受"、还是"期望"？（三种需要区分编码）
3. 这是用户自发说的，还是被问题引导出的？（引导式回答降低 confidence）
4. 这句话的情绪极性（Positive/Negative/Neutral）是否明确？（混合情绪单独标注）
5. 这个 signal 有多少"同类"已经出现过？（判断 anecdote vs signal 的阈值）

### 编码分类体系（初始标签集）

可以从以下维度打标签，之后聚类时用于归并：

**功能域标签（按需定义）**
- #onboarding #navigation #search #collaboration #export #notification #pricing

**体验层标签**
- #cognitive-load #learnability #speed #reliability #trust #delight

**动机层标签**
- #efficiency #control #status #safety #belonging #creativity

**问题类型标签**
- #bug #missing-feature #ux-confusion #value-unclear #too-complex #too-simple

### Signal 极性判断规则

| 极性 | 判断依据 | 示例 |
|-----|---------|------|
| Positive | 用户表达满意 / 赞扬 / 主动推荐 | "love the new dashboard" |
| Negative | 用户表达失望 / 抱怨 / 放弃 | "gave up after 10 minutes" |
| Neutral | 描述性陈述，无明显情绪 | "I use it every Monday morning" |
| Mixed | 同一句话含两种极性 | "powerful but hard to learn" → 拆成两条 |

---

## Stage 3

### 题库

1. 这两个 signals 说的是同一件事，还是相关但本质不同的事？（聚类边界判断）
2. 这个 cluster 里最能代表"核心痛点"的一句话是哪句？
3. 有没有哪个 signal 放进任何 cluster 都不太合适？（游离 signal 可能是新兴主题）
4. Cluster A 和 Cluster B 有没有更深的共同点？（可以向上合并为 super-theme）
5. 同一个 theme 在不同用户群体中是否有差异？（Power user vs New user 对同一问题的反应往往不同）

### User Archetype 发现方法

跨多个 themes 观察用户行为模式，尝试识别 2–4 个 Archetypes：

```
Archetype: The Efficiency Seeker
Signals: complains about speed ×6, asks for keyboard shortcuts ×3, skips tutorials ×4
Mental model: already knows what they want; product should stay out of the way
Representative quote: "just let me do my job"

Archetype: The Careful Beginner
Signals: confused by options ×8, asks for help ×5, appreciates templates ×4
Mental model: fears making mistakes; needs guardrails and clear first step
Representative quote: "I didn't know if I was doing it right"
```

**常见 Archetype 原型（参考，不要强行套用）**
- Explorer：喜欢发现新功能，高容错
- Efficiency Seeker：目标导向，厌恶摩擦
- Careful Beginner：低置信度，需要引导
- Expert / Power User：定制需求高，不需要解释
- Delegator：把任务分配给别人，关注结果而非过程

### Cluster 合并 vs 拆分判断树

```
同一个 theme 内的 signals 是否有共同的根因？
  ├─ 是 → 保持合并
  └─ 否 → 考虑拆分为子 theme

两个 theme 是否都是同一个更深问题的表现？
  ├─ 是 → 向上合并为 super-theme，两个保留为 sub-theme
  └─ 否 → 保持独立
```

---

## Stage 4

### 题库

1. 这个 observation 的背后，用户有什么"未被满足的假设"？（mental model gap）
2. 用户这样做 / 说，是因为工具的问题，还是流程的问题，还是认知的问题？
3. 如果把这个 pattern 去掉，用户的哪个核心任务会受影响？
4. 这个 insight 对 Power User 和 New User 的含义一样吗？如果不一样，分开写。
5. 有没有一个更简单的解释可以覆盖同样的 observation？（奥卡姆剃刀检验）

### Insight 推导模板

从 observation 到 insight 的三步推导：

```
Step 1 — What (Observation)
用户频繁放弃 onboarding 流程，在第 3 步退出。

Step 2 — Why (Mechanism / Mental Model)
用户在第 3 步遇到需要连接外部账户的操作，这打断了他们的"快速试用"心理模型。
他们来的目的是"先看看能不能用"，不是"立刻完成所有设置"。

Step 3 — So What (Implication)
产品把"完整激活"和"初次体验价值"绑定在一起了，
但用户需要先感受到价值，才愿意付出连接账户的成本。
```

### 动机层级模型（Motivation Ladder）

```
表面需求（Surface Want）
    ↓ "为什么想要这个？"
功能性需求（Functional Need）
    ↓ "完成这个之后，你要用它做什么？"
情感性需求（Emotional Need）
    ↓ "这让你感觉怎么样？"
社会性需求（Social / Identity Need）
    ↓ "这件事对你'是什么样的人'有什么意义？"
核心动机（Core Motivation）
```

示例：
```
Surface:    "我想要导出功能"
Functional: "我需要把数据交给我的老板"
Emotional:  "我需要证明我的工作成果"
Social:     "我需要在团队里被看见 / 被信任"
Core:       Visibility + Recognition
```

---

## Stage 5

### 题库

1. 这个机会目前有没有人在解决？用户现在的 workaround 是什么？它的天花板在哪里？
2. 如果我们什么都不做，用户会怎么办？他们会离开，还是凑合？
3. 这个机会解决了 Power User 的问题，还是 New User 的问题？两类用户的优先级是什么？
4. 解决这个机会需要的最小投入是多少？有没有 Quick Win（低成本高频痛点）？
5. 这个机会如果解决了，会不会伤害其他用户？（误伤 / 增加复杂度 / 影响其他 Archetype）

### Opportunity Scoring 完整计算

| Opportunity | Frequency (1–5) | Pain (1–5) | Solution Gap (1–5) | Strategic Fit (1–5) | Total |
|-------------|----------------|------------|--------------------|---------------------|-------|
| Example: Onboarding clarity | 4 | 5 | 4 | 3 | 16 |
| Example: Export options | 3 | 3 | 2 | 4 | 12 |

分级参考：
- 17–20：Must address（核心瓶颈）
- 13–16：High priority
- 9–12：Consider next quarter
- ≤8：Monitor / Low priority

### Quick Win vs Strategic Bet 判断

```
Quick Win = High Pain + Low effort + Already understood
Strategic Bet = High frequency + Unclear solution + Needs discovery
```

---

## Appendix

### Thematic Analysis 简介（给 AI 执行参考）

Thematic Analysis（主题分析）是社会科学中从定性数据中提取模式的标准方法，由 Braun & Clarke (2006) 系统化。核心步骤：

1. **Familiarization**：沉浸数据，建立整体感（= Stage 1–2）
2. **Generating initial codes**：给每个有意义的片段打标签（= Stage 2 signal extraction）
3. **Searching for themes**：把 codes 聚合为候选主题（= Stage 3 clustering）
4. **Reviewing themes**：检查主题是否有内聚性 + 主题间是否有区分度（= Stage 3 QA）
5. **Defining and naming themes**：给主题命名，写 theme definition（= Stage 3 output）
6. **Producing the report**：写出有论点、有证据的分析（= Stage 4–5 + Report）

### 反确认偏误检查清单

在输出 Report 之前，检查以下项目：

- [ ] 是否有任何 insight 没有 contradicting signal 或 minority view？
- [ ] 最强的 insight 对应的 evidence 是否来自多个渠道？
- [ ] 是否有 data gaps 被明确标注（而不是被忽略）？
- [ ] User Archetypes 是否覆盖了不同的用户群体（不只有理想用户）？
- [ ] Opportunity scoring 是否区分了"高频低痛"和"低频高痛"？
