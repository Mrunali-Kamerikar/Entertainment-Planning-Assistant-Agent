# app/ranking.py

def rank_movies(documents, user_data):

    ratings = user_data.get("ratings", {})
    genre_prefs = user_data.get("preferred_genres", {})
    history = user_data.get("history", [])

    ranked = []

    for doc in documents:

        title = doc.metadata.get("title", "")
        genre = doc.metadata.get("genre", "Unknown")

        score = 1.0  # base relevance

        # Rating weight
        if title in ratings:
            score += ratings[title] * 0.7

        # Genre preference weight
        if genre in genre_prefs:
            score += genre_prefs[genre] * 0.5

        # History penalty
        if title in history:
            score -= 1.0

        ranked.append((doc, score))

    ranked.sort(key=lambda x: x[1], reverse=True)

    return ranked
