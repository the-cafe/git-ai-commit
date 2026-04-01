package com.gitaicommit.services

import com.google.gson.Gson
import org.junit.Assert.assertEquals
import org.junit.Test

class LlmResponseParserTest {

    @Test
    fun `parse openai standard json response`() {
        val response = """
            {
              "choices": [
                {
                  "message": {
                    "content": "{\"type\":\"feature\",\"summary\":\"新增提交按钮\"}"
                  }
                }
              ]
            }
        """.trimIndent()

        val draft = LlmResponseParser.parse(response, "openai")
        assertEquals("feature", draft.type)
        assertEquals("新增提交按钮", draft.summary)
    }

    @Test
    fun `parse openai response wrapped as json string`() {
        val rawJson = """
            {
              "choices": [
                {
                  "message": {
                    "content": "{\"type\":\"bugfix\",\"summary\":\"修复解析异常\"}"
                  }
                }
              ]
            }
        """.trimIndent()
        val wrapped = Gson().toJson(rawJson)

        val draft = LlmResponseParser.parse(wrapped, "openai")
        assertEquals("bugfix", draft.type)
        assertEquals("修复解析异常", draft.summary)
    }

    @Test
    fun `parse openai sse chunk response`() {
        val response = """
            data: {"choices":[{"delta":{"content":"{\"type\":\"feature\","}}]}
            data: {"choices":[{"delta":{"content":"\"summary\":\"支持流式兼容\"}"}}]}
            data: [DONE]
        """.trimIndent()

        val draft = LlmResponseParser.parse(response, "openai")
        assertEquals("feature", draft.type)
        assertEquals("支持流式兼容", draft.summary)
    }

    @Test
    fun `parse anthropic content with markdown json`() {
        val response = """
            {
              "content": [
                {
                  "type": "text",
                  "text": "```json\n{\"type\":\"docs\",\"summary\":\"补充配置说明\"}\n```"
                }
              ]
            }
        """.trimIndent()

        val draft = LlmResponseParser.parse(response, "anthropic")
        assertEquals("docs", draft.type)
        assertEquals("补充配置说明", draft.summary)
    }

    @Test
    fun `parse direct markdown json response`() {
        val response = """
            ```json
            {"type":"bugfix","summary":"修复响应解析"}
            ```
        """.trimIndent()

        val draft = LlmResponseParser.parse(response, "openai")
        assertEquals("bugfix", draft.type)
        assertEquals("修复响应解析", draft.summary)
    }

    @Test
    fun `parse direct json object response`() {
        val response = """
            {"type":"refactor","summary":"整理提交生成逻辑"}
        """.trimIndent()

        val draft = LlmResponseParser.parse(response, "anthropic")
        assertEquals("refactor", draft.type)
        assertEquals("整理提交生成逻辑", draft.summary)
    }

    @Test
    fun `parse json string wrapping markdown json response`() {
        val response = Gson().toJson(
            """
            ```json
            {"type":"docs","summary":"补充连接测试说明"}
            ```
            """.trimIndent()
        )

        val draft = LlmResponseParser.parse(response, "openai")
        assertEquals("docs", draft.type)
        assertEquals("补充连接测试说明", draft.summary)
    }

    @Test
    fun `parse generic response field with direct json`() {
        val response = """
            {"response":"{\"type\":\"feature\",\"summary\":\"支持通用响应字段\"}"}
        """.trimIndent()

        val draft = LlmResponseParser.parse(response, "openai")
        assertEquals("feature", draft.type)
        assertEquals("支持通用响应字段", draft.summary)
    }

    @Test
    fun `parse deeply wrapped json string response without stack overflow`() {
        var response = """
            ```json
            {"type":"feature","summary":"深层包装仍可解析"}
            ```
        """.trimIndent()

        repeat(16) {
            response = Gson().toJson(response)
        }

        val draft = LlmResponseParser.parse(response, "openai")
        assertEquals("feature", draft.type)
        assertEquals("深层包装仍可解析", draft.summary)
    }
}
