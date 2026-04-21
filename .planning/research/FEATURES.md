# Feature Research

**Domain:** AI Git 提交信息生成工具（详细结构化格式）
**Researched:** 2026-04-08
**Confidence:** HIGH

## Feature Landscape

### Table Stakes (Users Expect These)

Features users assume exist. Missing these = product feels incomplete.

| Feature | Why Expected | Complexity | Notes |
|---------|--------------|------------|-------|
| AI 生成提交信息 | 工具的核心价值，用户期望自动生成而非手写 | MEDIUM | 已实现，基于 LLM 分析 git diff |
| Conventional Commits 格式 | 业界标准，用户期望支持 type(scope): description | LOW | 已实现，支持 feat/fix/docs 等类型 |
| 多 LLM 提供商支持 | 用户期望选择自己的 AI 提供商（成本、隐私考虑） | MEDIUM | 已实现，支持 OpenAI/Anthropic/Ollama |
| 配置管理系统 | 用户期望能配置 API keys、模型选择、格式偏好 | MEDIUM | 已实现，通过 config_service.py |
| Git diff 分析 | 工具必须理解代码变更才能生成准确信息 | MEDIUM | 已实现，分析 staged changes |
| 提交信息预览与编辑 | 用户期望在提交前能查看和修改 AI 生成的信息 | LOW | 标准 git 流程，通过编辑器或 IDE |
| 提交信息历史记录 | 用户期望能查看之前生成的提交信息 | LOW | Git 原生支持，通过 git log |
| 错误处理与重试 | API 调用失败时用户期望清晰的错误信息和重试机制 | LOW | 需要健壮的错误处理 |

### Differentiators (Competitive Advantage)

Features that set the product apart. Not required, but valuable.

| Feature | Value Proposition | Complexity | Notes |
|---------|-------------------|------------|-------|
| 详细结构化提交信息 | 生成包含版本号、任务号、详细变更列表的格式，清晰展示技术变更点 | HIGH | 项目核心差异化功能，区别于简单的一行提交信息 |
| 智能变更分类 | 自动识别数据库变更、API 变更、业务逻辑、配置变更、UI 变更 | HIGH | 基于文件路径、代码内容、diff 模式智能分类 |
| 版本号配置管理 | 支持项目级别的版本号配置和管理，通过可视化界面配置 | MEDIUM | 不同项目版本号格式不同，需要灵活配置 |
| 临时任务号生成 | 生成占位符任务号（如 TEMP-001），用户可手动替换为实际任务号 | LOW | 提供灵活性，避免自动识别的错误 |
| 格式回退机制 | 无版本号配置时自动使用普通 Conventional Commits 格式 | LOW | 向后兼容，不破坏现有功能 |
| IDEA 插件深度集成 | 专门为 IntelliJ IDEA 优化的集成体验 | MEDIUM | 通过插件调用 CLI，提供原生 IDE 体验 |
| 变更上下文理解 | 理解代码变更的业务含义，而非仅描述文件变化 | HIGH | 需要优化 LLM prompt，理解业务逻辑 |
| 多级详细程度控制 | 用户可选择简洁、标准、详细三种提交信息详细程度 | MEDIUM | 适应不同场景需求（快速提交 vs 重要功能） |

### Anti-Features (Commonly Requested, Often Problematic)

Features that seem good but create problems.

| Feature | Why Requested | Why Problematic | Alternative |
|---------|---------------|-----------------|-------------|
| 自动任务号识别 | 用户希望从分支名或历史提交自动提取任务号 | 分支命名不规范、多任务分支、识别错误率高 | 生成临时任务号，用户手动替换更可控 |
| 多语言提交信息 | 国际化团队希望支持多语言 | 增加复杂度，翻译质量难保证，团队内应统一语言 | 保持中文格式，团队约定统一语言 |
| 实时协作编辑提交信息 | 团队希望多人协作编写提交信息 | 提交信息是个人行为，协作会导致责任不清 | 通过 code review 讨论提交质量 |
| 复杂的模板系统 | 用户希望高度自定义提交信息格式 | 过度灵活导致格式混乱，失去标准化价值 | 提供 2-3 种预设格式，满足主要场景 |
| 自动提交功能 | 用户希望生成后自动提交 | 危险，用户应保持对提交的控制权 | 生成后展示，用户确认后手动提交 |
| CLI 命令行复杂交互 | 用户希望 CLI 提供丰富的交互式选项 | 项目专注 IDE 集成，CLI 仅作为底层工具 | 通过 IDE 插件提供交互体验 |
| 提交信息 AI 评分 | 用户希望 AI 评估提交信息质量 | 主观性强，增加复杂度，用户会过度依赖评分 | 通过团队 code review 保证质量 |

## Feature Dependencies

