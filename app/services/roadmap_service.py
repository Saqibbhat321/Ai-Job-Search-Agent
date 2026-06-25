class RoadmapService:

    ROADMAP = {

        "python": {
            "topic": "Python",
            "resources": [
                "Python OOP",
                "Advanced Python",
                "Async Programming"
            ]
        },

        "machine learning": {
            "topic": "Machine Learning",
            "resources": [
                "Scikit-Learn",
                "Regression",
                "Classification",
                "Model Evaluation"
            ]
        },

        "llm": {
            "topic": "Large Language Models",
            "resources": [
                "Transformers",
                "Prompt Engineering",
                "LLM Fundamentals",
                "OpenAI APIs"
            ]
        },

        "rag": {
            "topic": "Retrieval Augmented Generation",
            "resources": [
                "Embeddings",
                "FAISS",
                "Vector Search",
                "LangChain RAG"
            ]
        },

        "langchain": {
            "topic": "LangChain",
            "resources": [
                "Chains",
                "Agents",
                "Memory",
                "Tools"
            ]
        },

        "mlops": {
            "topic": "MLOps",
            "resources": [
                "MLflow",
                "Docker",
                "CI/CD",
                "Model Deployment"
            ]
        },

        "docker": {
            "topic": "Docker",
            "resources": [
                "Docker Images",
                "Containers",
                "Docker Compose"
            ]
        },

        "fastapi": {
            "topic": "FastAPI",
            "resources": [
                "Routing",
                "Dependency Injection",
                "Swagger",
                "Deployment"
            ]
        },

        "sql": {
            "topic": "SQL",
            "resources": [
                "Joins",
                "Indexes",
                "Optimization"
            ]
        },

        "postgresql": {
            "topic": "PostgreSQL",
            "resources": [
                "Database Design",
                "Transactions",
                "Performance"
            ]
        }
    }

    @classmethod
    def generate(cls, missing_skills):

        roadmap = []

        for skill in missing_skills:

            if skill in cls.ROADMAP:

                roadmap.append({
                    "skill": skill,
                    "topic": cls.ROADMAP[skill]["topic"],
                    "resources": cls.ROADMAP[skill]["resources"]
                })

        return roadmap