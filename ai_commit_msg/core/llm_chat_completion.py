from ai_commit_msg.services.config_service import ConfigService
from ai_commit_msg.services.llm_service_factory import LLMServiceFactory
from ai_commit_msg.utils.logger import Logger


def llm_chat_completion(prompt):
    select_model = ConfigService.get_model()

    service = LLMServiceFactory.create_service(select_model)

    if service is None:
        Logger().log("Unsupported model: " + select_model)
        return ""

    return service.chat_completion(prompt)
