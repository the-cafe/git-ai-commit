package com.gitaicommit.services

import com.intellij.openapi.diff.impl.patch.IdeaTextPatchBuilder
import com.intellij.openapi.diff.impl.patch.UnifiedDiffWriter
import com.intellij.openapi.project.Project
import com.intellij.openapi.vcs.changes.Change
import com.intellij.openapi.vcs.changes.patch.PatchWriter
import java.io.BufferedReader
import java.io.InputStreamReader
import java.io.StringWriter
import java.nio.charset.StandardCharsets
import java.nio.file.Path

class DiffCollector {

    fun collectStagedDiff(project: Project): String? {
        val basePath = project.basePath ?: return null

        return try {
            val process = ProcessBuilder("git", "diff", "--cached")
                .directory(java.io.File(basePath))
                .redirectErrorStream(true)
                .start()

            val output = BufferedReader(InputStreamReader(process.inputStream, StandardCharsets.UTF_8)).use {
                it.readText()
            }

            process.waitFor()

            if (output.isBlank()) null else output
        } catch (e: Exception) {
            null
        }
    }

    fun collectCommitDiff(project: Project, includedChanges: Collection<Change>): String? {
        return collectIncludedDiff(project, includedChanges) ?: collectStagedDiff(project)
    }

    fun collectIncludedDiff(project: Project, includedChanges: Collection<Change>): String? {
        if (includedChanges.isEmpty()) {
            return null
        }

        val basePath = PatchWriter.calculateBaseDirForWritingPatch(project, includedChanges)
        return buildUnifiedDiff(basePath, includedChanges, project, honorExcludedFromCommit = true)
    }

    internal fun buildUnifiedDiff(
        basePath: Path,
        changes: Collection<Change>,
        project: Project? = null,
        honorExcludedFromCommit: Boolean = false
    ): String? {
        if (changes.isEmpty()) {
            return null
        }

        return runCatching {
            val patches = IdeaTextPatchBuilder.buildPatch(project, changes, basePath, false, honorExcludedFromCommit)
            if (patches.isEmpty()) {
                null
            } else {
                val writer = StringWriter()
                UnifiedDiffWriter.write(project, basePath, patches, writer, "\n", null, null)
                writer.toString().trim().ifBlank { null }
            }
        }.getOrNull()
    }
}
