from app.llm.ollama_provider import OllamaProvider
from app.llm.gemini_provider import GeminiProvider


class LLMFactory:

    @staticmethod
    def create(
        provider: str
    ):

        provider = provider.lower()

        if provider == "ollama":
            return OllamaProvider()

        if provider == "gemini":
            return GeminiProvider()

        raise ValueError(
            "Unsupported provider"
        )