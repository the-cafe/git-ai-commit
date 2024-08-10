from ai_commit_msg.services.config_service import ConfigService
from ai_commit_msg.services.local_db_service import LocalDbService
from ai_commit_msg.services.openai_service import OpenAiService
from ai_commit_msg.utils.logger import Logger

def handle_config_setup():
    Logger().log("\nWelcome to `git-ai-commit` - never write a commit message again!\n")

    selected_model = input("""
Select the AI model you would like to use, we support the following providers:
    1. OpenAI GPT-4o-mini (default)
    2. Anthropics
    3. Ollama

Select another model (press enter to skip): """
    )

    open_ai_key = input("Enter your OpenAI API key (press enter to skip): ")
    anthropic_key = input("Enter your Anthropics API key (press enter to skip): ")

    if selected_model is not "":
        ConfigService().set_model(selected_model)
    if open_ai_key is not "":
        OpenAiService.set_openai_api_key(open_ai_key)
    if anthropic_key is not "":
        ConfigService().set_anthropic_api_key(anthropic_key)

    Logger().log("Configuration setup complete")
    return


def config_handler(args):
    config_service = ConfigService()

    has_updated = False

    if args.openai_key:
        OpenAiService.set_openai_api_key(args.openai_key)
        Logger().log("OpenAI API key set successfully")
        has_updated = True

    if args.anthropic_key:
        config_service.set_anthropic_api_key(args.anthropic_key)
        Logger().log("Anthropic API key set successfully")
        has_updated = True

    if args.reset:
        #reset the db the entire db
        LocalDbService().reset_db()
        Logger().log("Configuration has been reset")
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

    if args.setup:
        handle_config_setup(config_service)

        has_updated = True


    if not has_updated:
        display_config_db = LocalDbService().display_db()
        Logger().log(display_config_db)

    return
