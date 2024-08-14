from ai_commit_msg.utils.logger import Logger
from ai_commit_msg.utils.models import ANTHROPIC_MODEL_LIST
import anthropic
from ai_commit_msg.services.config_service import ConfigService
from ai_commit_msg.services.model_error_handling import handle_ai_model_error

class AnthropicService:
  api_key = ""

  def __init__(self):
    self.api_key = ConfigService().get_anthropic_api_key()

    if self.api_key is None or self.api_key == "":
      raise Exception("""Anthropic API key is not set. Run the following command to set the key:git-ai-commit config --anthropic-key=<insert your key>""")

    self.client = anthropic.Anthropic(
      api_key=self.api_key,
    )

  def chat_completion(self, messages):
    select_model = ConfigService.get_model()

    if select_model not in ANTHROPIC_MODEL_LIST:
        raise Exception(f"Attempted to call Anthropic with an invalid model: {select_model}")

    # filter messages with system role
    system_message = list(filter(lambda message: message["role"] == "system", messages))
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
    except anthropic.APIError as e:
      error_type = self._extract_error_type(e)
      handle_ai_model_error("ANTHROPIC", error_type)
    except Exception as e:
      error_type = str(type(e).__name__)
      handle_ai_model_error("ANTHROPIC", error_type)

      def _extract_error_type(self, e):
        if hasattr(e, 'error'):
          if isinstance(e.error, dict) and 'type' in e.error:
            return e.error['type']
          elif isinstance(e.error, dict) and 'error' in e.error and isinstance(e.error['error'], dict) and 'type' in e.error['error']:
            return e.error['error']['type']
          return str(type(e).__name__).lower().replace('error', '')
