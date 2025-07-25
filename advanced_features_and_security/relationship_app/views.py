from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView # Import ListView and DetailView
from .models import Book, Library, Author # Import your models

# Function-based view to list all books
def book_list(request):
    """
    Lists all books stored in the database.
    Renders a simple text list of book titles and their authors.
    """
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


# Class-based view to display details for a specific library
class LibraryDetailView(DetailView):
    """
    Displays details for a specific library, listing all books available in that library.
    Utilizes Django’s DetailView.
    """
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'