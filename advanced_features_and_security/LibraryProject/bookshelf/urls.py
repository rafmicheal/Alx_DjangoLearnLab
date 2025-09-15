from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),            # List all books
    path('create/', views.create_book, name='create_book'),  # Create a new book
    path('edit/<int:book_id>/', views.edit_book,
         name='edit_book'),   # Edit a book
    path('delete/<int:book_id>/', views.delete_book,
         name='delete_book'),  # Delete a book
]
