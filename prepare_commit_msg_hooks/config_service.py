from prepare_commit_msg_hooks.local_db_service import LocalDbService, CONFIG_COLLECTION_KEY

class ConfigService:
    openai_api_key = ""
    logger_enabled = False

    def __init__(self):
        config = ConfigService.get_config()
        self.openai_api_key = config["openai_api_key"]
        self.logger_enabled = config["logger_enabled"]

    @staticmethod
    def get_config():
        raw_json_db = LocalDbService().get_db()[CONFIG_COLLECTION_KEY]
        return raw_json_db

ConfigServiceSingleton = ConfigService()

