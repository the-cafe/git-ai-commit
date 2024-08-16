from ai_commit_msg.utils.model_error_handling import AIModelHandlerError
from ai_commit_msg.utils.get_ai_model_errors import AI_MODEL_ERRORS

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
