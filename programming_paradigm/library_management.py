class Book:
    def __init__(self, title, author,is_checked_out=False):
        self.title = title
        self.author = author
        self.checked_out = is_checked_out
        self.is_borrowed = False

    def __str__(self):
        return f"{self.title} by {self.author} ({'Checked Out' if self.checked_out else 'Available'})"
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)

    def list_books(self):
        for book in self.books:
            print(book)

    def check_out_book(self, book):
        if book in self.books and not book.checked_out:
            book.checked_out = True
            return True
        return False

    def return_book(self, book):
        if book in self.books and book.checked_out:
            book.checked_out = False
            return True
        return False