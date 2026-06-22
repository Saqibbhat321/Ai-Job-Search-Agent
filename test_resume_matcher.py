from app.resume.resume_matcher import (
    ResumeMatcher
)


with open(
    "data/sample_resume.txt",
    "r",
    encoding="utf-8"
) as file:

    resume_text = file.read()


matcher = ResumeMatcher()

results = matcher.match_resume(
    resume_text
)

for result in results:

    print()
    print("=" * 50)

    print(
        f"Job: {result['title']}"
    )

    print(
        f"Company: {result['company']}"
    )

    print(
        f"Match Score: {result['match_score']}%"
    )

    print(
        f"Missing Skills: {result['missing_skills']}"
    )