import sys

AI_MODEL_ERRORS = {
    "OPENAI": {
        "EXCEEDED_TOKEN_SIZE": ["context_length_exceeded", "rate_limit_exceeded"]
    },
    # Add other providers here as needed
}

def handle_ai_model_error(provider: str, error_code: str):
    for error_category, error_codes in AI_MODEL_ERRORS.get(provider, {}).items():
        if error_code in error_codes:
            print(f"""
                #############################################################
                #                                                           #
                # Sorry, you have encountered a {error_category} error.  #
                #                          ⚡️⚡️⚡️                           #
                #  Please write your commit message manually.               #
                #                                                           #
                #############################################################
                """)
            sys.exit(1)

    raise ValueError(f"Unknown error code '{error_code}' for provider '{provider}'")
