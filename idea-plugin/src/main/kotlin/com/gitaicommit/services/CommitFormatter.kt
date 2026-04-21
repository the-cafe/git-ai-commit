package com.gitaicommit.services

import com.gitaicommit.model.CommitDraft
import com.gitaicommit.model.CommitType

class CommitFormatter {

    fun format(draft: CommitDraft, version: String, ticketId: String?): Result<String> {
        val type = CommitType.fromString(draft.type)
            ?: return Result.failure(Exception("无效的提交类型: ${draft.type}"))

        val resolvedTicketId = resolveTicketId(type, ticketId)

        val versionPart = if (resolvedTicketId != null) {
            "$version-$resolvedTicketId"
        } else {
            version
        }

        val message = "【${type.label}】（$versionPart）${draft.summary}"
        return Result.success(message)
    }

    private fun resolveTicketId(type: CommitType, ticketId: String?): String? {
        if (!type.requiresTicket) {
            return null
        }

        return ticketId?.trim()?.ifBlank { null } ?: DEFAULT_TICKET_PLACEHOLDER
    }

    companion object {
        const val DEFAULT_TICKET_PLACEHOLDER = "待替换单号"
    }
}
