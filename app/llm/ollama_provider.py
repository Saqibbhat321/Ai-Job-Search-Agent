import re
import requests

from app.core.config import settings
from app.llm.base import BaseLLM


class OllamaProvider(BaseLLM):

    def __init__(self):

        self.base_url = settings.OLLAMA_BASE_URL

        self.model = settings.OLLAMA_MODEL

    def generate(
        self,
        prompt: str
    ):

        response = requests.post(

            f"{self.base_url}/api/generate",

            json={
                "model": self.model,
                "prompt": prompt,
                "stream": False,
                "think": False
            },

            timeout=600
        )

        response.raise_for_status()

        answer = response.json()["response"]

        answer = re.sub(
            r"<think>.*?</think>",
            "",
            answer,
            flags=re.DOTALL
        ).strip()

        return answer