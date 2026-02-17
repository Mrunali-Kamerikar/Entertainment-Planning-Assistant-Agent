import requests
import os
import json

# Create data folder
os.makedirs("data/raw", exist_ok=True)

def scrape_movies():
    """
    Scrapes movie data from Studio Ghibli API (safe and free)
    """

    url = "https://ghibliapi.vercel.app/films"

    try:
        response = requests.get(url)

        if response.status_code != 200:
            print("Failed to fetch data:", response.status_code)
            return

        data = response.json()

        movies = []

        for movie in data:
            movie_data = {
                "title": movie["title"],
                "description": movie["description"]
            }
            movies.append(movie_data)

        # Save to file
        with open("data/raw/movies.json", "w", encoding="utf-8") as f:
            json.dump(movies, f, indent=4, ensure_ascii=False)

        print(f"Scraped {len(movies)} movies successfully.")

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    scrape_movies()
