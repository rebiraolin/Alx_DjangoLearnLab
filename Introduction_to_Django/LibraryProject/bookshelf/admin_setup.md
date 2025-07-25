# Django Admin Setup for Book Model

- Registered the `Book` model in `bookshelf/admin.py`.
- Customized admin list view with `list_display` for title, author, publication_year.
- Added filters for `author` and `publication_year`.
- Enabled search on `title` and `author`.
- Verified functionality by accessing `/admin` interface and managing Book records.

Example admin.py snippet:

```python
from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('author', 'publication_year')
    search_fields = ('title', 'author')
