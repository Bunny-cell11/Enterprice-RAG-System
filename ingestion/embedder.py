
from sentence_transformers import SentenceTransformer
import chromadb

model = SentenceTransformer("all-MiniLM-L6-v2")

client = chromadb.Client()
collection = client.get_or_create_collection("enterprise_docs")

docs = [
    {
        "text": "Engineering propulsion report",
        "metadata": {
            "department": "Engineering",
            "allowed_roles": ["Engineering", "Executive"]
        }
    }
]

for i, doc in enumerate(docs):
    embedding = model.encode(doc["text"]).tolist()

    collection.add(
        ids=[str(i)],
        documents=[doc["text"]],
        embeddings=[embedding],
        metadatas=[doc["metadata"]]
    )

print("Embeddings stored.")
