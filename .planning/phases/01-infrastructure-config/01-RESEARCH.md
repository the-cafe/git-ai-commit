# Phase 1: 基础设施和配置管理 - Research

**研究日期：** 2026-04-08
**领域：** Python 配置管理、版本号验证、CLI 参数解析
**置信度：** HIGH

## 摘要

Phase 1 需要建立版本号配置系统和格式回退机制。研究发现项目已有完整的配置基础设施（`LocalDbService` + `ConfigService`），可以直接扩展。版本号验证推荐使用 `semver` 库（3.0.4，2025年1月发布），比 CLAUDE.md 中提到的 `semantic-version` 更新且活跃维护。临时任务号使用简单的计数器模式（TEMP-001, TEMP-002...）。格式回退通过检测版本号配置是否存在，未配置时调用现有的 `generate_conventional_commit_single_call` 函数。

**核心建议：** 扩展现有配置系统，添加 `project_version` 和 `temp_task_counter` 两个配置键，使用 `semver` 库验证版本号格式，在提交信息生成入口处实现格式选择逻辑。

<phase_requirements>
## Phase Requirements

| ID | Description | Research Support |
|----|-------------|------------------|
| CONFIG-01 | 用户可以通过可视化界面配置项目版本号 | 扩展 `config_handler.py` 添加 `--version` 参数，使用 argparse |
| CONFIG-02 | 系统自动验证版本号格式符合 SemVer 规范 | 使用 `semver.Version.parse()` 验证，抛出 `ValueError` 处理无效格式 |
| CONFIG-03 | 版本号配置持久化到配置文件 | 使用现有 `LocalDbService.set_db()` 方法，添加 `project_version` 键 |
| CONFIG-04 | 用户可以查看当前配置的版本号 | 扩展 `LocalDbService.display_db()` 显示版本号 |
| CONFIG-05 | 用户可以修改或删除已配置的版本号 | 支持 `--version=""` 清空版本号，使用 `set_project_version()` 方法 |
| CONFIG-06 | 系统提供版本号配置的帮助提示和示例 | 在 argparse help text 中添加示例："1.9.1" |
| FALLBACK-01 | 当用户未配置版本号时，系统自动使用普通格式 | 在生成入口检测 `project_version` 是否为空，调用 `generate_conventional_commit_single_call` |
| FALLBACK-02 | 格式回退过程对用户透明，无需额外操作 | 自动检测，无需用户干预 |
| FALLBACK-03 | 系统在回退时提示用户可以配置版本号 | 使用 `Logger().log()` 输出提示信息 |
| FALLBACK-04 | 回退格式与现有 conventional 命令一致 | 复用 `generate_conventional_commit_single_call` 函数 |
| DETAIL-03 | 系统自动生成临时任务号（TEMP-001） | 添加 `temp_task_counter` 配置键，每次生成后递增 |
</phase_requirements>

## 标准技术栈

### 核心库
| 库 | 版本 | 用途 | 为何标准 |
|---------|---------|---------|--------------|
| semver | 3.0.4 | SemVer 版本号解析和验证 | 官方推荐的 Python SemVer 库，活跃维护（2025-01-24 发布），支持完整的 SemVer 2.0.0 规范，提供 `Version.parse()` 和比较操作 |
| argparse | 内置 | CLI 参数解析 | Python 标准库，项目已使用，支持子命令和类型验证 |
| json | 内置 | 配置文件序列化 | Python 标准库，项目已使用 `.ai_commit_msg_config.json` |

### 现有基础设施（无需新增）
| 组件 | 文件 | 用途 | 如何使用 |
|---------|---------|---------|-------------|
| LocalDbService | `services/local_db_service.py` | 配置文件读写 | 扩展 `ConfigKeysEnum`，添加 `PROJECT_VERSION` 和 `TEMP_TASK_COUNTER` |
| ConfigService | `services/config_service.py` | 配置管理服务 | 添加 `set_project_version()` 和 `get_project_version()` 方法 |
| config_handler | `cli/config_handler.py` | CLI 配置命令处理 | 添加 `args.version` 参数处理逻辑 |
| Logger | `utils/logger.py` | 日志输出 | 用于回退提示信息 |

