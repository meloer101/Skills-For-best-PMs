# Worked Example — Resume Narrative Engine

> 从项目代码 + JD 到 PM 简历 bullets 的示例。重点演示**「工程 bullet → PM bullet」的 before/after 改写**，以及不编造指标的 counterfactual framing。示例数据为演示用途。

**输入**：一个个人项目 `mini-social-api`（Node/Express/Prisma 社交后端） + 目标 JD「AI 产品经理（增长方向），关注用户留存与数据驱动」。

---

## 1. Mapping Summary

### Ideal PM Persona（from JD）
- 优先级 1：数据驱动 / 关注留存指标
- 优先级 2：理解 AI/系统能力边界
- 优先级 3：0→1 产品定义

### Narrative Choice
- Primary：**Narrative A — 0→1 Builder**（个人项目全栈自建，产品定义信号强）
- Secondary：System Thinker（feed/ranking 架构，穿插 1 条）

### Top Signals
| 信号 | Evidence | JD 匹配 | 强度 |
|------|----------|---------|------|
| 定义了 feed 产品模型与排序逻辑 | `rankingEngine.ts` | 留存/数据驱动 | Strong |
| 设计了 User/Post/Follow 数据模型 | `schema.prisma` | 0→1 定义 | Strong |
| 关注度指标驱动排序 | `engagementRate` 字段 | 数据驱动 | Medium |

### Claim Map
| Claim | Evidence | PM Framing | JD match |
|-------|----------|-----------|----------|
| 设计了个性化 feed 排序 | rankingEngine.ts | 定义了以留存为目标的内容分发策略 | 留存 |
| 自建关注/内容数据模型 | schema.prisma | 0→1 定义社交产品数据骨架 | 0→1 |

### Gaps
- 无真实用户/指标（个人项目）→ 用 capability framing，不编数字。

---

## 2. Resume Bullets：工程 → PM 改写（Before / After）

### Bullet 1
- ❌ **工程写法**："用 Node.js + Express 实现了帖子的 CRUD 接口和 Prisma 数据库操作。"
  - 问题：只讲了做了什么技术活，没有决策、用户、产品价值。
- ✅ **PM 写法**："定义了社交产品的核心数据模型（User/Post/Follow）与内容分发结构，为个性化 feed 的可扩展流转打下基础。"
  - 好在哪：从"写了 CRUD"上升到"定义产品数据骨架"，对应 JD 的 0→1 定义。

### Bullet 2
- ❌ **工程写法**："写了一个 rankingEngine，根据点赞数和时间给帖子算分排序。"
- ✅ **PM 写法**："设计了以用户停留为目标的 feed 排序策略，综合内容新近度、互动率与关系强度，定义了 `rankingScore` 的产品含义与权重取舍。"
  - 好在哪：把变量 `rankingScore` 翻译成产品概念，体现数据驱动 + 取舍思维（对应 JD 优先级 1）。

### Bullet 3（counterfactual framing，无指标场景）
- ❌ **编造指标**："通过优化排序算法将用户停留时长提升了 30%。"（个人项目无此数据，属编造，禁止）
- ✅ **capability framing**："设计的排序与数据结构可支撑高频内容更新场景下的个性化分发，为后续 A/B 实验与留存优化预留了度量位。"
  - 好在哪：描述系统"能支撑什么"而非虚构"提升了多少"，诚实且仍显 PM 视角。

---

## 3. Missing Signals（Gap 诊断）

| Gap | 为什么重要 | 建议补充 |
|-----|-----------|----------|
| 无真实用户与留存数据 | JD 强调数据驱动，纯 capability 说服力有限 | 若做过小范围试用，补真实使用反馈/留存 |
| 无 A/B 实验经历 | 增长 PM 常考实验设计 | 可补一个哪怕是设计层面的实验方案 |

---

## 4. Assumptions

- A1：该项目为个人/作品集项目（toy/portfolio 定位），故全程用 capability framing，未使用任何数字化成果。
