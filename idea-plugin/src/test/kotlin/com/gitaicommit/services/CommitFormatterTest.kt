package com.gitaicommit.services

import com.gitaicommit.model.CommitDraft
import org.junit.Assert.*
import org.junit.Test

class CommitFormatterTest {

    private val formatter = CommitFormatter()

    @Test
    fun `format feature type with ticket`() {
        val draft = CommitDraft("feature", "添加用户登录功能")
        val result = formatter.format(draft, "1.0.0", "PROJ-123")

        assertTrue(result.isSuccess)
        assertEquals("【feature】（1.0.0-PROJ-123）添加用户登录功能", result.getOrNull())
    }

    @Test
    fun `format refactor type without ticket`() {
        val draft = CommitDraft("refactor", "重构数据库连接层")
        val result = formatter.format(draft, "1.0.0", null)

        assertTrue(result.isSuccess)
        assertEquals("【refactor】（1.0.0）重构数据库连接层", result.getOrNull())
    }

    @Test
    fun `use placeholder when feature type missing ticket`() {
        val draft = CommitDraft("feature", "添加新功能")
        val result = formatter.format(draft, "1.0.0", null)

        assertTrue(result.isSuccess)
        assertEquals("【feature】（1.0.0-待替换单号）添加新功能", result.getOrNull())
    }

    @Test
    fun `fail with invalid type`() {
        val draft = CommitDraft("invalid", "测试")
        val result = formatter.format(draft, "1.0.0", "PROJ-123")

        assertTrue(result.isFailure)
        assertTrue(result.exceptionOrNull()?.message?.contains("无效的提交类型") == true)
    }

    @Test
    fun `format all required ticket types`() {
        val types = listOf("feature", "bugfix", "docs", "style", "build")

        types.forEach { type ->
            val draft = CommitDraft(type, "测试内容")
            val result = formatter.format(draft, "1.0.0", "PROJ-123")
            assertTrue("$type should succeed with ticket", result.isSuccess)
        }
    }

    @Test
    fun `format all non-required ticket types`() {
        val types = listOf("refactor", "revert", "config")

        types.forEach { type ->
            val draft = CommitDraft(type, "测试内容")
            val result = formatter.format(draft, "1.0.0", null)
            assertTrue("$type should succeed without ticket", result.isSuccess)
        }
    }
}
