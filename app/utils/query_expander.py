QUERY_EXPANSIONS = {
    "llm": [
        "large language model",
        "transformers",
        "genai",
        "rag"
    ],

    "genai": [
        "llm",
        "rag",
        "langchain"
    ],

    "mlops": [
        "docker",
        "mlflow",
        "deployment"
    ]
}


def expand_query(query: str):

    query = query.lower()

    expanded = [query]

    for word in query.split():

        if word in QUERY_EXPANSIONS:

            expanded.extend(
                QUERY_EXPANSIONS[word]
            )

    return " ".join(expanded)