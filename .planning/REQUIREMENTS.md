# 需求文档

**项目：** Git AI Commit - 详细提交信息增强
**版本：** v1.0
**日期：** 2026-04-08

## v1 需求

### 配置管理（CONFIG）

- [ ] **CONFIG-01**: 用户可以通过可视化界面配置项目版本号（如 "1.9.1"）
- [ ] **CONFIG-02**: 系统自动验证版本号格式符合 SemVer 规范
- [ ] **CONFIG-03**: 版本号配置持久化到 `.ai_commit_msg_config.json` 文件
- [ ] **CONFIG-04**: 用户可以查看当前配置的版本号
- [ ] **CONFIG-05**: 用户可以修改或删除已配置的版本号
- [ ] **CONFIG-06**: 系统提供版本号配置的帮助提示和示例

### 详细格式生成（DETAIL）

- [ ] **DETAIL-01**: 系统生成包含版本号、临时任务号、标题和详细列表的提交信息
- [ ] **DETAIL-02**: 提交信息格式为：`type(version-taskid): 标题\n\n- 变更点1\n- 变更点2\n...`
- [ ] **DETAIL-03**: 系统自动生成临时任务号（格式：TEMP-001）供用户替换
- [ ] **DETAIL-04**: 详细列表包含 3-10 个具体的技术变更点
- [ ] **DETAIL-05**: 每个变更点描述清晰、具体，聚焦业务影响和技术决策
- [ ] **DETAIL-06**: 支持 bugfix 和 feature 两种提交类型的详细格式

### 智能变更分类（CLASSIFY）

- [ ] **CLASSIFY-01**: 系统自动分析 git diff 并分类变更为：数据库、API、业务逻辑、配置、UI
- [ ] **CLASSIFY-02**: 基于文件路径模式识别变更类型（如 `models/` → 数据库）
- [ ] **CLASSIFY-03**: 基于代码内容关键词识别变更类型（如 `CREATE TABLE` → 数据库）
- [ ] **CLASSIFY-04**: 基于文件扩展名识别变更类型（如 `.sql` → 数据库）
- [ ] **CLASSIFY-05**: 系统按优先级组织变更描述（数据库 > API > 业务逻辑 > 配置 > UI）
- [ ] **CLASSIFY-06**: 系统提取关键变更信息（新增/修改/删除的文件、函数、类）

### 格式回退机制（FALLBACK）

- [ ] **FALLBACK-01**: 当用户未配置版本号时，系统自动使用普通 Conventional Commits 格式
- [ ] **FALLBACK-02**: 格式回退过程对用户透明，无需额外操作
- [ ] **FALLBACK-03**: 系统在回退时提示用户可以配置版本号以启用详细格式
- [ ] **FALLBACK-04**: 回退格式与现有的 `conventional` 命令生成的格式一致

### LLM 集成（LLM）

- [ ] **LLM-01**: 系统支持 OpenAI、Anthropic、Ollama 三种 LLM 提供商
- [ ] **LLM-02**: 系统针对不同 LLM 提供商优化 prompt
- [ ] **LLM-03**: 系统使用结构化输出（JSON）确保格式一致性
- [ ] **LLM-04**: 系统处理 LLM 上下文窗口限制（压缩 diff、分段处理）
- [ ] **LLM-05**: 系统验证 LLM 生成的输出格式完整性
- [ ] **LLM-06**: 系统在 LLM 调用失败时提供清晰的错误信息和重试选项

### IDEA 插件集成（IDEA）

- [ ] **IDEA-01**: IDEA 插件提供版本号配置界面
- [ ] **IDEA-02**: 插件在生成提交信息后高亮显示临时任务号
- [ ] **IDEA-03**: 插件提供快捷方式快速跳转到临时任务号进行替换
- [ ] **IDEA-04**: 插件正确处理不同操作系统的换行符（\n vs \r\n）
- [ ] **IDEA-05**: 插件在提交前检测临时任务号并提示用户替换
- [ ] **IDEA-06**: 插件支持 Windows、macOS、Linux 三个平台

### 性能与可靠性（PERF）

- [ ] **PERF-01**: 中等规模提交（5-20 个文件）的生成时间 < 10 秒
- [ ] **PERF-02**: 大型提交（>20 个文件）的生成时间 < 30 秒
- [ ] **PERF-03**: 系统支持处理 500+ 行的 diff
- [ ] **PERF-04**: 系统在网络故障时提供离线降级方案
- [ ] **PERF-05**: 系统提供生成进度指示器
- [ ] **PERF-06**: 系统异步处理，不阻塞 IDE 界面

