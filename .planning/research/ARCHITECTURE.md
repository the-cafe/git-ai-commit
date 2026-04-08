# 架构研究：详细提交信息生成

**领域:** Python CLI 工具 - Git 提交信息生成
**研究日期:** 2026-04-08
**置信度:** HIGH

## 标准架构

### 系统概览

```
┌─────────────────────────────────────────────────────────────┐
│                    CLI 入口层 (Entry Point)                   │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐       │
│  │ main.py      │  │ handlers/    │  │ hook entry   │       │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘       │
├─────────┴──────────────────┴──────────────────┴──────────────┤
│                    核心生成层 (Core)                          │
│  ┌──────────────────────────────────────────────────────┐    │
│  │  gen_commit_msg.py                                   │    │
│  │  ┌────────────┐  ┌────────────┐  ┌────────────┐     │    │
│  │  │ Standard   │  │Conventional│  │ Detailed   │     │    │
│  │  │ Generator  │  │ Generator  │  │ Generator  │     │    │
│  │  └────────────┘  └────────────┘  └────────────┘     │    │
│  └──────────────────────────────────────────────────────┘    │
├─────────────────────────────────────────────────────────────┤
│                    分析层 (Analysis)                          │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐       │
│  │ Diff Parser  │  │ Change       │  │ File Path    │       │
│  │              │  │ Classifier   │  │ Analyzer     │       │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘       │
├─────────┴──────────────────┴──────────────────┴──────────────┤
│                    Prompt 层 (Prompt)                         │
│  ┌──────────────────────────────────────────────────────┐    │
│  │  prompt.py                                           │    │
│  │  ┌────────────┐  ┌────────────┐  ┌────────────┐     │    │
│  │  │ Standard   │  │Conventional│  │ Detailed   │     │    │
│  │  │ Prompt     │  │ Prompt     │  │ Prompt     │     │    │
│  │  └────────────┘  └────────────┘  └────────────┘     │    │
│  └──────────────────────────────────────────────────────┘    │
├─────────────────────────────────────────────────────────────┤
│                    服务层 (Services)                          │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐       │
│  │ LLM Service  │  │ Config       │  │ Git Service  │       │
│  │ Factory      │  │ Service      │  │              │       │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘       │
├─────────┴──────────────────┴──────────────────┴──────────────┤
│                    存储层 (Storage)                           │
│  ┌──────────────┐  ┌──────────────┐                          │
│  │ Local DB     │  │ Git Repo     │                          │
│  │ (JSON)       │  │ (.git/)      │                          │
│  └──────────────┘  └──────────────┘                          │
└─────────────────────────────────────────────────────────────┘
```

### 组件职责

| 组件 | 职责 | 典型实现 |
|------|------|---------|
| **CLI 入口层** | 命令行参数解析、路由到对应处理器 | argparse + handler 分发 |
| **核心生成层** | 协调整个生成流程、选择生成策略 | 策略模式，根据参数选择生成器 |
| **分析层** | 解析 diff、分类变更、提取语义信息 | 正则表达式 + 文件路径模式匹配 |
| **Prompt 层** | 构建 LLM 提示词、预处理 diff | 模板字符串 + diff 过滤 |
| **服务层** | LLM 调用、配置管理、Git 操作 | 工厂模式 + 服务抽象 |
| **存储层** | 配置持久化、Git 仓库访问 | JSON 文件 + Git 命令 |

## 推荐项目结构（新增详细提交信息功能）

```
ai_commit_msg/
├── cli/                          # CLI 处理器
│   ├── gen_ai_commit_message_handler.py
│   ├── conventional_commit_handler.py
│   └── detailed_commit_handler.py    # 新增：详细提交信息处理器
├── core/                         # 核心逻辑
│   ├── gen_commit_msg.py         # 扩展：添加详细生成函数
│   ├── prompt.py                 # 扩展：添加详细 prompt
│   ├── diff_analyzer.py          # 新增：diff 分析器
│   └── change_classifier.py      # 新增：变更分类器
├── services/                     # 服务层
│   ├── config_service.py         # 扩展：添加版本号配置
│   ├── llm_service.py
│   ├── llm_service_factory.py
│   ├── git_service.py
│   └── local_db_service.py       # 扩展：存储版本号配置
├── utils/                        # 工具函数
│   ├── file_pattern_matcher.py   # 新增：文件路径模式匹配
│   └── task_id_generator.py      # 新增：临时任务号生成
└── main.py                       # 主入口
```

