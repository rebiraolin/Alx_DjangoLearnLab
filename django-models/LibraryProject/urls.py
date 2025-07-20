"""
URL configuration for LibraryProject project.
"""
from django.contrib import admin
from django.urls import path, include # Ensure 'include' is imported

urlpatterns = [
    path('admin/', admin.site.urls),
    # Include all URLs from your relationship_app directly at the project root.
    # This means URLs like 'books/' and 'library/<pk>/' from your app's urls.py
    # will be accessible directly as /books/ and /library/<pk>/.
    path('', include('relationship_app.urls')),
]