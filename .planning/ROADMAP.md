# 项目路线图

**项目：** Git AI Commit - 详细提交信息增强
**版本：** v1.0
**粒度：** Coarse
**总需求：** 40 个 v1 需求
**覆盖率：** 100%

## Phases

- [ ] **Phase 1: 基础设施和配置管理** - 建立版本号配置系统和格式回退机制
- [ ] **Phase 2: Git Diff 解析和智能变更分类** - 实现结构化的 diff 解析和多维度变更分类
- [ ] **Phase 3: 详细提交信息生成** - 优化 LLM prompt 生成详细的、结构化的提交信息
- [ ] **Phase 4: IDEA 插件集成和用户体验优化** - 提供流畅的 IDEA 插件使用体验

## Phase Details

### Phase 1: 基础设施和配置管理
**Goal**: 用户可以配置版本号并在无配置时自动回退到普通格式
**Depends on**: Nothing (first phase)
**Requirements**: CONFIG-01, CONFIG-02, CONFIG-03, CONFIG-04, CONFIG-05, CONFIG-06, FALLBACK-01, FALLBACK-02, FALLBACK-03, FALLBACK-04, DETAIL-03
**Success Criteria** (what must be TRUE):
  1. 用户可以通过命令配置项目版本号并持久化保存到配置文件
  2. 用户可以查看、修改或删除已配置的版本号
  3. 用户在未配置版本号时自动获得普通 Conventional Commits 格式的提交信息
  4. 系统在回退时提示用户可以配置版本号以启用详细格式
  5. 系统自动生成临时任务号（格式：TEMP-001）供用户后续替换
**Plans**: 3 plans

Plans:
- [ ] 01-01-PLAN.md — 扩展配置基础设施以支持项目版本号和临时任务号管理
- [ ] 01-02-PLAN.md — 扩展 CLI 配置命令以支持版本号管理
- [ ] 01-03-PLAN.md — 实现格式回退机制，未配置版本号时自动使用普通格式

### Phase 2: Git Diff 解析和智能变更分类
**Goal**: 系统能够自动分析代码变更并准确分类为不同类型
**Depends on**: Phase 1
**Requirements**: CLASSIFY-01, CLASSIFY-02, CLASSIFY-03, CLASSIFY-04, CLASSIFY-05, CLASSIFY-06
**Success Criteria** (what must be TRUE):
  1. 系统能够识别数据库、API、业务逻辑、配置、UI 五种变更类型
  2. 系统基于文件路径、代码内容、文件扩展名进行多维度分类
  3. 系统按优先级组织变更描述（数据库 > API > 业务逻辑 > 配置 > UI）
  4. 系统提取关键变更信息（新增/修改/删除的文件、函数、类）
**Plans**: TBD

### Phase 3: 详细提交信息生成
**Goal**: 用户获得包含版本号、任务号和详细变更列表的结构化提交信息
**Depends on**: Phase 2
**Requirements**: DETAIL-01, DETAIL-02, DETAIL-04, DETAIL-05, DETAIL-06, LLM-01, LLM-02, LLM-03, LLM-04, LLM-05, LLM-06, PERF-01, PERF-02, PERF-03
**Success Criteria** (what must be TRUE):
  1. 用户获得格式为 `type(version-taskid): 标题\n\n- 变更点1\n- 变更点2` 的提交信息
  2. 提交信息包含 3-10 个具体的技术变更点，每个描述清晰具体
  3. 系统支持 OpenAI、Anthropic、Ollama 三种 LLM 提供商
  4. 中等规模提交（5-20 个文件）的生成时间 < 10 秒
  5. 系统能够处理大型提交（>20 个文件，500+ 行 diff）并在 30 秒内完成
**Plans**: TBD

### Phase 4: IDEA 插件集成和用户体验优化
**Goal**: 用户在 IDEA 中获得流畅的详细提交信息生成体验
**Depends on**: Phase 3
**Requirements**: IDEA-01, IDEA-02, IDEA-03, IDEA-04, IDEA-05, IDEA-06, PERF-04, PERF-05, PERF-06
**Success Criteria** (what must be TRUE):
  1. 用户可以在 IDEA 插件中配置版本号
  2. 用户在生成提交信息后看到高亮显示的临时任务号
  3. 用户可以通过快捷方式快速跳转到临时任务号进行替换
  4. 插件在提交前检测临时任务号并提示用户替换
  5. 插件支持 Windows、macOS、Linux 三个平台并正确处理换行符
**Plans**: TBD
**UI hint**: yes

## Progress

| Phase | Plans Complete | Status | Completed |
|-------|----------------|--------|-----------|
| 1. 基础设施和配置管理 | 0/3 | Not started | - |
| 2. Git Diff 解析和智能变更分类 | 0/0 | Not started | - |
| 3. 详细提交信息生成 | 0/0 | Not started | - |
| 4. IDEA 插件集成和用户体验优化 | 0/0 | Not started | - |

## Research Flags

### Phase 2: Git Diff 解析和智能变更分类
**需要更深入研究的原因：**
- 变更分类准确率直接影响生成质量，现有方法准确率仅 59-78%
- 不同项目的目录结构差异大，需要可配置的规则系统
- 多语言项目的分类策略需要特殊处理

**建议研究方向：**
- 收集多个真实项目的 diff 样本测试分类规则
- 研究机器学习方法是否能提升分类准确性
- 设计可配置的规则引擎

### Phase 3: 详细提交信息生成
**需要更深入研究的原因：**
- LLM prompt 优化是一个迭代过程，需要大量实验
- 不同 LLM 提供商的能力差异需要针对性优化
- 上下文窗口管理策略需要根据实际使用情况调整

**建议研究方向：**
- A/B 测试不同的 prompt 模板
- 建立生成质量评估指标
- 测试不同 LLM 提供商的生成质量

## Dependencies

```
Phase 1 (配置管理)
    ↓
Phase 2 (变更分类) ← 依赖 Phase 1 的配置系统
    ↓
Phase 3 (详细生成) ← 依赖 Phase 1 的配置 + Phase 2 的分类
    ↓
Phase 4 (插件集成) ← 依赖 Phase 1-3 的所有功能
```

## Key Risks

| 风险 | 概率 | 影响 | 缓解措施 |
|------|------|------|---------|
| 变更分类准确率不足 | 中 | 高 | 多维度特征提取，可配置规则，人工反馈循环 |
| LLM 生成质量不稳定 | 中 | 高 | Prompt 优化，结构化输出，多提供商支持 |
| 上下文窗口溢出 | 低 | 中 | Diff 压缩，分段处理，动态 token 预算 |
| IDEA 插件集成困难 | 低 | 中 | 提前研究 API，参考现有插件，寻求社区帮助 |

## Success Metrics

项目成功的标志：

**功能完整性：**
- ✓ 版本号配置功能正常工作
- ✓ 详细格式生成准确且格式正确
- ✓ 智能变更分类准确率 > 70%
- ✓ 格式回退机制可靠

**质量指标：**
- ✓ 消息-代码一致性 > 90%（通过人工抽样验证）
- ✓ 生成时间 < 10 秒（对于中等规模提交）
- ✓ 用户满意度 > 80%（通过反馈收集）

**技术指标：**
- ✓ 测试覆盖率 > 80%
- ✓ 支持 OpenAI、Anthropic、Ollama 三种提供商
- ✓ 无重大 bug（P0/P1 bug = 0）

---

**路线图版本：** v1.0
**创建日期：** 2026-04-08
**下一步：** `/gsd:plan-phase 1`
