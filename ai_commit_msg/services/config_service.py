from ai_commit_msg.services.local_db_service import LocalDbService, CONFIG_COLLECTION_KEY

class ConfigService:
    openai_api_key = ""
    logger_enabled = False
    model = "gpt-4o-mini"
    ollama_url = "http://localhost:11434/api/chat"

    def __init__(self):
        config = ConfigService.get_config()
        self.openai_api_key = config["openai_api_key"]
        self.logger_enabled = config["logger_enabled"]
        self.model = config["model"]
        self.ollama_url = config["ollama_url"]

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

    @staticmethod
    def set_logger_enabled(enabled):
        config = ConfigService.get_config()
        config["logger_enabled"] = enabled
        LocalDbService().set_db({CONFIG_COLLECTION_KEY: config})