### 替代方案对比
| 方案 | 优点 | 缺点 | 结论 |
|------------|-----------|----------|----------|
| semver 3.0.4 | 最新（2025-01），活跃维护，API 简洁 | 需要新增依赖 | **推荐** |
| semantic-version 2.10.0 | CLAUDE.md 提到 | 较旧（2022-05），更新频率低 | 不推荐 |
| 内置 regex | 零依赖 | 需要手动维护复杂正则，无法处理版本比较 | 仅用于简单验证 |

**安装命令：**
```bash
pip install semver==3.0.4
```

**版本验证（已确认）：**
```bash
# 验证于 2026-04-08
curl -s https://pypi.org/pypi/semver/json | python -c "import sys, json; data = json.load(sys.stdin); print(data['info']['version'])"
# 输出: 3.0.4
```

## 架构模式

### 推荐项目结构（扩展现有）
```
ai_commit_msg/
├── services/
│   ├── config_service.py       # 添加版本号管理方法
│   └── local_db_service.py     # 扩展 ConfigKeysEnum
├── cli/
│   └── config_handler.py       # 添加 --version 参数处理
└── core/
    └── gen_commit_msg.py       # 添加格式选择逻辑
```

### 模式 1：配置键扩展
**用途：** 添加新的配置项到现有系统
**实现：**
```python
# services/local_db_service.py
class ConfigKeysEnum(Enum):
    # ... 现有配置键 ...
    PROJECT_VERSION = "project_version"
    TEMP_TASK_COUNTER = "temp_task_counter"

default_db = {
    CONFIG_COLLECTION_KEY: {
        # ... 现有默认值 ...
        ConfigKeysEnum.PROJECT_VERSION.value: "",
        ConfigKeysEnum.TEMP_TASK_COUNTER.value: 1,
    }
}
```

### 模式 2：版本号验证
**用途：** 验证用户输入的版本号格式
**实现：**
```python
# services/config_service.py
import semver

def set_project_version(self, version):
    if version:  # 非空时验证
        try:
            semver.Version.parse(version)
        except ValueError as e:
            raise Exception(f"Invalid SemVer format: {version}. Example: 1.9.1")

    config = ConfigService.get_config()
    config["project_version"] = version
    LocalDbService().set_db({CONFIG_COLLECTION_KEY: config})
    self.project_version = version
```

### 模式 3：格式回退逻辑
**用途：** 根据版本号配置选择提交信息格式
**实现：**
```python
# core/gen_commit_msg.py
def generate_commit_message_with_fallback(diff: str) -> str:
    config_service = ConfigService()
    project_version = config_service.get_project_version()

    if not project_version:
        # 回退到普通格式
        Logger().log("💡 未配置版本号，使用普通格式。运行 `git-ai-commit config --version=X.Y.Z` 启用详细格式")
        result = generate_conventional_commit_single_call(diff)
        return format_conventional_commit(result)
    else:
        # 使用详细格式（Phase 3 实现）
        return generate_detailed_commit(diff, project_version)
```

### 模式 4：临时任务号生成
**用途：** 生成递增的临时任务号
**实现：**
```python
# services/config_service.py
def get_next_temp_task_id(self) -> str:
    config = ConfigService.get_config()
    counter = config.get("temp_task_counter", 1)
    task_id = f"TEMP-{counter:03d}"  # TEMP-001, TEMP-002, ...

    # 递增计数器
    config["temp_task_counter"] = counter + 1
    LocalDbService().set_db({CONFIG_COLLECTION_KEY: config})

    return task_id
```

### 反模式：避免的做法
- **硬编码版本号：** 不要在代码中写死版本号，必须从配置读取
- **全局变量：** 不要使用全局变量存储版本号，使用 ConfigService 单例
- **跳过验证：** 不要接受无效的版本号格式，必须验证后再保存
- **重复逻辑：** 不要在多处实现格式选择，集中在一个入口函数

## 不要手动实现

| 问题 | 不要构建 | 使用替代方案 | 原因 |
|---------|-------------|-------------|-----|
| SemVer 解析 | 手写正则表达式解析版本号 | `semver.Version.parse()` | SemVer 2.0.0 规范复杂（支持 pre-release、build metadata），正则易出错且难维护 |
| 版本号比较 | 手动字符串分割和数字比较 | `semver.Version` 对象的比较运算符 | 需要处理 pre-release 优先级（1.0.0-alpha < 1.0.0），手动实现容易出错 |
| 配置文件锁 | 手动实现文件锁防止并发写入 | 依赖 Git 仓库的单用户特性 | 配置文件在 `.git/` 目录下，Git 操作本身是单用户的，无需复杂锁机制 |
| 任务号持久化 | 使用独立文件存储计数器 | 复用现有配置文件 | 增加文件管理复杂度，配置文件已有完整的读写机制 |

