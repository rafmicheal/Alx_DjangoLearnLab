from rest_framework import generics
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer


class AuthorListCreateView(generics.ListCreateAPIView):
    """
    API view to list all authors or create a new author.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookListCreateView(generics.ListCreateAPIView):
    """
    API view to list all books or create a new book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
