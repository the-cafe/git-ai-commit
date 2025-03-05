from ai_commit_msg.core.llm_chat_completion import llm_chat_completion
from ai_commit_msg.core.prompt import get_prompt
from ai_commit_msg.services.config_service import ConfigService


def generate_commit_message(
    diff: str = None,
    conventional: bool = False,
    classify_type: bool = False,
    classify_scope: bool = False,
) -> str:

    if diff is None:
        raise ValueError("Diff is required to generate a commit message")

    prompt = get_prompt(
        diff,
        conventional=conventional,
        classify_type=classify_type,
        classify_scope=classify_scope,
    )
    ai_gen_commit_msg = llm_chat_completion(prompt)

    if not classify_type and not classify_scope:
        prefix = ConfigService().prefix
        return prefix + ai_gen_commit_msg
    else:
        return ai_gen_commit_msg.strip().lower()
