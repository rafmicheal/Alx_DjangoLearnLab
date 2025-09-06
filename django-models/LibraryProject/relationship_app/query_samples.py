from bookshelf.models import Book
from relationship_app.models import Author, Library

# Example: Get all books
all_books = Book.objects.all()
print(all_books)

# Example: Get all books by a specific author
author = Author.objects.get(id=1)
books_by_author = author.books.all()
print(books_by_author)

# Example: Get all books in a specific library
library = Library.objects.get(id=1)
books_in_library = library.books.all()
print(books_in_library)
