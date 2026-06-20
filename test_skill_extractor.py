from app.resume.skill_extractor import (
    SkillExtractor
)


with open(
    "data/sample_resume.txt",
    "r",
    encoding="utf-8"
) as file:

    resume_text = file.read()


skills = SkillExtractor.extract_skills(
    resume_text
)

print(skills)