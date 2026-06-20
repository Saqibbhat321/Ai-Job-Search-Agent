from fastapi import FastAPI

from app.core.config import settings
from app.core.logger import logger

from app.api.routes.search import router as search_router


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)

app.include_router(search_router)


@app.on_event("startup")
async def startup_event():
    logger.info("AI Job Search Agent Started")


@app.get("/")
async def root():
    return {
        "message": "AI Job Search Agent Running"
    }


@app.get("/health")
async def health_check():
    return {
        "status": "healthy"
    }