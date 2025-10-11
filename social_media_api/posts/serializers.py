from rest_framework import serializers
from django.conf import settings
from .models import Post, Comment
from django.contrib.auth import get_user_model

User = get_user_model()


class CommentSerializer(serializers.ModelSerializer):
    author_username = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'author_username',
                  'content', 'created_at', 'updated_at']
        read_only_fields = ['author', 'created_at',
                            'updated_at', 'author_username']


class PostSerializer(serializers.ModelSerializer):
    author_username = serializers.ReadOnlyField(source='author.username')
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author',
                  'author_username', 'created_at', 'updated_at', 'comments']
        read_only_fields = ['author', 'created_at',
                            'updated_at', 'author_username', 'comments']

    def validate_title(self, value):
        if not value.strip():
            raise serializers.ValidationError("Title cannot be empty.")
        return value
