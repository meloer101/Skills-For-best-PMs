# PM Skills Suite — 质量评审报告

> 评审日期：2026-07-13
> 评审范围：8 个 Skill 的 SKILL.md、references/、assets/ 全部文件
> 核心结论：内容不缺，缺的是「设计原则和 README 承诺在一半的 Skill 里没有真正落地」。

---

## 一、质量分层现状

这套 Skills 的质量分成明显的三个梯队。

### 第一梯队（方法论真正编码进去了）

**用户洞察提炼、问题澄清引擎、项目理解引擎**

- 有带示例的推导模板：如 `coding_guide.md` 的 Motivation Ladder 示例、Archetype 示例、反确认偏误清单。
- 模板本身带指导语：`user_insight_report_template.md` 278 行，每节有 blockquote 说明用法。

### 第二梯队（骨架完整但深度不足）

**功能排序引擎、PRD架构师、上线效果分析师**

- 明显是同一个模子快速生成的：英文、简短、题库问题偏泛（"What is the business goal?" 这种任何模型都会自己问的问题）。
- 对比悬殊：`prd_template.md` 只有 43 行，功能需求部分就是 `FR1: FR2: FR3:` 三个空行。

### 第三梯队（概念好但缺实例）

**简历适配助手、面试模拟工具**

- 框架设计其实很聪明（signal 强弱分类、counterfactual framing、三层答案），但通篇没有一个完整的 worked example。

---

## 二、各 Skill 的具体问题

### 1. PRD Architect —— 核心链路中最弱的一环

- 模板缺关键部分：没有 **Non-goals/Scope 边界**（PRD 最有价值的部分）、没有 Open Questions、没有 Rollout 计划、没有依赖项。Workflow 里提到 acceptance criteria，但模板里没有对应位置。
- `edge_case_matrix_template.md` 只有 5 行通用场景（invalid input / network failure…），没有边界类别框架（状态转换、并发、空状态、权限矩阵、数据量极值、首次使用）。
- 声称 "testable language"，但从未展示**可测试 vs 不可测试的对照示例**——few-shot 示例才是真正改变模型行为的东西。

### 2. Product Metrics Analyst —— 缺分析的"防坑"能力

- `anomaly_heuristics.md` 只有 18 行、4 条规则。README 把 "内置 Anomaly Heuristics" 列为核心能力，但真正的 PM 数据陷阱一个都没覆盖：辛普森悖论（分段混合效应）、新奇效应 vs 持续采用、周内季节性、分母漂移、埋点变更排查清单。
- **没有任何统计显著性护栏**——一个教 AI 从指标下结论的 Skill，没有"什么样的波动是噪声"的判断规则，很容易把噪声读成信号。
- `insight_report_template.md` 没有 Evidence 行和 Confidence 字段——**违反了这套 Skills 自己的两条设计原则**。

### 3. Feature Prioritization Engine —— 回避了它自己定义的问题

- README 说它解决"政治博弈"，但 Skill 里没有任何处理利益相关者的机制：HIPPO 给了分怎么办、异议如何记录（Minority tracking 原则在这里完全缺席）、多人打分如何校准。
- Stage 5 硬编码 "2 quick wins + 1 strategic bet + 1 infra"——组合比例应该是引导性的，不是固定配方。
- 缺一个完整打分示例（一个 feature 从收集到打分到 rationale 的全过程）。

### 4. Project Intelligence —— 概念最强，但许诺的能力没进模板

- `New skills Introduction.md` 里的第五层突破 **Impact Analysis（修改影响分析）** 和第七层 **System Evolution（git 历史考古）** 在报告模板的 9 个章节里都不存在。README 还写着"改一行代码会不会炸"。
- `analysis_guide.md` 里的 grep 命令只处理 `from './` 相对导入——alias 导入（`@/`）、Python、Go 都会漏。
- 没有防幻觉机制：Evidence-first 规则存在，但没有"断言调用次数前必须重新打开文件核实"这样的验证动作。声称 "Called by 7 files" 而实际没数过，是这类 Skill 最常见的失败模式。
- 没有大代码库的降级策略（50 万行怎么办？采样多少？跳过什么？）只有一句话带过。

### 5. Problem Discovery Engine —— 强，但有个尴尬细节

- `question_bank.md` Stage 4 的 Five Whys 题目硬编码了"邮件太多"这个具体案例（"为什么邮件很多是问题？"）——换个领域使用时这些问题直接失效，应改写成通用模板 + 单独的示例区。

