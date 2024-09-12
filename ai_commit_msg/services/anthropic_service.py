import os
import anthropic

from ai_commit_msg.utils.models import ANTHROPIC_MODEL_LIST
from ai_commit_msg.services.config_service import ConfigService
from ai_commit_msg.utils.error import map_error


class AnthropicService:
    api_key = ""

    def __init__(self):
        self.api_key = AnthropicService.get_anthropic_api_key()

        if self.api_key is None or self.api_key == "":
            raise Exception(
                """Anthropic API key is not set. Run the following command to set the key:git-ai-commit config --anthropic-key=<insert your key>"""
            )

        self.client = anthropic.Anthropic(
            api_key=self.api_key,
        )

    @staticmethod
    def get_anthropic_api_key():

        local_api_key = ConfigService().get_anthropic_api_key()

        if local_api_key != "":
            return local_api_key

        env_api_key = os.environ.get("ANTHROPIC_API_KEY")
        if env_api_key != "":
            return env_api_key

        return ""

    def chat_completion(self, messages):
        select_model = ConfigService.get_model()

        if select_model not in ANTHROPIC_MODEL_LIST:
            raise Exception(
                f"Attempted to call Anthropic with an invalid model: {select_model}"
            )

        # filter messages with system role
        system_message = list(
            filter(lambda message: message["role"] == "system", messages)
        )
        user_message = list(filter(lambda message: message["role"] == "user", messages))

        if len(system_message) == 0:
            raise Exception("No system message provided")

        if len(user_message) == 0:
            raise Exception("No user message provided")

        system_message = system_message[0]["content"]

        try:
            ai_gen_message = self.client.messages.create(
                model=select_model,
                max_tokens=1024,
                system=system_message,
                messages=user_message,
            )
            return ai_gen_message.content[0].text

        except Exception as e:
            error_type = e.__class__.__name__
            raise map_error("ANTHROPIC", error_type, e)
