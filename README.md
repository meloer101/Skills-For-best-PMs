# PM Skills Suite

一套专为产品经理设计的 AI Agent Skill 集合，覆盖从模糊想法到上线度量的完整产品工作流。

每个 Skill 都是一个**结构化工作流引擎**——不是问答机器人，而是一个有阶段、有规则、有强制产出物的协作系统，帮助 PM 在 AI 的辅助下完成真正困难的产品决策。

---

## 为什么需要这套 Skills？

产品经理的工作链路很长，但每个环节都有一个共同的敌人：

> **模糊性**——想法不清晰、数据太多但理解太少、决策没有依据、需求写完之后没人懂。

传统 AI 对话可以帮你写东西，但它无法保证你**问对了问题**、**看到了反例**、**不会 solution-first**、**每条判断都有证据**。

这套 Skills 做的事情是：**把最好的产品方法论编码进 AI 的行为规则里**，让 AI 成为一个「懂产品的协作者」，而不只是一个「执行指令的助手」。

---

## Skills 地图

这五个 Skill 覆盖产品工作的完整闭环：

```
模糊想法
    │
    ▼
┌─────────────────────────────┐
│  Problem Discovery Engine   │  把想法 → 结构化问题模型 + 可验证假设
└─────────────────────────────┘
    │
    ▼
┌─────────────────────────────┐
│  User Insight Synthesizer   │  把原始用户数据 → 用户认知模型 + 机会信号
└─────────────────────────────┘
    │
    ▼
┌──────────────────────────────────┐
│  Feature Prioritization Engine   │  把 Backlog → 透明排序的产品路线图
└──────────────────────────────────┘
    │
    ▼
┌─────────────────────────────┐
│       PRD Architect         │  把决策好的功能 → 工程可执行的 PRD
└─────────────────────────────┘
    │
    ▼
┌─────────────────────────────┐
│   Product Metrics Analyst   │  把上线数据 → 行动建议 + 下一轮假设
└─────────────────────────────┘
    │
    ▼
（进入下一个发现周期）
```

每个 Skill 可以独立触发，也可以串联使用。

---

## Skills 一览

### 1. Problem Discovery Engine

**解决什么问题**：PM 最容易犯的错——还没搞清楚问题，就开始设计解决方案。

**核心能力**：
- 对话式追问，阻止「solution-first」跳跃
- 建立 User Situation Model（谁 / 什么情境 / 触发点 / 目标 / 约束）
- 提炼 JTBD（Job To Be Done）
- 五问法 / 鱼骨图根因分析
- 把机会空间转为可证伪的产品假设

**产出物**：
- `Problem Discovery Brief`（结构化问题模型）
- `Hypothesis Ledger`（假设台账，含置信度与下一步验证计划）

---

### 2. User Insight Synthesizer

**解决什么问题**：做了 20 个用户访谈，结果每个人说的都不一样，团队陷入"数据有了但理解没有"的迷雾。

**核心能力**：
- 把原始文本拆成 atomic signals 并编码
- 主题聚类（Thematic Analysis）发现行为模式
- 识别 User Archetypes（行为人格）
- Motivation Ladder：从表面需求挖到核心动机
- 强制标注少数声音，防止确认偏误

**产出物**：
- `User Insight Report`（含 User Segments / Behavior Patterns / Pain Points / Hidden Needs / Motivations / Opportunity Signals，每条 Insight 附 Evidence）

---

### 3. Feature Prioritization Engine

**解决什么问题**：优先级讨论变成政治博弈——谁声音大谁赢，没有统一标准，没有显性的 trade-off。

**核心能力**：
- 统一评估标准（User Value / Business Impact / Strategic Alignment / Effort / Risk）
- 支持 RICE / ICE / MoSCoW / Impact-Effort 等框架
- 透明评分（每条分数都有明确理由）
- Quick Win vs Strategic Bet vs Defer 分类
- 组合视角：建立平衡路线图，而不只是按分数排列

**产出物**：
- `Prioritized Feature Roadmap`（含评分依据、trade-off 说明、风险项）
- `Feature Scoring Table`（CSV 格式，可导入表格工具）

---

### 4. PRD Architect

**解决什么问题**：PRD 写完之后，工程师说"看不懂"，设计师说"没讲清楚边界"，测试说"没有验收标准"。

**核心能力**：
- User Story 构建（As a / I want to / So that）
- 功能需求写成可测试的 shall/should 语句
- 边界条件与异常流程矩阵（Edge Case Matrix）
- 非功能需求（性能 / 安全 / 可靠性）量化阈值
- 成功指标定义（指标 + 目标值 + 数据来源）
- 完整性检查清单（输出前强制过一遍）

**产出物**：
- `Product Requirements Document`（Engineer-ready PRD）
- `Edge Case Matrix`
- `Metrics Table`

---

### 5. Product Metrics Analyst

**解决什么问题**：功能上线了，PM 盯着数据大盘不知道该看什么、为什么会这样、下一步该做什么。

**核心能力**：
- 确立分析框架（北极星指标 + 分层指标）
- 趋势检测 + 异常归因（内置 Anomaly Heuristics）
- 漏斗分析 + 激活路径 + Drop-off 识别
- 把 observation 转化为 testable hypothesis
- 推荐最小验证实验（含成功标准）

**产出物**：
- `Product Performance Insight Report`
- `Hypothesis Log`（CSV）
- `Metrics Snapshot Table`（CSV）

