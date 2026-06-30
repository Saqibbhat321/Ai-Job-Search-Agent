from app.llm.base import BaseLLM


class GeminiProvider(BaseLLM):

    def generate(
        self,
        prompt: str
    ):

        raise NotImplementedError(
            "Gemini provider not implemented yet."
        )