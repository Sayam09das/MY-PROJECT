
import user
import transaction
import pandas as pd
import matplotlib.pyplot as plt

def main():
    while True:
        print("\n--- Personal Finance Manager ---")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            user.User.register(username, password)

        elif choice == '2':
            username = input("Enter username: ")
            password = input("Enter password: ")
            if user.User.login(username, password):
                print(f"Welcome {username}!")
                user_id = user.User.get_user_id(username)
                while True:
                    print("\n1. Add Transaction")
                    print("2. View Transactions")
                    print("3. Generate Report")
                    print("4. Logout")
                    option = input("Choose an option: ")

                    if option == '1':
                        amount = float(input("Enter amount: "))
                        category = input("Enter category: ")
                        transaction.Transaction.add_transaction(user_id, amount, category)

                    elif option == '2':
                        transactions = transaction.Transaction.get_transactions(user_id)
                        for t in transactions:
                            print(t)

                    elif option == '3':
                        generate_report(user_id)

                    elif option == '4':
                        break

        elif choice == '3':
            print("Exiting...")
            break

def generate_report(user_id):
    transactions = transaction.Transaction.get_transactions(user_id)
    df = pd.DataFrame(transactions)
    if not df.empty:
        df['date'] = pd.to_datetime(df['date'])
        df.set_index('date', inplace=True)
        df.resample('M').sum()['amount'].plot(kind='bar')
        plt.title('Monthly Expense Report')
        plt.xlabel('Month')
        plt.ylabel('Amount')
        plt.show()
    else:
        print("No transactions found.")

if __name__ == "__main__":
    main()
