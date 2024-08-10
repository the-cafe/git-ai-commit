from ai_commit_msg.services.config_service import ConfigService
from ai_commit_msg.services.local_db_service import LocalDbService
from ai_commit_msg.services.openai_service import OpenAiService
from ai_commit_msg.utils.logger import Logger

def config_handler(args):
    config_service = ConfigService()

    has_updated = False

    if args.openai_key:
        OpenAiService.set_openai_api_key(args.openai_key)
        Logger().log("OpenAI API key set successfully")
        has_updated = True

    if args.reset:
        # reset the db the entire db
        LocalDbService().reset_db();
        Logger().log("OpenAI API key has been reset")
        has_updated = True

    if args.logger is not None:
        config_service.set_logger_enabled(args.logger)
        Logger().log("Logger " + ("enabled" if args.logger else "disabled"))
        has_updated = True

    if args.model:
        config_service.set_model(args.model)
        Logger().log("Model set to " + args.model)
        has_updated = True

    if args.ollama_url:
        config_service.set_ollama_url(args.ollama_url)
        Logger().log("Ollama URL set to " + args.ollama_url)
        has_updated = True

    #if there are not args, display the current config
    if not has_updated:
        display_config_db = LocalDbService().display_db()
        Logger().log(display_config_db)

    return
