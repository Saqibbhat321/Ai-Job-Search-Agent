import re


class SkillExtractor:

    SKILL_ALIASES = {

        "machine learning": [
            "machine learning",
            "ml"
        ],

        "deep learning": [
            "deep learning"
        ],

        "llm": [
            "llm",
            "llms",
            "large language model",
            "large language models"
        ],

        "mlops": [
            "mlops",
            "machine learning operations"
        ],

        "python": [
            "python"
        ],

        "sql": [
            "sql"
        ],

        "postgresql": [
            "postgresql",
            "postgres"
        ],

        "docker": [
            "docker"
        ],

        "fastapi": [
            "fastapi"
        ],

        "langchain": [
            "langchain"
        ],

        "rag": [
            "rag",
            "retrieval augmented generation"
        ],

        "faiss": [
            "faiss"
        ],

        "sentence transformers": [
            "sentence transformers"
        ],

        "transformers": [
            "transformers"
        ],

        "pytorch": [
            "pytorch"
        ],

        "tensorflow": [
            "tensorflow"
        ],

        "statistics": [
            "statistics"
        ],

        "numpy": [
            "numpy"
        ],

        "pandas": [
            "pandas"
        ]
    }

    @classmethod
    def extract_skills(
        cls,
        text: str
    ):

        text = text.lower()

        found_skills = set()

        for canonical_skill, aliases in cls.SKILL_ALIASES.items():

            for alias in aliases:

                pattern = (
                    r"\b" +
                    re.escape(alias) +
                    r"\b"
                )

                if re.search(
                    pattern,
                    text
                ):
                    found_skills.add(
                        canonical_skill
                    )
                    break

        return sorted(
            list(found_skills)
        )