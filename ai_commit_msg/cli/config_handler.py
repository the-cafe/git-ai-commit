from ai_commit_msg.services.openai_service import OpenAiService
from ai_commit_msg.services.config_service import ConfigServiceSingleton
from ai_commit_msg.utils.logger import Logger

def config_handler(args):
    if args.openai_key is not None:
        if args.openai_key.strip() == "":
            print("OpenAI API key is not set. Run the following command to set the key: gen_ai_commit_message config --openai-key=<insert-your-key>")
            return;
        OpenAiService.set_openai_api_key(args.openai_key)
        Logger().log("OpenAI API key set successfully")
    elif args.reset:
        OpenAiService.reset_openai_api_key()
        Logger().log("OpenAI API key has been reset")
    else:
        Logger().log("No valid configuration option provided")

    return 0
