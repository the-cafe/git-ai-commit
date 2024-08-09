from ai_commit_msg.services.local_db_service import LocalDbService, CONFIG_COLLECTION_KEY
from ai_commit_msg.services.git_service import GitService
import os

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

    @staticmethod
    def set_logger_enabled(enabled):
        config = ConfigService.get_config()
        config["logger_enabled"] = enabled
        LocalDbService().set_db({CONFIG_COLLECTION_KEY: config})

        git_dir = GitService.get_git_directory()
        log_file = os.path.join(git_dir, "ai_commit_message.log")

        if enabled:
            if not os.path.exists(log_file):
                open(log_file, 'a').close()
                print(f"Logging is now enabled. New log file created at: {log_file}")
            else:
                print(f"Logging is now enabled. You can find the logs at: {log_file}")
        else:
            if os.path.exists(log_file):
                os.remove(log_file)
                print(f"Logging is now disabled. Log file removed: {log_file}")
            else:
                print("Logging is now disabled. No log file found to remove.")
