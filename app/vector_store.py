# app/vector_store.py

from langchain_chroma import Chroma
from langchain_core.documents import Document
from app.config import VECTOR_DB_PATH
from app.embeddings import load_embedding_model
import json
import os


def build_vector_store_from_json(json_path: str):
    """
    Rebuild vector DB from cleaned JSON data.
    JSON format must contain:
    [
        {
            "title": "...",
            "description": "...",
            "genre": "..."
        }
    ]
    """

    embedding_model = load_embedding_model()

    with open(json_path, "r", encoding="utf-8") as f:
        movies = json.load(f)

    documents = []

    for movie in movies:
        documents.append(
            Document(
                page_content=movie["description"],
                metadata={
                    "title": movie["title"],
                    "genre": movie.get("genre", "Unknown")
                }
            )
        )

    vector_db = Chroma.from_documents(
        documents=documents,
        embedding=embedding_model,
        persist_directory=VECTOR_DB_PATH
    )

    vector_db.persist()

    return vector_db


def load_vector_store():
    embedding_model = load_embedding_model()

    return Chroma(
        persist_directory=VECTOR_DB_PATH,
        embedding_function=embedding_model
    )
