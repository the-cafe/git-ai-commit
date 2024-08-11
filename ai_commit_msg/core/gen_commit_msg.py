from __future__ import annotations

from ai_commit_msg.services.anthropic_service import AnthropicService
from ai_commit_msg.services.config_service import ConfigService
from ai_commit_msg.services.git_service import GitService
from ai_commit_msg.services.ollama_service import OLlamaService
from ai_commit_msg.services.openai_service import OpenAiService
from ai_commit_msg.utils.logger import Logger
from ai_commit_msg.utils.models import ANTHROPIC_MODEL_LIST, OPEN_AI_MODEL_LIST

def generate_commit_message(diff: str = None) -> str:
  COMMIT_MSG_SYSTEM_MESSAGE = '''
You will be provided with a set of code changes in diff format.
Your task is to read each file and explain every major change in a concise way.

Be sure to include details of major changes

You don't need to add any punctuation or capitalization.

Instead of and, use a comma to save characters.

Only respond with a short sentence no longer than 50 characters that I can use for my commit message
    '''

  select_model = ConfigService.get_model()

  prompt = [
          {"role": "system", "content": COMMIT_MSG_SYSTEM_MESSAGE},
          {"role": "user", "content": diff},
      ]

  # TODO - create a factory with a shared interface for calling the LLM models, this will make it easier to add new models
  ai_gen_commit_msg = None
  if str(select_model) in OPEN_AI_MODEL_LIST :
    ai_gen_commit_msg = OpenAiService().chat_with_openai(prompt)
  elif(select_model.startswith("ollama")):
    ai_gen_commit_msg = OLlamaService().chat_completion(prompt)
  elif(select_model in ANTHROPIC_MODEL_LIST):
    ai_gen_commit_msg = AnthropicService().chat_completion(prompt)

  if ai_gen_commit_msg is None:
    Logger().log("Unsupport: " + select_model)
    return ""

  prefix = ConfigService().prefix

  return prefix + ai_gen_commit_msg
