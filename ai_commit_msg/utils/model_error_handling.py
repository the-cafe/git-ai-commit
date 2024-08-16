from ai_commit_msg.utils.get_ai_model_errors import get_ai_model_errors

class AIModelHandlerError(Exception):
    def __init__(self, provider, error_type, original_error):
        self.provider = provider
        self.error_type = error_type
        self.original_error = original_error
        super().__init__(f"{provider} error: {error_type}")

get_ai_model_errors()
