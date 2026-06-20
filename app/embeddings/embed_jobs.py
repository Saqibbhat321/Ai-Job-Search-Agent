import numpy as np
import pandas as pd

from sqlalchemy import text

from app.database.db import engine
from app.embeddings.embedding_model import EmbeddingModel
from app.vectorstore.faiss_manager import FAISSManager
from app.core.config import settings


def fetch_jobs():

    query = text("""
        SELECT
            id,
            title,
            company,
            description
        FROM jobs
    """)

    with engine.connect() as conn:

        df = pd.read_sql(
            query,
            conn
        )

    return df


def build_embeddings():

    jobs_df = fetch_jobs()

    texts = []

    for _, row in jobs_df.iterrows():

        text_data = f"""
        {row['title']}
        {row['company']}
        {row['description']}
        """

        texts.append(text_data)

    model = EmbeddingModel.get_model()

    embeddings = model.encode(
        texts,
        convert_to_numpy=True
    )

    print(
        f"Generated {len(embeddings)} embeddings"
    )

    faiss_manager = FAISSManager()

    faiss_manager.add_embeddings(
        embeddings
    )

    faiss_manager.save(
        settings.FAISS_INDEX_PATH
    )

    print(
        "FAISS index saved successfully"
    )


if __name__ == "__main__":

    build_embeddings()