import json
import os

class Book:
    def __init__(self, title, author, genre, copies):
        self.title = title
        self.author = author
        self.genre = genre
        self.copies = copies

    def to_dict(self):
        return {
            'title': self.title,
            'author': self.author,
            'genre': self.genre,
            'copies': self.copies
        }

class BookManager:
    def __init__(self, filename='data/books.json'):
        self.filename = filename
        self.load_books()

    def load_books(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                self.books = json.load(f)
        else:
            self.books = []

    def save_books(self):
        with open(self.filename, 'w') as f:
            json.dump(self.books, f)

    def add_book(self, title, author, genre, copies):
        book = Book(title, author, genre, copies)
        self.books.append(book.to_dict())
        self.save_books()

    def update_book(self, index, title=None, author=None, genre=None, copies=None):
        if 0 <= index < len(self.books):
            if title:
                self.books[index]['title'] = title
            if author:
                self.books[index]['author'] = author
            if genre:
                self.books[index]['genre'] = genre
            if copies is not None:
                self.books[index]['copies'] = copies
            self.save_books()
            return True
        return False

    def delete_book(self, index):
        if 0 <= index < len(self.books):
            del self.books[index]
            self.save_books()
            return True
        return False

    def list_books(self):
        return self.books

    def find_book(self, title):
        return [book for book in self.books if title.lower() in book['title'].lower()]
