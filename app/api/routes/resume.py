from fastapi import APIRouter

from app.resume.resume_matcher import (
    ResumeMatcher
)

router = APIRouter()

matcher = ResumeMatcher()


@router.post("/resume/match")
def match_resume(
    resume_text: str
):

    results = matcher.match_resume(
        resume_text
    )

    return {
        "recommendations": results
    }