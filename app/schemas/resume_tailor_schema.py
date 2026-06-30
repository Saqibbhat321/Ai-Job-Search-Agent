from pydantic import BaseModel


class ResumeTailorResponse(BaseModel):

    ats_score: int

    missing_keywords: list[str]

    resume_summary: str

    improved_project_bullets: list[str]

    recommended_skills: list[str]