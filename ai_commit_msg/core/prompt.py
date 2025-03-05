from ai_commit_msg.services.config_service import ConfigService


def get_prompt(diff, conventional=False, classify_type=False, classify_scope=False):
    max_length = ConfigService().max_length

    if classify_type:
        COMMIT_MSG_SYSTEM_MESSAGE = f"""
You are a software engineer reviewing code changes to classify them according to conventional commit standards.
You will be provided with a set of code changes in diff format.

Your task is to analyze the changes and determine the most appropriate conventional commit type.
Choose ONE type from the following options:
- feat: New feature
- fix: Bug fix
- docs: Documentation changes
- style: Formatting changes
- refactor: Code refactoring
- perf: Performance improvements
- test: Adding or modifying tests
- chore: Maintenance tasks

Respond with ONLY the type (e.g., "feat", "fix", etc.) without any additional text or explanation.
"""
    elif classify_scope:
        COMMIT_MSG_SYSTEM_MESSAGE = f"""
You are a software engineer reviewing code changes to suggest an appropriate scope for a conventional commit.
You will be provided with a set of code changes in diff format.

Your task is to analyze the changes and suggest a concise, meaningful scope that indicates what part of the codebase or functionality is being modified.
Good scopes are typically:
- Short (1-3 words)
- Descriptive of the component or feature being changed
- Lowercase with no spaces (use hyphens if needed)

Examples of good scopes:
- "auth" for authentication changes
- "user-profile" for user profile features
- "api" for API-related changes
- "docs" for documentation
- "deps" for dependency updates
- "ui" for user interface changes

If you can't determine a meaningful scope, respond with "none".
Respond with ONLY the suggested scope without any additional text or explanation.
"""
    elif conventional:
        COMMIT_MSG_SYSTEM_MESSAGE = f"""
You are a software engineer reviewing code changes.
You will be provided with a set of code changes in diff format.

Your task is to write a concise commit message body that summarizes the changes. This will be used in a conventional commit format.

These are your requirements for the commit message body:
- Write in the imperative mood (e.g., "add feature" not "added feature")
- Focus only on the description part - do NOT include type prefixes like "feat:" or "fix:" as these will be added separately
- Be specific but concise about what was changed
- You don't need to add any punctuation or capitalization
- Your response cannot be more than {max_length} characters
"""
    else:
        COMMIT_MSG_SYSTEM_MESSAGE = f"""
Your a software engineer and you are reviewing a set of code changes.
You will be provided with a set of code changes in diff format.

Your task is to write a concise commit message that summarizes the changes. Only include major code in the commit message. Avoid including details about minor changes.

These are your requirements for the commit message:
- You don't need to add any punctuation or capitalization.
- Instead of and, use a comma to save characters.
- Your response cannot more than {max_length} characters.
"""

    return [
        {"role": "system", "content": COMMIT_MSG_SYSTEM_MESSAGE},
        {"role": "user", "content": diff},
    ]
