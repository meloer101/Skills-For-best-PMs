# Worked Example — Feature Prioritization Engine

> 从 6 个候选功能到透明排序的示例。演示：继承上游 Opportunity、统一打分、trade-off、组合视角。承接前面 User Insight Report 的机会项。示例数据为演示用途。

---

## Stage 1 — Feature Intake（含上游继承）

上游 `User Insight Report` 已给出 Opportunity Areas，直接作为候选项与初始证据：

| # | Feature | Target user | Problem | 上游 Evidence |
|---|---------|-------------|---------|---------------|
| A | 会后结论一键同步 | 会议组织者 | 忘记/费力同步 | Insight #1, Opp#1 (17/20) |
| B | 决策/待办高亮召回 | 全体成员 | 摘要漏关键决策 | Insight #2, Opp#2 (13/20) |
| C | 同步频率控制（防刷屏） | 高频会议团队 | 日会刷屏 | 6 工单（少数声音） |
| D | 摘要多语言 | 跨国团队 | 语言障碍 | 3 访谈 |
| E | 摘要导出 PDF | 组织者 | 存档需求 | 2 工单 |
| F | 会议工具深链 | 全体成员 | 想回看原会议 | Open Question |

---

## Stage 2 — Evaluation Criteria

- 本季度策略焦点：**协作留存**。
- 权重（sum=1.0）：User Value 0.3 / Business Impact 0.25 / Strategic Alignment 0.25 / Effort 0.1 / Risk(penalty) 0.1。
- 框架：加权评分为主，Effort 用反向分（分越高越省力）。

---

## Stage 3 — Scoring（节选，1–5 分）

| Feature | UV | BI | SA | Effort | Risk | 加权分 | Confidence | Rationale |
|---------|----|----|----|--------|------|--------|-----------|-----------|
| A 一键同步 | 5 | 4 | 5 | 2 | 3 | **3.75** | M | 高频高痛，直击留存；但依赖 IM 授权，工程量中 |
| B 决策高亮 | 4 | 3 | 3 | 4 | 2 | **3.30** | M | 痛点明确，改摘要引擎即可，成本低 |
| C 频率控制 | 3 | 2 | 3 | 4 | 2 | **2.80** | L | 仅高频团队，样本小；是 A 的配套 |
| D 多语言 | 3 | 3 | 2 | 2 | 3 | **2.55** | L | 证据弱，非本季策略 |
| E 导出 PDF | 2 | 2 | 2 | 5 | 1 | **2.35** | M | 低频需求，但极省力 |
| F 深链 | 3 | 2 | 3 | 3 | 2 | **2.70** | L | 依赖不明，先归入 Open Question |

> 每个分都有 rationale；证据弱的项 Confidence 标 Low，不因分数接近就假装确定。

---

## Stage 4 — Trade-off Analysis

- **Quick wins**（高价值低成本）: B 决策高亮、E 导出。
- **Strategic bet**（高价值高成本）: A 一键同步。
- **配套项**: C 频率控制（依附于 A，A 不上则不单独做）。
- **Defer**: D 多语言、F 深链（证据/依赖不足）。

**Top 3 trade-offs**:
1. A 分最高但工程量最大——先做还是先用 B 快速见效？→ 建议 A 立项同时 B 并行（B 快，先给用户价值）。
2. C 依赖 A，单独做无意义——绑定 A 的灰度阶段一起评估。
3. E 极省力但价值低——放进"边角料 sprint"填空，不占主线。

---

## Stage 5 — Portfolio View

组合（避免全押一个方向）：
- 1 Strategic bet：A 一键同步
- 1 Quick win：B 决策高亮
- 1 低成本填充：E 导出 PDF
- Defer：D、F；C 随 A

> 注：组合比例是引导性的，按团队容量与依赖调整，不是固定配方。此处因 A 依赖 IM 授权模块，先与平台组确认排期再定灰度。

---

## Stage 6 — Recommendation（Roadmap 节选）

| Rank | Feature | 分 | Key driver | Main risk | Next validation |
|------|---------|----|-----------|-----------|-----------------|
| 1 | A 一键同步 | 3.75 | 直击留存、高频高痛 | IM 授权漏斗 | 查现有授权率 + concierge |
| 2 | B 决策高亮 | 3.30 | 低成本、痛点明确 | 召回提升幅度未知 | 摘要 A/B 测召回 |
| 3 | E 导出 PDF | 2.35 | 极省力 | 价值有限 | 观察需求量再定 |

**Now（本季）**: A + B 并行。**Next**: C（若 A 验证成功）、F（待深链能力）。**Later**: D。
