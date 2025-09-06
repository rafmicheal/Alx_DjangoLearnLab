from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
author = Author.objects.get(name="George Orwell")
books_by_author = Book.objects.filter(author=author)
print("Books by George Orwell:", books_by_author)

# 2. List all books in a library
library = Library.objects.get(name="Central Library")
books_in_library = library.books.all()
print("Books in Central Library:", books_in_library)

# 3. Retrieve the librarian for a library
library = Library.objects.get(name="Central Library")
librarian = library.librarian
print("Librarian of Central Library:", librarian)
