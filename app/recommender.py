# app/recommender.py

from app.ranking import rank_movies


def get_personalized_context(retriever, query, user_data):

    documents = retriever.invoke(query)

    ranked = rank_movies(documents, user_data)

    top_docs = [doc for doc, _ in ranked[:2]]

    explanation = "\n".join([
        f"{doc.metadata.get('title')} → Score: {score:.2f}"
        for doc, score in ranked[:2]
    ])

    return top_docs, explanation
