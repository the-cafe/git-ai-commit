from ai_commit_msg.services.openai_service import OpenAiService
from ai_commit_msg.services.config_service import ConfigServiceSingleton
from ai_commit_msg.utils.logger import Logger

def config_handler(args):
    if args.openai_key is not None:
        if args.openai_key.strip() == "":
            OpenAiService.reset_openai_api_key()
            Logger().log("OpenAI API key has been reset")
        else:
            OpenAiService.set_openai_api_key(args.openai_key)
            Logger().log("OpenAI API key set successfully")
        return 1

    if args.reset:
        OpenAiService.reset_openai_api_key()
        Logger().log("OpenAI API key has been reset")
        return 1

    if args.logger is not None:
        ConfigServiceSingleton.set_logger_enabled(args.logger)
        Logger().log(f"Logging {'enabled' if args.logger else 'disabled'}")
        return 1

    help_message = (
        "No valid configuration option provided. You can use:\n"
        "     -k, --openai-key Set OpenAI API key (or reset if empty)\n"
        "     -r, --reset Reset the OpenAI API key\n"
        "     -l, --logger Enable or disable logging (true/false)\n"
        "     -h, --help Display this help message"
    )
    Logger().log(help_message)
    return 0
