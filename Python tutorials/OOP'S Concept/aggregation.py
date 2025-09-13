# Aggregation is a relationship where one object contains or uses another object, but the contained object can 
# still exist independently.

class Library:
    def __init__(self):
        self.name = "Pranamya's library"
        self.books = []
    
    def add_books(self,book):
        self.books.append(book)
        
    def book_details(self):
        return [f"{book.bookname} written by {book.author}"for book in self.books]

class Book:
    def __init__(self,bookname,author) :
        self.bookname = bookname
        self.author = author

library = Library()        
book1 = Book("Python for beginners","Pranamya\n")
book2 = Book("C++","Jethalal\n")
book3 = Book("Javascript","Champaklal\n")

library.add_books(book1)
library.add_books(book2)
library.add_books(book3)

print(f"{library.name}\n")
for details in library.book_details():
    print(details)
