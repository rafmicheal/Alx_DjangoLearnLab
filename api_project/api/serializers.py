from rest_framework import serializers
from .models import Book

# Serializer for Book model


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'   # include all fields (title, author, etc.)
