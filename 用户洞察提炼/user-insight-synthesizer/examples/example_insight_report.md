# Worked Example — User Insight Synthesizer（节选）

> 从原始用户声音走到有证据的 insight 的示例。数据：25 场访谈 + 40 条工单 + 15 条应用商店评价，主题为"会议协作工具"。演示 signal 编码、聚类、observation→insight 分层、少数声音。示例数据为演示用途。

---

## 1. Data Inventory

| Source Type | Sample Size | User Type | Time Range | Known Biases |
|-------------|-------------|-----------|------------|--------------|
| 用户访谈 | 25 | 活跃组织者为主 | 2026-05~06 | CS 招募，偏重度用户 |
| 工单 | 40 | 混合 | 2026-Q2 | 只有遇到问题的人发声 |
| 应用商店评价 | 15 | 混合 | 2026-Q2 | 情绪强、细节少 |

**质量提示**: 沉默的轻度用户缺席，"忘记同步"类痛点可能被高估，需补充满意用户访谈。

---

## 2. Signal Extraction（节选）

```
[interview_04 | Neg] "开完会经常忘了发结论" → #sync #forgetfulness
[ticket_112   | Neg] "摘要漏了最重要的决策"   → #summary-quality #recall
[review_007   | Pos] "一键发频道太方便了"     → #sync #ease
[interview_11 | Neg] "手动复制粘贴要好几分钟" → #sync #effort
```

---

## 3. Pattern Clustering（节选）

```
Theme: 会后同步的遗漏与成本
Signal count: 19 (interview ×11, ticket ×5, review ×3)
Representative quotes:
  - "开完会经常忘了发结论" (interview_04)
  - "手动复制粘贴要好几分钟" (interview_11)
Contradicting signals: 2 ("我们有固定纪要人，不存在这问题" — 大团队, interview_18)
```

**Archetype 发现**:
- The Overloaded Organizer：一天多场会，记性是瓶颈，要"别让我记着这事"。
- The Structured Team：已有专职纪要，痛点在质量不在遗漏。

---

## 6. Key Insights（核心）

### Insight 1: "忘记同步"不是记性问题，是流程缺省问题
- **Observation**: 19/40 来源提到会后没把结论发出去。
- **Insight**: 用户不是懒或健忘——是"同步"这一步依赖人主动发起且跨工具，任何高频场景下都会规律性掉链子。这是流程缺省，不是个人失误。
- **Implication**: 应把同步从"人记得做"变成"系统默认发生"。
- **Evidence**: `Evidence: 11/25 interviews, 5 tickets, 3 reviews`
- **Confidence**: High —（跨三渠道复现，机制一致）
- **Minority view**: 2 个有专职纪要人的大团队不受此困，说明该 insight 主要适用于中小无专人团队。

### Insight 2: 摘要质量的痛点集中在"决策召回"，不在文采
- **Observation**: 工单里的质量抱怨，8/12 是"漏了决策/待办"，而非"写得不好"。
- **Insight**: 用户对摘要的价值判断是"有没有抓住该记的事"，不是语言流畅度。
- **Implication**: 摘要优化优先做决策/待办的召回，而非润色。
- **Evidence**: `Evidence: 8/12 quality tickets`
- **Confidence**: Medium —（单渠道为主，样本偏小）

---

## 8. Opportunity Signals（节选）

| Rank | Opportunity | F | P | SG | SF | Total | Type |
|------|-------------|---|---|----|----|-------|------|
| 1 | 会后结论自动/一键触达 | 5 | 4 | 4 | 4 | 17 | Strategic Bet |
| 2 | 决策/待办高亮召回 | 3 | 4 | 3 | 3 | 13 | Quick Win |

---

## 9. Minority Views & Contradicting Signals

| Finding | Majority | Minority | n | 可能解释 |
|---------|----------|----------|---|----------|
| 同步是普遍痛点 | 中小无专人团队普遍痛 | 有专职纪要的大团队不痛 | 2 | 团队规模与角色分工不同 |

---

## 10. Data Gaps

- 缺满意/轻度用户视角，"遗漏"痛点强度可能被高估 → 建议补 5 场满意用户访谈。
