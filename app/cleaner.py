import json
import os

# Create processed folder
os.makedirs("data/processed", exist_ok=True)

def clean_movies():
    """
    Cleans raw movie data and prepares it for vector storage
    """

    input_file = "data/raw/movies.json"
    output_file = "data/processed/cleaned_movies.json"

    try:
        with open(input_file, "r", encoding="utf-8") as f:
            movies = json.load(f)

        cleaned_movies = []

        for movie in movies:
            title = movie["title"].strip()
            description = movie["description"].strip()

            # Combine into structured text
            clean_text = f"Title: {title}\nDescription: {description}"

            cleaned_movies.append({
                "text": clean_text,
                "metadata": {
                    "title": title
                }
            })

        # Save cleaned data
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(cleaned_movies, f, indent=4, ensure_ascii=False)

        print(f"Cleaned {len(cleaned_movies)} movies successfully.")

    except Exception as e:
        print("Error cleaning data:", e)


if __name__ == "__main__":
    clean_movies()
