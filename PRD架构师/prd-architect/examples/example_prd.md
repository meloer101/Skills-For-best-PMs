# Worked Example — PRD Architect

> 这是一份走完整模板的示例 PRD，供参照「填到什么颗粒度算合格」。功能：**会议摘要一键同步到团队频道**。示例数据为演示用途。

---

## Feature Overview

- **Feature name**: 会议摘要一键同步（Meeting Summary → Channel Sync）
- **Owner**: PM - Lin
- **Date**: 2026-07-13
- **Status**: In Review
- **Related docs**: Prioritized Roadmap #1 项、Problem Discovery Brief（2026-06）

---

## 1. Problem Statement

- **Problem**: 会议结束后，摘要停留在会议工具里，团队成员要主动去找才看得到，导致关键决策同步延迟。
- **Target user**: 8–30 人的产品/研发团队里的会议组织者，周均开会 5+ 次。
- **Current behavior / workaround**: 组织者手动复制摘要，粘到 Slack/飞书频道，平均耗时 3–5 分钟，且经常忘记。
- **Evidence**: 12 场用户访谈中 9 人提到"忘记同步"；工单里 23 条相关反馈。`Evidence: 9/12 interviews, 23 tickets`

---

## 2. Goals & Non-goals

**Goals**
- User goal: 会议一结束，摘要自动/一键出现在团队频道，无需手动搬运。
- Business goal: 提升协作类功能周活（retention），目标 +8%。

**Non-goals（本次明确不做）**
- NG1: 不做摘要内容的 AI 重写/润色——沿用现有摘要引擎，避免范围扩大到 NLP 质量优化。
- NG2: 不支持同步到邮件/第三方 Webhook——首版只做 Slack + 飞书两个频道类型，其余下季度评估。

**Scope 边界**
- In scope: 会议结束触发、目标频道选择、一键同步、同步状态回显。
- Out of scope: 摘要编辑、历史摘要批量补同步、跨工作区同步。

---

## 3. User Stories

- **US1** — As a 会议组织者, I want to 在会议结束时一键把摘要发到指定频道, so that 团队无需我手动搬运就能第一时间看到决策。
- **US2** — As a 团队成员, I want to 在频道里直接看到结构化摘要, so that 我不必进会议工具翻找。

---

## 4. Functional Requirements

### FR1: 会议结束后触发同步入口
- **Requirement**: The system **shall** 在会议结束且摘要生成完成后，向组织者展示"同步到频道"入口。
- **Priority**: Must
- **Traces to**: US1
- **Acceptance Criteria**:
  - Given 摘要已生成, When 会议结束, Then 5 秒内在会议结束页展示"同步到频道"按钮。
  - Given 摘要尚未生成完成, When 会议结束, Then 按钮置为 loading 态并提示"摘要生成中"。
- **Evidence**: 现有摘要引擎平均 8s 出结果 `Evidence: analytics 2026-06`

### FR2: 目标频道选择与同步
- **Requirement**: The system **shall** 允许组织者选择 1 个已授权频道并将结构化摘要发送过去。
- **Priority**: Must
- **Traces to**: US1, US2
- **Acceptance Criteria**:
  - Given 组织者已授权至少 1 个频道, When 点击同步并选中频道, Then 摘要在 3 秒内出现在该频道且按钮变为"已同步"。
  - Given 未授权任何频道, When 点击同步, Then 引导完成频道授权后再同步。

---

## 5. Edge Cases

| # | 类别 | 场景 | 预期行为 |
|---|------|------|----------|
| 1 | 服务失败 | 频道 API 返回超时 | 同步失败态 + "重试"，本地保留摘要，不丢失 |
| 2 | 幂等/重试 | 组织者连点两次同步 | 幂等键去重，频道内只出现 1 条 |
| 3 | 权限 | 频道授权已过期 | 提示重新授权，不静默失败 |
| 4 | 空状态 | 摘要为空（会议过短） | 隐藏同步入口并提示"本次会议无可同步摘要" |

---

## 6. Non-Functional Requirements

| # | 维度 | 需求（含阈值） | 度量方式 |
|---|------|----------------|----------|
| NFR1 | Performance | 同步请求 p95 < 3s | APM |
| NFR2 | Reliability | 同步成功率 ≥ 99%，失败可重试 | 频道 API 监控 |
| NFR3 | Privacy | 摘要仅发送到用户显式选择的频道，不缓存到第三方 | 安全评审 |

---

## 7. Dependencies & Risks

| 类型 | 项 | 影响 | 应对 / Owner |
|------|----|------|--------------|
| Dependency | Slack/飞书 OAuth 授权模块 | 无授权无法同步 | 复用现有 IM 集成，Owner: 平台组 |
| Risk | 摘要引擎延迟波动 | 触发入口 loading 过久 | 超过 15s 降级为"稍后手动同步"，Owner: Lin |

---

## 8. Rollout Plan

- **Rollout 方式**: feature flag 灰度
- **灰度阶段与门槛**: 内部 dogfood → 5% 团队（监控同步成功率 & 周活）→ 50% → 100%
- **回滚触发条件**: 同步成功率 < 95% 或引发频道刷屏投诉
- **Kill switch**: 有

---

## 9. Success Metrics

| 指标 | 定义 | 目标值 & 时限 | 数据来源 | Confidence |
|------|------|---------------|----------|------------|
| 同步采用率 | 会议中使用同步的比例 | 上线 4 周内 ≥ 40% | 埋点 | M |
| 协作功能周活 | 相关功能 WAU | +8%（8 周） | 数仓 | L |
| 手动搬运耗时 | 组织者自评省时 | 从 3–5min 降到 <30s | 用户调研 | M |

---

## 10. Open Questions

- **Q1**: 是否允许同步到多个频道？（需产品负责人 2026-07-20 前决策）
- **Q2**: 摘要在频道内是否可点开进入原会议？依赖会议深链能力，待平台组确认。

---

## 11. Assumptions Log

| # | 假设 | 若为假的影响 | 如何验证 |
|---|------|--------------|----------|
| A1 | 多数团队已授权至少 1 个 IM 频道 | 授权环节成大漏斗 | 查现有 IM 集成授权率 |
| A2 | 摘要引擎 15s 内出结果 | 触发入口体验差 | 拉 P95 延迟分布 |
