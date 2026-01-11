from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential
from config import *

def retrieve_documents(username: str, query: str, top_k: int = 5):
    print("\n--- DEBUG: Starting document retrieval ---")

    user_prefix = f"{STORAGE_URL}/{CONTAINER}/{username}/"
    upper_bound = user_prefix + "~"

    print("DEBUG: User prefix:", user_prefix)
    print("DEBUG: Upper bound:", upper_bound)
    print("DEBUG: Query:", query)

    filter_expression = (
        f"metadata_storage_path ge '{user_prefix}' and "
        f"metadata_storage_path lt '{upper_bound}'"
    )

    print("DEBUG: Filter expression:", filter_expression)

    search_client = SearchClient(
        endpoint=SEARCH_ENDPOINT,
        index_name=SEARCH_INDEX,
        credential=AzureKeyCredential(SEARCH_KEY)
    )

    results = search_client.search(
        search_text=query,
        filter=filter_expression,
        select=["content", "metadata_storage_path"],
        top=top_k
    )

    documents = []
    count = 0
    for r in results:
        count += 1
        print("\n--- RESULT", count, "---")
        print("SOURCE:", r["metadata_storage_path"])
        print("CONTENT PREVIEW:", r["content"][:300])
        documents.append({
            "content": r["content"],
            "source": r["metadata_storage_path"]
        })

    print(f"\nDEBUG: Total results fetched: {count}")
    print("--- DEBUG: Retrieval finished ---\n")

    return documents

