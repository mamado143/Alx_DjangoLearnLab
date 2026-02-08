from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from api.models import Author, Book
from django.urls import reverse

class BookAPITestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.author = Author.objects.create(name="Test Author")
        
        # Create BOTH books here so they exist for all tests
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
        
        # Dynamic URLs using reverse
        self.list_url = reverse('book-list')
        self.create_url = reverse('book-create')
        self.detail_url = reverse('book-detail', kwargs={'pk': self.book_new.pk})
        self.update_url = reverse('book-update', kwargs={'pk': self.book_new.pk})
        self.delete_url = reverse('book-delete', kwargs={'pk': self.book_new.pk})

    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Handle potential pagination
        data = response.data['results'] if isinstance(response.data, dict) else response.data
        self.assertEqual(len(data), 2)

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
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_book_authenticated(self):
        self.client.force_authenticate(user=self.user)
        data = {"title": "Updated Title"}
        response = self.client.patch(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Updated Title")

    def test_delete_book_authenticated(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_search(self):
        response = self.client.get(self.list_url + '?search=Old')
        data = response.data['results'] if isinstance(response.data, dict) else response.data
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['title'], "Old Book")

    def test_filtering(self):
        response = self.client.get(self.list_url + '?publication_year=1990')
        data = response.data['results'] if isinstance(response.data, dict) else response.data
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['publication_year'], 1990)

    def test_ordering(self):
        response = self.client.get(self.list_url + '?ordering=publication_year')
        data = response.data['results'] if isinstance(response.data, dict) else response.data
        self.assertEqual(data[0]['publication_year'], 1990)
        self.assertEqual(data[1]['publication_year'], 2020)
