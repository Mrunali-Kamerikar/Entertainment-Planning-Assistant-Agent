# app/user_memory.py

import json
import os

MEMORY_FILE = "data/user_memory.json"


class UserMemory:

    def __init__(self):
        os.makedirs("data", exist_ok=True)

        if not os.path.exists(MEMORY_FILE):
            with open(MEMORY_FILE, "w") as f:
                json.dump({}, f)

    def _load(self):
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)

    def _save(self, data):
        with open(MEMORY_FILE, "w") as f:
            json.dump(data, f, indent=4)

    def init_user(self, username):
        data = self._load()

        if username not in data:
            data[username] = {
                "ratings": {},
                "preferred_genres": {},
                "history": []
            }

        self._save(data)

    def get_user(self, username):
        data = self._load()
        return data.get(username, {})

    def add_rating(self, username, title, rating):
        data = self._load()
        data[username]["ratings"][title] = rating
        self._save(data)

    def add_genre_preference(self, username, genre):
        data = self._load()
        prefs = data[username]["preferred_genres"]
        prefs[genre] = prefs.get(genre, 0) + 1
        self._save(data)

    def add_history(self, username, title):
        data = self._load()
        if title not in data[username]["history"]:
            data[username]["history"].append(title)
        self._save(data)
