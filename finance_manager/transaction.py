from pymongo import MongoClient
from datetime import datetime

class Transaction:
    @staticmethod
    def get_db():
        client = MongoClient("mongodb://localhost:27017/py_data_set")  #mongoDB URI
        db = client['finance_db']
        return db

    @staticmethod
    def add_transaction(user_id, amount, category):
        db = Transaction.get_db()
        transactions_collection = db['transactions']
        transactions_collection.insert_one({
            "user_id": user_id,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "amount": amount,
            "category": category
        })

    @staticmethod
    def get_transactions(user_id):
        db = Transaction.get_db()
        transactions_collection = db['transactions']
        return list(transactions_collection.find({"user_id": user_id}))

