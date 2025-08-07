from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from api.models import Author, Book

class BookAPITestCase(APITestCase):
    def setUp(self):
        self.author = Author.objects.create(name='Test Author')

        self.book = Book.objects.create(
            title = 'Test Book Title',
            publication_year=2024,
            author = self.author
        )

        self.list_url = reverse('book-list')

    def test_list_books(self):
        """
        Ensure we can get the list of books.
        """
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Test Book Title')

    def test_filter_books_by_year(self):
        """
        Ensure filtering books by publication year works.
        """
        # Create a second book with a different publication year
        Book.objects.create(
            title='Another Book',
            publication_year=2025,
            author=self.author
        )

        # Test filtering for the year 2024
        response = self.client.get(self.list_url, {'publication_year': 2024})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Test Book Title')

    def test_search_books_by_title(self):
        """
        Ensure searching for books by title works.
        """
        # Create a second book with a different title
        Book.objects.create(
            title='The Second Book',
            publication_year=2023,
            author=self.author
        )

        # Test searching for a keyword in the title
        response = self.client.get(self.list_url, {'search': 'Book Title'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Test Book Title')

    def test_ordering_books_by_title(self):
        """
        Ensure ordering books by title works correctly.
        """
        # Create a second book that will be ordered differently
        book2 = Book.objects.create(
            title='A New Book Title',
            publication_year=2023,
            author=self.author
        )

        # Test ordering by title in ascending order
        response = self.client.get(self.list_url, {'ordering': 'title'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['title'], 'A New Book Title')
        self.assertEqual(response.data[1]['title'], 'Test Book Title')