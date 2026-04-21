# 技术栈

**项目：** Git AI Commit - 详细提交信息增强
**研究日期：** 2026-04-08

## 推荐技术栈

### 核心框架
| 技术 | 版本 | 用途 | 理由 |
|------|------|------|------|
| Python | >=3.8 | 运行时环境 | 现有项目要求 >=3.6，但建议升级到 3.8+ 以支持更好的类型提示和 f-string 调试功能。当前系统运行 3.14.3，完全兼容 |

### Git Diff 解析
| 技术 | 版本 | 用途 | 理由 |
|------|------|------|------|
| unidiff | 0.7.5 | 结构化解析 git diff 输出 | 成熟稳定的库（2023年3月发布），提供面向对象的 API 来解析 unified diff 格式。可以按文件、按 hunk 访问变更，便于实现智能分类。比手动字符串解析更可靠 |

**为什么选择 unidiff：**
- 提供 `PatchSet`、`PatchedFile`、`Hunk` 等结构化对象
- 支持访问添加/删除的行、行号、上下文
- 可以轻松提取文件路径、变更类型（新增/修改/删除）
- 零依赖，轻量级（~10KB）

**替代方案：**
- `whatthepatch`：功能类似但更新较少
- 手动解析：现有方式，但难以实现复杂的变更分类逻辑

### 代码分析
| 技术 | 版本 | 用途 | 理由 |
|------|------|------|------|
| ast | 内置 | Python 代码 AST 分析 | Python 标准库，无需额外依赖。可以解析 Python 代码变更，识别函数定义、类定义、导入语句等，用于更精确的变更分类 |
| pathlib | 内置 | 文件路径模式匹配 | Python 3.4+ 标准库，面向对象的路径操作。使用 `Path.match()` 进行模式匹配，比 `fnmatch` 更现代 |

**使用场景：**
- `ast.parse()` 解析 Python 文件变更，识别 API 变更（函数签名修改）
- `pathlib.Path.match()` 匹配文件模式（如 `**/models/*.py` 识别数据库模型变更）
- 不需要外部依赖，保持项目轻量

### 结构化输出
| 技术 | 版本 | 用途 | 理由 |
|------|------|------|------|
| json | 内置 | JSON 序列化/反序列化 | 现有项目已使用，OpenAI 和 Anthropic 都支持 JSON 模式输出。无需额外依赖 |
| Pydantic | 2.x（可选） | 数据验证和类型安全 | 可选依赖。如果需要更严格的数据验证和类型提示，可以添加。但现有的 JSON + 字典方式已足够 |

**推荐方案：**
- **阶段 1**：继续使用现有的 JSON 解析方式（`json.loads()` + 字典访问）
- **阶段 2**（可选）：如果需要更复杂的验证逻辑，引入 Pydantic

**为什么不立即使用 Pydantic：**
- 现有代码已有 JSON 输出实现（`generate_conventional_commit_single_call`）
- 增加依赖会增加安装体积
- 对于简单的结构化输出，内置 JSON 已足够

### 配置管理
| 技术 | 版本 | 用途 | 理由 |
|------|------|------|------|
| json | 内置 | 配置文件存储 | 现有项目使用 `.ai_commit_msg_config.json`，保持一致性 |
| semantic-version | 2.10.0 | 版本号验证 | 轻量级库（~20KB），严格遵循 SemVer 2.0.0 规范。用于验证用户输入的版本号格式，避免无效配置 |

**配置扩展：**
```python
# 在 ConfigKeysEnum 中添加
VERSION_NUMBER = "version_number"  # 如 "1.9.1"
TASK_PREFIX = "task_prefix"        # 如 "TASK-" 或 "#"
ENABLE_DETAILED_FORMAT = "enable_detailed_format"  # bool
```

### 文件路径匹配
| 技术 | 版本 | 用途 | 理由 |
|------|------|------|------|
| pathlib | 内置 | 路径操作和模式匹配 | Python 标准库，面向对象 API，支持 glob 模式 |
| fnmatch | 内置 | Unix shell 风格模式匹配 | 标准库，用于更复杂的文件名模式匹配（如 `*.{py,java,js}`） |

**使用场景：**
```python
# 识别数据库变更
if path.match("**/models/*.py") or path.match("**/migrations/*.sql"):
    category = "数据库变更"

# 识别 API 变更
if path.match("**/api/*.py") or path.match("**/routes/*.py"):
    category = "API 变更"
```

### LLM 提供商（现有）
| 技术 | 版本 | 用途 | 理由 |
|------|------|------|------|
| openai | 已安装 | OpenAI API 客户端 | 现有依赖，支持结构化输出（JSON mode） |
| anthropic | 已安装 | Anthropic API 客户端 | 现有依赖，支持工具调用和结构化输出 |
| requests | 已安装 | Ollama HTTP 请求 | 现有依赖，用于本地 Ollama 模型 |

**结构化输出支持：**
- OpenAI：`response_format={"type": "json_object"}` 或 Structured Outputs API
- Anthropic：工具调用（tool use）或 JSON 模式提示
- Ollama：JSON 模式提示

### 用户界面（现有）
| 技术 | 版本 | 用途 | 理由 |
|------|------|------|------|
| rich | 已安装 | 终端富文本输出 | 现有依赖，用于美化输出 |
| prompt_toolkit | 已安装 | 交互式输入 | 现有依赖，用于配置界面 |
| inquirer | 已安装 | 交互式选择菜单 | 现有依赖，用于配置选项 |

## 新增依赖

### 必需
```bash
pip install unidiff==0.7.5
pip install semantic-version==2.10.0
```

### 可选（未来优化）
```bash
# 如果需要更严格的数据验证
pip install pydantic>=2.0.0
```

