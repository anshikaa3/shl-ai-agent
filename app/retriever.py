import json

# load catalog
with open("catalog_detailed.json", "r", encoding="utf-8") as f:
    products = json.load(f)

print(f"Loaded {len(products)} products")


def search(query, k=5):

    query_words = query.lower().split()

    scored_results = []

    for product in products:

        score = 0

        text = (
            product["name"] + " " +
            product["description"]
        ).lower()

        for word in query_words:

            if word in text:
                score += 1

        if score > 0:

            scored_results.append((score, product))

    scored_results.sort(
        key=lambda x: x[0],
        reverse=True
    )

    results = [
        item[1]
        for item in scored_results[:k]
    ]

    return results