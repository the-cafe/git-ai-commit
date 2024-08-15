class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
vvclass AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)
class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

AI_MODEL_ERRORS = {
    "OPENAI": {
        "context_length_exceeded": "EXCEEDED_TOKEN_SIZE",
        "rate_limit_exceeded": "EXCEEDED_TOKEN_SIZE",
        # Add other OpenAI error codes here
    },
    "ANTHROPIC": {
        "AuthenticationError": "AUTHENTICATION_ERROR",
        "PermissionDeniedError": "PERMISSION_DENIED",
        "NotFoundError": "NOT_FOUND",
        "RateLimitError": "RATE_LIMIT_ERROR",
        "InternalServerError": "INTERNAL_SERVER_ERROR",
        "APIConnectionError": "API_CONNECTION_ERROR",
        "InvalidRequestError": "INVALID_REQUEST_ERROR",
        "BadRequestError": "EXCEEDED_TOKEN_SIZE",
    },
    "OLLAMA": {
        # Add Ollama-specific error codes here
    }
}

def map_error(provider: str, error_code: str, original_error: Exception):
    error_categories = AI_MODEL_ERRORS.get(provider, {})
    print(f"Mapping error for provider: {provider}, error_code: {error_code}")

    error_type = error_categories.get(error_code, "UNKNOWN_ERROR")
    print(f"Mapped to error category: {error_type}")
    return AIModelHandlerError(provider, error_type, original_error)

