from django.urls import path, include
from .views import like_post, unlike_post, PostViewSet  # adapt imports
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, FeedView

router = DefaultRouter()
router.register('posts', PostViewSet)
router.register('comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('feed/', FeedView.as_view(), name='feed'),
    path('posts/<int:pk>/like/', like_post, name='post-like'),      # << added
    path('posts/<int:pk>/unlike/', unlike_post, name='post-unlike'),  # << added
]
