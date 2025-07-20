from django.urls import path
from . import views
from django.views.generic import TemplateView # For the simple home page

urlpatterns = [
    # Home page (function-based or TemplateView)
    path('', TemplateView.as_view(template_name='relationship_app/home.html'), name='home'),

    # Function-based view for listing all books
    path('books/', views.book_list, name='book_list'),

    # Class-based view for library details
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]