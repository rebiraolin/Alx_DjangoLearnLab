# Retrieve Operation

## Python Commands:

```python
from bookshelf.models import Book

# Retrieve all books
books = Book.objects.all()
print(books)

# Access the first book and print its attributes
book_instance = books[0]
print(book_instance.title)
print(book_instance.author)
print(book_instance.publication_year

book = Book.objects.get(title="1984")
book.title, book.author, book.publication_year
# ('1984', 'George Orwell', 1949)