```
详细结构化提交信息
    ├──requires──> 版本号配置管理
    ├──requires──> 智能变更分类
    └──requires──> 变更上下文理解

智能变更分类
    └──requires──> Git diff 分析

格式回退机制
    └──requires──> 版本号配置管理

IDEA 插件深度集成
    ├──requires──> 配置管理系统
    └──requires──> 详细结构化提交信息

多级详细程度控制
    └──enhances──> 详细结构化提交信息

临时任务号生成
    └──enhances──> 详细结构化提交信息
```

### Dependency Notes

- **详细结构化提交信息 requires 版本号配置管理:** 详细格式需要版本号信息，必须先有配置功能
- **详细结构化提交信息 requires 智能变更分类:** 详细列表需要对变更进行分类，依赖分类功能
- **智能变更分类 requires Git diff 分析:** 分类基于 diff 内容，必须先能分析 diff
- **格式回退机制 requires 版本号配置管理:** 回退逻辑依赖于检测是否有版本号配置
- **IDEA 插件深度集成 requires 配置管理系统:** 插件需要读取和修改配置
- **多级详细程度控制 enhances 详细结构化提交信息:** 提供不同详细程度的变体
- **临时任务号生成 enhances 详细结构化提交信息:** 为详细格式提供任务号占位符

## MVP Definition

### Launch With (v1)

Minimum viable product — what's needed to validate the concept.

- [x] AI 生成提交信息 — 核心功能，已实现
- [x] Conventional Commits 格式 — 业界标准，已实现
- [x] 多 LLM 提供商支持 — 灵活性需求，已实现
- [x] 配置管理系统 — 基础设施，已实现
- [ ] 版本号配置管理 — 详细格式的前置依赖
- [ ] 详细结构化提交信息生成 — 项目核心价值
- [ ] 智能变更分类 — 详细格式的关键组成
- [ ] 格式回退机制 — 向后兼容保证

### Add After Validation (v1.x)

Features to add once core is working.

- [ ] 临时任务号生成 — 用户反馈后确定占位符格式
- [ ] 变更上下文理解优化 — 基于用户反馈优化 prompt
- [ ] IDEA 插件深度集成 — 核心功能验证后再做 IDE 集成
- [ ] 多级详细程度控制 — 用户反馈后确定是否需要多级控制

### Future Consideration (v2+)

Features to defer until product-market fit is established.

- [ ] 提交信息模板系统 — 用户有定制需求时再考虑
- [ ] 提交信息统计分析 — 团队管理需求，非核心功能
- [ ] 其他 IDE 支持（VS Code, PyCharm） — 验证 IDEA 集成后再扩展
- [ ] 提交信息搜索与过滤 — Git 原生功能已足够

## Feature Prioritization Matrix

| Feature | User Value | Implementation Cost | Priority |
|---------|------------|---------------------|----------|
| 详细结构化提交信息 | HIGH | HIGH | P1 |
| 版本号配置管理 | HIGH | MEDIUM | P1 |
| 智能变更分类 | HIGH | HIGH | P1 |
| 格式回退机制 | MEDIUM | LOW | P1 |
| 临时任务号生成 | MEDIUM | LOW | P2 |
| 变更上下文理解优化 | HIGH | HIGH | P2 |
| IDEA 插件深度集成 | HIGH | MEDIUM | P2 |
| 多级详细程度控制 | MEDIUM | MEDIUM | P2 |
| 提交信息模板系统 | LOW | HIGH | P3 |
| 提交信息统计分析 | LOW | MEDIUM | P3 |

**Priority key:**
- P1: Must have for launch — 核心功能，必须实现
- P2: Should have, add when possible — 重要功能，核心验证后添加
- P3: Nice to have, future consideration — 锦上添花，未来考虑

## Competitor Feature Analysis

| Feature | aicommits | commitizen | git-ai-commit (current) | Our Approach (enhanced) |
|---------|-----------|------------|-------------------------|-------------------------|
| AI 生成 | ✓ 简单一行 | ✗ 手动选择 | ✓ 简单/详细 | ✓ 结构化详细格式 |
| 格式标准 | Conventional | Conventional | Conventional | Conventional + 详细扩展 |
| 变更分类 | ✗ 无 | ✗ 无 | ✗ 无 | ✓ 智能分类（数据库/API/业务） |
| 版本号支持 | ✗ 无 | ✗ 无 | ✗ 无 | ✓ 可配置版本号 |
| 任务号支持 | ✗ 无 | ✗ 无 | ✗ 无 | ✓ 临时任务号生成 |
| IDE 集成 | ✗ CLI only | ✗ CLI only | ✗ CLI only | ✓ IDEA 深度集成 |
| LLM 提供商 | OpenAI only | N/A | OpenAI/Anthropic/Ollama | OpenAI/Anthropic/Ollama |
| 配置管理 | 简单配置 | 简单配置 | 完整配置系统 | 完整配置系统 + 版本号管理 |

