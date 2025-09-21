from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication, SessionAuthentication

from .models import Book
from .serializers import BookSerializer

# Optional: keep the public list endpoint (if you want unauthenticated users to view)


class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # public list — remove or change to IsAuthenticated if you want it protected
    permission_classes = [AllowAny]

# Protected CRUD ViewSet


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # explicitly set auth + permission for clarity (defaults already set in settings.py)
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
