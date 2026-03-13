# Project Intelligence Report
# [Project Name]

---

## 1. System Overview

> One paragraph. What does this system do? Who uses it? What problem does it solve?

[Example]
A social content platform where users publish posts, follow other users, and receive a personalized feed. Built for consumer mobile use. Core value: surfacing the most relevant content for each user at the moment they open the app.

---

## 2. System Architecture

**Tech Stack**
- Language / Runtime: [e.g., TypeScript / Node.js]
- Framework: [e.g., Express, NestJS, Django]
- Database: [e.g., PostgreSQL, MongoDB, Redis]
- Infrastructure: [e.g., Docker, AWS, Vercel]

**Architectural Pattern**
[e.g., MVC monolith / Microservices / Event-driven / Layered]

**Layer Diagram**

```
[User Request]
     ↓
[Frontend — React]
     ↓
[API Layer — Express]
     ↓
[Service Layer]
     ↓
[Database — Postgres]
```

---

## 3. Core Modules

> Modules that are imported by many files, orchestrate business logic, or control critical paths.

### [Module: filename.ts]
- **Role**: Orchestrator / Gatekeeper / Async Processor / Data Layer / API Gateway
- **Why core**:
  - Called by N files
  - Calls N downstream modules
  - Contains primary logic for: [feature/concern]
- **Summary**: [One plain-language sentence — what does this file actually do in the system?]

### [Module: filename.ts]
- **Role**: ...
- **Why core**: ...
- **Summary**: ...

---

## 4. Key Request Flows

> Trace 2–4 critical user actions from UI to database.

### Flow: [User Action — e.g., "Create Post"]

| Step | Component | What it does |
|------|-----------|--------------|
| 1 | React Form | Captures user input, validates client-side |
| 2 | POST /api/posts | HTTP request to API layer |
| 3 | postController.ts | Validates request, extracts userId from auth token |
| 4 | postService.ts | Business logic: attach metadata, check limits |
| 5 | prisma.post.create() | Writes to Postgres |
| 6 | Response JSON | Returns created post |
| 7 | UI update | Optimistic update shows post instantly |

### Flow: [User Action — e.g., "Load Feed"]

| Step | Component | What it does |
|------|-----------|--------------|
| 1 | ... | ... |

---

## 5. Business Scenarios

> Narrative explanations. Write for humans, not compilers. 3–5 scenarios covering the most important user journeys.

### Scenario: [Feature Name — e.g., "Creating a Post"]

When a user writes content and taps "Post", the frontend sends a `POST /api/posts` request with the text content and any attached media. `postController.ts` receives the request and verifies the auth token to identify the user. It hands off to `postService.ts`, which enforces business rules (e.g., rate limits, content length) before calling Prisma to persist the post. On success, the new post is returned to the frontend, which updates the feed instantly using optimistic UI. A background job in `notificationWorker.ts` then fans out notifications to followers.

### Scenario: [Feature Name]

[Narrative...]

---

## 6. Important Data Models

> Key entities and how they relate. Focus on models that drive core product behavior.

### Model: [ModelName]

**Fields** (key fields only):
```
id          String    @id
userId      String
content     String
createdAt   DateTime  @default(now())
```

**Role**: [What this entity represents in product terms]
Example: "The primary unit of content. Posts are what users create, share, and react to. Everything in the feed is a Post."

**Relationships**:
```
User  →  Post  (1:N)
Post  →  Like  (1:N)
Post  →  Comment  (1:N)
```

### Model: [ModelName]

...

---

## 7. Domain Concepts

> Important variables, computed values, or business terms that are not obvious from the code alone.

### Concept: `[variableName]`
- **Meaning**: [What it represents in product terms]
- **Purpose**: [Why it exists and how it's used]

[Example]
### Concept: `rankingScore`
- **Meaning**: A numeric value assigned to each post, used to sort the feed for a given user.
- **Purpose**: Higher scores push posts toward the top of the feed. Computed from recency, engagement rate, and relationship strength between poster and viewer.

### Concept: `[variableName]`
...

---

## 8. Complexity Map

> Where the dangerous code lives. These files deserve extra caution and review.

| Level | Files | Reason |
|-------|-------|--------|
| 🔥 High | `recommendationEngine.ts`, `paymentProcessor.ts` | Complex business logic, many dependencies, frequent changes |
| 🟡 Medium | `feedController.ts`, `notificationService.ts` | Moderate dependencies, some business logic |
| 🟢 Low | `components/Button.tsx`, `utils/formatDate.ts` | Isolated, stateless, minimal dependencies |

> ⚠️ Before modifying any 🔥 file, trace all callers and run full test coverage.

---

## 9. Developer Onboarding Path

> Recommended reading order for a new engineer joining this project.

| Order | File / Area | Why |
|-------|-------------|-----|
| 1 | `server.ts` or `main.ts` | Entry point — see how the app boots and what middleware is registered |
| 2 | `routes/` | API surface — understand what endpoints exist before diving into logic |
| 3 | `schema.prisma` or `models/` | Data model — ground truth for what entities exist and how they relate |
| 4 | `services/feedService.ts` | Core business logic — the most important domain code |
| 5 | `middleware/auth.ts` | Auth/gating — understand who can do what before reading controllers |

**First task suggestion**: [Suggest a small, well-scoped first task that touches the core without being dangerous]

---

## Appendix: PM View *(optional)*

> For non-engineering stakeholders. Focus on features, user flows, and business rules.

**Core Features**
- [Feature 1] — [what it does for the user]
- [Feature 2] — ...

**Key Business Rules**
- [Rule 1, e.g., "A user can follow up to 5,000 accounts"]
- [Rule 2, e.g., "Posts are soft-deleted, not hard-deleted"]

**User-Facing Flows** (plain language)
- [Flow 1]: User opens app → sees personalized feed → scrolls → taps post → reads detail
- [Flow 2]: ...
