from app.utils.skill_extractor import SkillExtractor


class SkillGapService:

    @staticmethod
    def analyze(
        resume_text: str,
        job_skills: str
    ):

        resume_skills = set(
            SkillExtractor.extract_skills(
                resume_text
            )
        )

        required_skills = set(
            SkillExtractor.extract_skills(
                job_skills
            )
        )

        matched_skills = sorted(
            list(
                resume_skills &
                required_skills
            )
        )

        missing_skills = sorted(
            list(
                required_skills -
                resume_skills
            )
        )

        match_percentage = 0

        if len(required_skills) > 0:

            match_percentage = round(
                (
                    len(matched_skills)
                    /
                    len(required_skills)
                ) * 100,
                2
            )

        return {
            "match_percentage": match_percentage,
            "matched_skills": matched_skills,
            "missing_skills": missing_skills
        }