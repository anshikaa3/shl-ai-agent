from app.retriever import search

def process_chat(messages):

    latest_message = messages[-1].content.lower()

    conversation_text = " ".join(
        [msg.content.lower() for msg in messages]
    )

    # off-topic protection
    unrelated_keywords = [
        "weather",
        "movie",
        "politics",
        "recipe",
        "cricket",
        "tax"
    ]

    for word in unrelated_keywords:
        if word in latest_message:
            return {
                "reply": "I can only help with SHL assessment recommendations.",
                "recommendations": [],
                "end_of_conversation": False
            }

    # clarification handling
    if len(conversation_text.split()) < 4:
        return {
            "reply": (
                "Could you provide more details about the role?\n"
                "- seniority level\n"
                "- technical skills needed\n"
                "- communication requirements\n"
                "- personality assessment needs"
            ),
            "recommendations": [],
            "end_of_conversation": False
        }

    # refinement support
    refined_query = conversation_text

    # retrieve recommendations
    results = search(refined_query)

    recommendations = []

    for result in results[:5]:

        recommendations.append({
            "name": result["name"],
            "url": result["url"]
        })

    names = [r["name"] for r in recommendations]

    reply = (
        "Based on the updated hiring requirements, "
        "these SHL assessments may be relevant: "
        + ", ".join(names)
    )

    return {
        "reply": reply,
        "recommendations": recommendations,
        "end_of_conversation": False
    }