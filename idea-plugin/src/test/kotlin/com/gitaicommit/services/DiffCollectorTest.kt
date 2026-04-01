package com.gitaicommit.services

import com.intellij.openapi.vcs.changes.Change
import com.intellij.openapi.vcs.changes.ContentRevision
import com.intellij.openapi.vcs.history.VcsRevisionNumber
import com.intellij.testFramework.LightPlatformTestCase
import com.intellij.vcsUtil.VcsUtil
import java.nio.file.Files
import java.nio.file.Path
import java.util.Comparator

class DiffCollectorTest : LightPlatformTestCase() {

    private val collector = DiffCollector()

    fun testBuildUnifiedDiffFromSelectedChanges() {
        val baseDir = Files.createTempDirectory("git-ai-commit-diff")
        val file = baseDir.resolve("src/App.kt")
        Files.createDirectories(file.parent)
        Files.writeString(file, "fun greet() = \"new\"\n")

        try {
            val change = Change(
                textRevision(file, "fun greet() = \"old\"\n", VcsRevisionNumber.Int(1)),
                textRevision(file, "fun greet() = \"new\"\n", VcsRevisionNumber.NULL)
            )

            val diff = collector.buildUnifiedDiff(baseDir, listOf(change))

            assertNotNull(diff)
            assertTrue(diff!!.contains("diff --git"))
            assertTrue(diff.contains("-fun greet() = \"old\""))
            assertTrue(diff.contains("+fun greet() = \"new\""))
        } finally {
            Files.walk(baseDir)
                .sorted(Comparator.reverseOrder())
                .forEach { Files.deleteIfExists(it) }
        }
    }

    private fun textRevision(path: Path, content: String, revision: VcsRevisionNumber): ContentRevision {
        return object : ContentRevision {
            override fun getContent(): String = content

            override fun getFile() = VcsUtil.getFilePath(path, false)

            override fun getRevisionNumber(): VcsRevisionNumber = revision
        }
    }
}
