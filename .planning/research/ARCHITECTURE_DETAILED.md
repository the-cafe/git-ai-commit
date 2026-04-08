# 详细提交信息生成系统架构

**项目:** git-ai-commit 详细格式增强
**研究日期:** 2026-04-08
**置信度:** MEDIUM

## 推荐架构

详细格式生成系统采用分层架构，在现有 git-ai-commit 基础上新增专门的组件来处理详细格式需求。

```
┌─────────────────────────────────────────────────────────────┐
│                      IDEA Plugin Layer                       │
│  (调用入口，传递 repo_path, version_config, format_type)      │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│                  Format Orchestrator                         │
│  - 检测是否配置版本号                                          │
│  - 决定使用详细格式 vs 普通格式                                │
│  - 协调各组件调用顺序                                          │
└────┬────────────────────┬─────────────────────┬─────────────┘
     │                    │                     │
     ▼                    ▼                     ▼
┌──────────┐      ┌──────────────┐      ┌─────────────────┐
│ Version  │      │ Change       │      │ Prompt          │
│ Manager  │      │ Classifier   │      │ Builder         │
│          │      │              │      │                 │
│ - 读取   │      │ - 解析 diff  │      │ - 构建详细格式  │
│ - 验证   │      │ - 分类变更   │      │   prompt        │
│ - 格式化 │      │ - 提取关键   │      │ - 注入分类结果  │
└──────────┘      │   信息       │      │ - 添加示例      │
                  └──────────────┘      └─────────────────┘
                           │                     │
                           └──────────┬──────────┘
                                      ▼
                           ┌─────────────────────┐
                           │  LLM Service        │
                           │  (现有)             │
                           │  - OpenAI           │
                           │  - Anthropic        │
                           │  - Ollama           │
                           └──────────┬──────────┘
                                      │
                                      ▼
                           ┌─────────────────────┐
                           │ Message Formatter   │
                           │ - 生成临时任务号    │
                           │ - 组装最终格式      │
                           │ - 验证格式正确性    │
                           └─────────────────────┘
                                      │
                                      ▼
                           ┌─────────────────────┐
                           │  返回给 IDEA Plugin │
                           └─────────────────────┘
```

## 组件边界

### 1. Format Orchestrator (格式编排器)
**职责:** 详细格式生成的入口点和协调中心

**输入:**
- `repo_path`: Git 仓库路径
- `diff`: Git diff 内容
- `format_type`: "detailed" | "normal" | "conventional"

**输出:** 格式化的提交信息字符串

**通信:**
- → Version Manager: 获取版本号配置
- → Change Classifier: 获取变更分类结果
- → Prompt Builder: 传递分类结果构建 prompt
- → LLM Service: 调用 LLM 生成内容
- → Message Formatter: 组装最终格式

**实现:** `ai_commit_msg/core/detailed_format_orchestrator.py` (新建)

---

### 2. Version Manager (版本号管理器)
**职责:** 管理项目级别的版本号配置

**数据结构:**
```python
{
    "version_number": "1.9.1",
    "format_pattern": "{version}-{task}",
    "enabled": True
}
```

**存储:** 使用 LocalDbService，按 repo_path 隔离

**通信:**
- ← Format Orchestrator: 被查询版本配置
- → LocalDbService: 读写配置数据

**实现:** `ai_commit_msg/services/version_manager.py` (新建)

---

### 3. Change Classifier (变更分类器)
**职责:** 解析和分类 git diff 内容

**分类规则:**
- **数据库变更**: `*.sql`, `*migration*.py`, `models.py`
- **API 变更**: `*routes*.py`, `*api*.py`, `*controller*.py`
- **业务逻辑**: `*service*.py`, `*handler*.py`
- **配置变更**: `*.yaml`, `*.json`, `*.env`
- **UI 变更**: `*.vue`, `*.jsx`, `*.tsx`, `*.css`

**输出:**
```python
{
    "database_changes": [...],
    "api_changes": [...],
    "business_logic_changes": [...],
    "config_changes": [...],
    "ui_changes": [...]
}
```

**通信:**
- ← Format Orchestrator: 被调用进行分类
- → Prompt Builder: 传递分类结果

**实现:** `ai_commit_msg/core/change_classifier.py` (新建)

---

### 4. Prompt Builder (提示构建器)
**职责:** 构建详细格式专用的 LLM prompt

**Prompt 结构:**
- System message: 格式规范 + 示例
- User message: diff + 分类上下文

**通信:**
- ← Format Orchestrator: 接收分类结果和配置
- → LLM Service: 传递构建好的 prompt

**实现:** `ai_commit_msg/core/detailed_prompt_builder.py` (新建)

---

### 5. Message Formatter (消息格式化器)
**职责:** 格式化 LLM 输出为最终提交信息

**处理逻辑:**
1. 解析 LLM 输出
2. 生成临时任务号（TEMP-001）
3. 组装格式：`{type}({version}-{task}): {summary}`
4. 添加变更列表
5. 验证格式

**通信:**
- ← Format Orchestrator: 接收 LLM 输出
- → Format Orchestrator: 返回最终结果

**实现:** `ai_commit_msg/core/message_formatter.py` (新建)

---

## 数据流

### 详细格式生成流程

```
IDEA Plugin 调用
   ↓
Format Orchestrator 接收
   ↓
Version Manager 检查配置
   ├─ 有配置 → 继续
   └─ 无配置 → 回退到普通格式
   ↓
Change Classifier 分析 diff
   ↓
Prompt Builder 构建 prompt
   ↓
LLM Service 生成内容
   ↓
Message Formatter 格式化
   ↓
返回给 IDEA Plugin
```

## 构建顺序

### Phase 1: 基础设施层
1. Version Manager (无依赖)
2. 扩展 Config Service

**验收:** 可以存储和读取版本配置

### Phase 2: 变更分析层
3. Change Classifier (无依赖)

**验收:** 分类准确率 > 80%

### Phase 3: Prompt 构建层
4. Prompt Builder (依赖: Change Classifier)

**验收:** Prompt 包含完整格式说明

### Phase 4: 格式化层
5. Message Formatter (依赖: Version Manager)

**验收:** 格式符合规范

### Phase 5: 编排层
6. Format Orchestrator (依赖: 所有组件)

**验收:** 完整流程可运行

### Phase 6: 集成层
7. IDEA Plugin 接口

**验收:** 插件可调用详细格式生成

## 关键技术决策

### 1. 变更分类策略
**决策:** 基于规则的分类 + LLM 辅助
**理由:** 速度快、成本低、准确性高

### 2. 临时任务号生成
**决策:** 内存计数器，不持久化
**理由:** 用户需手动替换，持久化价值有限

### 3. 版本配置存储
**决策:** LocalDbService，按 repo_path 隔离
**理由:** 复用现有基础设施，支持多项目

### 4. 回退机制
**决策:** 无配置时自动回退
**理由:** 向后兼容，不破坏现有功能

### 5. Prompt 设计
**决策:** 结构化 prompt + 示例 + 分类上下文
**理由:** 提高输出一致性和准确性

## 源引用

- [Commit Message Generator Guide](https://indibloghub.com/post/git-commit-message-generator-meaningful-version-history)
- [Repository Intelligence 2026](https://iterathon.tech/blog/repository-intelligence-ai-code-understanding-enterprise-2026)
- [Automated Classification of Source Code Changes](https://arxiv.org/html/2602.14591v1)
- [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)
- [Tower 16 AI Commits](https://www.git-tower.com/blog/tower-mac-16)
