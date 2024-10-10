from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = generate_password_hash(password)

    @staticmethod
    def get_db():
        client = MongoClient("mongodb://localhost:27017/py_data_set")  #mongoDB URL
        db = client['finance_db']
        return db

    @staticmethod
    def register(username, password):
        db = User.get_db()
        users_collection = db['users']
        if users_collection.find_one({"username": username}):
            print("Username already exists.")
            return False
        else:
            users_collection.insert_one({"username": username, "password": generate_password_hash(password)})
            print("User registered successfully.")
            return True

    @staticmethod
    def login(username, password):
        db = User.get_db()
        users_collection = db['users']
        user = users_collection.find_one({"username": username})
        if user and check_password_hash(user['password'], password):
            return True
        return False

    @staticmethod
    def get_user_id(username):
        db = User.get_db()
        users_collection = db['users']
        user = users_collection.find_one({"username": username})
        return user['_id'] if user else None
