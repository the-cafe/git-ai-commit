# Phase 1: Git-AI-Commit 问题修复与优化

## 目标
修复 git-ai-commit 项目中影响提交信息质量的关键问题，支持自定义提交格式（如中文方括号格式），提升在 IntelliJ IDEA 插件场景下的用户体验。

## 用户自定义提交规范
```
【代码类型】（版本号 - 关联需求单/bug单 ID）这次提交的Msg
【feature】（V1.1.4-需求编号）新功能
【bugfix】（V1.1.4-bug编号）bug修复
【docs】（V1.1.4-1309）纯文档注释/更新
【style】（V1.1.4-1309）代码格式变动
【refactor】（V1.1.4）代码重构、优化
【revert】（V1.1.4）代码回退
【build】（V1.1.4-1309）代码打包
【config】（V1.1.4）项目配置修改
```

---

## Wave 1: 核心 Prompt 质量修复（最高优先级）

### Task 1.1: 修复 prompt.py 中的语法错误和提示词质量
**文件**: `ai_commit_msg/core/prompt.py`
**问题**:
- 第62行: `"Your a software engineer"` → 应为 `"You're a software engineer"`
- `"Your response cannot more than {max_length} characters"` → 缺少 `be`
- f-string 未使用插值变量（第8、26行）
**修改**:
- 修复所有语法错误
- 优化 system prompt 指令清晰度
- 增加中文 prompt 支持能力
- 要求 LLM 输出结构化提交信息

### Task 1.2: 调整默认 max_length 配置
**文件**: `ai_commit_msg/services/config_service.py`
**问题**: 默认 `max_length=50` 过短，导致 LLM 强制缩写丢失语义
**修改**:
- 将默认值从 50 提升到 120
- 确保 conventional 模式的 max_length 也合理

### Task 1.3: 添加 LLM 温度参数控制
**文件**: `ai_commit_msg/services/openai_service.py`, `ai_commit_msg/services/anthropic_service.py`
**问题**: OpenAI 未设置 temperature（默认1.0），导致输出不稳定
**修改**:
- OpenAI: 添加 `temperature=0.3`
- Anthropic: 添加 `temperature=0.3`
- Ollama: 已设为0，保持不变
- 可选：在配置中暴露 temperature 参数

---

## Wave 2: Diff 处理与 Token 优化

### Task 2.1: 添加 diff 预处理和智能截断
**文件**: `ai_commit_msg/services/git_service.py`, `ai_commit_msg/utils/git_utils.py`
**问题**: 原始 diff 无过滤，锁文件/二进制/自动生成文件占大量 token
**修改**:
- 过滤常见噪声文件（lock files, .min.js, .map, node_modules, etc.）
- 对超长 diff 进行智能截断（保留头部和文件变更摘要）
- 设置 diff 最大字符数限制（建议 8000 字符）
- 过滤二进制文件变更

### Task 2.2: 优化 Conventional Commit 的 LLM 调用策略
**文件**: `ai_commit_msg/cli/conventional_commit_handler.py`
**问题**: 分3次独立调用 LLM 获取 type/scope/body，导致结果不一致且慢
**修改**:
- 合并为单次 LLM 调用，使用结构化输出
- 新增 prompt：一次性返回 JSON `{ "type": "...", "scope": "...", "message": "..." }`
- 解析 LLM 输出并组装最终提交信息

---

## Wave 3: Bug 修复与兼容性

### Task 3.1: 修复 conventional commit 的引号 bug
**文件**: `ai_commit_msg/cli/conventional_commit_handler.py`
**问题**: 第165行 `f'"{formatted_commit}"'` 导致提交信息包含多余引号
**修改**:
```python
# 修复前
execute_cli_command(["git", "commit", "-m", f'"{formatted_commit}"'], output=True)
# 修复后
execute_cli_command(["git", "commit", "-m", formatted_commit], output=True)
```

### Task 3.2: 修复字符串比较 bug
**文件**: `ai_commit_msg/services/config_service.py`
**问题**: 第81行 `model is not ""` 使用身份比较而非值比较
**修改**: `model is not ""` → `model != ""`

### Task 3.3: 修复 diff 获取路径不一致
**文件**: `ai_commit_msg/cli/conventional_commit_handler.py`
**问题**: hook 使用 `cwd=repo_root`，但 conventional handler 不设置 cwd
**修改**: 统一使用 repo_root 作为工作目录

### Task 3.4: 更新 Anthropic 模型列表
**文件**: `ai_commit_msg/utils/models.py`
**问题**: 模型列表冻结在 2024 年初，缺少最新模型
**修改**: 添加 Claude 3.5 Sonnet、Claude 4 等新模型

---

## Wave 4: 自定义提交格式支持

### Task 4.1: 支持自定义提交消息模板
**文件**: `ai_commit_msg/services/config_service.py`, `ai_commit_msg/core/prompt.py`
**问题**: 当前只支持标准 conventional commits 格式
**修改**:
- 在配置中新增 `commit_template` 字段
- 支持用户定义自己的提交格式模板
- prompt 中注入用户自定义格式规范
- 支持中文方括号格式：`【type】（version-id）message`

### Task 4.2: 修复 help_ai_handler 中的硬编码
**文件**: `ai_commit_msg/cli/help_ai_handler.py`
**问题**: 第17行硬编码 `"Hey GPT"`
**修改**: 移除 provider 特定的称呼

---

## Wave 5: OpenAI 服务健壮性

### Task 5.1: 为 OpenAI 添加 max_tokens 限制
**文件**: `ai_commit_msg/services/openai_service.py`
**问题**: 未设置 max_tokens，可能返回过长内容
**修改**: 添加 `max_tokens=1024`，与 Anthropic 保持一致

### Task 5.2: 清理 debug 日志
**文件**: `ai_commit_msg/cli/conventional_commit_handler.py`
**问题**: 第126行残留 debug 日志
**修改**: 移除或降级为 DEBUG 级别

---

## 验证标准

### 功能验证
- [ ] 默认模式生成的提交信息准确描述代码变更
- [ ] Conventional commit 模式一次调用生成完整结果
- [ ] 自定义模板格式正确应用
- [ ] 大 diff（>10个文件）不会 token 溢出
- [ ] 引号 bug 不再出现
- [ ] 所有三个 LLM provider 行为一致

### 用户体验验证
- [ ] 提交信息长度合理（不过度缩写）
- [ ] 相同代码变更多次生成结果稳定
- [ ] IntelliJ IDEA hook 模式正常工作
- [ ] 中文提交格式正确生成

---

## 文件变更清单

| 文件 | 涉及任务 | 变更类型 |
|---|---|---|
| `ai_commit_msg/core/prompt.py` | 1.1, 4.1 | 重大修改 |
| `ai_commit_msg/services/config_service.py` | 1.2, 3.2, 4.1 | 修改 |
| `ai_commit_msg/services/openai_service.py` | 1.3, 5.1 | 修改 |
| `ai_commit_msg/services/anthropic_service.py` | 1.3 | 修改 |
| `ai_commit_msg/services/git_service.py` | 2.1 | 修改 |
| `ai_commit_msg/utils/git_utils.py` | 2.1 | 修改 |
| `ai_commit_msg/cli/conventional_commit_handler.py` | 2.2, 3.1, 3.3, 5.2 | 重大修改 |
| `ai_commit_msg/utils/models.py` | 3.4 | 修改 |
| `ai_commit_msg/cli/help_ai_handler.py` | 4.2 | 小修改 |
