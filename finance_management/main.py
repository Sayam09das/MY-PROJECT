import json
from user import User
from transaction import Transaction
from goal import Goal

class FinanceManagement:
    def __init__(self):
        self.users = self.load_users()
        self.transactions = self.load_transactions()
        self.goals = self.load_goals()

    def load_users(self):
        try:
            with open('data/users.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def load_transactions(self):
        try:
            with open('data/transactions.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def load_goals(self):
        try:
            with open('data/goals.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_users(self):
        with open('data/users.json', 'w') as f:
            json.dump(self.users, f)

    def save_transactions(self):
        with open('data/transactions.json', 'w') as f:
            json.dump(self.transactions, f)

    def save_goals(self):
        with open('data/goals.json', 'w') as f:
            json.dump(self.goals, f)

    def register_user(self):
        username = input("Enter a username: ")
        password = input("Enter a password: ")
        if username in self.users:
            print("Username already exists.")
            return False
        self.users[username] = User(username, password).to_dict()
        self.save_users()
        print("User registered successfully.")
        return True

    def login_user(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if username in self.users and self.users[username]['password'] == password:
            print(f"Welcome back, {username}!")
            return username
        else:
            print("Invalid credentials.")
            return None

    def add_transaction(self, username):
        amount = float(input("Enter the transaction amount: "))
        category = input("Enter the transaction category (income/expense): ")
        transaction = Transaction(username, amount, category).to_dict()
        self.transactions.append(transaction)
        self.save_transactions()
        print("Transaction added successfully.")

    def view_transactions(self, username):
        print("Your transactions:")
        for transaction in self.transactions:
            if transaction['username'] == username:
                print(f"{transaction['category']} of {transaction['amount']}")

    def set_goal(self, username):
        goal_name = input("Enter your savings goal name: ")
        target_amount = float(input("Enter your target amount: "))
        goal = Goal(username, goal_name, target_amount).to_dict()
        self.goals.append(goal)
        self.save_goals()
        print("Savings goal set successfully.")

    def view_goals(self, username):
        print("Your savings goals:")
        for goal in self.goals:
            if goal['username'] == username:
                print(f"{goal['goal_name']}: {goal['target_amount']}")

    def main_menu(self):
        while True:
            print("\nPersonal Finance Management System")
            print("1. Register")
            print("2. Login")
            print("3. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                self.register_user()
            elif choice == '2':
                username = self.login_user()
                if username:
                    while True:
                        print("\n1. Add Transaction")
                        print("2. View Transactions")
                        print("3. Set Savings Goal")
                        print("4. View Savings Goals")
                        print("5. Logout")
                        option = input("Choose an option: ")

                        if option == '1':
                            self.add_transaction(username)
                        elif option == '2':
                            self.view_transactions(username)
                        elif option == '3':
                            self.set_goal(username)
                        elif option == '4':
                            self.view_goals(username)
                        elif option == '5':
                            print("Logging out...")
                            break
                        else:
                            print("Invalid option. Please try again.")
            elif choice == '3':
                print("Exiting the system. Goodbye!")
                break
            else:
                print("Invalid choice. Please select again.")

if __name__ == '__main__':
    FinanceManagement().main_menu()
