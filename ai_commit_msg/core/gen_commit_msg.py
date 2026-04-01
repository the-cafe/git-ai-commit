from ai_commit_msg.core.llm_chat_completion import llm_chat_completion
from ai_commit_msg.core.prompt import get_prompt
from ai_commit_msg.services.config_service import ConfigService

import json
import re


def generate_commit_message(
    diff: str = None,
    conventional: bool = False,
    classify_type: bool = False,
    classify_scope: bool = False,
    commit_template: str = None,
) -> str:

    if diff is None:
        raise ValueError("Diff is required to generate a commit message")

    prompt = get_prompt(
        diff,
        conventional=conventional,
        classify_type=classify_type,
        classify_scope=classify_scope,
        commit_template=commit_template,
    )
    ai_gen_commit_msg = llm_chat_completion(prompt)

    if not classify_type and not classify_scope:
        prefix = ConfigService().prefix
        return prefix + ai_gen_commit_msg
    else:
        return ai_gen_commit_msg.strip().lower()


def generate_conventional_commit_single_call(diff: str) -> dict:
    """Generate type, scope, and message in a single LLM call for consistency and speed."""
    max_length = ConfigService().max_length

    from ai_commit_msg.core.prompt import preprocess_diff
    processed_diff = preprocess_diff(diff)

    system_prompt = f"""You are a software engineer reviewing code changes. Analyze the diff and generate a conventional commit with type, scope, and message.

Return your response as a JSON object with exactly these keys:
- "type": one of feat, fix, docs, style, refactor, perf, test, chore
- "scope": a short scope (1-3 words, lowercase, use hyphens) or "none" if not applicable
- "message": a concise commit message body in imperative mood, no more than {max_length} characters

Example response:
{{"type": "feat", "scope": "auth", "message": "add JWT token refresh mechanism"}}

Respond with ONLY the JSON object, no markdown code blocks, no extra text."""

    prompt = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": processed_diff},
    ]

    response = llm_chat_completion(prompt)

    # Try to parse JSON from LLM response
    try:
        # Clean up response - remove markdown code blocks if present
        cleaned = response.strip()
        if cleaned.startswith("```"):
            cleaned = re.sub(r"^```(?:json)?\s*", "", cleaned)
            cleaned = re.sub(r"\s*```$", "", cleaned)

        result = json.loads(cleaned)
        return {
            "type": result.get("type", "chore"),
            "scope": result.get("scope", "none"),
            "message": result.get("message", "update code"),
        }
    except (json.JSONDecodeError, KeyError):
        # Fallback: return defaults
        return {
            "type": "chore",
            "scope": "none",
            "message": response.strip()[:max_length],
        }
