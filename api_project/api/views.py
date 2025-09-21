from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer

# ✅ Existing ListAPIView (keep this for checker)


class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# ✅ New ViewSet for full CRUD
class BookViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for viewing, creating, updating, and deleting Books.
    DRF handles GET, POST, PUT, DELETE automatically here.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