**关键洞察：** 项目已有完整的配置基础设施，Phase 1 的核心工作是"扩展"而非"重建"。避免重复造轮子，最大化复用现有代码。

## 常见陷阱

### 陷阱 1：版本号验证不完整
**问题：** 只验证格式（如 `1.9.1`），不验证边界情况（如 `0.0.0`、`999.999.999`）
**原因：** SemVer 规范允许任意大的数字，但某些系统可能有限制
**避免方法：** 使用 `semver.Version.parse()` 自动处理所有规范情况，不需要额外验证
**警告信号：** 用户输入 `1.9.1-alpha` 或 `1.9.1+build123` 时验证失败

### 陷阱 2：配置文件路径错误
**问题：** 在子目录运行命令时，配置文件路径解析错误
**原因：** `LocalDbService` 依赖 `GitService.get_git_directory()` 获取 `.git/` 路径
**避免方法：** 始终使用 `GitService.get_git_directory()` 而非 `os.getcwd()`
**警告信号：** 在子目录运行 `git-ai-commit config --version=1.0.0` 时报错找不到配置文件

### 陷阱 3：回退提示过于频繁
**问题：** 每次生成提交信息都提示用户配置版本号，造成干扰
**原因：** 未记录用户是否已看过提示
**避免方法：** 每次会话只提示一次，或者使用更温和的提示方式（如在 `config` 命令的 help 中说明）
**警告信号：** 用户反馈提示信息"太吵"

### 陷阱 4：临时任务号计数器溢出
**问题：** 计数器无限增长，可能达到 TEMP-999999
**原因：** 没有重置机制
**避免方法：** 使用 3 位数字格式（TEMP-001 到 TEMP-999），超过 999 后循环或提示用户手动重置
**警告信号：** 长期使用后任务号变得很长

## 代码示例

### 示例 1：版本号配置（CLI 入口）
```python
# cli/config_handler.py
def config_handler(args):
    config_service = ConfigService()
    has_updated = False

    # ... 现有参数处理 ...

    if args.version is not None:  # 支持空字符串清空
        try:
            config_service.set_project_version(args.version)
            if args.version:
                Logger().log(f"项目版本号设置为: {args.version}")
            else:
                Logger().log("项目版本号已清空")
            has_updated = True
        except Exception as e:
            Logger().log(f"错误: {e}")
            return

    if not has_updated:
        display_config_db = LocalDbService().display_db()
        Logger().log(display_config_db)
```

### 示例 2：版本号验证（ConfigService）
```python
# services/config_service.py
import semver

class ConfigService:
    # ... 现有代码 ...

    def set_project_version(self, version: str):
        """设置项目版本号，验证 SemVer 格式"""
        if version:  # 非空时验证
            try:
                semver.Version.parse(version)
            except ValueError:
                raise Exception(
                    f"版本号格式无效: '{version}'\n"
                    f"请使用 SemVer 格式，例如: 1.9.1, 2.0.0-beta, 1.0.0+build123"
                )

        config = ConfigService.get_config()
        config[ConfigKeysEnum.PROJECT_VERSION.value] = version
        LocalDbService().set_db({CONFIG_COLLECTION_KEY: config})

    def get_project_version(self) -> str:
        """获取项目版本号，未配置时返回空字符串"""
        config = ConfigService.get_config()
        return config.get(ConfigKeysEnum.PROJECT_VERSION.value, "")
```

### 示例 3：格式回退逻辑
```python
# core/gen_commit_msg.py
def generate_commit_with_auto_fallback(diff: str) -> str:
    """根据版本号配置自动选择格式"""
    config_service = ConfigService()
    project_version = config_service.get_project_version()

    if not project_version:
        # 回退到普通格式
        Logger().log(
            "💡 提示: 未配置项目版本号，使用普通 Conventional Commits 格式\n"
            "   运行 `git-ai-commit config --version=X.Y.Z` 启用详细格式"
        )
        result = generate_conventional_commit_single_call(diff)
        commit_type = result["type"]
        scope = result["scope"] if result["scope"] != "none" else ""
        message = result["message"]

        if scope:
            return f"{commit_type}({scope}): {message}"
        else:
            return f"{commit_type}: {message}"
    else:
        # 使用详细格式（Phase 3 实现）
        # 这里先返回占位符，Phase 3 会实现完整逻辑
        temp_task_id = config_service.get_next_temp_task_id()
        return f"feat({project_version}-{temp_task_id}): 详细格式占位符（Phase 3 实现）"
```

