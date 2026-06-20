import faiss
import numpy as np


class FAISSManager:

    def __init__(self):

        self.dimension = 384

        self.index = faiss.IndexFlatL2(
            self.dimension
        )

    def add_embeddings(
        self,
        embeddings: np.ndarray
    ):

        self.index.add(
            embeddings.astype("float32")
        )

    def save(
        self,
        path: str
    ):

        faiss.write_index(
            self.index,
            path
        )

    def load(
        self,
        path: str
    ):

        self.index = faiss.read_index(
            path
        )

    def search(
        self,
        query_embedding,
        k=5
    ):

        distances, indices = self.index.search(
            query_embedding.astype("float32"),
            k
        )

        return distances, indices