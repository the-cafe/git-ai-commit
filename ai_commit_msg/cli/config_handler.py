from ai_commit_msg.services.openai_service import OpenAiService
from ai_commit_msg.services.config_service import ConfigService
from ai_commit_msg.utils.logger import Logger

def config_handler(args):
    if args.openai_key is None:
        Logger().log("No OpenAI API key provided")
        return None

    if args.openai_key.strip() == "":
        OpenAiService.reset_openai_api_key()
        Logger().log("OpenAI API key has been reset")
        return None
    elif args.openai_key:
        OpenAiService.set_openai_api_key(args.openai_key)
        Logger().log("OpenAI API key set successfully")
        return

    return 0
