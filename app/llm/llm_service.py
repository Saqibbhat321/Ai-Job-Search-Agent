from app.llm.factory import LLMFactory


class LLMService:

    def __init__(
        self,
        provider="ollama"
    ):

        self.client = LLMFactory.create(
            provider
        )

    def generate(
        self,
        prompt: str
    ):

        return self.client.generate(
            prompt
        )