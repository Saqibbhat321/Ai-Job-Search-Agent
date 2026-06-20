import faiss
import pandas as pd

from sqlalchemy import text

from app.database.db import engine
from app.embeddings.embedding_model import EmbeddingModel
from app.core.config import settings


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
                description
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
        top_k: int = 5
    ):

        print("SEARCH SERVICE VERSION 2")

        top_k = min(
            top_k,
            len(self.jobs_df)
        )

        query_embedding = self.model.encode(
            [query_text],
            convert_to_numpy=True
        )

        distances, indices = self.index.search(
            query_embedding.astype("float32"),
            top_k
        )

        print("INDICES:", indices)
        print("DISTANCES:", distances)

        unique_indices = []

        for idx in indices[0]:

            idx = int(idx)

            if idx not in unique_indices:
                unique_indices.append(idx)

        results = []

        for idx in unique_indices:

            if idx >= len(self.jobs_df):
                continue

            row = self.jobs_df.iloc[idx]

            results.append(
                {
                    "id": int(row["id"]),
                    "title": row["title"],
                    "company": row["company"],
                    "location": row["location"],
                    "skills": row["skills"]
                }
            )

        return results