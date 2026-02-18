# app/ranking.py

def rank_movies(similarity_results, user_data):
    """
    similarity_results = [(Document, similarity_score)]
    """

    ratings = user_data.get("ratings", {})
    genre_prefs = user_data.get("preferred_genres", {})
    history = user_data.get("history", [])

    ranked = []

    for doc, sim_score in similarity_results:

        title = doc.metadata.get("title", "")
        genre = doc.metadata.get("genre", "Unknown")

        # Convert similarity distance to positive score
        base_score = 1 - sim_score

        rating_boost = ratings.get(title, 0) * 0.5
        genre_boost = genre_prefs.get(genre, 0) * 0.3
        history_penalty = -0.7 if title in history else 0

        final_score = base_score + rating_boost + genre_boost + history_penalty

        ranked.append(
            {
                "document": doc,
                "score": round(final_score, 3),
                "breakdown": {
                    "base_similarity": round(base_score, 3),
                    "rating_boost": rating_boost,
                    "genre_boost": genre_boost,
                    "history_penalty": history_penalty
                }
            }
        )

    ranked.sort(key=lambda x: x["score"], reverse=True)

    return ranked
