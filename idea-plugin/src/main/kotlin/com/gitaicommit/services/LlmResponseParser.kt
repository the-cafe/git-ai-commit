package com.gitaicommit.services

import com.gitaicommit.model.CommitDraft
import com.google.gson.JsonElement
import com.google.gson.JsonObject
import com.google.gson.JsonParser

internal object LlmResponseParser {

    fun parse(rawResponse: String, provider: String): CommitDraft {
        parseSseResponse(rawResponse, provider)?.let { return it }
        parseAnyDraftOrNull(rawResponse)?.let { return it }

        val responseJson = parseJsonObjectOrNull(rawResponse)
            ?: throw IllegalStateException("响应不是合法 JSON 对象")

        val content = try {
            when (provider.lowercase()) {
                "openai" -> extractOpenAIContent(responseJson)
                "anthropic" -> extractAnthropicContent(responseJson)
                else -> throw IllegalArgumentException("未知提供商: $provider")
            }
        } catch (e: Exception) {
            parseDraftFromElementOrNull(responseJson, ArrayDeque())?.let { return it }
            throw e
        }

        return parseDraftFromContent(content)
    }

    private fun parseSseResponse(rawResponse: String, provider: String): CommitDraft? {
        if (!rawResponse.contains("data:")) {
            return null
        }

        val dataLines = rawResponse.lineSequence()
            .map { it.trim() }
            .filter { it.startsWith("data:") }
            .map { it.removePrefix("data:").trim() }
            .filter { it.isNotBlank() && !it.equals("[DONE]", ignoreCase = true) }
            .toList()

        if (dataLines.isEmpty()) {
            return null
        }

        val mergedContent = StringBuilder()
        dataLines.forEach { line ->
            val chunk = parseJsonObjectOrNull(line) ?: return@forEach
            val chunkContent = when (provider.lowercase()) {
                "openai" -> runCatching { extractOpenAIContent(chunk) }.getOrNull()
                "anthropic" -> runCatching { extractAnthropicContent(chunk) }.getOrNull()
                else -> null
            }
            if (!chunkContent.isNullOrBlank()) {
                mergedContent.append(chunkContent)
            }
        }

        if (mergedContent.isNotEmpty()) {
            return parseDraftFromContent(mergedContent.toString())
        }

        for (index in dataLines.indices.reversed()) {
            val chunk = parseJsonObjectOrNull(dataLines[index]) ?: continue
            val chunkContent = when (provider.lowercase()) {
                "openai" -> runCatching { extractOpenAIContent(chunk) }.getOrNull()
                "anthropic" -> runCatching { extractAnthropicContent(chunk) }.getOrNull()
                else -> null
            }
            if (!chunkContent.isNullOrBlank()) {
                return parseDraftFromContent(chunkContent)
            }
        }

        return null
    }

    private fun extractOpenAIContent(responseJson: JsonObject): String {
        if (responseJson.has("choices") && responseJson.get("choices").isJsonArray) {
            val choices = responseJson.getAsJsonArray("choices")
            if (choices.size() > 0 && choices[0].isJsonObject) {
                val firstChoice = choices[0].asJsonObject
                extractContentElement(firstChoice.get("message"))?.let { return it }
                extractContentElement(firstChoice.get("delta"))?.let { return it }
                extractContentElement(firstChoice.get("content"))?.let { return it }
                extractContentElement(firstChoice.get("text"))?.let { return it }
            }
        }

        if (responseJson.has("output") && responseJson.get("output").isJsonArray) {
            val output = responseJson.getAsJsonArray("output")
            if (output.size() > 0 && output[0].isJsonObject) {
                val firstOutput = output[0].asJsonObject
                extractContentElement(firstOutput.get("content"))?.let { return it }
            }
        }

        throw IllegalStateException("OpenAI 响应缺少可解析的内容字段")
    }

    private fun extractAnthropicContent(responseJson: JsonObject): String {
        extractContentElement(responseJson.get("content"))?.let { return it }
        extractContentElement(responseJson.get("delta"))?.let { return it }
        throw IllegalStateException("Anthropic 响应缺少可解析的内容字段")
    }

    private fun parseAnyDraftOrNull(rawResponse: String): CommitDraft? {
        val pendingTexts = ArrayDeque<String>()
        val visitedTexts = linkedSetOf<String>()
        pendingTexts.addLast(rawResponse)

        while (pendingTexts.isNotEmpty()) {
            val current = pendingTexts.removeFirst().trim()
            if (current.isBlank() || !visitedTexts.add(current)) {
                continue
            }

            val draftJson = parseJsonObjectFromText(current)
            if (draftJson != null && looksLikeDraftJson(draftJson)) {
                return parseDraftFromJson(draftJson)
            }

            val element = parseJsonElementOrNull(current) ?: continue
            parseDraftFromElementOrNull(element, pendingTexts)?.let { return it }
        }

        return null
    }

    private fun parseDraftFromElementOrNull(
        element: JsonElement?,
        pendingTexts: ArrayDeque<String>,
        depth: Int = 0
    ): CommitDraft? {
        if (element == null || element.isJsonNull) {
            return null
        }
        if (depth > 64) {
            return null
        }

        if (element.isJsonPrimitive && element.asJsonPrimitive.isString) {
            val text = element.asString.trim()
            if (text.isNotBlank()) {
                pendingTexts.addLast(text)
            }
            return null
        }

        if (element.isJsonArray) {
            val array = element.asJsonArray
            for (index in 0 until array.size()) {
                parseDraftFromElementOrNull(array[index], pendingTexts, depth + 1)?.let { return it }
            }
            return null
        }

        if (!element.isJsonObject) {
            return null
        }

        val json = element.asJsonObject
        if (looksLikeDraftJson(json)) {
            return parseDraftFromJson(json)
        }

        val candidateKeys = listOf(
            "response",
            "message",
            "content",
            "text",
            "output_text",
            "generated_text",
            "completion",
            "result",
            "data",
            "output"
        )

        candidateKeys.forEach { key ->
            if (json.has(key)) {
                parseDraftFromElementOrNull(json.get(key), pendingTexts, depth + 1)?.let { return it }
            }
        }

        json.entrySet().forEach { (_, value) ->
            parseDraftFromElementOrNull(value, pendingTexts, depth + 1)?.let { return it }
        }

        return null
    }

