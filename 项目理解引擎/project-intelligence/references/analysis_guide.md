# Analysis Guide

Reference for Stage 1–3 of the Project Intelligence workflow.

---

## System Role Definitions

Assign one of these roles to each core module.

| Role | Description | Signals |
|------|-------------|---------|
| **Orchestrator** | Coordinates multiple services to fulfill a business operation | Calls 3+ downstream services; contains the main business flow logic |
| **Gatekeeper** | Controls access, validates identity, or enforces authorization | Runs before most requests; contains auth/permission checks |
| **Async Processor** | Handles background jobs, queues, or event-driven tasks | Uses queues, workers, cron, or message brokers; doesn't respond to HTTP directly |
| **Data Layer** | Manages database access and data transformation | Wraps ORM/query calls; used by services, not controllers |
| **API Gateway** | Routes and dispatches HTTP requests | Contains route definitions; minimal business logic |
| **Config / Bootstrap** | Initializes the application and wires dependencies | Loaded once at startup; registers middleware, DB connections, etc. |

---

## Signals for Core Module Identification

### High import count
If a file appears in `import` or `require` statements across many other files, it is likely foundational. Use grep or code search to count references.

### Dependency fan-out
If a file imports many other services or modules (fan-out), it is likely an orchestrator.

### Business logic density
Files containing conditionals, calculations, rules, or domain-specific decisions are business logic files — higher value than pure CRUD.

### Naming patterns that often indicate core files
- `*Service.ts` / `*service.py` — business logic
- `*Controller.ts` — request handling
- `*Middleware.ts` / `*middleware.py` — cross-cutting concerns
- `*Worker.ts` / `*Queue.ts` — async processing
- `*Repository.ts` / `*Store.ts` — data access
- `*Engine.ts` / `*Processor.ts` — complex domain computation

---

## Complexity Assessment Heuristics

Use these signals to assign complexity levels (🔥 High / 🟡 Medium / 🟢 Low):

**🔥 High Complexity — treat with caution**
- High cyclomatic complexity (many branches, nested conditions)
- Many incoming and outgoing dependencies
- Frequently modified in git history (if available)
- Contains financial, security, or ranking logic
- Long functions (200+ lines) without clear decomposition

**🟡 Medium Complexity — review before modifying**
- Moderate dependencies
- Some business logic mixed with infrastructure concerns
- Occasionally modified

**🟢 Low Complexity — safe to modify**
- Single responsibility, stateless
- Few or no dependencies on other business modules
- Pure utilities, UI components, config constants

---

## Request Flow Tracing Method

For each key user action:

1. **Identify the trigger** — what user action or event starts the flow?
2. **Find the entry point** — which route or handler receives it?
3. **Follow the call chain** — trace function calls through controllers → services → data layer
4. **Note side effects** — are there async jobs, events, or notifications triggered?
5. **Find the terminal state** — what is written to the database or returned to the client?

Useful commands（覆盖多语言 / 多导入风格，别只认相对导入）:
```bash
# Find where a route is defined
grep -rn "POST /api/posts" .

# Find all callers of a symbol
grep -rn "feedService" src/

# Most-imported files — JS/TS 相对导入 + alias 导入（@/、~/ 等）
grep -rhoE "from ['\"][@~.][^'\"]+['\"]" src/ | sort | uniq -c | sort -rn | head -20

# Python imports
grep -rhoE "^(from|import) [a-zA-Z0-9_.]+" --include=*.py . | sort | uniq -c | sort -rn | head -20

# Go imports
grep -rhoE "\"[a-zA-Z0-9_./-]+\"" --include=*.go . | sort | uniq -c | sort -rn | head -20

# 改动热点（System Evolution 用）
git log --pretty=format: --name-only | sort | uniq -c | sort -rn | head -20
```

> 若项目用 alias（`@/services/feed`）、绝对导入或 barrel file（`index.ts` re-export），单一 grep 会漏。跨几种模式各跑一遍再合并判断。

---

## Anti-Hallucination Rule（防幻觉，强制）

这类报告最常见的失败模式是**编造精确数字**——声称 "Called by 7 files" 而其实没数过。

- 写「Called by N files」「Calls M downstream modules」这类**具体数字前，必须实际跑一次 grep 计数**，用命令输出作为依据。
- 没核实的量化断言，**标为 estimate**（如 "~high fan-in, not counted"）而不是给一个假装精确的数字。
- 引用某个文件/函数/字段前，确认它真实存在（打开过或搜到过），不要凭命名惯例推测存在。
- Core Module 的每条 "Why core" 证据，都要能对应到一条可复现的命令或一处代码位置。

---

## 大代码库降级策略（Large Codebase Fallback）

当代码库过大（如 >10 万行 / >2000 文件）无法通读时，显式降级而不是假装读完：

1. **优先级采样**：只深挖 entry points → routing → 高 fan-in 的 top 10–15 文件 → 核心数据模型；其余按目录级摘要。
2. **声明覆盖范围**：报告开头写明"本次深度分析覆盖 X（模块/目录），未覆盖 Y"，不让读者误以为全库通读。
3. **按业务域切**：若是 monorepo，选 1–2 个最相关的 package/service 深入，其余列清单。
4. **宁可少而准**：Complexity Map 和 Core Modules 只列有证据支撑的，不为凑数硬填。

---

## Business Scenario Writing Guide

A good scenario narrative answers:
1. **Who** does what (user action)?
2. **What happens** at each layer (technical path, simplified)?
3. **Where** does the key logic live (the important file)?
4. **What is the outcome** (what the user sees or what changes in the system)?

Keep scenarios at the level of "smart non-technical stakeholder" — someone who understands software but doesn't read code daily.

**Good example:**
> When a user taps "Follow", the app sends a `POST /follows` request. `followService.ts` checks the follow limits and creates the relationship in the database. A background job then queues a notification for the followed user, which `notificationWorker.ts` delivers asynchronously.

**Bad example (too technical):**
> `followController.ts` calls `followService.createFollow(followerId, followeeId)` which calls `prisma.follow.create({data: {followerId, followeeId}})` and returns the created record.

---

## Data Model Analysis Checklist

For each data model, answer:
- [ ] What real-world thing does this model represent?
- [ ] What is the product significance? (Is this a core entity or a supporting table?)
- [ ] What are the cardinality relationships to other models?
- [ ] Are there any non-obvious fields that encode business rules? (e.g., `status` enum, `rankingScore`, `isArchived`)
- [ ] Is this model frequently read, written, or both? (informs caching and indexing decisions)

---

## Domain Concept Identification

Look for variables and fields that represent business decisions rather than technical mechanics:

- **Computed scores** — `rankingScore`, `engagementRate`, `riskScore`
- **Status enums** — `PostStatus.DRAFT / PUBLISHED / ARCHIVED`
- **Thresholds** — `MAX_FOLLOW_COUNT`, `FEED_PAGE_SIZE`
- **Flags** — `isVerified`, `isShadowBanned`, `requiresApproval`
- **Derived states** — `isFollowing`, `hasUnreadNotifications`

For each, explain the product intent behind it — not just what the variable holds, but *why it exists* and *what decision it drives*.
