from ai_commit_msg.core.llm_chat_completion import llm_chat_completion
from ai_commit_msg.core.prompt import get_prompt
from ai_commit_msg.services.config_service import ConfigService


def generate_commit_message(diff: str = None) -> str:

    if diff is None:
        raise ValueError("Diff is required to generate a commit message")

    prompt = get_prompt(diff)
    ai_gen_commit_msg = llm_chat_completion(prompt)

    prefix = ConfigService().prefix
    return prefix + ai_gen_commit_msg
