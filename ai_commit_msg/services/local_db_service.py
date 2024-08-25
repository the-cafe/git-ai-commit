import time
import os
import json
from enum import Enum

from ai_commit_msg.services.git_service import GitService

CONFIG_COLLECTION_KEY = "config"

class ConfigKeysEnum(Enum):
    ANTHROPIC_API_KEY = "anthropic_api_key"
    OPENAI_API_KEY = "openai_api_key"
    LOGGER_ENABLED = "logger_enabled"
    MODEL = "model"
    OLLAMA_URL = "ollama_url"
    LAST_UPDATED_AT = "last_updated_at"
    MAX_LENGTH = "max_length"

default_db = {
    CONFIG_COLLECTION_KEY: {
        ConfigKeysEnum.ANTHROPIC_API_KEY.value: "",
        ConfigKeysEnum.OPENAI_API_KEY.value: "",
        ConfigKeysEnum.LOGGER_ENABLED.value: False,
        ConfigKeysEnum.MODEL.value: "gpt-4o-mini",
        ConfigKeysEnum.OLLAMA_URL.value: "http://localhost:11434/api/chat",
        ConfigKeysEnum.LAST_UPDATED_AT.value: "",
        ConfigKeysEnum.MAX_LENGTH.value: 50,
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
