from app.services.roadmap_service import RoadmapService

missing_skills = [
    "llm",
    "mlops"
]

roadmap = RoadmapService.generate(
    missing_skills
)

for item in roadmap:

    print(item)