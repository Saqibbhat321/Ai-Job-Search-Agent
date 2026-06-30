from app.services.resume_tailor_service import ResumeTailorService

resume = """
Python
FastAPI
Docker
Machine Learning
"""

job = """
Python
FastAPI
Docker
LLM
RAG
MLOps
"""

service = ResumeTailorService()

result = service.analyze(
    resume,
    job
)

print(result)