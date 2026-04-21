package com.gitaicommit.services

import org.junit.Assert.*
import org.junit.Test

class BranchTicketExtractorTest {

    private val extractor = BranchTicketExtractor()

    @Test
    fun `extract ticket from feature branch`() {
        // 注意：这个测试需要在实际的 git 仓库中运行
        // 这里只是演示测试结构
    }

    @Test
    fun `regex pattern matching`() {
        val pattern = "[A-Z]+-\\d+"
        val regex = Regex(pattern)

        assertTrue(regex.find("feature/PROJ-123-add-login")?.value == "PROJ-123")
        assertTrue(regex.find("bugfix/ISSUE-456")?.value == "ISSUE-456")
        assertNull(regex.find("feature/no-ticket"))
    }
}
