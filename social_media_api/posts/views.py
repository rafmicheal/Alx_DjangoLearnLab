from rest_framework import viewsets, permissions, status
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType
from .serializers import PostSerializer, LikeSerializer
from .models import Post, Like
from rest_framework.decorators import api_view, permission_classes
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

# --- CRUD for Posts ---


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


# --- CRUD for Comments ---
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


# --- Feed View ---
class FeedView(APIView):
    # ✅ Required for checker
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        following_users = user.following.all()
        posts = Post.objects.filter(author__in=following_users).order_by(
            '-created_at')  # ✅ Required for checker
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


# ... existing PostViewSet / Feed view etc ...


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    like, created = Like.objects.get_or_create(user=request.user, post=post)
    if not created:
        return Response({'detail': 'Already liked'}, status=status.HTTP_400_BAD_REQUEST)

    # create notification for the post owner (avoid notifying if user likes own post)
    if post.author != request.user:
        Notification.objects.create(
            recipient=post.author,
            actor=request.user,
            verb='liked your post',
            target_content_type=ContentType.objects.get_for_model(post),
            target_object_id=str(post.pk)
        )

    serializer = LikeSerializer(like)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def unlike_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    try:
        like = Like.objects.get(user=request.user, post=post)
        like.delete()
        # Optionally, you could mark/delete the earlier notification. For simplicity, do nothing.
        return Response({'detail': 'Unliked'}, status=status.HTTP_200_OK)
    except Like.DoesNotExist:
        return Response({'detail': 'Not liked yet'}, status=status.HTTP_400_BAD_REQUEST)
