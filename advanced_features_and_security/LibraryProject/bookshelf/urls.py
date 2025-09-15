from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.book_list, name='book_list'),          # List all books
    path('books/create/', views.create_book,
         name='create_book'),  # Create a new book
    path('books/edit/<int:book_id>/', views.edit_book,
         name='edit_book'),  # Edit a book
    path('books/delete/<int:book_id>/', views.delete_book,
         name='delete_book'),  # Delete a book
]
