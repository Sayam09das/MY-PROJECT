from user import UserManager
from book import BookManager
from transaction import TransactionManager

class Library:
    def __init__(self):
        self.user_manager = UserManager()
        self.book_manager = BookManager()
        self.transaction_manager = TransactionManager()

    def register_user(self, username, password, role='user'):
        return self.user_manager.register_user(username, password, role)

    def authenticate_user(self, username, password):
        return self.user_manager.authenticate_user(username, password)

    def add_book(self, title, author, genre, copies):
        self.book_manager.add_book(title, author, genre, copies)

    def update_book(self, index, title=None, author=None, genre=None, copies=None):
        return self.book_manager.update_book(index, title, author, genre, copies)

    def delete_book(self, index):
        return self.book_manager.delete_book(index)

    def borrow_book(self, username, book_title):
        book = self.book_manager.find_book(book_title)
        if book and book[0]['copies'] > 0:
            book[0]['copies'] -= 1
            self.book_manager.save_books()
            self.transaction_manager.add_transaction(username, book_title, 'borrow')
            return True
        return False

    def return_book(self, username, book_title):
        book = self.book_manager.find_book(book_title)
        if book:
            book[0]['copies'] += 1
            self.book_manager.save_books()
            self.transaction_manager.add_transaction(username, book_title, 'return')
            return True
        return False

    def list_books(self):
        return self.book_manager.list_books()

    def list_transactions(self):
        return self.transaction_manager.list_transactions()
