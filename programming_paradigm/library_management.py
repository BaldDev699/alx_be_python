# Script to manage a library system with books

class Book: # Represents a book in the library
    """A class representing a book in the library."""
    def __init__(self, title, author): # Initialize a book with title and author
        """Initialize a book with title and author."""
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self): # Mark the book as checked out
        """Mark the book as checked out."""
        self._is_checked_out = True

    def return_book(self): # Mark the book as returned
        """Mark the book as returned."""
        self._is_checked_out = False

    def is_checked_out(self): # Check if the book is currently checked out
        """Check if the book is currently checked out."""
        return self._is_checked_out

class Library: # Represents a collection of books in the library
    """A class representing a library that manages books."""
    def __init__(self): # Initialize the library with an empty book collection
        self._books = []

    def add_book(self, book): # Add a book to the library's collection
        self.books.append(book)

    def find_book(self, title): # Find a book by its title
        """Find a book by its title."""
        for book in self.books:
            if book.title == title:
                return book
        return None

    def check_out_book(self, title): # Check out a book by its title
        """Check out a book by its title."""
        book = self.find_book(title)
        if book and not book.is_checked_out():
            book.check_out()
            return True
        return False

    def return_book(self, title): # Return a book by its title
        """Return a book by its title."""
        book = self.find_book(title)
        if book and book.is_checked_out():
            book.return_book()
            return True
        return False

    def list_available_books(self): # List all available books in the library
        """List all available books in the library."""
        for book in self.books:
            if not book.is_checked_out():
                print(f"{book.title} by {book.author}")