# app/embeddings.py

from langchain_huggingface import HuggingFaceEmbeddings
from app.config import EMBEDDING_MODEL

def load_embedding_model():
    return HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL
    )
