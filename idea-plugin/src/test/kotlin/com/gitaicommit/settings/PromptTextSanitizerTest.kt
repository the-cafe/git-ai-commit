package com.gitaicommit.settings

import org.junit.Assert.assertEquals
import org.junit.Test
import java.nio.charset.StandardCharsets

class PromptTextSanitizerTest {

    @Test
    fun `blank prompt should fallback to default`() {
        val normalized = PromptTextSanitizer.normalizePrompt("   ", GitAICommitSettings.DEFAULT_CUSTOM_PROMPT)
        assertEquals(GitAICommitSettings.DEFAULT_CUSTOM_PROMPT, normalized)
    }

    @Test
    fun `normal prompt should keep original`() {
        val prompt = "请基于 {diff} 生成 JSON，摘要使用简体中文。"
        val normalized = PromptTextSanitizer.normalizePrompt(prompt, GitAICommitSettings.DEFAULT_CUSTOM_PROMPT)
        assertEquals(prompt, normalized)
    }

    @Test
    fun `suspicious garbled prompt should fallback to default`() {
        val garbled = "锟斤拷娴嬭瘯杩炴帴锛屽洖澶嶆牸寮忛敊璇?"
        val normalized = PromptTextSanitizer.normalizePrompt(garbled, GitAICommitSettings.DEFAULT_CUSTOM_PROMPT)
        assertEquals(GitAICommitSettings.DEFAULT_CUSTOM_PROMPT, normalized)
    }

    @Test
    fun `latin1 mojibake should be repaired to utf8`() {
        val original = "返回 JSON: {\"type\":\"feature\",\"summary\":\"测试\"}，并包含 {diff}"
        val mojibake = String(original.toByteArray(StandardCharsets.UTF_8), StandardCharsets.ISO_8859_1)
        val normalized = PromptTextSanitizer.normalizePrompt(mojibake, GitAICommitSettings.DEFAULT_CUSTOM_PROMPT)
        assertEquals(original, normalized)
    }
}
