package com.gitaicommit.settings

import java.nio.charset.Charset
import java.nio.charset.StandardCharsets

internal object PromptTextSanitizer {

    private val latin1: Charset = StandardCharsets.ISO_8859_1
    private val suspiciousTokens = listOf("锟", "鈥", "�", "娴", "杩", "璇", "锛", "涓", "鏄", "鐨", "寮", "浜")

    fun normalizePrompt(raw: String?, defaultPrompt: String): String {
        if (raw.isNullOrBlank()) {
            return defaultPrompt
        }

        val trimmed = raw.trim()
        val repaired = repairMojibake(trimmed)
        if (repaired.isBlank()) {
            return defaultPrompt
        }
        if (isLikelyBrokenText(repaired)) {
            return defaultPrompt
        }
        return repaired
    }

    private fun repairMojibake(text: String): String {
        val repairedLatin1 = convert(text, latin1, StandardCharsets.UTF_8)
        if (score(repairedLatin1) > score(text)) {
            return repairedLatin1
        }
        return text
    }

    private fun convert(text: String, source: Charset, target: Charset): String {
        return runCatching { String(text.toByteArray(source), target) }.getOrDefault(text)
    }

    private fun score(text: String): Int {
        var score = 0
        score += countChinese(text) * 2
        if (text.contains("{diff}")) {
            score += 30
        }
        if (text.contains("JSON", ignoreCase = true)) {
            score += 5
        }
        score -= countReplacement(text) * 10
        score -= suspiciousPenalty(text)
        return score
    }

    private fun countChinese(text: String): Int {
        return text.count {
            val block = Character.UnicodeBlock.of(it)
            block == Character.UnicodeBlock.CJK_UNIFIED_IDEOGRAPHS ||
                    block == Character.UnicodeBlock.CJK_UNIFIED_IDEOGRAPHS_EXTENSION_A ||
                    block == Character.UnicodeBlock.CJK_UNIFIED_IDEOGRAPHS_EXTENSION_B
        }
    }

    private fun countReplacement(text: String): Int = text.count { it == '\uFFFD' }

    private fun suspiciousPenalty(text: String): Int {
        var penalty = 0
        suspiciousTokens.forEach { token ->
            if (text.contains(token)) {
                penalty += 6
            }
        }
        return penalty
    }

    private fun isLikelyBrokenText(text: String): Boolean {
        if (text.contains('\uFFFD')) {
            return true
        }

        val hitCount = suspiciousTokens.count { token -> text.contains(token) }
        if (hitCount >= 2) {
            return true
        }

        val questionMarkCount = text.count { it == '?' }
        if (questionMarkCount >= 6 && !text.contains("{diff}")) {
            return true
        }

        return false
    }
}
