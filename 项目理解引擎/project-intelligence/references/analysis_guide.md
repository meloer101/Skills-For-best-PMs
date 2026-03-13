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

Useful commands:
```bash
# Find where a route is defined
grep -r "POST /api/posts" .

# Find all callers of a function
grep -r "feedService" src/

# Find the most-imported files
grep -rh "from './" src/ | sort | uniq -c | sort -rn | head -20
```

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
