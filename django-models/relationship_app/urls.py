from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from .views import LibraryDetailView # Keep this if you have it
# No need to import the new views specifically, as we're using views.BookCreateView etc.

app_name = 'relationship_app'

urlpatterns = [
    # Existing URLs (keep these as they are)
    path('books/', views.book_list, name='book_list'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='relationship_app:login'), name='logout'),
    path('register/', views.register, name='register'),
    path('home/', views.home, name='home'), # Assuming you have a /home/ URL as well for the home view

    # Role-Based Access Control URLs (keep these as they are)
    path('admin-dashboard/', views.admin_view, name='admin_dashboard'),
    path('librarian-dashboard/', views.librarian_view, name='librarian_dashboard'),
    path('member-dashboard/', views.member_view, name='member_dashboard'),

    # --- New URLs for Book Operations with Custom Permissions ---
    path('books/add/', views.BookCreateView.as_view(), name='book_add'),
    path('books/<int:pk>/edit/', views.BookUpdateView.as_view(), name='book_edit'),
    path('books/<int:pk>/delete/', views.BookDeleteView.as_view(), name='book_delete'),
]