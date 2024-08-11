import time
import os
import json

from ai_commit_msg.services.git_service import GitService

CONFIG_COLLECTION_KEY = "config"

default_db = {
    CONFIG_COLLECTION_KEY: {
      "anthropic_api_key": "",
      "openai_api_key": "",
      "logger_enabled": False,
      "model": "gpt-4o-mini",
      "ollama_url": "http://localhost:11434/api/chat",
      "last_updated_at": ""
    }
}

class LocalDbService:
    def __init__(self):
        repo_git_directory = GitService.get_git_directory()

        self.db_path = os.path.join(repo_git_directory, '.ai_commit_msg_config.json')

        # Ensure the directory exists
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)

        # check if file exist
        if not os.path.exists(self.db_path):
            self.create_db()

    def create_db(self):
        with open(self.db_path, 'w') as db:
            json.dump(default_db, db)

    def get_db(self):
        with open(self.db_path, 'r') as db:
            return json.load(db)

    def set_db(self, data):
        data["config"]["last_updated_at"] = int(time.time())
        with open(self.db_path, 'w') as db:
            json.dump(data, db)

    def append_db(self, data):
        with open(self.db_path, 'a') as db:
            db.write(data)

    def reset_db(self):
        self.set_db(default_db)

    def display_db(self):
        db_contents = self.get_db()
        config = db_contents.get("config", {})

        output = "Settings\n"
        output += "----------------------\n"
        for key, value in config.items():
            if key == "last_updated_at" and isinstance(value, int):
                value = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(value))
            elif key.endswith("_api_key") and value:
                value = value[:8] + "..." + value[-4:]
            output += f"{key.replace('_', ' ').title()}: {value}\n"

        return output