## Domain-Specific Insights

### 企业级开发场景需求

基于项目上下文（医疗系统开发），企业级开发有以下特殊需求：

1. **可追溯性要求高** - 需要版本号和任务号关联，便于问题追溯
2. **变更细节要求详细** - 需要清晰列出技术变更点，便于 code review 和后续维护
3. **多人协作场景** - 提交信息需要让其他开发者快速理解变更内容
4. **合规性要求** - 医疗系统需要详细的变更记录用于审计

### 提交信息格式演进趋势

从研究中发现的趋势：

1. **从简单到结构化** - 早期工具生成简单一行信息，现在趋向结构化详细信息
2. **从通用到领域特定** - 通用工具适用性广但不够深入，领域特定工具更有价值
3. **从 CLI 到 IDE 集成** - 开发者更倾向于在 IDE 内完成所有操作
4. **从单一格式到可配置** - 不同团队、不同项目需要不同格式

### 智能变更分类实现策略

基于研究和项目需求，变更分类应包含：

1. **文件路径模式匹配**
   - 数据库：`*.sql`, `migrations/`, `models/`, `schema/`
   - API：`routes/`, `controllers/`, `api/`, `endpoints/`
   - 业务逻辑：`services/`, `business/`, `domain/`
   - 配置：`config/`, `*.yaml`, `*.json`, `.env`
   - UI：`views/`, `components/`, `*.vue`, `*.jsx`

2. **代码内容分析**
   - SQL 关键字检测（CREATE, ALTER, DROP）
   - API 装饰器/注解（@route, @api, @endpoint）
   - 业务方法命名模式（process*, handle*, calculate*）

3. **Diff 模式识别**
   - 大量增删行 → 重构或新功能
   - 少量修改 → Bug 修复或优化
   - 新文件 → 新功能
   - 删除文件 → 清理或重构

## Sources

**AI Commit Tools:**
- [Git 4.0 Workflow: AI-Generated Commit Messages](https://markaicode.com/git-4-workflow-ai-commit-messages/)
- [Writing Git commit messages with Claude](https://andrewian.dev/blog/ai-git-commits)
- [Nutlope/aicommits - GitHub](https://github.com/Nutlope/aicommits)
- [tak-bro/aicommit2 - GitHub](https://github.com/tak-bro/aicommit2)
- [insulineru/ai-commit - GitHub](https://github.com/insulineru/ai-commit)

**Conventional Commits:**
- [Conventional Commits in Git: Clean History, Automated Releases](https://www.averagedevs.com/blog/conventional-commits-git)
- [What Are Conventional Commits?](https://jeffbailey.us/blog/2025/09/28/what-are-conventional-commits/)
- [Write Perfect Commit Messages with Conventional Commits](https://rivereditor.com/blogs/write-commit-messages-conventional-commits)

**Commit Message Best Practices:**
- [Complete Guide to Git Commit Message Best Practices in 2024](https://autocommit.top/blog/git-commit-message-best-practices-2024)
- [Recommended format for Git commit messages - Stack Overflow](https://stackoverflow.com/questions/4126442/recommended-format-for-git-commit-messages)
- [An opinionated guide to git collaboration](https://dangerlanc.com/writing/git-guidelines-for-commit-messages/)

**IDE Integration:**
- [MobileTribe/commit-template-idea-plugin - GitHub](https://github.com/MobileTribe/commit-template-idea-plugin)
- [anatolykopyl/auto-commit-message-plugin - GitHub](https://github.com/anatolykopyl/auto-commit-message-plugin)
- [Using AI in Your IDE - Industrial Logic](https://www.industriallogic.com/blog/using-ai-in-your-ide-commit-messages/)

**Configuration Management:**
- [Per-project git commit templates](https://tylercipriani.com/blog/2025/05/21/git-commits/)
- [Commit message templates](https://dev.to/hartmann/commit-message-templates-2ek0)

**Change Classification:**
- [git-commit-message skill by vasilyu1983](https://playbooks.com/skills/vasilyu1983/ai-agents-public/git-commit-message)
- [AI commit message generator change classification](https://pypi.org/project/py-ai-commit)

**Task ID Integration:**
- [On Git commit messages and issue trackers](https://medium.com/hackernoon/on-git-commit-messages-and-issue-trackers-f700f3cbb5a7)
- [Add the ticket ID to your commit messages automatically](https://medium.com/@adrian.garcia.estaun/add-the-ticket-id-to-your-commit-messages-automatically-2debfa0fbe9d)

---
*Feature research for: Git AI Commit - 详细提交信息增强*
*Researched: 2026-04-08*
