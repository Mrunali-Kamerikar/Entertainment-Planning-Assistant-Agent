import json
import os
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

# Create vector DB folder
os.makedirs("data/vector_db", exist_ok=True)

def create_vector_store():
    """
    Converts cleaned movie data into embeddings
    and stores them in Chroma vector database
    """

    input_file = "data/processed/cleaned_movies.json"

    try:
        # Load cleaned data
        with open(input_file, "r", encoding="utf-8") as f:
            cleaned_movies = json.load(f)

        texts = [movie["text"] for movie in cleaned_movies]
        metadatas = [movie["metadata"] for movie in cleaned_movies]

        print("Creating embeddings...")

        # Load embedding model (UPDATED)
        embedding_model = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

        # Create vector store
        vector_db = Chroma.from_texts(
            texts=texts,
            embedding=embedding_model,
            metadatas=metadatas,
            persist_directory="data/vector_db"
        )

        vector_db.persist()

        print("Vector database created successfully.")

    except Exception as e:
        print("Error creating vector store:", e)


if __name__ == "__main__":
    create_vector_store()
