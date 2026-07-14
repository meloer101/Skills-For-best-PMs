# Worked Example — Project Intelligence（节选）

> 一个小型社交后端 repo 的报告节选，演示 Core Modules 的证据写法、一条 Flow、以及 Impact Analysis / System Evolution。数字均来自实际 grep / git 命令（演示值），体现"Verify before you quantify"。

**Repo**: `mini-social-api`（Node.js + Express + Prisma + Postgres，约 8,000 行）

---

## 1. System Overview

一个社交内容后端：用户发帖、关注他人、收到个性化 feed。核心价值是在用户打开 app 的瞬间，把最相关的内容排到最前。

---

## 3. Core Modules（节选）

### `feedService.ts`
- **Role**: Orchestrator
- **Why core**（证据可复现）:
  - Called by 7 files — `grep -rn "feedService" src/ | grep import` → 7 处
  - Calls 5 downstream modules（postRepo, followRepo, rankingEngine, blocklist, cache）
  - 含主要业务逻辑：feed 聚合 + ranking + 过滤 blocked users
- **Summary**: 几乎所有与"看 feed"相关的请求最终都流经这个文件——它是 feed 系统的调度中枢。

### `authMiddleware.ts`
- **Role**: Gatekeeper
- **Why core**:
  - 在大多数受保护路由前执行 — `grep -rn "authMiddleware" src/routes/` → 挂在 12 条路由
  - 含 token 校验 + 权限判定
- **Summary**: 系统的门卫，决定谁能访问什么。

---

## 4. Key Request Flow（节选）：Load Feed

| Step | Component | What it does |
|------|-----------|--------------|
| 1 | `GET /api/feed` | 客户端请求个性化 feed |
| 2 | `authMiddleware.ts` | 校验 token，注入 userId |
| 3 | `feedController.ts` | 解析分页参数，调 feedService |
| 4 | `feedService.ts` | 聚合关注内容 + 热门，调 rankingEngine 排序，过滤 blocked |
| 5 | `rankingEngine.ts` | 按 recency/engagement/关系强度算 rankingScore |
| 6 | `prisma.post.findMany()` | 拉取帖子 |
| 7 | Response JSON | 返回排序后的 feed |

---

## 10. Impact Analysis（节选）

### If you modify: `feedService.ts`
- **Directly affected**: `feedController.ts`（feed 接口）、`profileController.ts`（个人页也复用了聚合逻辑）
- **Indirectly affected**: 首页 feed、个人主页、通知里的"你可能感兴趣"
- **Blast radius**: 🔥 Wide
- **Before changing**: 跑通 feed + profile 两条集成测试；改 ranking 相关逻辑需灰度观察停留时长。

### If you modify: `authMiddleware.ts`
- **Directly affected**: 挂载的 12 条路由（登录态相关全部）
- **Blast radius**: 🔥 Wide — 动一行可能影响所有受保护接口
- **Before changing**: 覆盖登录/越权/过期三类用例的测试全绿再合。

---

## 11. System Evolution（节选）

取数：`git log --pretty=format: --name-only | sort | uniq -c | sort -rn | head`

| File | 改动次数 | 推断 |
|------|---------|------|
| `feedService.ts` | 118 | 核心且仍在快速演化——feed 策略还在调，改动需谨慎 |
| `rankingEngine.ts` | 64 | 排序算法持续迭代，是产品竞争力所在 |
| `authMiddleware.ts` | 4 | 已稳定，改动多与安全相关，需重点评审 |

- **Active zone**: feed / ranking 子系统
- **Stable zone**: auth
- **Hotspot ∩ Complexity**: `rankingEngine.ts`（既高频改动又高复杂度）= 最危险区域，优先补测试。
