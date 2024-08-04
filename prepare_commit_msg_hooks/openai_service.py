from openai import OpenAI

class OpenAiService:
    def __init__(self, api_key=None):

      if(api_key is None):
        raise Exception("OPENAI_API_KEY is not set")
      self.client = OpenAI(api_key=api_key)

    def chat_with_openai(self, messages):
        completion = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages
        )
        return completion.choices[0].message.content
