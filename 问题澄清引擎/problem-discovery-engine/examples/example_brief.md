# Worked Example — Problem Discovery Engine

> 从一个模糊想法走到结构化 Brief 的示例。起点：「我们想做一个 AI 会议摘要功能」。演示如何 freeze solution、追根因、产出可验证假设。示例数据为演示用途。

---

## 对话起点（用户给的想法 + solution）

> "会议太多记不住，我们想做一个 AI 自动生成会议摘要的功能。"

**Skill 的第一步反应**：这是 solution-first。把"AI 摘要"记为候选干预手段（不是需求本身），转而澄清问题。

---

## Problem Discovery Brief

### Problem Statement
- One-liner: 会议结束后，关键决策与待办没有可靠地传达给需要的人，导致重复确认和执行延迟。
- Evidence: `Evidence: 9/12 interviews, 23 support tickets`

### Target User
- Primary user: 8–30 人产品/研发团队的会议组织者，周均开会 5+ 次。
- Secondary: 未参会但需要知道结论的团队成员。
- Evidence: `Evidence: 12 interviews (2026-06)`

### User Situation
- Context: 会议密集，一天多场，组织者身兼记录。
- Trigger: 会议结束，需要把结论同步出去。
- Goal: 让该知道的人第一时间知道决策和待办。
- Constraints: 时间紧、经常忘、跨工具（会议工具 ↔ IM）。
- Evidence: `Evidence: 7/12 interviews`

### Job To Be Done (JTBD)
```
When 一场会议刚结束
I want to 让关键决策和待办可靠地到达相关的人
So I can 不用反复口头确认、执行不掉链子
```
- 注：用户要的不是"摘要"这个动作，而是"结论可靠触达"这个结果。
- Success criteria: 相关成员在会后短时间内看到结论；减少"这事儿定了吗"的重复询问。

### Current Solutions
- 手动记录 + 复制粘贴到 IM 频道；有人用录音转写工具。
- 为什么仍在用：没有更省事的替代，切换成本低但结果不可靠。
- Evidence: `Evidence: 5/12 interviews`

### Pain Points
- P1: 忘记同步（最高频）。
- P2: 手动搬运耗时 3–5 分钟。
- P3: 摘要质量参差，遗漏关键决策。
- Prioritization rationale: 频率(P1) × 严重度(P3) — P1 最普遍，P3 最伤信任。

### Root Causes（Five Whys 节选）
- RC1（机制）: Because 记录与同步是纯手工且依赖组织者记性，therefore 高频会议下必然遗漏。
- RC2（机制）: Because 结论散落在会议工具里、不主动推送，therefore 相关成员要主动找才看得到。
- Non-causes: "摘要不够智能" 更像症状而非根因——即使摘要完美，不主动触达仍然会漏。

### Opportunity Areas
- OA1: 降低"同步"这一步的成本/遗漏（自动或一键触达）。
- OA2: 把结论从"拉取"变成"推送"。
- OA3: 提升摘要对关键决策的召回。

### Product Hypotheses
- H1: If we 在会议结束时一键把结论推送到团队频道 for 会议组织者 in 高频会议场景, then 会后 30 分钟内相关成员触达率显著提升, because RC1+RC2（手工遗漏 + 非推送）。
- H2: If we 自动高亮"决策/待办"两类信息, then 关键遗漏下降, because RC 摘要召回不足。

### Validation Plan
- H1: concierge 测试——手动帮 5 个团队做一周"一键同步"，测触达率与省时；成功阈值：触达率 ≥ 70% 且组织者愿意继续用。
- H2: 对比"高亮版 vs 纯文本"摘要的关键决策召回。

### Open Questions
- Q1: "触达"如何度量？看频道已读还是详情页打开？
- Q2: 高频日会会不会造成频道刷屏？（可能引入频率控制）

---

## Hypothesis Ledger（节选）

| ID | Hypothesis | Type | Evidence | Confidence | Fastest test | Success threshold | Next step |
|----|-----------|------|----------|-----------|--------------|-------------------|-----------|
| H1 | 一键推送结论提升触达 | Desirability | 9/12 访谈提"忘记同步" | M | concierge 1 周 | 触达≥70% | 招募 5 团队 |
| H2 | 决策/待办高亮降低遗漏 | Feasibility | 3 访谈提"漏结论" | L | 摘要 A/B | 召回+20% | 取历史会议样本 |
