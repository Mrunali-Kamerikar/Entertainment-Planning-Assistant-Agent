# app/recommender.py

from app.ranking import rank_movies


def get_personalized_context(retriever, query, user_memory):

    documents = retriever.get_relevant_documents(query)

    ranked_docs = rank_movies(documents, user_memory)

    # Take top 2 after ranking
    return ranked_docs[:2]
