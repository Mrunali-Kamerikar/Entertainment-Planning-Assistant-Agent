# app/user_memory.py

import json
import os

MEMORY_FILE = "data/user_memory.json"


class UserMemory:

    def __init__(self):
        os.makedirs("data", exist_ok=True)

        if not os.path.exists(MEMORY_FILE):
            with open(MEMORY_FILE, "w") as f:
                json.dump({
                    "ratings": {},
                    "preferred_genres": [],
                    "history": []
                }, f)

    def load_memory(self):
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)

    def save_memory(self, memory):
        with open(MEMORY_FILE, "w") as f:
            json.dump(memory, f, indent=4)

    def add_rating(self, movie_title, rating):
        memory = self.load_memory()
        memory["ratings"][movie_title] = rating
        self.save_memory(memory)

    def add_history(self, movie_title):
        memory = self.load_memory()
        if movie_title not in memory["history"]:
            memory["history"].append(movie_title)
        self.save_memory(memory)

    def get_memory(self):
        return self.load_memory()
