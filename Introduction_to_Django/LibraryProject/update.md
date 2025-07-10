# Update Operation

## Python Commands:

```python
from bookshelf.models import Book

# Get the book instance to update
book_to_update = Book.objects.get(title='1984')

# Update its title
book_to_update.title = "Nineteen Eighty-Four"

# Save the changes
book_to_update.save()

# Verify the update (optional, but good practice)
updated_book = Book.objects.get(id=book_to_update.id) # Re-fetch or use the same object
print(updated_book.title)