from fastapi import APIRouter

from app.services.search_service import SearchService


router = APIRouter()

search_service = SearchService()


@router.get("/search")
def semantic_search(
    query: str
):

    results = search_service.search(
        query_text=query
    )

    return {
        "query": query,
        "results": results
    }