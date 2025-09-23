from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

# List all books / Create a new book


class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Allow anyone to GET, but require authentication for POST
    def get_permissions(self):
        if self.request.method == "GET":
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]


# Retrieve / Update / Delete a specific book
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Allow anyone to GET, but require authentication for PUT/PATCH/DELETE
    def get_permissions(self):
        if self.request.method in ["GET"]:
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]
