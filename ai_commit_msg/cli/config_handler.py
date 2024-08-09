from ai_commit_msg.services.openai_service import OpenAiService
from ai_commit_msg.utils.logger import Logger
from ai_commit_msg.services.config_service import ConfigService

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
        ConfigService.set_logger_enabled(args.logger)
    else:
        help_message = (
            "No valid configuration option provided. You can use:\n"
            "     -k, --openai-key Set OpenAI API key\n"
            "     -r, --reset Reset the OpenAI API key\n"
            "     -l, --logger Enable or disable logging (true/false)\n"
            "     -h, --help Display this help message\n"
        )
        Logger().log(help_message)
    return None
