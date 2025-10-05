from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='home'),
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),

    # Comment URLs
    path('post/<int:post_id>/comments/new/',
         views.comment_create, name='comment-create'),
    path('comment/<int:pk>/update/', views.comment_update, name='comment-update'),
    path('comment/<int:pk>/delete/', views.comment_delete, name='comment-delete'),

    # Tag and search URLs
    path('tags/<str:tag_name>/', views.TagPostListView.as_view(), name='tag-posts'),
]
