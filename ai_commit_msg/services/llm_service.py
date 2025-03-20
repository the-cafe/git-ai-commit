from abc import ABC, abstractmethod


class LLMService(ABC):
    """Abstract base class for LLM services"""

    @abstractmethod
    def chat_completion(self, messages):
        """
        Process a chat completion request with the given messages

        Args:
            messages: The prompt messages to send to the LLM

        Returns:
            str: The generated response from the LLM
        """
        pass
