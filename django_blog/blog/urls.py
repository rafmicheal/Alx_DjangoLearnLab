from django.urls import path
from . import views

urlpatterns = [
    # List of all posts (homepage)
    path('', views.PostListView.as_view(), name='home'),

    # Create a new post
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),

    # View a single post
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),

    # Update an existing post
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),

    # Delete a post
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
]