## v2 需求（延后）

### 高级功能

- [ ] **ADV-01**: 多级详细程度控制（简洁、标准、详细）
- [ ] **ADV-02**: 从分支名智能提取任务号建议
- [ ] **ADV-03**: 学习历史提交模式，优化生成质量
- [ ] **ADV-04**: 提交信息模板系统
- [ ] **ADV-05**: 提交信息统计分析

### 扩展支持

- [ ] **EXT-01**: VS Code 插件支持
- [ ] **EXT-02**: PyCharm 插件支持
- [ ] **EXT-03**: 其他 JetBrains IDE 支持
- [ ] **EXT-04**: 集成 Jira API 自动获取任务号
- [ ] **EXT-05**: 集成 GitHub Issues API 自动获取 issue 号

## Out of Scope（明确排除）

- **自动任务号识别** — 识别错误率高，用户手动替换更可控
- **多语言提交信息** — 保持中文格式，团队应统一语言
- **实时协作编辑** — 提交信息是个人行为，不需要协作
- **复杂模板系统** — 过度灵活导致格式混乱，提供预设格式即可
- **自动提交功能** — 危险，用户应保持对提交的控制权
- **提交信息 AI 评分** — 主观性强，通过 code review 保证质量
- **CLI 复杂交互** — 专注 IDE 集成，CLI 仅作为底层工具

## 需求追溯

### 追溯表格

| 需求 | 阶段 | 状态 |
|------|------|------|
| CONFIG-01 | Phase 1 | Pending |
| CONFIG-02 | Phase 1 | Pending |
| CONFIG-03 | Phase 1 | Pending |
| CONFIG-04 | Phase 1 | Pending |
| CONFIG-05 | Phase 1 | Pending |
| CONFIG-06 | Phase 1 | Pending |
| DETAIL-01 | Phase 3 | Pending |
| DETAIL-02 | Phase 3 | Pending |
| DETAIL-03 | Phase 1 | Pending |
| DETAIL-04 | Phase 3 | Pending |
| DETAIL-05 | Phase 3 | Pending |
| DETAIL-06 | Phase 3 | Pending |
| CLASSIFY-01 | Phase 2 | Pending |
| CLASSIFY-02 | Phase 2 | Pending |
| CLASSIFY-03 | Phase 2 | Pending |
| CLASSIFY-04 | Phase 2 | Pending |
| CLASSIFY-05 | Phase 2 | Pending |
| CLASSIFY-06 | Phase 2 | Pending |
| FALLBACK-01 | Phase 1 | Pending |
| FALLBACK-02 | Phase 1 | Pending |
| FALLBACK-03 | Phase 1 | Pending |
| FALLBACK-04 | Phase 1 | Pending |
| LLM-01 | Phase 3 | Pending |
| LLM-02 | Phase 3 | Pending |
| LLM-03 | Phase 3 | Pending |
| LLM-04 | Phase 3 | Pending |
| LLM-05 | Phase 3 | Pending |
| LLM-06 | Phase 3 | Pending |
| IDEA-01 | Phase 4 | Pending |
| IDEA-02 | Phase 4 | Pending |
| IDEA-03 | Phase 4 | Pending |
| IDEA-04 | Phase 4 | Pending |
| IDEA-05 | Phase 4 | Pending |
| IDEA-06 | Phase 4 | Pending |
| PERF-01 | Phase 3 | Pending |
| PERF-02 | Phase 3 | Pending |
| PERF-03 | Phase 3 | Pending |
| PERF-04 | Phase 4 | Pending |
| PERF-05 | Phase 4 | Pending |
| PERF-06 | Phase 4 | Pending |

### 阶段分组

#### Phase 1: 基础设施和配置管理
**需求：** CONFIG-01, CONFIG-02, CONFIG-03, CONFIG-04, CONFIG-05, CONFIG-06, FALLBACK-01, FALLBACK-02, FALLBACK-03, FALLBACK-04, DETAIL-03
**目标：** 建立版本号配置系统和格式回退机制

#### Phase 2: Git Diff 解析和智能变更分类
**需求：** CLASSIFY-01, CLASSIFY-02, CLASSIFY-03, CLASSIFY-04, CLASSIFY-05, CLASSIFY-06
**目标：** 实现结构化的 diff 解析和多维度变更分类

