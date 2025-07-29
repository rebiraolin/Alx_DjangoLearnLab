# advanced_features_and_security/bookshelf/urls.py

from django.urls import path
from . import views

app_name = 'bookshelf' # Defines the application namespace

urlpatterns = [
    path('books/', views.book_list_view, name='book_list'),
    path('books/create/', views.book_create_view, name='book_create'),
    path('books/edit/', views.book_edit_view, name='book_edit'), # Note: A real edit view would likely take an ID
    path('books/delete/', views.book_delete_view, name='book_delete'), # Note: A real delete view would likely take an ID
    path('example-form/', views.example_form_view, name='example_form'),
]