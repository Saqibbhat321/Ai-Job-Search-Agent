import re


class SkillExtractor:

    SKILLS = [

        "python",
        "sql",
        "postgresql",
        "mysql",

        "machine learning",
        "deep learning",

        "pytorch",
        "tensorflow",

        "scikit-learn",

        "fastapi",
        "flask",
        "django",

        "docker",
        "kubernetes",

        "aws",
        "azure",
        "gcp",

        "langchain",
        "rag",

        "faiss",
        "mlflow",

        "sentence transformers",

        "transformers",

        "llm",

        "genai",

        "numpy",
        "pandas"
    ]

    @classmethod
    def extract_skills(
        cls,
        text: str
    ):

        text = text.lower()

        found_skills = []

        for skill in cls.SKILLS:

            pattern = r"\b" + re.escape(skill) + r"\b"

            if re.search(
                pattern,
                text
            ):

                found_skills.append(
                    skill
                )

        return sorted(
            list(
                set(found_skills)
            )
        )