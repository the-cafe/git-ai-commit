package com.gitaicommit.services

import com.gitaicommit.settings.GitAICommitSettings
import com.intellij.openapi.components.Service
import com.intellij.openapi.project.Project
import java.io.BufferedReader
import java.io.InputStreamReader
import java.nio.charset.StandardCharsets

@Service
class GitAICommitService {

    fun executeCommand(project: Project, vararg args: String): Result {
        return try {
            val settings = GitAICommitSettings.getInstance()
            val command = mutableListOf("git-ai-commit").apply { addAll(args) }

            val processBuilder = ProcessBuilder(command)
            processBuilder.directory(project.basePath?.let { java.io.File(it) })
            processBuilder.redirectErrorStream(true)

            // 设置环境变量
            val env = processBuilder.environment()
            val effectiveModel = resolveModel(settings.provider, settings.model)
            val providerModelMismatch = hasProviderModelMismatch(settings.provider, effectiveModel)
            if (providerModelMismatch != null) {
                return Result.Error(providerModelMismatch)
            }

            if (settings.apiKey.isNotEmpty()) {
                when (settings.provider) {
                    "openai" -> env["OPENAI_API_KEY"] = settings.apiKey
                    "anthropic" -> env["ANTHROPIC_API_KEY"] = settings.apiKey
                }
            }
            if (settings.apiBase.isNotEmpty()) {
                env["API_BASE"] = settings.apiBase
            }
            env["MODEL"] = effectiveModel

            val process = processBuilder.start()
            val output = StringBuilder()

            BufferedReader(InputStreamReader(process.inputStream, StandardCharsets.UTF_8)).use { reader ->
                reader.lines().forEach { line ->
                    output.append(line).append("\n")
                }
            }

            val exitCode = process.waitFor()

            if (exitCode == 0) {
                Result.Success(output.toString().trim())
            } else {
                Result.Error("Command failed with exit code $exitCode\n$output")
            }
        } catch (e: Exception) {
            Result.Error("Failed to execute git-ai-commit: ${e.message}")
        }
    }

    private fun resolveModel(provider: String, configuredModel: String): String {
        if (configuredModel.isNotBlank()) {
            return configuredModel
        }

        return when (provider.lowercase()) {
            "anthropic" -> "claude-3-5-sonnet-20241022"
            else -> "gpt-4o-mini"
        }
    }

    private fun hasProviderModelMismatch(provider: String, model: String): String? {
        val normalizedProvider = provider.lowercase()
        val normalizedModel = model.lowercase()

        if (normalizedProvider == "openai" && normalizedModel.startsWith("claude")) {
            return "当前 Provider 是 OpenAI，但 Model 看起来是 Anthropic 模型：$model"
        }

        if (normalizedProvider == "anthropic" && (normalizedModel.startsWith("gpt") || normalizedModel.startsWith("o"))) {
            return "当前 Provider 是 Anthropic，但 Model 看起来是 OpenAI 模型：$model"
        }

        return null
    }

    sealed class Result {
        data class Success(val output: String) : Result()
        data class Error(val message: String) : Result()
    }
}
