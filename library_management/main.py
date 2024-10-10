from library import Library

def main():
    library = Library()

    while True:
        print("Welcome to the Library Management System")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            if library.register_user(username, password):
                print("Registration successful!")
            else:
                print("Username already exists.")

        elif choice == '2':
            username = input("Enter username: ")
            password = input("Enter password: ")
            if library.authenticate_user(username, password):
                print("Login successful!")
                while True:
                    print("\nLibrary Management Options")
                    print("1. Add Book (Admin Only)")
                    print("2. List Books")
                    print("3. Update Book (Admin Only)")
                    print("4. Delete Book (Admin Only)")
                    print("5. Borrow Book")
                    print("6. Return Book")
                    print("7. List Transactions (Admin Only)")
                    print("8. Logout")
                    option = input("Choose an option: ")

                    if option == '1':
                        title = input("Enter book title: ")
                        author = input("Enter book author: ")
                        genre = input("Enter book genre: ")
                        copies = int(input("Enter number of copies: "))
                        library.add_book(title, author, genre, copies)
                        print("Book added successfully.")

                    elif option == '2':
                        books = library.list_books()
                        for idx, book in enumerate(books):
                            print(f"{idx}. {book['title']} by {book['author']} - Copies: {book['copies']}")

                    elif option == '3':
                        index = int(input("Enter book index to update: "))
                        title = input("Enter new title (or leave blank): ")
                        author = input("Enter new author (or leave blank): ")
                        genre = input("Enter new genre (or leave blank): ")
                        copies = input("Enter new copies (or leave blank): ")
                        copies = int(copies) if copies else None
                        if library.update_book(index, title if title else None,
                                                author if author else None,
                                                genre if genre else None,
                                                copies):
                            print("Book updated successfully.")
                        else:
                            print("Update failed.")

                    elif option == '4':
                        index = int(input("Enter book index to delete: "))
                        if library.delete_book(index):
                            print("Book deleted successfully.")
                        else:
                            print("Delete failed.")

                    elif option == '5':
                        book_title = input("Enter book title to borrow: ")
                        if library.borrow_book(username, book_title):
                            print("Book borrowed successfully.")
                        else:
                            print("Book is not available.")

                    elif option == '6':
                        book_title = input("Enter book title to return: ")
                        if library.return_book(username, book_title):
                            print("Book returned successfully.")
                        else:
                            print("Return failed.")

                    elif option == '7':
                        transactions = library.list_transactions()
                        for transaction in transactions:
                            print(f"{transaction['timestamp']}: {transaction['username']} {transaction['action']}ed '{transaction['book_title']}'")

                    elif option == '8':
                        print("Logging out...")
                        break

                    else:
                        print("Invalid option. Please try again.")
            else:
                print("Login failed. Check your credentials.")

        elif choice == '3':
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please select again.")

if __name__ == '__main__':
    main()
