package com.gitaicommit.services

import com.gitaicommit.model.CommitDraft
import com.google.gson.Gson
import com.google.gson.JsonObject
import java.net.HttpURLConnection
import java.net.URL
import java.nio.charset.StandardCharsets

class LlmProviderClient {

    private val gson = Gson()

    fun generateCommit(
        provider: String,
        apiKey: String,
        apiBase: String,
        model: String,
        diff: String,
        timeout: Int,
        customPrompt: String
    ): Result<CommitDraft> {
        return try {
            when (provider.lowercase()) {
                "openai" -> callOpenAI(apiKey, apiBase, model, diff, timeout, customPrompt)
                "anthropic" -> callAnthropic(apiKey, apiBase, model, diff, timeout, customPrompt)
                else -> Result.failure(Exception("不支持的提供商: $provider"))
            }
        } catch (e: Exception) {
            Result.failure(e)
        }
    }

    private fun callOpenAI(apiKey: String, apiBase: String, model: String, diff: String, timeout: Int, customPrompt: String): Result<CommitDraft> {
        val url = "${apiBase.ifBlank { "https://api.openai.com/v1" }}/chat/completions"
        val prompt = buildPrompt(diff, customPrompt)

        val requestBody = JsonObject().apply {
            addProperty("model", model.ifBlank { "gpt-4" })
            add("messages", gson.toJsonTree(listOf(
                mapOf("role" to "user", "content" to prompt)
            )))
            addProperty("temperature", 0.3)
            addProperty("stream", false)
        }

        return sendRequest(url, apiKey, requestBody.toString(), timeout, "openai")
    }

    private fun callAnthropic(apiKey: String, apiBase: String, model: String, diff: String, timeout: Int, customPrompt: String): Result<CommitDraft> {
        val url = "${apiBase.ifBlank { "https://api.anthropic.com/v1" }}/messages"
        val prompt = buildPrompt(diff, customPrompt)

        val requestBody = JsonObject().apply {
            addProperty("model", model.ifBlank { "claude-3-5-sonnet-20241022" })
            addProperty("max_tokens", 1024)
            add("messages", gson.toJsonTree(listOf(
                mapOf("role" to "user", "content" to prompt)
            )))
            addProperty("stream", false)
        }

        return sendRequest(url, apiKey, requestBody.toString(), timeout, "anthropic")
    }

    private fun buildPrompt(diff: String, customPrompt: String): String {
        return customPrompt.replace("{diff}", diff)
    }

    private fun sendRequest(url: String, apiKey: String, body: String, timeout: Int, provider: String): Result<CommitDraft> {
        val connection = URL(url).openConnection() as HttpURLConnection
        connection.requestMethod = "POST"
        connection.setRequestProperty("Content-Type", "application/json; charset=UTF-8")
        connection.setRequestProperty("Accept", "application/json, text/event-stream")

        when (provider) {
            "openai" -> connection.setRequestProperty("Authorization", "Bearer $apiKey")
            "anthropic" -> {
                connection.setRequestProperty("x-api-key", apiKey)
                connection.setRequestProperty("anthropic-version", "2023-06-01")
            }
        }

        connection.connectTimeout = timeout
        connection.readTimeout = timeout
        connection.doOutput = true

        connection.outputStream.use { it.write(body.toByteArray(StandardCharsets.UTF_8)) }

        val responseCode = connection.responseCode
        if (responseCode !in 200..299) {
            val errorBody = connection.errorStream
                ?.bufferedReader(StandardCharsets.UTF_8)
                ?.use { it.readText() }
                ?.trim()
                .orEmpty()
            val details = if (errorBody.isBlank()) "" else "，详情: ${errorBody.take(300)}"
            return Result.failure(Exception("API 请求失败: $responseCode$details"))
        }

        val response = connection.inputStream.bufferedReader(StandardCharsets.UTF_8).use { it.readText() }
        return parseResponse(response, provider)
    }

    private fun parseResponse(response: String, provider: String): Result<CommitDraft> {
        return try {
            val draft = LlmResponseParser.parse(response, provider)
            Result.success(draft)
        } catch (e: Exception) {
            Result.failure(Exception("解析响应失败: ${e.message}"))
        }
    }
}
