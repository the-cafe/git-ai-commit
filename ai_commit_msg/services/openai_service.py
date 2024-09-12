from logging import Logger
from ai_commit_msg.utils.error import map_error
from openai import OpenAI
from ai_commit_msg.services.config_service import ConfigService
from ai_commit_msg.services.local_db_service import (
    LocalDbService,
    CONFIG_COLLECTION_KEY,
)
from ai_commit_msg.utils.models import OPEN_AI_MODEL_LIST


class OpenAiService:
    client = None

    def __init__(self):
        api_key = OpenAiService.get_openai_api_key()

        if api_key is None or api_key == "":
            raise Exception(
                """
        OpenAI API key is not set. Run the following command to set the key:

        git-ai-commit config --openai-key=<insert-your-key>
        """
            )
        self.client = OpenAI(api_key=api_key)

    def chat_with_openai(self, messages):
        model_name = ConfigService.get_model()

        if model_name not in OPEN_AI_MODEL_LIST:
            raise Exception(
                f"Attempted to call OpenAI with an invalid model: {model_name}"
            )
        try:
            completion = self.client.chat.completions.create(
                model=model_name, messages=messages
            )
            return completion.choices[0].message.content
        except Exception as e:
            raise map_error("OPENAI", getattr(e, "code", str(e)), e)

    @staticmethod
    def get_openai_api_key():
        raw_json_db = LocalDbService().get_db()[CONFIG_COLLECTION_KEY]
        return raw_json_db["openai_api_key"]

    @staticmethod
    def set_openai_api_key(api_key):
        raw_json_db = LocalDbService().get_db()
        raw_json_db[CONFIG_COLLECTION_KEY]["openai_api_key"] = api_key
        LocalDbService().set_db(raw_json_db)
