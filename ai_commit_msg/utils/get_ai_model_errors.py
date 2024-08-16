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


def get_ai_model_errors():
    return {
        "OPENAI": {
            "context_length_exceeded": ErrorCode.EXCEEDED_TOKEN_SIZE,
            "rate_limit_exceeded": ErrorCode.EXCEEDED_TOKEN_SIZE,
            # Add other OpenAI error codes here
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
            # Add Ollama-specific error codes here
        }
    }
