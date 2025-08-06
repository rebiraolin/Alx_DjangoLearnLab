from .models import Book
from .serializers import BookSerializer
from rest_framework import generics, permissions


# Create your views here.
class ListView(generics.ListCreateAPIView):
    """
    Handles listing books and creating new books.
    - GET method is public (read-only).
    - POST method requires authentication.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class DetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Handles retrieving, updating, and deleting a single book.
    - GET method is public (read-only).
    - PUT, PATCH, DELETE methods require authentication.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]