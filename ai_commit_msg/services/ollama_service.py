import requests

from ai_commit_msg.services.config_service import ConfigService
from ai_commit_msg.utils.logger import Logger

class LlamaChatService:
    def __init__(self,):
        self.url = ConfigService.get_ollama_url()

    def chat_with_llama(self, prompt):
        select_model = ConfigService.get_model()

        # remove the ollama prefix
        ollama_model = select_model.replace("ollama/", "")

        Logger().log("Using Ollama model: " + ollama_model)

        data = {
            "model": ollama_model,
            "messages": prompt,
            "stream": False,
        }

        headers = {
            "Content-Type": "application/json"
        }

        response = requests.post(self.url, headers=headers, json=data)
        answer = response.json()["message"]["content"]
        print(answer)
        return answer
