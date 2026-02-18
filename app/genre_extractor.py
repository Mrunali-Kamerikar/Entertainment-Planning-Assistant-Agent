# app/genre_extractor.py

def extract_genre(document):
    return document.metadata.get("genre", "Unknown")