### 结构理由

- **cli/detailed_commit_handler.py:** 独立处理器，专门处理 IDEA 插件调用，不影响现有 CLI 流程
- **core/diff_analyzer.py:** 解析 git diff，提取文件变更、行变更、语义信息
- **core/change_classifier.py:** 基于文件路径和 diff 内容分类变更（数据库/API/业务逻辑等）
- **utils/file_pattern_matcher.py:** 可配置的文件路径模式匹配规则
- **utils/task_id_generator.py:** 生成临时任务号（如 TEMP-001），用户可手动替换

## 架构模式

### 模式 1: 策略模式 - 多种生成策略

**作用:** 根据不同场景选择不同的提交信息生成策略

**使用场景:**
- 标准提交信息（现有）
- Conventional Commits（现有）
- 详细提交信息（新增）

**权衡:**
- 优点：易于扩展新格式，各策略独立
- 缺点：需要维护多个生成器

**示例:**
```python
# core/gen_commit_msg.py

def generate_commit_message(
    diff: str,
    conventional: bool = False,
    detailed: bool = False,  # 新增参数
    commit_template: str = None,
) -> str:
    if detailed:
        return generate_detailed_commit_message(diff)
    elif conventional:
        return generate_conventional_commit_single_call(diff)
    else:
        prompt = get_prompt(diff, commit_template=commit_template)
        return llm_chat_completion(prompt)

def generate_detailed_commit_message(diff: str) -> str:
    """生成详细提交信息"""
    # 1. 获取版本号配置
    version = ConfigService().get_version_number()

    # 2. 生成临时任务号
    task_id = generate_temp_task_id()

    # 3. 分析变更
    changes = ChangeClassifier().classify(diff)

    # 4. 构建 prompt
    prompt = get_detailed_prompt(diff, changes)

    # 5. 调用 LLM
    result = llm_chat_completion(prompt)

    # 6. 格式化输出
    return format_detailed_commit(version, task_id, result)
```

### 模式 2: 管道模式 - 变更分析流水线

**作用:** 将 diff 分析分解为多个独立步骤

**使用场景:**
- 解析 diff → 提取文件变更 → 分类变更类型 → 生成描述

**权衡:**
- 优点：每个步骤可独立测试和优化
- 缺点：增加了中间数据结构

**示例:**
```python
# core/change_classifier.py

class ChangeClassifier:
    def classify(self, diff: str) -> List[ChangeCategory]:
        """分析 diff 并分类变更"""
        # 步骤 1: 解析 diff
        parsed = DiffParser().parse(diff)

        # 步骤 2: 按文件路径分类
        categorized = self._categorize_by_path(parsed)

        # 步骤 3: 按内容分类
        categorized = self._categorize_by_content(categorized)

        # 步骤 4: 合并同类变更
        return self._merge_categories(categorized)

    def _categorize_by_path(self, parsed_diff):
        """基于文件路径分类"""
        categories = []
        for file_change in parsed_diff.files:
            if self._is_database_file(file_change.path):
                categories.append(ChangeCategory.DATABASE)
            elif self._is_api_file(file_change.path):
                categories.append(ChangeCategory.API)
            # ... 更多规则
        return categories
```

### 模式 3: 工厂模式 - Prompt 构建器

**作用:** 根据不同生成模式构建不同的 prompt

**使用场景:**
- 标准 prompt
- Conventional prompt
- 详细 prompt（新增）

**权衡:**
- 优点：prompt 逻辑集中管理
- 缺点：prompt 复杂度增加

