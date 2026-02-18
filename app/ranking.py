# app/ranking.py

def rank_movies(documents, user_memory):

    ratings = user_memory.get("ratings", {})
    history = user_memory.get("history", [])

    scored = []

    for doc in documents:
        title = doc.metadata.get("title", "")
        score = 1.0

        # Boost if user rated highly
        if title in ratings:
            score += ratings[title] * 0.5

        # Penalize if already recommended
        if title in history:
            score -= 0.5

        scored.append((doc, score))

    scored.sort(key=lambda x: x[1], reverse=True)

    return [doc for doc, _ in scored]
