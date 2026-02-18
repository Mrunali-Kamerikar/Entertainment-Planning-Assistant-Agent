# app/recommender.py

from app.ranking import rank_movies


def get_personalized_recommendations(vector_db, query, user_data):

    # Get similarity scores
    similarity_results = vector_db.similarity_search_with_score(
        query,
        k=5
    )

    ranked = rank_movies(similarity_results, user_data)

    top_items = ranked[:2]

    documents = [item["document"] for item in top_items]

    explanation = "\n".join([
        f"{item['document'].metadata.get('title')} "
        f"(Score: {item['score']}, "
        f"Details: {item['breakdown']})"
        for item in top_items
    ])

    return documents, explanation
