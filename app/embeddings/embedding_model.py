from sentence_transformers import SentenceTransformer

from app.core.config import settings


class EmbeddingModel:

    _model = None

    @classmethod
    def get_model(cls):

        if cls._model is None:

            cls._model = SentenceTransformer(
                settings.EMBEDDING_MODEL
            )

        return cls._model