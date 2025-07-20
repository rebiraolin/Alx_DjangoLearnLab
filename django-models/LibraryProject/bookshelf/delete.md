# Delete Operation

## Python Commands:

```python
from bookshelf.models import Book

# Get the book instance to delete
book_to_delete = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book
book_to_delete.delete()

# Confirm deletion by retrieving all books
print(Book.objects.all())


book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
Book.objects.all()
