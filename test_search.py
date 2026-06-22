from app.services.search_service import SearchService

service = SearchService()

results = service.search(
    "llm engineer"
)

print("\nTOP RESULTS\n")

for result in results[:10]:

    print(
        f"{result['title']} | "
        f"{result['company']} | "
        f"Final={result['final_score']} | "
        f"Semantic={result['similarity_score']} | "
        f"Keyword={result['keyword_score']}"
    )