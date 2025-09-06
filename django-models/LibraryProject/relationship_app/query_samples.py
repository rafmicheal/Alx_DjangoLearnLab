from .models import Author, Book, Library, Librarian

# Define variables for names (exact variable names may be expected)
author_name = "Author Name"
library_name = "Library Name"

# Query all books by a specific author
books_by_author = Book.objects.filter(author__name=author_name)

# List all books in a library
books_in_library = Library.objects.get(name=library_name).books.all()

# Retrieve the librarian for a library
librarian_for_library = Librarian.objects.get(library__name=library_name)
