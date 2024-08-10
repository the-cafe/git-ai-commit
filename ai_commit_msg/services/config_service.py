from ai_commit_msg.services.local_db_service import LocalDbService, CONFIG_COLLECTION_KEY
from ai_commit_msg.utils.models import OPEN_AI_MODEL_LIST, ANTHROPIC_MODEL_LIST

class ConfigService:
    anthropic_api_key = ""
    openai_api_key = ""
    logger_enabled = False
    model = "gpt-4o-mini"
    ollama_url = "http://localhost:11434/api/chat"

    def __init__(self):
        config = ConfigService.get_config()

        if "anthropic_api_key" in config: self.anthropic_api_key = config["anthropic_api_key"]
        if "openai_api_key" in config: self.openai_api_key = config["openai_api_key"]
        if "logger_enabled" in config: self.logger_enabled = config["logger_enabled"]
        if "model" in config: self.model = config["model"]
        if "ollama_url" in config: self.ollama_url = config["ollama_url"]


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

    def set_model(self, model):
        if not ConfigService.is_supported_model(model):
            raise Exception(f"Model {model} is not supported")

        config = ConfigService.get_config()
        config["model"] = model
        LocalDbService().set_db({CONFIG_COLLECTION_KEY: config})
        self.model = model

    @staticmethod
    def is_supported_model(model):
        # check if the model has ollama prefix
        if model.startswith("ollama") or model in ANTHROPIC_MODEL_LIST or model in OPEN_AI_MODEL_LIST:
            return True

        return False
