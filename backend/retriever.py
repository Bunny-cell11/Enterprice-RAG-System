
import chromadb

client = chromadb.Client()
collection = client.get_or_create_collection("enterprise_docs")

def retrieve(query, role):
    results = collection.query(
        query_texts=[query],
        n_results=5,
        where={
            "allowed_roles": {
                "$in": [role]
            }
        }
    )
    return results
