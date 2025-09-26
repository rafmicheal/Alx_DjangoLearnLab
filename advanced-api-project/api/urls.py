# api/urls.py
from django.urls import path
from .views import ListView, DetailView, CreateView, UpdateView, DeleteView

urlpatterns = [
    # ?search=python&ordering=title
    path('books/', ListView.as_view(), name='book-list'),
    path('books/<int:pk>/', DetailView.as_view(),
         name='book-detail'),  # GET single book
    path('books/create/', CreateView.as_view(),
         name='book-create'),   # POST new book
    path('books/update/<int:pk>/', UpdateView.as_view(),
         name='book-update'),  # PUT/PATCH
    path('books/delete/<int:pk>/', DeleteView.as_view(),
         name='book-delete'),  # DELETE
]
