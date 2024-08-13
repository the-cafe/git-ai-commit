import tiktoken
OPEN_AI_MODEL_LIST = {
  "gpt-3.5-turbo": 4096,
  "gpt-3.5-turbo-instruct": 4096,
  "gpt-3.5-turbo-0613": 4096,
  "gpt-3.5-turbo-0301": 4096,
  "gpt-3.5-turbo-1106": 4096,
  "gpt-3.5-turbo-0125": 4096,
  "gpt-3.5-turbo-16k": 16384,
  "gpt-3.5-turbo-16k-0613": 16384,
  "gpt-3.5-turbo-16k-0301": 16384,
  "gpt-4": 4096,
  "gpt-4-0314": 4096,
  "gpt-4-0613": 4096,
  "gpt-4-1106-preview": 4096,
  "gpt-4-0125-preview": 4096,
  "gpt-4-turbo-preview": 4096,
  "gpt-4-vision-preview": 4096,
  "gpt-4-1106-vision-preview": 4096,
  "gpt-4-turbo": 4096,
  "gpt-4-turbo-2024-04-09": 4096,
  "gpt-4-32k": 32768,
  "gpt-4-32k-0314": 32768,
  "gpt-4-32k-0613": 32768,
  "gpt-4o": 4096,
  "gpt-4o-2024-05-13": 4096,
  "gpt-4o-mini": 4096,
  "gpt-4o-mini-2024-07-18": 4096
}
def truncate_diff(diff: str, model_name: str) -> str:
    # Retrieve the max tokens for the given model name from the dictionary
    # If the model name is not found, default to 4096 tokens
    max_tokens = OPEN_AI_MODEL_LIST.get(model_name, 4096)

    # Initialize the tokenizer for the given model
    tokenizer = tiktoken.encoding_for_model(model_name)

    # Tokenize the diff
    tokens = tokenizer.encode(diff)
    if len(tokens) <= max_tokens:
        return diff

    # Truncate the diff to fit within the max tokens
    truncated_tokens = tokens[:max_tokens - 10]  # Reserve some tokens for the truncation message
    truncated_diff = tokenizer.decode(truncated_tokens)

    # Add truncation message
    truncation_message = "\n... (diff truncated due to length) ..."
    truncated_diff += truncation_message

    return truncated_diff
