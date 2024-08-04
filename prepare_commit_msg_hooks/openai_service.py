from openai import OpenAI
from prepare_commit_msg_hooks.local_db_service import LocalDbService, CONFIG_COLLECTION_KEY

class OpenAiService:
    def __init__(self):
      api_key = OpenAiService.get_openai_api_key()

      if(api_key is None or api_key == ""):
        raise Exception("""OpenAI API key is not set. Run the following command to set the key:

gen_ai_commit_message_cli config --openai-key=<insert-your-key>
                        """)
      self.client = OpenAI(api_key=api_key)

    def chat_with_openai(self, messages):
        completion = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages
        )
        return completion.choices[0].message.content

    @staticmethod
    def get_openai_api_key():
        raw_json_db = LocalDbService().get_db()[CONFIG_COLLECTION_KEY]
        return raw_json_db["openai_api_key"]

    @staticmethod
    def set_openai_api_key(api_key):
        raw_json_db = LocalDbService().get_db()
        raw_json_db[CONFIG_COLLECTION_KEY]["openai_api_key"] = api_key
        LocalDbService().set_db(raw_json_db)




