from abc import ABC, abstractmethod

class LLMService(ABC):
    @abstractmethod
    def chat_completion(self, messages):
        pass