#### Phase 3: 详细提交信息生成
**需求：** DETAIL-01, DETAIL-02, DETAIL-04, DETAIL-05, DETAIL-06, LLM-01, LLM-02, LLM-03, LLM-04, LLM-05, LLM-06, PERF-01, PERF-02, PERF-03
**目标：** 优化 LLM prompt 生成详细的、结构化的提交信息

#### Phase 4: IDEA 插件集成和用户体验优化
**需求：** IDEA-01, IDEA-02, IDEA-03, IDEA-04, IDEA-05, IDEA-06, PERF-04, PERF-05, PERF-06
**目标：** 提供流畅的 IDEA 插件使用体验

## 需求优先级

### P0 - 必须有（MVP）
- CONFIG-01, CONFIG-02, CONFIG-03
- DETAIL-01, DETAIL-02, DETAIL-03, DETAIL-04
- CLASSIFY-01, CLASSIFY-02, CLASSIFY-05
- FALLBACK-01, FALLBACK-02
- LLM-01, LLM-03

### P1 - 应该有
- CONFIG-04, CONFIG-05, CONFIG-06
- DETAIL-05, DETAIL-06
- CLASSIFY-03, CLASSIFY-04, CLASSIFY-06
- FALLBACK-03, FALLBACK-04
- LLM-02, LLM-04, LLM-05, LLM-06

### P2 - 可以有
- IDEA-01, IDEA-02, IDEA-03, IDEA-04, IDEA-05, IDEA-06
- PERF-01, PERF-02, PERF-03, PERF-04, PERF-05, PERF-06

## 验收标准

### 功能验收
1. 用户可以配置版本号并生成包含版本号的详细提交信息
2. 生成的提交信息格式符合示例要求
3. 智能变更分类准确率 > 70%（通过人工标注验证）
4. 无版本号配置时自动回退到普通格式
5. 支持 OpenAI、Anthropic、Ollama 三种 LLM 提供商

### 质量验收
1. 消息-代码一致性 > 90%（通过人工抽样验证）
2. 生成时间 < 10 秒（中等规模提交）
3. 测试覆盖率 > 80%
4. 无 P0/P1 级别 bug

### 用户体验验收
1. 配置过程简单（< 5 分钟）
2. 临时任务号替换提示明显
3. IDEA 插件集成流畅
4. 错误信息清晰易懂

## 示例场景

### 场景 1：首次配置和使用
1. 用户安装 git-ai-commit 工具
2. 用户通过 `git-ai-commit config --version=1.9.1` 配置版本号
3. 用户修改代码并 `git add`
4. 用户运行 `git-ai-commit` 或通过 IDEA 插件触发
5. 系统生成详细格式的提交信息，包含版本号和临时任务号
6. 用户在 IDEA 中看到高亮的临时任务号，替换为实际任务号（如 15118）
7. 用户确认并提交

**预期输出：**
```
bugfix(1.9.1-15118): 【SIT】【免疫组化切片】反复取消切片后，执行状态不正确

- 根据病例是否存在染色封片工作站动态决定任务流转方向
- 添加了 DoctorAdviecDyeingUserTask 和 DoctorAdviceSlideUserTask 的条件判断
- 实现了基于工作站存在性的任务类型分配机制
```

### 场景 2：无版本号配置时的回退
1. 用户未配置版本号
2. 用户修改代码并 `git add`
3. 用户运行 `git-ai-commit`
4. 系统检测到无版本号配置，自动使用普通格式
5. 系统提示："未配置版本号，使用普通格式。运行 `git-ai-commit config --version=X.Y.Z` 启用详细格式"

**预期输出：**
```
fix: 修复免疫组化切片执行状态问题
```

### 场景 3：大型提交的处理
1. 用户进行大规模重构（50+ 个文件）
2. 用户运行 `git-ai-commit`
3. 系统检测到大型提交，显示进度指示器
4. 系统压缩 diff，仅保留关键变更信息
5. 系统生成简化版详细列表（5-7 项主要变更）
6. 生成时间 < 30 秒

**预期输出：**
```
refactor(1.9.1-TEMP-001): 重构病理申请模块架构

- 重构数据库模型层，优化表结构和索引
- 重构 API 层，统一接口规范和错误处理
- 重构业务逻辑层，提取公共服务
- 更新配置文件，支持新的模块结构
- 更新前端组件，适配新的 API 接口
```

---

**需求文档版本：** v1.0
**最后更新：** 2026-04-08