## 不推荐使用的技术

| 技术 | 原因 | 替代方案 |
|------|------|----------|
| whatthepatch | 更新频率低，功能与 unidiff 重叠 | unidiff |
| python-patch | 主要用于应用补丁，不适合解析分析 | unidiff |
| 正则表达式解析 diff | 容易出错，难以维护，无法处理复杂场景 | unidiff |
| 外部 AST 库（如 astroid） | 过于复杂，内置 ast 模块已足够 | ast（内置） |
| Pydantic（初期） | 增加复杂度和依赖，现有 JSON 方式已足够 | json（内置） |

## 安装

### 更新 setup.cfg
```ini
[options]
packages = find:
install_requires =
    openai
    requests
    anthropic
    rich
    pyfiglet
    prompt_toolkit
    inquirer
    unidiff>=0.7.5
    semantic-version>=2.10.0
python_requires = >=3.8
```

### 开发依赖
```ini
[options.extras_require]
dev =
    black==24.8.0
    pytest>=7.0.0
    mypy>=1.0.0
```

## 架构集成

### 1. Git Diff 解析层
```python
# 新模块：ai_commit_msg/utils/diff_parser.py
from unidiff import PatchSet

def parse_diff(diff_text: str) -> PatchSet:
    """解析 git diff 输出为结构化对象"""
    return PatchSet(diff_text)

def classify_changes(patch_set: PatchSet) -> dict:
    """分类变更：数据库、API、业务逻辑等"""
    pass
```

### 2. 变更分类器
```python
# 新模块：ai_commit_msg/core/change_classifier.py
from pathlib import Path
import ast

class ChangeClassifier:
    def classify_file(self, file_path: str, hunks: list) -> str:
        """基于文件路径和变更内容分类"""
        path = Path(file_path)

        # 数据库变更
        if path.match("**/models/*.py") or path.match("**/migrations/*.sql"):
            return "数据库变更"

        # API 变更
        if path.match("**/api/*.py") or path.match("**/routes/*.py"):
            return "API 变更"

        # 配置变更
        if path.match("**/*.{yaml,yml,json,toml,ini,cfg}"):
            return "配置变更"

        return "业务逻辑"
```

### 3. 版本号管理
```python
# 扩展：ai_commit_msg/services/config_service.py
from semantic_version import Version

def set_version_number(self, version: str):
    """设置并验证版本号"""
    try:
        Version(version)  # 验证格式
        config = ConfigService.get_config()
        config["version_number"] = version
        LocalDbService().set_db({CONFIG_COLLECTION_KEY: config})
    except ValueError:
        raise ValueError(f"Invalid version format: {version}")
```

### 4. 详细提交信息生成
```python
# 扩展：ai_commit_msg/core/gen_commit_msg.py
def generate_detailed_commit_message(diff: str, version: str) -> dict:
    """生成详细格式的提交信息"""

    # 1. 解析 diff
    patch_set = parse_diff(diff)

    # 2. 分类变更
    changes = classify_changes(patch_set)

    # 3. 构建 prompt
    prompt = build_detailed_prompt(changes, version)

    # 4. 调用 LLM
    response = llm_chat_completion(prompt)

    # 5. 解析 JSON 响应
    return json.loads(response)
```

## 置信度评估

| 领域 | 置信度 | 依据 |
|------|--------|------|
| Git Diff 解析 | HIGH | unidiff 是成熟稳定的库，PyPI 官方文档确认版本 0.7.5 |
| 代码分析 | HIGH | Python 内置 ast 模块，官方文档完整 |
| 结构化输出 | HIGH | 现有项目已实现 JSON 输出，OpenAI/Anthropic 官方支持 |
| 版本号管理 | HIGH | semantic-version 库遵循 SemVer 2.0.0 规范，PyPI 确认版本 2.10.0 |
| 文件路径匹配 | HIGH | pathlib 是 Python 标准库，官方文档完整 |

## 来源

### Git Diff 解析
- [unidiff PyPI](https://pypi.org/project/unidiff/) - 官方包页面，确认版本 0.7.5
- [Python Git diff parser - Stack Overflow](https://stackoverflow.com/questions/39423122/python-git-diff-parser) - 社区讨论

### 代码分析
- [Code-Change-Aware Methods Overview](https://www.emergentmind.com/topics/code-change-aware-methods) - AST 变更分析方法
- [Parsing Python Code from Within Python](https://copyprogramming.com/howto/parsing-python-code-from-within-python) - Python AST 解析指南

### 结构化输出
- [5 Python Tools for Structured LLM Outputs](https://codecut.ai/structured-llm-outputs-tools-comparison/) - 工具对比
- [Structured outputs with OpenAI and Pydantic](https://dida.do/blog/structured-outputs-with-openai-and-pydantic) - OpenAI 结构化输出
- [Producing Structured Output with Anthropics API](https://tspi.at/2025/10/30/claudestructured.html) - Anthropic 结构化输出
- [OpenAI Structured Outputs - Getting Reliable JSON from LLMs](https://team400.ai/blog/2026-03-openai-structured-outputs-practical-guide) - 2026 实践指南

### 版本号管理
- [semantic-version PyPI](https://pypi.org/project/semantic-version/) - 官方包页面
- [Python Package Versioning Guide](https://inventivehq.com/blog/python-package-versioning-guide) - SemVer 最佳实践

### 文件路径匹配
- [Python Pathlib Glob Guide](https://copyprogramming.com/howto/python-python-use-pathlib-glob-to-match-filename) - pathlib 模式匹配
- [Python Filter Files in Directory](https://copyprogramming.com/howto/python-python-filter-files-in-directory-by-name) - 文件过滤实践
