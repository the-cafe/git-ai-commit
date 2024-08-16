from enum import Enum

class ErrorCode(Enum):
    EXCEEDED_TOKEN_SIZE = "EXCEEDED_TOKEN_SIZE"
    AUTHENTICATION_ERROR = "AUTHENTICATION_ERROR"
    PERMISSION_DENIED = "PERMISSION_DENIED"
    NOT_FOUND = "NOT_FOUND"
    RATE_LIMIT_ERROR = "RATE_LIMIT_ERROR"
    INTERNAL_SERVER_ERROR = "INTERNAL_SERVER_ERROR"
    API_CONNECTION_ERROR = "API_CONNECTION_ERROR"
    INVALID_REQUEST_ERROR = "INVALID_REQUEST_ERROR"

AI_MODEL_ERRORS = {
        "OPENAI": {
            "context_length_exceeded": ErrorCode.EXCEEDED_TOKEN_SIZE,
            "rate_limit_exceeded": ErrorCode.EXCEEDED_TOKEN_SIZE,
            "tokens_exceeded_error": ErrorCode.EXCEEDED_TOKEN_SIZE,
            "authentication_error": ErrorCode.AUTHENTICATION_ERROR,
            "not_found_error": ErrorCode.NOT_FOUND,
            "server_error": ErrorCode.INTERNAL_SERVER_ERROR,
            "permission_error": ErrorCode.PERMISSION_DENIED,
            # TODO - Add other OpenAI error codes here
        },
        "ANTHROPIC": {
            "AuthenticationError": ErrorCode.AUTHENTICATION_ERROR,
            "PermissionDeniedError": ErrorCode.PERMISSION_DENIED,
            "NotFoundError": ErrorCode.NOT_FOUND,
            "RateLimitError": ErrorCode.RATE_LIMIT_ERROR,
            "InternalServerError": ErrorCode.INTERNAL_SERVER_ERROR,
            "APIConnectionError": ErrorCode.API_CONNECTION_ERROR,
            "InvalidRequestError": ErrorCode.INVALID_REQUEST_ERROR,
            "BadRequestError": ErrorCode.EXCEEDED_TOKEN_SIZE,
        },
        "OLLAMA": {
            # TODO - Add Ollama-specific error codes here
        }
    }

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    return AIModelHandlerError(provider, error_type, original_error)


class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

class LLMProviderError(Exception):
    def __init__(self, provider):
        self.provider = provider
