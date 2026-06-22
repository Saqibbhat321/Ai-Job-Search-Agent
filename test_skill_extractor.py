
from app.utils.skill_extractor import SkillExtractor

text = """
Python
FastAPI
Docker
PostgreSQL
Machine Learning
LLM
MLOps
"""

print(
    SkillExtractor.extract_skills(
        text
    )
)