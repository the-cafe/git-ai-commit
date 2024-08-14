import sys
import anthropic

AI_MODEL_ERRORS = {
    "OPENAI": {
        "EXCEEDED_TOKEN_SIZE": ["context_length_exceeded", "rate_limit_exceeded"]
    },
    "ANTHROPIC": {
        "AUTHENTICATION_ERROR": "authentication_error",
        "PERMISSION_DENIED": "permission_denied",
        "NOT_FOUND": "not_found",
        "RATE_LIMIT_ERROR": "rate_limit_error",
        "INTERNAL_SERVER_ERROR": "internal_server_error",
        "API_CONNECTION_ERROR": "api_connection_error"
    }
}

def handle_ai_model_error(provider: str, error_code: str):
    error_categories = AI_MODEL_ERRORS.get(provider, {})

    for error_category, error_codes in error_categories.items():
        if error_code == error_codes or (isinstance(error_codes, list) and error_code in error_codes):
            if (provider == "OPENAI" and error_category == "EXCEEDED_TOKEN_SIZE") or \
               (provider == "ANTHROPIC" and error_category == "RATE_LIMIT_ERROR"):
                print("""
                    #############################################################
                    #                                                           #
                    # Sorry, you have exceeded the token size or rate limit.    #
                    #                          ⚡️⚡️⚡️                           #
                    #  Please write your commit message manually.               #
                    #                                                           #
                    #############################################################
                    """)
            else:
                print(f"""
                    #############################################################
                    #                                                           #
                    # Sorry, you have encountered a {error_category} error.     #
                    #                          ⚡️⚡️⚡️                           #
                    #                                                           #
                    #############################################################
                    """)
            sys.exit(1)

    print(f"""
        #############################################################
        #                                                           #
        # Sorry, an unexpected error occurred: {error_code}       #
        #                          ⚡️⚡️⚡️                           #
        #                                                           #
        #############################################################
        """)
    sys.exit(1)
