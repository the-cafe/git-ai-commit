from ai_commit_msg.services.openai_service import OpenAiService
from ai_commit_msg.services.anthropic_service import AnthropicService
from ai_commit_msg.services.ollama_service import OLlamaService
from ai_commit_msg.utils.models import OPEN_AI_MODEL_LIST, ANTHROPIC_MODEL_LIST
from ai_commit_msg.utils.logger import Logger


class LLMServiceFactory:

    @staticmethod
    def create_service(model_name):
        if model_name in OPEN_AI_MODEL_LIST:
            return OpenAiService()
        elif model_name.startswith("ollama"):
            return OLlamaService()
        elif model_name in ANTHROPIC_MODEL_LIST:
            return AnthropicService()
        else:
            Logger().log(f"Unsupported model: {model_name}")
            return None