### 6. 面试模拟工具 —— 名字和能力不匹配

- 名字叫"模拟"，但 Skill 只会生成答案文档，**从不真正模拟面试**。最有价值的迭代方向：加一个 Drill Mode——AI 扮演面试官，逐层追问、评分、指出答案哪里会被压垮。这才配得上"模拟"二字。
- `openai.yaml` 有个 typo：`Use -interview-defense-system`，丢了 `pm` 前缀。

### 7. Resume Narrative Engine

- Template A/B/C 是抽象填空，缺"工程 bullet → PM bullet"的 before/after 改写示例。
- 没有中英文简历规范差异的处理（目标用户大概率两种都要写）。

---

## 三、套件级问题（比单个 Skill 更值得修）

### 1. 四大设计原则执行率约 50%

- Minority tracking 只在用户洞察提炼里存在。
- Confidence 标注在 PRD 和 Metrics 模板里缺失。
- Exit criteria 只有前两个 Skill 有。

建议做一次"原则合规扫描"，让每个 Skill 的模板都带 Evidence + Confidence 字段。

### 2. 串联是"文档级"的，不是"机制级"的

README 画了漂亮的 pipeline，但 Skill 之间互不认识对方的产出物。功能排序引擎的 Stage 1 应该写明："如果存在 Problem Discovery Brief 或 User Insight Report，把 Opportunity Areas 和 Evidence 直接作为打分输入"。给每个 Skill 加一节标准的 **Upstream Inputs**（找什么文件、字段怎么映射），8 个 Skill 才真正变成一个系统。

### 3. 提问经济学没有上限

所有 Skill 都有"每轮 5–8 题"，但**没有轮次上限**。真实使用中最大的体验风险是审讯疲劳——用户答了三轮还没看到产出就放弃了。建议统一加规则："最多 2–3 轮提问，之后带着显式假设直接出草稿"。另外 5–8 题一轮其实偏多，3–5 更现实。

### 4. 没有 Express Mode

每个 Skill 都强制全流程。真实场景需要快慢两档："lite 模式（一轮问答 + 直接产出带假设标注的草稿）vs full 模式"。这是采用率问题。

### 5. 工程卫生

- `validate_skill.py` 现在复制了 8 份，其实应该是仓库根目录一份，校验所有 Skill，顺便检查 SKILL.md 里引用的 references/assets 路径是否真实存在。
- 用户洞察提炼里写死了 `cursor-ide-browser MCP`——与 Codex/Claude Code 不兼容，应改成工具无关的表述。
- 没有任何 golden test（一份样例输入 + 期望产出骨架），迭代 prompt 时无法回归验证。

---

## 四、如果只做五件事，按这个优先级

1. **重做 PRD Architect 的模板和示例**——核心链路中使用频率最高、目前最薄的环节（Non-goals、acceptance criteria 结构、testable 对照示例、边界类别框架）。
2. **套件级加"轮次上限 + Express Mode"**——最大的真实使用体验提升。
3. **给 Project Intelligence 补上 Impact Analysis + System Evolution 章节和验证规则**——兑现自己设计文档的承诺，防幻觉。
4. **每个 Skill 加 1 个完整 worked example**——对模型输出质量的边际收益最高的投入。
5. **加 Upstream Inputs 机制**——让串联从 README 的图变成 Skill 的行为。

---

## 附：问题优先级矩阵

| 问题 | 影响面 | 修复成本 | 优先级 |
|------|--------|----------|--------|
| PRD 模板过薄 | 高（核心链路） | 中 | P0 |
| 轮次上限 + Express Mode | 高（全套件体验） | 低 | P0 |
| Metrics 缺统计护栏 | 高（会误导决策） | 中 | P1 |
| Project Intelligence 未兑现承诺 | 中 | 中 | P1 |
| 每个 Skill 缺 worked example | 高（输出质量） | 高 | P1 |
| Upstream Inputs 串联机制 | 中 | 低 | P1 |
| 四大原则合规扫描 | 中 | 低 | P2 |
| Feature Prioritization 缺利益相关者机制 | 中 | 中 | P2 |
| 面试模拟缺 Drill Mode | 中 | 中 | P2 |
| validate_skill 去重 + 路径校验 | 低 | 低 | P2 |
| question_bank 硬编码案例 | 低 | 低 | P3 |
| openai.yaml typo | 低 | 低 | P3 |
| cursor-ide-browser 工具耦合 | 低 | 低 | P3 |
