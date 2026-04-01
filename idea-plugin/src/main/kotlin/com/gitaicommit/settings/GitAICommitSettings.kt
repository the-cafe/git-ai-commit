package com.gitaicommit.settings

import com.intellij.openapi.components.PersistentStateComponent
import com.intellij.openapi.components.State
import com.intellij.openapi.components.Storage
import com.intellij.openapi.components.service
import com.intellij.util.xmlb.XmlSerializerUtil

@State(
    name = "GitAICommitSettings",
    storages = [Storage("GitAICommitPlugin.xml")]
)
class GitAICommitSettings : PersistentStateComponent<GitAICommitSettings> {

    var provider: String = "openai"
    var apiKey: String = ""
    var apiBase: String = ""
    var model: String = ""
    var releaseVersion: String = "1.0.0"
    var ticketIdRegex: String = "[A-Z]+-\\d+"
    var requestTimeoutMs: Int = 30000
    var customPrompt: String = DEFAULT_CUSTOM_PROMPT

    override fun getState(): GitAICommitSettings = this

    override fun loadState(state: GitAICommitSettings) {
        XmlSerializerUtil.copyBean(state, this)
        customPrompt = PromptTextSanitizer.normalizePrompt(customPrompt, DEFAULT_CUSTOM_PROMPT)
    }

    companion object {
        val DEFAULT_CUSTOM_PROMPT: String = """
根据以下 git diff 生成提交消息。只返回 JSON 格式：{"type": "类型", "summary": "中文摘要"}

类型必须是以下之一：feature, bugfix, docs, style, refactor, revert, build, config
摘要必须是简体中文，简洁描述改动内容，不超过50字。

Git diff:
{diff}
        """.trimIndent()

        fun getInstance(): GitAICommitSettings = service()
    }
}
