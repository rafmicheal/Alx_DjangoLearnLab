from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

# API View for listing all books


class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
