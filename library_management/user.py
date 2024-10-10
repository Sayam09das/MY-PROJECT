import json
import os
from hashlib import sha256

class User:
    def __init__(self, username, password, role='user'):
        self.username = username
        self.password_hash = sha256(password.encode()).hexdigest()
        self.role = role

    def to_dict(self):
        return {'username': self.username, 'password_hash': self.password_hash, 'role': self.role}

class UserManager:
    def __init__(self, filename='data/users.json'):
        self.filename = filename
        self.load_users()

    def load_users(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                self.users = json.load(f)
        else:
            self.users = {}

    def save_users(self):
        with open(self.filename, 'w') as f:
            json.dump(self.users, f)

    def register_user(self, username, password, role='user'):
        if username in self.users:
            return False  # User already exists
        user = User(username, password, role)
        self.users[username] = user.to_dict()
        self.save_users()
        return True

    def authenticate_user(self, username, password):
        password_hash = sha256(password.encode()).hexdigest()
        user = self.users.get(username)
        return user and user['password_hash'] == password_hash

    def list_users(self):
        return self.users.keys()
