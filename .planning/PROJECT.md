# Git AI Commit - 详细提交信息增强

## What This Is

为 git-ai-commit 工具增加详细提交信息格式支持，生成包含版本号、任务号和详细变更列表的结构化提交信息，专门用于 IDEA 插件集成。

## Core Value

生成结构化、详细的提交信息，清晰展示每次提交的具体技术变更点，而不仅仅是概括性描述。

## Requirements

### Validated

- ✓ 基础 AI 提交信息生成功能 — existing
- ✓ 支持多种 LLM 提供商（OpenAI、Anthropic、Ollama）— existing
- ✓ Conventional Commits 格式支持 — existing
- ✓ 配置管理系统 — existing

### Active

- [ ] 版本号配置功能（通过可视化界面配置和保存）
- [ ] 详细提交信息格式生成（包含版本号、任务号、详细变更列表）
- [ ] 临时任务号生成（用户可手动替换）
- [ ] 智能变更分类（基于 git diff、代码内容、文件路径）
- [ ] 格式回退机制（无版本号配置时使用普通格式）
- [ ] IDEA 插件集成支持

### Out of Scope

- CLI 命令行使用场景 — 仅专注于 IDEA 插件
- 自动任务号识别（从分支名或 commit 历史）— 用户手动替换即可
- 多语言提交信息 — 保持中文格式

## Context

**现有代码库：**
- Python 项目，使用 pip 包管理
- 核心模块：`ai_commit_msg/`
- 已有配置系统：`config_service.py`
- 已有 LLM 服务：`llm_service.py`、`llm_service_factory.py`
- 已有 prompt 系统：`core/prompt.py`、`core/gen_commit_msg.py`

**目标格式示例：**

```
bugfix(1.9.1-15118): 【SIT】【免疫组化切片】反复取消切片后，执行状态不正确

- 根据病例是否存在染色封片工作站动态决定任务流转方向
- 添加了 DoctorAdviecDyeingUserTask 和 DoctorAdviceSlideUserTask 的条件判断
- 实现了基于工作站存在性的任务类型分配机制
```

```
【feature】（V1.9.2-4012）【标本取出】支持内镜开单后做自动存放然后取出

- ma_hospital_quality_certificate增加字段auto_deposit_config 自动存放配置
- 增加三个调用自动存放的入口：pathologyApplication/save   病理申请保存-开单时候添加标本
   pathologyApplication/offlineSample/save   病理申请工作站-采样添加标本
   pathologyApplication/pageDetail/offlineSample/saveOrUpdate     申请列表病例详情-添加编辑样本-我的申请中追加标本
- 标本取出的信息会返回给交接单、汇总码
- 打包送出接口中增加确认取出的事件流程（和产品沟通确认过）
```

**变更分类逻辑：**
- 数据库变更：检测 SQL、migration 文件、model 定义
- API 变更：检测路由定义、endpoint 变更
- 业务逻辑：检测 service 层、业务方法
- 配置变更：检测配置文件、环境变量
- UI 变更：检测前端文件、样式文件

## Constraints

- **技术栈**: Python 3.x，保持现有架构
- **兼容性**: 不破坏现有功能，向后兼容
- **使用场景**: 仅针对 IDEA 插件使用
- **配置存储**: 使用现有的配置系统（local_db_service.py）
- **LLM 提示**: 需要优化 prompt 以生成详细列表

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| 使用临时任务号而非自动识别 | 用户需要灵活性，手动替换更可控 | — Pending |
| 版本号通过配置管理 | 不同项目版本号格式不同，需要可配置 | — Pending |
| 智能变更分类 | 提供结构化的变更列表，提升可读性 | — Pending |
| 保持现有架构 | 最小化改动，降低风险 | — Pending |

## Evolution

此文档在阶段转换和里程碑边界时演进。

**每次阶段转换后** (通过 `/gsd:transition`):
1. 需求失效？→ 移至 Out of Scope 并说明原因
2. 需求验证？→ 移至 Validated 并标注阶段
3. 新需求出现？→ 添加至 Active
4. 需要记录的决策？→ 添加至 Key Decisions
5. "What This Is" 仍然准确？→ 如有偏差则更新

**每次里程碑后** (通过 `/gsd:complete-milestone`):
1. 全面审查所有部分
2. Core Value 检查 — 仍然是正确的优先级？
3. 审计 Out of Scope — 原因仍然有效？
4. 更新 Context 为当前状态

---
*Last updated: 2026-04-08 after initialization*
