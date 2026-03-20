class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def describe(self):
        print(f"{self.title} by {self.author}")

class Library:
    def __init__(self):
        self.books = []
    def add(self, book):
        self.books.append(book)
    def list_books(self):
        for b in self.books:
            b.describe()

lib = Library()
lib.add(Book("1984", "Orwell"))
lib.add(Book("Art of loving", "Wanja"))
lib.list_books()