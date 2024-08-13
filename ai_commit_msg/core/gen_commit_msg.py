from __future__ import annotations

from ai_commit_msg.services.anthropic_service import AnthropicService
from ai_commit_msg.services.config_service import ConfigService
from ai_commit_msg.services.git_service import GitService
from ai_commit_msg.services.ollama_service import OLlamaService
from ai_commit_msg.services.openai_service import OpenAiService
from ai_commit_msg.utils.logger import Logger
from ai_commit_msg.utils.models import ANTHROPIC_MODEL_LIST, OPEN_AI_MODEL_LIST
from ai_commit_msg.utils.diff_truncator import truncate_diff

def generate_commit_message(diff: str = None) -> str:

  if diff is None:
    raise ValueError("Diff is required to generate a commit message")

  COMMIT_MSG_SYSTEM_MESSAGE = '''
You will be provided with a set of code changes in diff format.
Your task is to read each file and explain every major change in a concise way.

Be sure to include details of major changes

You don't need to add any punctuation or capitalization.

Instead of and, use a comma to save characters.

Only respond with a short sentence no longer than 50 characters that I can use for my commit message
    '''

  select_model = ConfigService.get_model()

  def try_generate_message(current_diff):
    prompt = [
        {"role": "system", "content": COMMIT_MSG_SYSTEM_MESSAGE},
        {"role": "user", "content": current_diff},
    ]

    if str(select_model) in OPEN_AI_MODEL_LIST:
        try:
            return OpenAiService().chat_with_openai(prompt)
        except Exception as e:
            if "maximum context length" in str(e) or "Request too large" in str(e):
                Logger().log(f"Switching to gpt-4 due to token limit: {e}")
                try:
                    return OpenAiService().chat_with_openai(prompt, model="gpt-4")
                except Exception as e2:
                    if "maximum context length" in str(e2) or "Request too large" in str(e2):
                        return None
                    else:
                        raise e2
            else:
                raise e
    elif select_model.startswith("ollama"):
        return OLlamaService().chat_completion(prompt)
    elif select_model in ANTHROPIC_MODEL_LIST:
        return AnthropicService().chat_completion(prompt)

    return None

  ai_gen_commit_msg = try_generate_message(diff)

  if ai_gen_commit_msg is None:
    truncated_diff = truncate_diff(diff)
    ai_gen_commit_msg = try_generate_message(truncated_diff)

  if ai_gen_commit_msg is None:
    Logger().log(f"Unsupported or token limit exceeded for model: {select_model}")
    return ""

  prefix = ConfigService().prefix
  return prefix + ai_gen_commit_msg
