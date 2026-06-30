from app.services.skill_gap_service import SkillGapService
from app.services.roadmap_service import RoadmapService


class ResumeTailorService:

    def analyze(
        self,
        resume_text: str,
        job_skills: str
    ):

        gap = SkillGapService.analyze(
            resume_text,
            job_skills
        )

        roadmap = RoadmapService.generate(
            gap["missing_skills"]
        )

        ats_score = gap["match_percentage"]

        return {

            "ats_score": ats_score,

            "missing_keywords": gap["missing_skills"],

            "resume_summary":

            "Resume already matches many technical requirements. "
            "Add the missing skills where applicable and quantify achievements.",

            "improved_project_bullets":[

                "Quantify project impact using measurable metrics.",

                "Mention deployment, Docker, APIs, and cloud technologies.",

                "Highlight production-ready architecture."
            ],

            "recommended_skills": roadmap
        }