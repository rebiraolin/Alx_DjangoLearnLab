from django.urls import path
from .views import ListView, DetailView

urlpatterns = [
    path('books/', ListView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', DetailView.as_view(), name='book-detail-update-delete'),
]