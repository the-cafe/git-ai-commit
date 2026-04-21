# Phase 2: Git Diff 解析和智能变更分类 - Discussion Log

> **Audit trail only.** Do not use as input to planning, research, or execution agents.
> Decisions are captured in CONTEXT.md -- this log preserves the alternatives considered.

**Date:** 2026-04-09
**Phase:** 02-git-diff
**Areas discussed:** 分类策略, 分类粒度, 语言覆盖

---

## 分类策略

| Option | Description | Selected |
|--------|-------------|----------|
| 规则优先 + LLM 辅助 | 先用文件路径/扩展名规则快速分类，仅对无法确定的文件才调用 LLM。速度快、可靠，LLM 用量最少 | ✓ |
| 纯规则匹配 | 仅用文件路径模式和关键词匹配，不涉及 LLM。最快但准确率有限 | |
| 全部交给 LLM | 将分类完全交给 Phase 3 的 LLM prompt。不在 Phase 2 做分类逻辑，仅做 diff 解析和信息提取 | |

**User's choice:** 规则优先 + LLM 辅助
**Notes:** 推荐选项。Phase 2 做规则分类，未分类文件的信息传递给 Phase 3 由 LLM 补充。

---

## 分类粒度

| Option | Description | Selected |
|--------|-------------|----------|
| 按文件分类 | 每个变更文件归入一个类别。简单可靠，与 diff 的文件结构天然对齐 | ✓ |
| 按代码块分类 | 同一文件内不同 hunk 可能属于不同类别。更精确但复杂度高 | |
| 按文件分类 + 多标签 | 每个文件可以有多个类别标签。兼顾简单性和准确性 | |

**User's choice:** 按文件分类
**Notes:** 推荐选项。简单可靠，与 unidiff 的 PatchedFile 结构天然对齐。

---

## 语言覆盖

| Option | Description | Selected |
|--------|-------------|----------|
| 通用多语言 | 支持常见语言的文件路径模式（Java/Python/JS/TS/Go/C# 等） | ✓ |
| Java 生态优先 | 优先支持 Java/Spring Boot 项目路径模式，其他语言基础支持 | |
| 可配置规则 | 分类规则通过配置文件定义，用户可自定义 | |

**User's choice:** 通用多语言
**Notes:** 推荐选项。工具定位为通用 git 工具，应覆盖主流编程语言。

---

## Claude's Discretion

- 分类规则的具体关键词列表和文件路径模式
- 测试用例的具体 diff 内容设计
- 模块内部的函数/类组织方式

## Deferred Ideas

None
