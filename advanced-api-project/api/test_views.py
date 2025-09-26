# api/test_views.py

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Book, Author
from django.contrib.auth.models import User


class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

        # Create authors
        self.author1 = Author.objects.create(name="Author One")
        self.author2 = Author.objects.create(name="Author Two")

        # Create books
        self.book1 = Book.objects.create(
            title="Book One",
            publication_year=2000,
            author=self.author1
        )
        self.book2 = Book.objects.create(
            title="Book Two",
            publication_year=2010,
            author=self.author2
        )

    def test_list_books(self):
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_book_authenticated(self):
        url = reverse('book-create')
        data = {
            "title": "Book Three",
            "publication_year": 2020,
            "author": self.author1.id
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_create_book_unauthenticated(self):
        self.client.logout()
        url = reverse('book-create')
        data = {
            "title": "Book Four",
            "publication_year": 2021,
            "author": self.author2.id
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_retrieve_book(self):
        url = reverse('book-detail', args=[self.book1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book1.title)

    def test_update_book_authenticated(self):
        url = reverse('book-update', args=[self.book1.id])
        data = {
            "title": "Updated Book One",
            "publication_year": 2001,
            "author": self.author1.id
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Book One")

    def test_delete_book_authenticated(self):
        url = reverse('book-delete', args=[self.book2.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_filter_books_by_author(self):
        url = reverse('book-list')
        response = self.client.get(url, {'author': self.author1.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['author'], self.author1.id)

    def test_search_books_by_title(self):
        url = reverse('book-list')
        response = self.client.get(url, {'search': 'Book One'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_order_books_by_publication_year(self):
        url = reverse('book-list')
        response = self.client.get(url, {'ordering': 'publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['publication_year'], 2000)
