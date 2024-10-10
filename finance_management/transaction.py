from datetime import datetime

class Transaction:
    def __init__(self, username, amount, category):
        self.username = username
        self.amount = amount
        self.category = category
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {
            "username": self.username,
            "amount": self.amount,
            "category": self.category,
            "timestamp": self.timestamp,
        }