**示例:**
```python
# core/prompt.py

def get_detailed_prompt(diff: str, changes: List[ChangeCategory]) -> List[dict]:
    """构建详细提交信息的 prompt"""

    processed_diff = preprocess_diff(diff)

    # 构建变更分类提示
    change_hints = "\n".join([
        f"- 检测到 {cat.name} 变更: {cat.description}"
        for cat in changes
    ])

    system_prompt = f"""你是一个代码审查专家，负责生成详细的提交信息。

分析以下代码变更，生成一个详细的变更列表。

检测到的变更类型：
{change_hints}

要求：
1. 每个变更点用一个独立的列表项（以 "- " 开头）
2. 描述要具体，包含：
   - 修改了什么组件/模块
   - 添加/修改/删除了什么功能
   - 为什么做这个改动（如果能从代码推断）
3. 按重要性排序（数据库变更 > API 变更 > 业务逻辑 > UI 变更）
4. 使用中文
5. 每个列表项不超过 80 字

示例格式：
- 根据病例是否存在染色封片工作站动态决定任务流转方向
- 添加了 DoctorAdviecDyeingUserTask 和 DoctorAdviceSlideUserTask 的条件判断
- 实现了基于工作站存在性的任务类型分配机制

只返回列表项，不要添加额外的说明文字。"""

    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": processed_diff},
    ]
```

## 数据流

### 详细提交信息生成流程

```
[IDEA 插件调用]
    ↓
[CLI Handler] → 检查版本号配置
    ↓
[有配置?] ─No→ [使用标准格式生成]
    ↓ Yes
[Git Service] → 获取 staged diff
    ↓
[Diff Analyzer] → 解析 diff 结构
    ↓
[Change Classifier] → 分类变更类型
    ↓                   (数据库/API/业务逻辑/UI/配置)
[Prompt Builder] → 构建详细 prompt
    ↓
[LLM Service] → 调用 LLM 生成列表
    ↓
[Formatter] → 格式化输出
    ↓           (类型(版本号-任务号): 标题\n\n- 列表项...)
[返回给 IDEA 插件]
```

### 配置管理流程

```
[IDEA 插件配置界面]
    ↓
[设置版本号] → ConfigService.set_version_number()
    ↓
[LocalDbService] → 保存到 .git/.ai_commit_msg_config.json
    ↓
[下次生成时读取] → ConfigService.get_version_number()
```

### 关键数据流

1. **版本号配置流:** IDEA 插件 → ConfigService → LocalDbService → JSON 文件
2. **变更分析流:** Git diff → DiffParser → ChangeClassifier → 分类结果
3. **Prompt 构建流:** 分类结果 + diff → PromptBuilder → LLM prompt
4. **格式化流:** LLM 输出 → Formatter → 最终提交信息

## 扩展性考虑

| 规模 | 架构调整 |
|------|---------|
| 单项目使用 | 当前架构足够，配置存储在 .git/ 目录 |
| 多项目使用 | 考虑全局配置 + 项目级覆盖 |
| 团队使用 | 添加共享配置模板功能 |

### 扩展优先级

1. **首要瓶颈:** LLM 调用延迟 → 缓存相似 diff 的结果
2. **次要瓶颈:** 大型 diff 处理 → 智能截断和摘要

## 反模式

### 反模式 1: 在 Prompt 中硬编码格式

**错误做法:** 将版本号格式、任务号格式硬编码在 prompt 中

**为什么错误:** 不同项目格式不同，难以适配

**正确做法:**
```python
# 使用配置驱动
version_format = ConfigService().get_version_format()  # "1.9.1" 或 "V1.9.2"
task_format = ConfigService().get_task_format()        # "15118" 或 "TEMP-001"

# 在格式化阶段应用
formatted = f"{commit_type}({version_format}-{task_format}): {title}"
```

### 反模式 2: 过度依赖 LLM 分类

**错误做法:** 让 LLM 同时负责分类和生成描述

