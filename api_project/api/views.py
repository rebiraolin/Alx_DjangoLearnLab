from rest_framework import generics
from rest_framework import viewsets
from .serializers import BookSerializer
from .models import Book
# Import permission class to restrict access
from rest_framework.permissions import IsAuthenticated


# Create your views here.

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # This permission class enforces that only authenticated users can access this viewset
    permission_classes = (IsAuthenticated,)