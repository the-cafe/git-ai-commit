
from ai_commit_msg.services.openai_service import OpenAiService
from ai_commit_msg.utils.logger import Logger

def config_handler(args):
    if(args.openai_key is None):
        Logger().log("OpenAI API key is required")
        return

    OpenAiService.set_openai_api_key(args.openai_key)

    Logger().log("OpenAI API key set successfully")