    private fun extractContentElement(element: JsonElement?): String? {
        if (element == null || element.isJsonNull) {
            return null
        }

        if (element.isJsonPrimitive && element.asJsonPrimitive.isString) {
            return element.asString
        }

        if (element.isJsonObject) {
            val obj = element.asJsonObject
            extractContentElement(obj.get("content"))?.let { return it }
            extractContentElement(obj.get("text"))?.let { return it }
            extractContentElement(obj.get("delta"))?.let { return it }
            return null
        }

        if (element.isJsonArray) {
            val merged = StringBuilder()
            val array = element.asJsonArray
            for (i in 0 until array.size()) {
                val part = extractContentElement(array[i]) ?: continue
                merged.append(part)
            }
            return merged.toString().ifBlank { null }
        }

        return null
    }

    private fun parseDraftFromContent(content: String): CommitDraft {
        val draftJson = parseJsonObjectFromText(content)
            ?: throw IllegalStateException("模型返回内容中未找到有效 JSON")

        return parseDraftFromJson(draftJson)
    }

    private fun parseDraftFromJson(draftJson: JsonObject): CommitDraft {
        val type = readTextField(draftJson, "type")
            ?: throw IllegalStateException("模型返回缺少 type 字段")
        val summary = readTextField(draftJson, "summary")
            ?: readTextField(draftJson, "message")
            ?: throw IllegalStateException("模型返回缺少 summary 字段")

        return CommitDraft(type, summary)
    }

    private fun readTextField(json: JsonObject, key: String): String? {
        if (!json.has(key)) {
            return null
        }
        val value = json.get(key)
        if (!value.isJsonPrimitive || !value.asJsonPrimitive.isString) {
            return null
        }
        return value.asString.trim().ifBlank { null }
    }

    private fun looksLikeDraftJson(json: JsonObject): Boolean {
        val hasType = readTextField(json, "type") != null
        val hasSummary = readTextField(json, "summary") != null || readTextField(json, "message") != null
        return hasType && hasSummary
    }

    private fun parseJsonObjectFromText(text: String): JsonObject? {
        val cleaned = stripMarkdownCodeFence(text).trim()
        parseJsonObjectOrNull(cleaned)?.let { return it }

        val embeddedJson = extractFirstJsonObject(cleaned) ?: return null
        return parseJsonObjectOrNull(embeddedJson)
    }

    private fun stripMarkdownCodeFence(text: String): String {
        val trimmed = text.trim()
        if (!trimmed.startsWith("```")) {
            return trimmed
        }

        val withoutOpeningFence = trimmed.removePrefix("```")
        val newlineIndex = withoutOpeningFence.indexOfFirst { it == '\n' || it == '\r' }
        if (newlineIndex < 0) {
            return trimmed
        }

        val fenceLanguage = withoutOpeningFence.substring(0, newlineIndex).trim()
        if (fenceLanguage.isNotEmpty() && !fenceLanguage.equals("json", ignoreCase = true)) {
            return trimmed
        }

        val body = withoutOpeningFence.substring(newlineIndex + 1).trimStart('\n', '\r')
        val bodyTrimmedEnd = body.trimEnd()
        val withoutClosingFence = if (bodyTrimmedEnd.endsWith("```")) {
            bodyTrimmedEnd.removeSuffix("```").trimEnd()
        } else {
            bodyTrimmedEnd
        }

        return withoutClosingFence.trim()
    }

    private fun parseJsonObjectOrNull(raw: String): JsonObject? {
        val element = parseJsonElementOrNull(raw) ?: return null
        return when {
            element.isJsonObject -> element.asJsonObject
            element.isJsonPrimitive && element.asJsonPrimitive.isString -> {
                val inner = element.asString.trim()
                if (inner == raw.trim()) null else parseJsonObjectOrNull(inner)
            }
            else -> null
        }
    }

    private fun parseJsonElementOrNull(raw: String): JsonElement? {
        val candidate = raw.trim()
        if (candidate.isBlank()) {
            return null
        }

        return runCatching { JsonParser.parseString(candidate) }.getOrNull()
    }

    // 从自由文本中提取第一个 JSON 对象，兼容前后解释性文本。
    private fun extractFirstJsonObject(text: String): String? {
        var start = -1
        var depth = 0
        var inString = false
        var escaped = false

        for (index in text.indices) {
            val char = text[index]
            if (inString) {
                if (escaped) {
                    escaped = false
                    continue
                }
                if (char == '\\') {
                    escaped = true
                    continue
                }
                if (char == '"') {
                    inString = false
                }
                continue
            }

            when (char) {
                '"' -> inString = true
                '{' -> {
                    if (depth == 0) {
                        start = index
                    }
                    depth++
                }
                '}' -> {
                    if (depth == 0) {
                        continue
                    }
                    depth--
                    if (depth == 0 && start >= 0) {
                        return text.substring(start, index + 1)
                    }
                }
            }
        }

        return null
    }
}
