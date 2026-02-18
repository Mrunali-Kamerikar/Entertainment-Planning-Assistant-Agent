# app/auth.py

import json
import os

USERS_FILE = "data/users.json"


class AuthManager:

    def __init__(self):
        os.makedirs("data", exist_ok=True)

        if not os.path.exists(USERS_FILE):
            with open(USERS_FILE, "w") as f:
                json.dump({}, f)

    def register(self, username):
        users = self._load_users()

        if username not in users:
            users[username] = {}
            self._save_users(users)

        return username

    def _load_users(self):
        with open(USERS_FILE, "r") as f:
            return json.load(f)

    def _save_users(self, users):
        with open(USERS_FILE, "w") as f:
            json.dump(users, f, indent=4)
