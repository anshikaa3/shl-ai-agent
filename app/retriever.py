from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import json

# load embedding model
print("Loading model...")

model = SentenceTransformer("all-MiniLM-L6-v2")

print("Model loaded!")

# load catalog
with open("catalog_detailed.json", "r", encoding="utf-8") as f:
    catalog = json.load(f)

print(f"Loaded {len(catalog)} products")

# combine text for embeddings
texts = []

for item in catalog:

    combined_text = (
        item["name"] + " " + item["description"]
    )

    texts.append(combined_text)

print("Creating embeddings...")

embeddings = model.encode(texts)

print("Embeddings created!")

# create FAISS index
dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(np.array(embeddings))

print("FAISS index created!")

# semantic search function
def search(query, k=5):

    query_embedding = model.encode([query])

    distances, indices = index.search(
        np.array(query_embedding),
        k
    )

    results = []

    for i in indices[0]:
        results.append(catalog[i])

    return results

# test query
query = "Hiring Java backend developer"

print(f"\nQUERY: {query}\n")

results = search(query)

print("SEARCH RESULTS:\n")

for result in results:
    print(result["name"])
    print(result["url"])
    print("=" * 50)