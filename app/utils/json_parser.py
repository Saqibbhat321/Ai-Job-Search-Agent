import json
import re


class JSONParser:

    @staticmethod
    def parse(text: str):

        # Remove markdown code fences
        text = re.sub(
            r"```json|```",
            "",
            text
        ).strip()

        # Find first JSON object
        start = text.find("{")
        end = text.rfind("}")

        if start == -1 or end == -1:
            raise ValueError("No JSON found in LLM response.")

        json_text = text[start:end + 1]

        return json.loads(json_text)