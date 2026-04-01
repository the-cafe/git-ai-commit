package com.gitaicommit.model

enum class CommitType(val label: String, val requiresTicket: Boolean) {
    FEATURE("feature", true),
    BUGFIX("bugfix", true),
    DOCS("docs", true),
    STYLE("style", true),
    REFACTOR("refactor", false),
    REVERT("revert", false),
    BUILD("build", true),
    CONFIG("config", false);

    companion object {
        fun fromString(value: String): CommitType? {
            return values().find { it.name.equals(value, ignoreCase = true) }
        }
    }
}
