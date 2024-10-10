import json
import os
from datetime import datetime

class Transaction:
    def __init__(self, username, book_title, action):
        self.username = username
        self.book_title = book_title
        self.action = action  # 'borrow' or 'return'
        self.timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def to_dict(self):
        return {
            'username': self.username,
            'book_title': self.book_title,
            'action': self.action,
            'timestamp': self.timestamp
        }

class TransactionManager:
    def __init__(self, filename='data/transactions.json'):
        self.filename = filename
        self.load_transactions()

    def load_transactions(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                self.transactions = json.load(f)
        else:
            self.transactions = []

    def save_transactions(self):
        with open(self.filename, 'w') as f:
            json.dump(self.transactions, f)

    def add_transaction(self, username, book_title, action):
        transaction = Transaction(username, book_title, action)
        self.transactions.append(transaction.to_dict())
        self.save_transactions()

    def list_transactions(self):
        return self.transactions
