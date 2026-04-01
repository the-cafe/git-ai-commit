package com.gitaicommit.actions

import com.gitaicommit.services.*
import com.gitaicommit.settings.GitAICommitSettings
import com.intellij.openapi.actionSystem.AnAction
import com.intellij.openapi.actionSystem.AnActionEvent
import com.intellij.openapi.application.ApplicationManager
import com.intellij.openapi.progress.ProgressIndicator
import com.intellij.openapi.progress.ProgressManager
import com.intellij.openapi.progress.Task
import com.intellij.openapi.ui.Messages
import com.intellij.openapi.vcs.CheckinProjectPanel
import com.intellij.openapi.vcs.VcsDataKeys
import com.intellij.openapi.vcs.ui.Refreshable

class GenerateCommitAction : AnAction() {

    override fun actionPerformed(e: AnActionEvent) {
        val project = e.project ?: return
        val settings = GitAICommitSettings.getInstance()

        if (settings.apiKey.isBlank()) {
            Messages.showErrorDialog(project, "请先在设置中配置 API Key", "配置错误")
            return
        }

        ProgressManager.getInstance().run(object : Task.Backgroundable(project, "生成 AI 提交消息", false) {
            override fun run(indicator: ProgressIndicator) {
                indicator.text = "采集提交 diff..."
                val diffCollector = DiffCollector()
                val workflowUi = VcsDataKeys.COMMIT_WORKFLOW_UI.getData(e.dataContext)
                val commitPanel = Refreshable.PANEL_KEY.getData(e.dataContext) as? CheckinProjectPanel
                val includedChanges = workflowUi?.getIncludedChanges().orEmpty().ifEmpty {
                    commitPanel?.selectedChanges.orEmpty()
                }
                val diff = diffCollector.collectCommitDiff(project, includedChanges)

                if (diff.isNullOrBlank()) {
                    ApplicationManager.getApplication().invokeLater {
                        Messages.showWarningDialog(project, "没有可用于生成提交消息的变更", "警告")
                    }
                    return
                }

                indicator.text = "提取单号..."
                val ticketExtractor = BranchTicketExtractor()
                val ticketId = ticketExtractor.extractTicketId(project, settings.ticketIdRegex)

                indicator.text = "调用 LLM 生成提交消息..."
                val llmClient = LlmProviderClient()
                val draftResult = llmClient.generateCommit(
                    settings.provider,
                    settings.apiKey,
                    settings.apiBase,
                    settings.model,
                    diff,
                    settings.requestTimeoutMs,
                    settings.customPrompt
                )

                if (draftResult.isFailure) {
                    ApplicationManager.getApplication().invokeLater {
                        Messages.showErrorDialog(project, "生成失败: ${draftResult.exceptionOrNull()?.message}", "错误")
                    }
                    return
                }

                indicator.text = "格式化提交消息..."
                val formatter = CommitFormatter()
                val messageResult = formatter.format(
                    draftResult.getOrThrow(),
                    settings.releaseVersion,
                    ticketId
                )

                if (messageResult.isFailure) {
                    ApplicationManager.getApplication().invokeLater {
                        Messages.showErrorDialog(project, messageResult.exceptionOrNull()?.message ?: "格式化失败", "错误")
                    }
                    return
                }

                val message = messageResult.getOrThrow()

                // 尝试回填到提交框，失败则显示对话框
                val bridge = CommitUiBridge()
                if (!bridge.setCommitMessage(project, message)) {
                    ApplicationManager.getApplication().invokeLater {
                        Messages.showInfoMessage(project, message, "生成成功（请手动复制）")
                    }
                }
            }
        })
    }
}
