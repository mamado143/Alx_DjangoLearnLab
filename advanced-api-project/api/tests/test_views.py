from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from api.models import Author, Book

class BookAPITestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        
        self.author = Author.objects.create(name="Test Author")
        
        # Create multiple books for better filtering/searching/ordering tests
        self.book_old = Book.objects.create(
            title="Old Book",
            publication_year=1990,
            author=self.author
        )
        self.book_new = Book.objects.create(
            title="New Book",
            publication_year=2020,
            author=self.author
        )
        
        # Hardcoded URLs (bypasses reverse issues)
        self.list_url = '/api/books/'
        self.detail_url = f'/api/books/{self.book_new.pk}/'

    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_book(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "New Book")

    def test_create_book_authenticated(self):
        self.client.force_authenticate(user=self.user)
        data = {
            "title": "Valid Book",
            "publication_year": 2025,
            "author": self.author.id
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], "Valid Book")

    def test_create_book_unauthenticated(self):
        data = {
            "title": "Invalid Create",
            "publication_year": 2025,
            "author": self.author.id
        }
        response = self.client.post(self.list_url, data)
        self.assertIn(response.status_code, [status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN])

    def test_update_book_authenticated(self):
        self.client.force_authenticate(user=self.user)
        data = {"title": "Updated Title"}
        response = self.client.patch(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Updated Title")

    def test_delete_book_authenticated(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(pk=self.book_new.pk).exists())

    def test_validation_future_year(self):
        self.client.force_authenticate(user=self.user)
        data = {
            "title": "Future Book",
            "publication_year": 2030,  # Future year (current date: Feb 2026)
            "author": self.author.id
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_search(self):
        response = self.client.get(self.list_url + '?search=Old')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertIn("Old Book", response.data[0]['title'])

    def test_filtering(self):
        # Filter by publication year
        response = self.client.get(self.list_url + '?publication_year=1990')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['publication_year'], 1990)

        # Filter by author name
        response = self.client.get(self.list_url + '?author__name=Test Author')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_ordering(self):
        response = self.client.get(self.list_url + '?ordering=publication_year')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['publication_year'], 1990)
        self.assertEqual(response.data[1]['publication_year'], 2020)

        # Descending
        response = self.client.get(self.list_url + '?ordering=-publication_year')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['publication_year'], 2020)
