from relationship_app.models import Library, Book

# Example variable
library_name = "Central Library"

# Retrieve a library by its name
library = Library.objects.get(name=library_name)
print(library)
