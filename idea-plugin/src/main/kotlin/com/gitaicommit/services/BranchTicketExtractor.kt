package com.gitaicommit.services

import com.intellij.openapi.project.Project
import java.io.BufferedReader
import java.io.InputStreamReader
import java.nio.charset.StandardCharsets

class BranchTicketExtractor {

    fun extractTicketId(project: Project, regex: String): String? {
        val branchName = getCurrentBranch(project) ?: return null

        if (regex.isBlank()) return null

        return try {
            val pattern = Regex(regex)
            pattern.find(branchName)?.value
        } catch (e: Exception) {
            null
        }
    }

    private fun getCurrentBranch(project: Project): String? {
        val basePath = project.basePath ?: return null

        return try {
            val process = ProcessBuilder("git", "branch", "--show-current")
                .directory(java.io.File(basePath))
                .redirectErrorStream(true)
                .start()

            val output = BufferedReader(InputStreamReader(process.inputStream, StandardCharsets.UTF_8)).use {
                it.readText().trim()
            }

            process.waitFor()

            if (output.isBlank()) null else output
        } catch (e: Exception) {
            null
        }
    }
}
