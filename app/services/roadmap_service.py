class RoadmapService:

    ROADMAP = {

        "llm": {
            "topic": "Large Language Models",
            "resources": [
                "HuggingFace Transformers",
                "OpenAI API Concepts",
                "Prompt Engineering"
            ]
        },

        "mlops": {
            "topic": "MLOps",
            "resources": [
                "MLflow",
                "Docker",
                "Model Deployment"
            ]
        },

        "rag": {
            "topic": "Retrieval Augmented Generation",
            "resources": [
                "LangChain",
                "FAISS",
                "Vector Databases"
            ]
        },

        "langchain": {
            "topic": "LangChain",
            "resources": [
                "Chains",
                "Agents",
                "Memory"
            ]
        },

        "docker": {
            "topic": "Docker",
            "resources": [
                "Containers",
                "Images",
                "Docker Compose"
            ]
        },

        "fastapi": {
            "topic": "FastAPI",
            "resources": [
                "Routing",
                "Dependency Injection",
                "Swagger Docs"
            ]
        }
    }

    @classmethod
    def generate(
        cls,
        missing_skills
    ):

        roadmap = []

        for skill in missing_skills:

            if skill in cls.ROADMAP:

                roadmap.append(
                    cls.ROADMAP[skill]
                )

        return roadmap