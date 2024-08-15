import requests

from ai_commit_msg.services.config_service import ConfigService
from ai_commit_msg.utils.logger import Logger
from ai_commit_msg.services.model_error_handling import map_error

class OLlamaService:
    def __init__(self,):
        self.url = ConfigService.get_ollama_url()

    def chat_completion(self, prompt):
        select_model = ConfigService.get_model()

        # remove the ollama prefix
        ollama_model = select_model.replace("ollama/", "")

        Logger().log("Using Ollama model: " + ollama_model)

        data = {
            "model": ollama_model,
            "messages": prompt,
            "stream": False,
            "options": {
                # "num_keep": 5,
                # "seed": 42,
                # "num_predict": 100,
                # "top_k": 20,
                "top_p": 0.1,
                # "min_p": 0.0,
                # "tfs_z": 0.5,
                # "typical_p": 0.7,
                # "repeat_last_n": 33,
                "temperature": 0, # larger value = more randomness
                # "repeat_penalty": 1.2,
                # "presence_penalty": 1.5,
                # "frequency_penalty": 1.0,
                # "mirostat": 1,
                # "mirostat_tau": 0.8,
                # "mirostat_eta": 0.6,
                # "penalize_newline": true,
                # "stop": ["\n", "user:"],
                # "numa": false,
                # "num_ctx": 1024,
                # "num_batch": 2,
                # "num_gpu": 1,
                # "main_gpu": 0,
                # "low_vram": false,
                # "f16_kv": true,
                # "vocab_only": false,
                # "use_mmap": true,
                # "use_mlock": false,
                # "num_thread": 8
            }
        }

        headers = {
            "Content-Type": "application/json"
        }

        response = requests.post(self.url, headers=headers, json=data)
        answer = response.json()["message"]["content"]
        return answer
