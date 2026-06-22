from app.services.skill_gap_service import SkillGapService


resume_text = """
Python
FastAPI
Docker
PostgreSQL
Machine Learning
"""

job_skills = """
Python
FastAPI
LLM
MLOps
Docker
"""


result = SkillGapService.analyze(
    resume_text,
    job_skills
)

print(result)