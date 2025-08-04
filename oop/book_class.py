# Script that defines a Book class with attributes and methods

class Book:
    # initializer method to set the title, author, and year of publication
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    
    # method to display book information
    def __str__(self):
        return f"{self.title} by {self.author}, published in ({self.year})"
    
    # method to represent the book object
    def __repr__(self):
        return f"Book({self.title!r}, {self.author!r}, {self.year!r})"
    
    # method to delete the book object
    def __del__(self):
        print(f"Deleting {self.title}")