### 示例 4：临时任务号生成
```python
# services/config_service.py
def get_next_temp_task_id(self) -> str:
    """生成下一个临时任务号，格式: TEMP-001"""
    config = ConfigService.get_config()
    counter = config.get(ConfigKeysEnum.TEMP_TASK_COUNTER.value, 1)

    # 生成任务号
    task_id = f"TEMP-{counter:03d}"

    # 递增计数器（循环到 999 后重置）
    next_counter = (counter % 999) + 1
    config[ConfigKeysEnum.TEMP_TASK_COUNTER.value] = next_counter
    LocalDbService().set_db({CONFIG_COLLECTION_KEY: config})

    return task_id

def reset_temp_task_counter(self):
    """重置临时任务号计数器（用户手动调用）"""
    config = ConfigService.get_config()
    config[ConfigKeysEnum.TEMP_TASK_COUNTER.value] = 1
    LocalDbService().set_db({CONFIG_COLLECTION_KEY: config})
```

## 技术现状

| 旧方法 | 当前方法 | 变更时间 | 影响 |
|--------------|------------------|--------------|--------|
| 单一格式 | 多格式支持（普通/详细） | Phase 1 引入 | 需要格式选择逻辑 |
| 无版本号配置 | 版本号配置系统 | Phase 1 引入 | 新增配置项和验证 |
| 固定提交格式 | 动态格式回退 | Phase 1 引入 | 需要检测配置状态 |

**已弃用/过时：**
- 无 - Phase 1 是新功能添加，不涉及弃用

## 开放问题

1. **临时任务号计数器重置策略**
   - 已知：计数器会无限增长
   - 不明确：是否需要自动重置？重置阈值是多少？
   - 建议：提供手动重置命令 `git-ai-commit config --reset-counter`，不自动重置

2. **版本号配置作用域**
   - 已知：配置文件在 `.git/` 目录下，仅对当前仓库生效
   - 不明确：是否需要全局默认版本号？
   - 建议：Phase 1 仅支持仓库级别，全局配置留待 v2

3. **回退提示的显示频率**
   - 已知：每次生成都提示可能过于频繁
   - 不明确：用户期望的提示频率
   - 建议：每次会话只提示一次，或在配置命令的 help 中说明

## 来源

### 主要来源（HIGH 置信度）
- [semver · PyPI](https://pypi.org/project/semver/) - 官方包页面，确认版本 3.0.4
- [python-semver GitHub](https://github.com/python-semver/python-semver) - 官方仓库，活跃维护
- [Argparse Tutorial — Python 3.14.3 documentation](https://docs.python.org/3/howto/argparse.html) - Python 官方文档
- 项目现有代码：`config_service.py`, `local_db_service.py`, `config_handler.py` - 直接读取

### 次要来源（MEDIUM 置信度）
- [Semver Validation in Python — Parse, Compare & CI/CD Gates](https://isvalid.dev/semver-validation-python) - SemVer 验证最佳实践
- [Python Configuration Management Best Practices](https://configu.com/blog/working-with-python-configuration-files-tutorial-best-practices/) - 配置管理模式
- [Mastering Python Configuration Files: A Complete 2026 Guide](https://copyprogramming.com/howto/design-for-dealing-with-configuration-files) - 2026 配置文件指南

### 三级来源（LOW 置信度）
- [Creating Unique IDs in JavaScript](https://copyprogramming.com/howto/javascript-create-unique-id-counter-javascript) - 计数器模式参考（跨语言）
- [Fallback Patterns for AI Applications](https://michaeljohnpena.com/blog/2024-09-24-fallback-patterns) - 回退模式设计

## 元数据

**置信度细分：**
- 标准技术栈: HIGH - semver 库版本已验证，现有代码已审查
- 架构模式: HIGH - 基于现有代码结构，扩展点明确
- 陷阱识别: MEDIUM - 基于通用最佳实践，需实际测试验证

**研究日期：** 2026-04-08
**有效期至：** 2026-05-08（30天，配置管理模式稳定）
