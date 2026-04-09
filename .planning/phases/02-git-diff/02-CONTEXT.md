# Phase 2: Git Diff 解析和智能变更分类 - Context

**Gathered:** 2026-04-09
**Status:** Ready for planning

<domain>
## Phase Boundary

本阶段交付：将 git diff 输出解析为结构化数据，并通过规则引擎将每个变更文件分类为数据库、API、业务逻辑、配置、UI 五种类型之一。输出结构化的分类结果供 Phase 3 的 LLM prompt 使用。

不包含：LLM prompt 优化、提交信息文本生成、CLI 命令扩展。

</domain>

<decisions>
## Implementation Decisions

### 分类策略
- **D-01:** 采用规则优先 + LLM 辅助策略。先用文件路径模式、文件扩展名、代码内容关键词三个维度做规则匹配，仅对规则无法确定的文件标记为"未分类"交给 Phase 3 的 LLM 处理。
- **D-02:** Phase 2 不直接调用 LLM。"LLM 辅助"的含义是：Phase 2 产出的分类结果中包含未分类文件的原始信息，Phase 3 在构造 prompt 时利用这些信息让 LLM 补充分类。

### 分类粒度
- **D-03:** 按文件级别分类。每个变更文件归入且仅归入一个类别（数据库/API/业务逻辑/配置/UI/未分类）。
- **D-04:** 当一个文件可能属于多个类别时，取优先级最高的类别。优先级顺序：数据库 > API > 业务逻辑 > 配置 > UI。

### 语言覆盖
- **D-05:** 通用多语言支持。内置常见语言/框架的文件路径模式规则：
  - Java/Spring Boot: `**/controller/**`, `**/service/**`, `**/repository/**`, `**/entity/**`, `**/mapper/**`
  - Python/Django/Flask: `**/views/**`, `**/models/**`, `**/serializers/**`, `**/urls/**`
  - JavaScript/TypeScript: `**/routes/**`, `**/components/**`, `**/api/**`, `**/store/**`
  - Go: `**/handler/**`, `**/model/**`, `**/router/**`
  - C#/.NET: `**/Controllers/**`, `**/Models/**`, `**/Services/**`
  - 通用: `**/migrations/**`, `**/config/**`, `**/static/**`, `**/templates/**`

### Diff 解析
- **D-06:** 使用 unidiff 0.7.5 库解析 git diff，提取 PatchSet → PatchedFile → Hunk 结构。
- **D-07:** 复用现有 `prompt.py` 中的 `NOISE_FILE_PATTERNS` 过滤逻辑，在解析阶段跳过噪音文件。

### 信息提取
- **D-08:** 从每个变更文件提取：文件路径、变更类型（新增/修改/删除/重命名）、添加行数、删除行数、变更摘要。
- **D-09:** 对 Python 文件使用内置 `ast` 模块提取新增/修改/删除的函数和类名。其他语言使用正则表达式做基础提取。

### 数据结构
- **D-10:** 分类结果使用 Python 字典/JSON 结构，不引入 Pydantic。保持与现有代码风格一致。
- **D-11:** 输出结构示例：
  ```json
  {
    "summary": {
      "total_files": 5,
      "added": 2,
      "modified": 2,
      "deleted": 1,
      "total_additions": 120,
      "total_deletions": 30
    },
    "categories": {
      "database": [
        {
          "path": "src/models/user.py",
          "change_type": "modified",
          "additions": 15,
          "deletions": 3,
          "key_changes": ["add field: email_verified", "modify class: User"]
        }
      ],
      "api": [...],
      "business_logic": [...],
      "config": [...],
      "ui": [...],
      "unclassified": [...]
    },
    "priority_order": ["database", "api", "business_logic", "config", "ui"]
  }
  ```

### Claude's Discretion
- 分类规则的具体关键词列表和文件路径模式可由 Claude 根据最佳实践决定
- 测试用例的具体 diff 内容可由 Claude 设计
- 模块内部的函数/类组织方式

</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### 项目约束
- `.planning/PROJECT.md` -- 项目核心价值、目标格式示例、变更分类逻辑定义
- `.planning/REQUIREMENTS.md` -- CLASSIFY-01 到 CLASSIFY-06 需求详情

### Phase 1 产出
- `.planning/phases/01-infrastructure-config/01-VERIFICATION.md` -- Phase 1 验证报告，确认基础设施就绪

### 现有代码
- `ai_commit_msg/core/prompt.py` -- NOISE_FILE_PATTERNS 定义、preprocess_diff() 函数
- `ai_commit_msg/services/git_service.py` -- GitService.get_staged_diff() 获取 diff
- `ai_commit_msg/core/gen_commit_msg.py` -- generate_commit_with_auto_fallback() 占位符待替换

### 技术栈
- `setup.cfg` -- 依赖管理，需添加 unidiff==0.7.5

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets
- `GitService.get_staged_diff()` -- 已有获取 staged diff 的方法，返回原始 diff 字符串
- `GitService.get_staged_files()` -- 已有获取 staged 文件列表的方法
- `preprocess_diff()` -- 已有噪音文件过滤和 diff 截断逻辑，可复用过滤规则
- `NOISE_FILE_PATTERNS` -- 已有噪音文件模式列表

### Established Patterns
- 服务类使用静态方法（GitService 模式）
- 配置通过 ConfigService 单例访问
- LLM 调用通过 llm_chat_completion() 统一入口
- JSON 解析使用内置 json 模块 + 正则清理

### Integration Points
- `gen_commit_msg.py` line 120-125: Phase 3 将替换占位符逻辑，调用本阶段的分类器
- `prompt.py`: 新的详细格式 prompt 将使用分类结果构造上下文

</code_context>

<specifics>
## Specific Ideas

- 分类结果中的 `key_changes` 字段直接服务于 Phase 3 的详细变更列表生成
- PROJECT.md 中的示例格式表明每个变更点应聚焦业务影响和技术决策，分类器需提取足够信息支持这种描述
- 优先级排序（数据库 > API > 业务逻辑 > 配置 > UI）与 PROJECT.md 中"变更分类逻辑"部分一致

</specifics>

<deferred>
## Deferred Ideas

None -- discussion stayed within phase scope

</deferred>

---

*Phase: 02-git-diff*
*Context gathered: 2026-04-09*
