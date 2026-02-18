# app/retriever.py

def get_retriever(vector_db):

    return vector_db.as_retriever(
        search_type="mmr",
        search_kwargs={
            "k": 2
        }
    )
