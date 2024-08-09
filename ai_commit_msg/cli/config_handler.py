from ai_commit_msg.services.openai_service import OpenAiService
from ai_commit_msg.services.config_service import ConfigServiceSingleton
from ai_commit_msg.utils.logger import Logger
from ai_commit_msg.services.git_service import GitService
import os

def config_handler(args):
    if args.openai_key is not None:
        if args.openai_key.strip() == "":
            raise ValueError("OpenAI API key is not set. Run the following command to set the key: gen_ai_commit_message_cli config --openai-key=<insert-your-key>")
        OpenAiService.set_openai_api_key(args.openai_key)
        Logger().log("OpenAI API key set successfully")
    elif args.reset:
        OpenAiService.reset_openai_api_key()
        Logger().log("OpenAI API key has been reset")
    elif args.logger is not None:
        ConfigServiceSingleton.set_logger_enabled(args.logger)
        git_dir = GitService.get_git_directory()
        log_file = os.path.join(git_dir, "ai_commit_message.log")

        if args.logger:
            Logger().log("Logger enabled")
            if not os.path.exists(log_file):
                open(log_file, 'a').close()
                print(f"Logging is now enabled. New log file created at: {log_file}")
            else:
                print(f"Logging is now enabled. You can find the logs at: {log_file}")
        else:
            Logger().log("Logger disabled")
            if os.path.exists(log_file):
                os.remove(log_file)
                print(f"Logging is now disabled. Log file removed: {log_file}")
            else:
                print("Logging is now disabled. No log file found to remove.")
    else:
        Logger().log("No valid configuration option provided you can use:")
        Logger().log("     -k, --openai-key Set OpenAI API key")
        Logger().log("     -r, --reset Reset the OpenAI API key")
        Logger().log("     -l, --logger Enable or disable logging (true/false)")
        Logger().log("     -h, --help Display this help message")
        Logger().log("     fuck u")

    return 0
