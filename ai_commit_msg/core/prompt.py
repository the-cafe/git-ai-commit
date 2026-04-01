from ai_commit_msg.services.config_service import ConfigService


# Maximum characters allowed for diff content sent to LLM
MAX_DIFF_CHARS = 8000

# File patterns to exclude from diff (noise reduction)
NOISE_FILE_PATTERNS = [
    "package-lock.json",
    "yarn.lock",
    "pnpm-lock.yaml",
    "Pipfile.lock",
    "poetry.lock",
    "Cargo.lock",
    "Gemfile.lock",
    "composer.lock",
    "go.sum",
    ".min.js",
    ".min.css",
    ".map",
    ".svg",
    ".ico",
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".woff",
    ".woff2",
    ".ttf",
    ".eot",
]


def preprocess_diff(diff: str) -> str:
    """Filter noise files and truncate oversized diffs for better LLM accuracy."""
    if not diff:
        return diff

    lines = diff.split("\n")
    filtered_lines = []
    skip_current_file = False

    for line in lines:
        # Detect file header in diff
        if line.startswith("diff --git"):
            skip_current_file = any(
                pattern in line for pattern in NOISE_FILE_PATTERNS
            )
            if skip_current_file:
                filtered_lines.append(
                    f"# [Filtered: {line.split('b/')[-1] if 'b/' in line else 'noise file'} - skipped for brevity]"
                )
            else:
                filtered_lines.append(line)
        elif line.startswith("Binary files"):
            filtered_lines.append(f"# [Binary file change - skipped]")
            skip_current_file = True
        elif not skip_current_file:
            filtered_lines.append(line)

    result = "\n".join(filtered_lines)

    # Truncate if still too long
    if len(result) > MAX_DIFF_CHARS:
        truncated = result[:MAX_DIFF_CHARS]
        # Find the last complete line
        last_newline = truncated.rfind("\n")
        if last_newline > 0:
            truncated = truncated[:last_newline]
        result = truncated + "\n\n# [Diff truncated - showing first ~8000 chars of changes]"

    return result


def get_prompt(diff, conventional=False, classify_type=False, classify_scope=False, commit_template=None):
    max_length = ConfigService().max_length

    # Preprocess diff to filter noise and truncate
    processed_diff = preprocess_diff(diff)

    if classify_type:
        COMMIT_MSG_SYSTEM_MESSAGE = """
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
        COMMIT_MSG_SYSTEM_MESSAGE = """
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
- Do not add any punctuation or capitalization
- Your response must not be more than {max_length} characters
- Respond with ONLY the commit message, no quotes or extra text
"""
    else:
        # Check if a custom commit template is provided
        if commit_template:
            COMMIT_MSG_SYSTEM_MESSAGE = f"""
You are a software engineer reviewing code changes.
You will be provided with a set of code changes in diff format.

Your task is to write a concise commit message that summarizes the changes following the custom format below.

Custom commit format specification:
{commit_template}

Requirements:
- Follow the custom format strictly
- Write a clear, accurate description of the actual code changes
- Focus on the most significant changes, ignore minor formatting or whitespace changes
- Your response must not be more than {max_length} characters
- Respond with ONLY the formatted commit message, nothing else
"""
        else:
            COMMIT_MSG_SYSTEM_MESSAGE = f"""
You are a software engineer reviewing a set of code changes.
You will be provided with a set of code changes in diff format.

Your task is to write a concise commit message that summarizes the changes. Focus on the most significant changes and their purpose.

These are your requirements for the commit message:
- Write in the imperative mood (e.g., "add feature" not "added feature")
- Be specific about what was changed and why
- Focus on major changes, ignore minor formatting or whitespace changes
- Your response must not be more than {max_length} characters
- Respond with ONLY the commit message, no quotes or extra text
"""

    return [
        {"role": "system", "content": COMMIT_MSG_SYSTEM_MESSAGE},
        {"role": "user", "content": processed_diff},
    ]
