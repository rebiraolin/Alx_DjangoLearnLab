from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer
from rest_framework import generics, permissions


# Create your views here.
class BookList(generics.ListAPIView):
    """
    View to handle listing all books in the database.
    It provides a read-only endpoint for unauthenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

class BookDetail(generics.RetrieveAPIView):
    """
    View to retrieve a single book by its primary key.
    It provides a read-only endpoint for unauthenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

class BookCreate(generics.CreateAPIView):
    """
    View to handle the creation of a new book.
    This endpoint is restricted to authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

class BookUpdate(generics.UpdateAPIView):
    """
    View to handle updating an existing book by its primary key.
    This endpoint is restricted to authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

class BookDelete(generics.DestroyAPIView):
    """
    View to handle the deletion of a book by its primary key.
    This endpoint is restricted to authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]