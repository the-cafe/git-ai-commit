package com.gitaicommit.actions

import com.gitaicommit.services.GitAICommitService
import com.intellij.openapi.actionSystem.AnAction
import com.intellij.openapi.actionSystem.AnActionEvent
import com.intellij.openapi.application.ApplicationManager
import com.intellij.openapi.components.service
import com.intellij.openapi.progress.ProgressIndicator
import com.intellij.openapi.progress.ProgressManager
import com.intellij.openapi.progress.Task
import com.intellij.openapi.ui.Messages

class SummarizeChangesAction : AnAction() {

    override fun actionPerformed(e: AnActionEvent) {
        val project = e.project ?: return
        val service = service<GitAICommitService>()

        ProgressManager.getInstance().run(object : Task.Backgroundable(project, "Summarizing Changes", false) {
            override fun run(indicator: ProgressIndicator) {
                indicator.text = "Calling git-ai-commit summarize..."

                when (val result = service.executeCommand(project, "summarize")) {
                    is GitAICommitService.Result.Success -> {
                        ApplicationManager.getApplication().invokeLater {
                            Messages.showInfoMessage(project, result.output, "Changes Summary")
                        }
                    }
                    is GitAICommitService.Result.Error -> {
                        ApplicationManager.getApplication().invokeLater {
                            Messages.showErrorDialog(project, result.message, "Error")
                        }
                    }
                }
            }
        })
    }
}
