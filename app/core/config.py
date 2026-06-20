from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = Field(...)
    APP_VERSION: str = Field(...)
    DEBUG: bool = Field(...)

    HOST: str = Field(...)
    PORT: int = Field(...)

    DATABASE_URL: str = Field(...)

    EMBEDDING_MODEL: str = Field(...)

    FAISS_INDEX_PATH: str = Field(...)

    MLFLOW_TRACKING_URI: str = Field(...)

    class Config:
        env_file = ".env"


settings = Settings()