import time

from ai_commit_msg.services.local_db_service import (
    ConfigKeysEnum,
    LocalDbService,
    CONFIG_COLLECTION_KEY,
)
from ai_commit_msg.utils.models import OPEN_AI_MODEL_LIST, ANTHROPIC_MODEL_LIST


class ConfigService:
    anthropic_api_key = ""
    openai_api_key = ""
    logger_enabled = False
    model = "gpt-4o-mini"
    ollama_url = "http://localhost:11434/api/chat"
    last_updated_at = ""
    prefix = ""
    max_length = 50

    def __init__(self):
        config = ConfigService.get_config()

        if "anthropic_api_key" in config:
            self.anthropic_api_key = config["anthropic_api_key"]
        if "openai_api_key" in config:
            self.openai_api_key = config["openai_api_key"]
        if "logger_enabled" in config:
            self.logger_enabled = config["logger_enabled"]
        if "model" in config:
            self.model = config["model"]
        if "ollama_url" in config:
            self.ollama_url = config["ollama_url"]
        if "last_updated_at" in config:
            self.last_updated_at = config["last_updated_at"]
        if "prefix" in config:
            self.prefix = config["prefix"]
        if ConfigKeysEnum.MAX_LENGTH.value in config:
            self.max_length = config[ConfigKeysEnum.MAX_LENGTH.value]

    @staticmethod
    def get_config():
        raw_json_db = LocalDbService().get_db()[CONFIG_COLLECTION_KEY]
        return raw_json_db

    @staticmethod
    def get_model():
        raw_json_db = LocalDbService().get_db()[CONFIG_COLLECTION_KEY]
        return raw_json_db["model"]

    @staticmethod
    def get_ollama_url():
        raw_json_db = LocalDbService().get_db()[CONFIG_COLLECTION_KEY]
        return raw_json_db["ollama_url"]

    def set_logger_enabled(self, enabled):
        config = ConfigService.get_config()
        config["logger_enabled"] = enabled
        LocalDbService().set_db({CONFIG_COLLECTION_KEY: config})
        self.logger_enabled = enabled

    def get_anthropic_api_key(self):
        raw_config = ConfigService.get_config()
        self.anthropic_api_key = raw_config["anthropic_api_key"]

        return self.anthropic_api_key

    def set_anthropic_api_key(self, api_key):
        config = ConfigService.get_config()
        config["anthropic_api_key"] = api_key
        LocalDbService().set_db({CONFIG_COLLECTION_KEY: config})
        self.anthropic_api_key = api_key

    def set_openai_api_key(self, api_key):
        config = ConfigService.get_config()
        config["openai_api_key"] = api_key
        LocalDbService().set_db({CONFIG_COLLECTION_KEY: config})
        self.openai_api_key = api_key

    def set_model(self, model):
        if not ConfigService.is_supported_model(model) and model is not "":
            raise Exception(f"Model {model} is not supported")

        config = ConfigService.get_config()
        config["model"] = model
        LocalDbService().set_db({CONFIG_COLLECTION_KEY: config})
        self.model = model

    def set_ollama_url(self, url):
        config = ConfigService.get_config()
        config["ollama_url"] = url
        LocalDbService().set_db({CONFIG_COLLECTION_KEY: config})
        self.ollama_url = url

    def set_last_updated_at(self, last_updated_at=str(time.time())):
        config = ConfigService.get_config()
        config["last_updated_at"] = last_updated_at
        LocalDbService().set_db({CONFIG_COLLECTION_KEY: config})
        self.last_updated_at = last_updated_at

    def set_prefix(self, prefix):
        config = ConfigService.get_config()
        config["prefix"] = prefix
        LocalDbService().set_db({CONFIG_COLLECTION_KEY: config})
        self.prefix = prefix

    def set_max_length(self, max_length):
        config = ConfigService.get_config()
        config[ConfigKeysEnum.MAX_LENGTH.value] = int(max_length)
        LocalDbService().set_db({CONFIG_COLLECTION_KEY: config})
        self.max_length = max_length

    @staticmethod
    def is_supported_model(model):
        # check if the model has ollama prefix
        if (
            model.startswith("ollama")
            or model in ANTHROPIC_MODEL_LIST
            or model in OPEN_AI_MODEL_LIST
        ):
            return True

        return False
