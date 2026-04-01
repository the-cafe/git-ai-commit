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

class ConventionalCommitAction : AnAction() {

    override fun actionPerformed(e: AnActionEvent) {
        val project = e.project ?: return
        val service = service<GitAICommitService>()

        ProgressManager.getInstance().run(object : Task.Backgroundable(project, "Generating Conventional Commit", false) {
            override fun run(indicator: ProgressIndicator) {
                indicator.text = "Calling git-ai-commit conventional..."

                when (val result = service.executeCommand(project, "conventional")) {
                    is GitAICommitService.Result.Success -> {
                        ApplicationManager.getApplication().invokeLater {
                            Messages.showInfoMessage(project, result.output, "Conventional Commit Generated")
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
