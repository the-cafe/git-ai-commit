from ai_commit_msg.services.anthropic_service import AnthropicService
from ai_commit_msg.services.config_service import ConfigService
from ai_commit_msg.services.ollama_service import OLlamaService
from ai_commit_msg.services.openai_service import OpenAiService
from ai_commit_msg.utils.logger import Logger
from ai_commit_msg.utils.models import ANTHROPIC_MODEL_LIST, OPEN_AI_MODEL_LIST


def llm_chat_completion(prompt):
    select_model = ConfigService.get_model()

    # TODO - create a factory with a shared interface for calling the LLM models, this will make it easier to add new models
    ai_gen_commit_msg = None
    if str(select_model) in OPEN_AI_MODEL_LIST:
        ai_gen_commit_msg = OpenAiService().chat_with_openai(prompt)
    elif select_model.startswith("ollama"):
        ai_gen_commit_msg = OLlamaService().chat_completion(prompt)
    elif select_model in ANTHROPIC_MODEL_LIST:
        ai_gen_commit_msg = AnthropicService().chat_completion(prompt)

    if ai_gen_commit_msg is None:
        Logger().log("Unsupported model: " + select_model)
        return ""

    return ai_gen_commit_msg