**为什么错误:**
- LLM 分类不稳定
- 增加 token 消耗
- 难以调试

**正确做法:**
```python
# 使用规则引擎预分类
changes = ChangeClassifier().classify(diff)  # 基于文件路径和关键词

# LLM 只负责生成描述
prompt = get_detailed_prompt(diff, changes)  # 传入分类提示
```

### 反模式 3: 单一 Prompt 处理所有场景

**错误做法:** 用一个复杂的 prompt 处理标准、conventional、详细三种格式

**为什么错误:**
- Prompt 过于复杂，难以维护
- 不同格式的优化互相干扰

**正确做法:**
```python
# 每种格式独立 prompt
if detailed:
    prompt = get_detailed_prompt(diff, changes)
elif conventional:
    prompt = get_conventional_prompt(diff)
else:
    prompt = get_standard_prompt(diff)
```

## 集成点

### 外部服务

| 服务 | 集成模式 | 注意事项 |
|------|---------|---------|
| IDEA 插件 | CLI 调用 + JSON 输出 | 需要标准化输出格式 |
| LLM 服务 | HTTP API | 已有工厂模式支持多提供商 |
| Git | 命令行调用 | 使用 GitService 封装 |

### 内部边界

| 边界 | 通信方式 | 考虑因素 |
|------|---------|---------|
| CLI ↔ Core | 函数调用 | 参数传递要清晰 |
| Core ↔ Services | 服务接口 | 保持服务无状态 |
| Services ↔ Storage | 文件 I/O | 错误处理要完善 |

## 构建顺序建议

基于组件依赖关系，推荐以下构建顺序：

### 阶段 1: 基础设施（无依赖）
1. **ConfigService 扩展** - 添加版本号配置方法
2. **LocalDbService 扩展** - 支持版本号存储
3. **TaskIdGenerator** - 临时任务号生成工具

### 阶段 2: 分析层（依赖基础设施）
4. **FilePatternMatcher** - 文件路径模式匹配
5. **DiffAnalyzer** - diff 解析器
6. **ChangeClassifier** - 变更分类器（依赖 FilePatternMatcher）

### 阶段 3: Prompt 层（依赖分析层）
7. **Prompt 扩展** - 添加 get_detailed_prompt()

### 阶段 4: 核心生成层（依赖 Prompt 层）
8. **gen_commit_msg 扩展** - 添加 generate_detailed_commit_message()
9. **Formatter** - 格式化输出

### 阶段 5: CLI 层（依赖核心层）
10. **DetailedCommitHandler** - CLI 处理器

### 依赖关系图

```
ConfigService ←─┐
LocalDbService  │
TaskIdGenerator │
                ├─→ ChangeClassifier ─→ PromptBuilder ─→ CoreGenerator ─→ CLIHandler
FilePatternMatcher ─┘
DiffAnalyzer ───────┘
```

## 源引用

**架构模式:**
- [Repurposing Git Commit Messages as a Structured Knowledge Protocol](https://arxiv.org/html/2603.15566) - 结构化提交信息协议
- [Code-Change-Aware Methods Overview](https://www.emergentmind.com/topics/code-change-aware-methods) - 代码变更分析方法

**LLM 集成:**
- [Automated Commit Message Generation with Large Language Models](https://arxiv.org/html/2404.14824v1) - LLM 提交信息生成
- [Only diff Is Not Enough: Generating Commit Messages Leveraging Reasoning and Action](https://dl.acm.org/doi/10.1145/3643760) - ReAct prompting 方法

**变更分类:**
- [Detecting Multiple Semantic Concerns in Tangled Code Commits](https://arxiv.org/html/2601.21298v1) - 语义关注点检测
- [Python AST code analysis](https://copyprogramming.com/howto/parsing-python-code-from-within-python) - Python AST 分析

**现有代码库分析:**
- 基于 git-ai-commit 现有架构（HIGH 置信度）

---
*架构研究领域: Python CLI 工具 - Git 提交信息生成*
*研究日期: 2026-04-08*
