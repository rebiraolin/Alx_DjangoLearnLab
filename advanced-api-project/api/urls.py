from django.urls import path
from .views import BookList, BookCreate, BookDelete, BookDetail, BookUpdate

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('books/create/', BookCreate.as_view(), name='book-create'),
    path('books/<int:pk>/update/', BookUpdate.as_view(), name='book-update'),
    path('books/<int:pk>/detail/', BookDetail.as_view(), name='book-detail'),
    path('books/<int:pk>/delete/', BookDelete.as_view(), name='book-delete'),
]