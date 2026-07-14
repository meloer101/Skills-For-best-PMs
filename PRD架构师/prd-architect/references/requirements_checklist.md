# Requirements Checklist

输出 PRD 前逐条过一遍。任一项不满足，回到对应 Stage 补齐或写入 Open Questions。

## Completeness（完整性）

- [ ] Problem statement 清晰且以用户为中心。
- [ ] Target user segment 已定义（角色 + 规模 + 频率）。
- [ ] **Non-goals 已明确**（本次不做什么 + 为什么）。
- [ ] User stories 存在且能映射到功能需求。
- [ ] 每条功能需求可测试，且挂有 **Acceptance Criteria（Given/When/Then）**。
- [ ] Edge cases 按 8 类边界框架扫描过，每条有预期行为。
- [ ] NFR 含可度量阈值（有数字，无"快/稳/友好"这类形容词）。
- [ ] **Dependencies & Risks 已列出**并指派 Owner。
- [ ] **Rollout Plan 含灰度阶段与回滚触发条件**。
- [ ] Success metrics 有目标值、时限、数据来源。
- [ ] **Open Questions 显式列出**（不假装已解决）。

## Consistency（一致性）

- [ ] Goals 与 Success metrics 对齐。
- [ ] 每条功能需求都能追溯到某条 User story。
- [ ] Edge cases 不与核心行为矛盾。
- [ ] NFR 不与功能需求冲突。
- [ ] Non-goals 不与 Goals / Scope 自相矛盾。

## Testability（可测试性）— 抽查每条 FR

- [ ] 需求里没有不可验证的形容词（快、友好、稳定、直观、高效）。
- [ ] 每条需求都能写成一个通过/失败明确的测试。
- [ ] 阈值型需求都带具体数字 + 度量方式。

## Evidence & Confidence（证据与置信度）

- [ ] 关键判断都标了 `Evidence:` 或 `Assumption:`。
- [ ] 所有 `Assumption:` 汇总进了 Assumptions Log。
- [ ] Success metrics 每条标了 Confidence（L/M/H）。
