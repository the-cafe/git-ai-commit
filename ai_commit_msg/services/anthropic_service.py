from ai_commit_msg.utils.models import ANTHROPIC_MODEL_LIST
import anthropic
from ai_commit_msg.services.config_service import ConfigService

class AnthropicService:
  api_key = ""

  def __init__(self, ):
    self.api_key = ConfigService().get_anthropic_api_key()

    if(self.api_key is None or self.api_key == ""):
      raise Exception("""Anthropic API key is not set. Run the following command to set the key:

                   git_ai_commit config --anthropic-key=<insert  your key>
                   """)

    self.client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key=self.api_key,
    )

  def chat_completion(self, messages):
    select_model = ConfigService.get_model()

    if(select_model not in ANTHROPIC_MODEL_LIST):
        raise Exception(f"Attempted to call Anthropic with an invalid model: {select_model}")


    message = self.client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=1024,
        system=messages[0]["content"],
        messages=[messages[1]],
    )
    print(message.content[0].text)

    return message.content[0].text