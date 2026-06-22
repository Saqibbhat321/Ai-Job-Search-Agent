import faiss
import pandas as pd

from sqlalchemy import text

from app.database.db import engine
from app.embeddings.embedding_model import EmbeddingModel
from app.resume.skill_extractor import SkillExtractor
from app.core.config import settings
from app.mlops.mlflow_tracker import MLflowTracker

class ResumeMatcher:

    def __init__(self):

        self.model = EmbeddingModel.get_model()

        self.index = faiss.read_index(
            settings.FAISS_INDEX_PATH
        )

        self.jobs_df = self.load_jobs()

    def load_jobs(self):

        query = text("""
            SELECT
                id,
                title,
                company,
                location,
                skills,
                description
            FROM jobs
        """)

        with engine.connect() as conn:

            return pd.read_sql(
                query,
                conn
            )

    def calculate_match_score(
        self,
        distance
    ):

        score = max(
            0,
            100 - float(distance)
        )

        return round(
            score,
            2
        )

    def match_resume(
        self,
        resume_text,
        top_k=3
    ):

        resume_skills = set(
            SkillExtractor.extract_skills(
                resume_text
            )
        )

        embedding = self.model.encode(
            [resume_text],
            convert_to_numpy=True
        )

        distances, indices = self.index.search(
            embedding.astype("float32"),
            top_k
        )

        recommendations = []

        for rank, idx in enumerate(indices[0]):

            if idx >= len(self.jobs_df):
                continue

            row = self.jobs_df.iloc[idx]

            job_skills = set()

            if row["skills"]:

                job_skills = {
                    SkillExtractor.normalize_skill(skill)
                    for skill in row["skills"].split(",")
                }
            print("RESUME SKILLS:", resume_skills)
            print("JOB SKILLS:", job_skills)
            missing_skills = sorted(
                list(
                    job_skills - resume_skills
                )
            )

            recommendations.append(
                {
                    "job_id": int(row["id"]),
                    "title": row["title"],
                    "company": row["company"],
                    "location": row["location"],
                    "match_score": self.calculate_match_score(
                        distances[0][rank]
                    ),
                    "resume_skills": sorted(
                        list(resume_skills)
                    ),
                    "job_skills": sorted(
                        list(job_skills)
                    ),
                    "missing_skills": missing_skills
                }
            )
            avg_score = sum(
                item["match_score"]
                for item in recommendations
            ) / len(recommendations)

            MLflowTracker.log_resume_match_run(
                num_matches=len(recommendations),
                avg_score=avg_score
            )
        return recommendations