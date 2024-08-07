

from ai_commit_msg.services.openai_service import OpenAiService

def config_handler(args):
    OpenAiService.set_openai_api_key(args.openai_key)