---

## 如何使用

### 在 Codex 中使用

把任意 Skill 文件夹安装到 Codex 的 skill 目录（文件夹名须与 `SKILL.md` 中的 `name` 一致）：

```bash
# 以符号链接方式安装（修改后实时生效，推荐）
ln -s "/Users/m/Documents/Skills/Problem Discovery Engine" ~/.codex/skills/problem-discovery-engine
ln -s "/Users/m/Documents/Skills/User Insight Synthesizer" ~/.codex/skills/user-insight-synthesizer
ln -s "/Users/m/Documents/Skills/Feature Prioritization Engine/feature-prioritization-engine" ~/.codex/skills/feature-prioritization-engine
ln -s "/Users/m/Documents/Skills/PRD Architect/prd-architect" ~/.codex/skills/prd-architect
ln -s "/Users/m/Documents/Skills/Product Metrics Analyst/product-metrics-analyst" ~/.codex/skills/product-metrics-analyst
```

安装后**重启 Codex**，Skill 即生效。

**触发方式**：直接描述你的任务，Codex 会自动匹配触发对应 Skill；或者在对话中明确说明，例如：

> 「用 problem-discovery-engine 帮我分析这个需求」

### 在 Cursor 中使用

把 Skill 文件夹安装到 Cursor 的个人 skill 目录（适用于所有项目）：

```bash
mkdir -p ~/.cursor/skills
ln -s "/Users/m/Documents/Skills/Problem Discovery Engine" ~/.cursor/skills/problem-discovery-engine
ln -s "/Users/m/Documents/Skills/User Insight Synthesizer" ~/.cursor/skills/user-insight-synthesizer
ln -s "/Users/m/Documents/Skills/Feature Prioritization Engine/feature-prioritization-engine" ~/.cursor/skills/feature-prioritization-engine
ln -s "/Users/m/Documents/Skills/PRD Architect/prd-architect" ~/.cursor/skills/prd-architect
ln -s "/Users/m/Documents/Skills/Product Metrics Analyst/product-metrics-analyst" ~/.cursor/skills/product-metrics-analyst
```

Cursor 会自动读取 `~/.cursor/skills/` 目录，无需重启。

> 注意：不要将文件放入 `~/.cursor/skills-cursor/`，该目录为 Cursor 内置系统目录。

---

## 串联使用示例

**场景：从一个模糊想法出发，一路做到上线度量**

```
1. 「我们要做一个 AI 会议摘要功能」
   → Problem Discovery Engine
   → 产出：Problem Brief + Hypothesis Ledger

2. 「这是我们收集到的 30 个用户访谈记录」
   → User Insight Synthesizer
   → 产出：User Insight Report（包含 User Archetypes + Opportunity Signals）

3. 「结合 Brief 和 Insight Report，现在有 8 个功能候选」
   → Feature Prioritization Engine
   → 产出：Prioritized Roadmap + Scoring Table

4. 「会议摘要功能排名第一，现在需要写需求」
   → PRD Architect
   → 产出：Engineer-ready PRD + Edge Case Matrix

5. 「功能上线两周，这是数据」
   → Product Metrics Analyst
   → 产出：Performance Insight Report + 下一轮假设与实验建议
```

---

## 设计原则

这套 Skills 遵循四个核心设计原则：

**1. Evidence-first（证据优先）**
每条判断、每个 insight、每项需求都必须附带证据来源。推断必须显式标注为推断。

**2. Forced structure（强制结构）**
每个 Skill 都有明确的 Stage 和 Exit Criteria。AI 不能跳跃阶段，用户也不能在问题没搞清楚之前就进入方案讨论。

**3. Minority tracking（少数声音保留）**
主流观点旁必须记录反例和少数声音，防止确认偏误。这是大多数 PM 工具缺失的能力。

**4. Explicit uncertainty（显式不确定性）**
用 Low / Medium / High 置信度标注每条结论，并明确「数据缺口」和「下一步需要验证什么」。

---

## 目录结构

```
Skills/
├── Problem Discovery Engine/         # Skill 1：发现 & 定义问题
├── User Insight Synthesizer/         # Skill 2：用户洞察分析
├── Feature Prioritization Engine/    # Skill 3：功能排优先级
│   └── feature-prioritization-engine/
├── PRD Architect/                    # Skill 4：撰写需求文档
│   └── prd-architect/
└── Product Metrics Analyst/          # Skill 5：上线数据分析
    └── product-metrics-analyst/
```

每个 Skill 目录结构：
```
skill-name/
├── SKILL.md                    # 核心：工作流 + 操作规则
├── agents/openai.yaml          # UI 元数据（display name, default prompt）
├── references/                 # 方法论参考 + 分阶段题库
├── assets/                     # 输出物模板（Report / PRD / Roadmap 等）
└── scripts/
    └── validate_skill.py       # 零依赖结构校验脚本
```

---

## 贡献 & 迭代

每个 Skill 都设计为**可独立迭代**的模块。如需改进某个 Skill：

1. 修改对应 `SKILL.md` 或 `references/` 文件
2. 运行校验脚本确认格式正确：
   ```bash
   python3 "path/to/skill/scripts/validate_skill.py" "path/to/skill"
   ```
3. 在真实任务中测试，根据使用体验调整

> 这套 Skills 本身就是用 [skill-creator](https://github.com/openai/skills) 构建的。
