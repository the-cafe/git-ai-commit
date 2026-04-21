package com.gitaicommit.services

import com.intellij.openapi.project.Project

class CommitUiBridge {

    fun setCommitMessage(project: Project, message: String): Boolean {
        // 暂时返回 false，让 Action 显示对话框供用户手动复制
        // 后续可以实现真正的回填逻辑
        return false
    }
}
