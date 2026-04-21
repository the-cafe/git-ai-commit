package com.gitaicommit.settings

import com.gitaicommit.services.LlmProviderClient
import com.intellij.openapi.options.Configurable
import com.intellij.ui.components.JBLabel
import com.intellij.ui.components.JBPasswordField
import com.intellij.ui.components.JBTextField
import com.intellij.util.ui.FormBuilder
import javax.swing.*

class GitAICommitConfigurable : Configurable {

    private val settings = GitAICommitSettings.getInstance()

    private val providerCombo = JComboBox(arrayOf("openai", "anthropic"))
    private val apiKeyField = JBPasswordField()
    private val apiBaseField = JBTextField()
    private val modelField = JBTextField()
    private val releaseVersionField = JBTextField()
    private val ticketIdRegexField = JBTextField()
    private val requestTimeoutField = JBTextField()
    private val customPromptArea = JTextArea(8, 50)
    private val testButton = JButton("测试连接")

    override fun getDisplayName(): String = "Git AI Commit"

    override fun createComponent(): JComponent {
        customPromptArea.lineWrap = true
        customPromptArea.wrapStyleWord = true
        val scrollPane = JScrollPane(customPromptArea)

        // 测试按钮点击事件
        testButton.addActionListener {
            testConnection()
        }

        val testPanel = JPanel().apply {
            layout = BoxLayout(this, BoxLayout.X_AXIS)
            add(testButton)
            add(Box.createHorizontalGlue())
        }

        return FormBuilder.createFormBuilder()
            .addLabeledComponent(JBLabel("Provider (OpenAI/Anthropic):"), providerCombo, 1, false)
            .addLabeledComponent(JBLabel("API Key (必填):"), apiKeyField, 1, false)
            .addLabeledComponent(JBLabel("API Base URL (可选):"), apiBaseField, 1, false)
            .addLabeledComponent(JBLabel("Model (可选，留空使用默认):"), modelField, 1, false)
            .addComponent(testPanel, 1)
            .addSeparator()
            .addLabeledComponent(JBLabel("Release Version (如 1.0.0):"), releaseVersionField, 1, false)
            .addLabeledComponent(JBLabel("Ticket ID Regex (如 [A-Z]+-\\d+):"), ticketIdRegexField, 1, false)
            .addLabeledComponent(JBLabel("Request Timeout (ms):"), requestTimeoutField, 1, false)
            .addSeparator()
            .addLabeledComponent(JBLabel("Custom Prompt (使用 {diff} 占位符):"), scrollPane, 1, false)
            .addComponentFillVertically(JPanel(), 0)
            .panel
    }

    override fun isModified(): Boolean {
        return providerCombo.selectedItem != settings.provider ||
                String(apiKeyField.password) != settings.apiKey ||
                apiBaseField.text != settings.apiBase ||
                modelField.text != settings.model ||
                releaseVersionField.text != settings.releaseVersion ||
                ticketIdRegexField.text != settings.ticketIdRegex ||
                requestTimeoutField.text != settings.requestTimeoutMs.toString() ||
                customPromptArea.text != settings.customPrompt
    }

    override fun apply() {
        settings.provider = providerCombo.selectedItem as String
        settings.apiKey = String(apiKeyField.password)
        settings.apiBase = apiBaseField.text
        settings.model = modelField.text
        settings.releaseVersion = releaseVersionField.text
        settings.ticketIdRegex = ticketIdRegexField.text
        settings.requestTimeoutMs = requestTimeoutField.text.toIntOrNull() ?: 30000
        settings.customPrompt = PromptTextSanitizer.normalizePrompt(
            customPromptArea.text,
            GitAICommitSettings.DEFAULT_CUSTOM_PROMPT
        )
    }

    override fun reset() {
        providerCombo.selectedItem = settings.provider
        apiKeyField.text = settings.apiKey
        apiBaseField.text = settings.apiBase
        modelField.text = settings.model
        releaseVersionField.text = settings.releaseVersion
        ticketIdRegexField.text = settings.ticketIdRegex
        requestTimeoutField.text = settings.requestTimeoutMs.toString()
        customPromptArea.text = PromptTextSanitizer.normalizePrompt(
            settings.customPrompt,
            GitAICommitSettings.DEFAULT_CUSTOM_PROMPT
        )
    }

    private fun testConnection() {
        val provider = providerCombo.selectedItem as String
        val apiKey = String(apiKeyField.password)
        val apiBase = apiBaseField.text
        val model = modelField.text
        val timeout = requestTimeoutField.text.toIntOrNull() ?: 30000

        if (apiKey.isBlank()) {
            JOptionPane.showMessageDialog(null, "请先输入 API Key", "错误", JOptionPane.ERROR_MESSAGE)
            return
        }

        testButton.isEnabled = false
        testButton.text = "测试中..."

        Thread {
            try {
                val client = LlmProviderClient()
                val result = client.generateCommit(
                    provider, apiKey, apiBase, model,
                    "test diff", timeout,
                    """请只返回一个 JSON 对象，不要使用 Markdown，不要补充解释：{"type":"feature","summary":"测试连接正常"}。
Git diff:
{diff}"""
                )

                SwingUtilities.invokeLater {
                    if (result.isSuccess) {
                        JOptionPane.showMessageDialog(null, "连接成功！模型响应正常", "成功", JOptionPane.INFORMATION_MESSAGE)
                    } else {
                        JOptionPane.showMessageDialog(null, "连接失败：${result.exceptionOrNull()?.message}", "错误", JOptionPane.ERROR_MESSAGE)
                    }
                    testButton.isEnabled = true
                    testButton.text = "测试连接"
                }
            } catch (e: Exception) {
                SwingUtilities.invokeLater {
                    JOptionPane.showMessageDialog(null, "测试失败：${e.message}", "错误", JOptionPane.ERROR_MESSAGE)
                    testButton.isEnabled = true
                    testButton.text = "测试连接"
                }
            }
        }.start()
    }
}
