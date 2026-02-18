# app/vector_store.py

from langchain_chroma import Chroma
from app.config import VECTOR_DB_PATH
from app.embeddings import load_embedding_model


def load_vector_store():

    embedding_model = load_embedding_model()

    return Chroma(
        persist_directory=VECTOR_DB_PATH,
        embedding_function=embedding_model
    )
