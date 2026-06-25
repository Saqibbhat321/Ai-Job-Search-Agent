from app.services.skill_gap_service import SkillGapService
from app.services.roadmap_service import RoadmapService


resume_text = """
Python
FastAPI
Docker
Machine Learning
"""

job_skills = """
Python
FastAPI
Docker
LLM
MLOps
RAG
"""

gap = SkillGapService.analyze(
    resume_text,
    job_skills
)

roadmap = RoadmapService.generate(
    gap["missing_skills"]
)

print("SKILL GAP")
print(gap)

print("\nLEARNING ROADMAP")

for item in roadmap:
    print(item)