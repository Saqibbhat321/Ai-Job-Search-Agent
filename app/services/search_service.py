import faiss
import pandas as pd

from sqlalchemy import text

from app.database.db import engine
from app.embeddings.embedding_model import EmbeddingModel
from app.core.config import settings
from app.utils.query_expander import expand_query

class SearchService:

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
                description,
                source
            FROM jobs
        """)

        with engine.connect() as conn:

            df = pd.read_sql(
                query,
                conn
            )

        return df
    def search(
        self,
        query_text: str,
        top_k: int = 10
    ):

        top_k = min(
            top_k,
            len(self.jobs_df)
        )

        query_lower = query_text.lower()

        expanded_query = expand_query(query_text)
        query_embedding = self.model.encode(
               [expanded_query],
               convert_to_numpy=True
        )
        distances, indices = self.index.search(
            query_embedding.astype("float32"),
            top_k
        )

        results = []

        seen_job_ids = set()

        for rank, idx in enumerate(indices[0]):

            idx = int(idx)

            if idx >= len(self.jobs_df):
                continue

            row = self.jobs_df.iloc[idx]

            job_id = int(row["id"])

            if job_id in seen_job_ids:
                continue

            seen_job_ids.add(job_id)

            distance = float(
                distances[0][rank]
            )

            similarity_score = round(
                1 / (1 + distance),
                4
            )

            title = str(
                row["title"]
            ).lower()

            skills = str(
                row["skills"]
            ).lower()

            description = str(
                row["description"]
            ).lower()

            keyword_score = 0.0

            
            query_words = query_lower.split()
            for word in query_words:
                
                if word in title:
                    keyword_score += 0.3

                if word in skills:
                    keyword_score += 0.2

                if word in description:
                    keyword_score += 0.1
            final_score = round(
                similarity_score + keyword_score,
                4
            )

            results.append(
                {
                    "job_id": job_id,
                    "title": row["title"],
                    "company": row["company"],
                    "location": row["location"],
                    "skills": row["skills"],
                    "source": row["source"],
                    "similarity_score": similarity_score,
                    "keyword_score": round(
                        keyword_score,
                        4
                    ),
                    "final_score": final_score
                }
            )

        results = sorted(
            results,
            key=lambda x: x["final_score"],
            reverse=True
        )

        return results