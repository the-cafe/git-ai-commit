from ai_commit_msg.services.openai_service import OpenAiService
from ai_commit_msg.services.config_service import ConfigService
from ai_commit_msg.utils.logger import Logger
from ai_commit_msg.services.git_service import GitService
import os

def config_handler(args):
    if args.openai_key is not None:
        handle_openai_key(args.openai_key)
    elif args.reset:
        handle_reset()
    elif args.logger is not None:
        handle_logger(args.logger)
    else:
        display_help()
    return 0

def handle_openai_key(key):
    if key.strip() == "":
        raise ValueError("OpenAI API key is not set. Run the following command to set the key: gen_ai_commit_message_cli config --openai-key=<insert-your-key>")
    OpenAiService.set_openai_api_key(key)
    Logger().log("OpenAI API key set successfully")

def handle_reset():
    OpenAiService.reset_openai_api_key()
    Logger().log("OpenAI API key has been reset")

def handle_logger(enabled):
    ConfigService.set_logger_enabled(enabled)
    git_dir = GitService.get_git_directory()
    log_file = os.path.join(git_dir, "ai_commit_message.log")

    if enabled:
        enable_logging(log_file)
    else:
        disable_logging(log_file)

def enable_logging(log_file):
    Logger().log("Logger enabled")
    if not os.path.exists(log_file):
        open(log_file, 'a').close()
        print(f"Logging is now enabled. New log file created at: {log_file}")
    else:
        print(f"Logging is now enabled. You can find the logs at: {log_file}")

def disable_logging(log_file):
    Logger().log("Logger disabled")
    if os.path.exists(log_file):
        os.remove(log_file)
        print(f"Logging is now disabled. Log file removed: {log_file}")
    else:
        print("Logging is now disabled. No log file found to remove.")

def display_help():
    help_message = (
        "No valid configuration option provided. You can use:\n"
        "     -k, --openai-key Set OpenAI API key\n"
        "     -r, --reset Reset the OpenAI API key\n"
        "     -l, --logger Enable or disable logging (true/false)\n"
        "     -h, --help Display this help message\n"
    )
    Logger().log(help_message)
