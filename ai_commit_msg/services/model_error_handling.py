class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "EXCEEDED_TOKEN_SIZE": ["context_length_exceeded", "rate_limit_exceeded"],
    },
    "ANTHROPIC": {
        "AUTHENTICATION_ERROR": "AuthenticationError",
        "PERMISSION_DENIED": "PermissionDeniedError",
        "NOT_FOUND": "NotFoundError",
        "RATE_LIMIT_ERROR": "RateLimitError",
        "INTERNAL_SERVER_ERROR": "InternalServerError",
        "API_CONNECTION_ERROR": "APIConnectionError",
        "INVALID_REQUEST_ERROR": "InvalidRequestError",
        "EXCEEDED_TOKEN_SIZE": "BadRequestError",
        "BAD_REQUEST_ERROR": "BadRequestError"
    },
    "OLLAMA": {
        # Add Ollama-specific error types here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    for error_category, error_codes in error_categories.items():
        if error_code == error_codes or (isinstance(error_codes, list) and error_code in error_codes):
            print(f"Mapped to error category: {error_category}")
            return AIModelHandlerError(provider, error_category, original_error)

    print(f"No matching error category found, defaulting to UNKNOWN_ERROR")
    return AIModelHandlerError(provider, "UNKNOWN_ERROR", original_error)
