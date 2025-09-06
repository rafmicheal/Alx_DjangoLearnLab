from .models import Author, Book, Library, Librarian

# Define variable names
author_name = "Author Name"
library_name = "Library Name"

# Get the author object first
author = Author.objects.get(name=author_name)

# Query all books by this specific author
books_by_author = Book.objects.filter(author=author)

# Get the library object first
library = Library.objects.get(name=library_name)

# List all books in this library
books_in_library = library.books.all()

# Retrieve the librarian for this library
librarian_for_library = Librarian.objects.get(library=library)
