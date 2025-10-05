from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('posts/', views.PostListView.as_view(),
         name='post_list'),                     # /posts/
    path('posts/new/', views.PostCreateView.as_view(),
         name='post_create'),            # /posts/new/
    path('posts/<int:pk>/', views.PostDetailView.as_view(),
         name='post_detail'),       # /posts/<pk>/
    path('posts/<int:pk>/edit/', views.PostUpdateView.as_view(),
         name='post_update'),  # /posts/<pk>/edit/
    path('posts/<int:pk>/delete/', views.PostDeleteView.as_view(),
         name='post_delete'),  # /posts/<pk>/delete/
]
