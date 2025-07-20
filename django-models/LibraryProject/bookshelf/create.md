# Create Operation

## Python Command:

```python
# Create Operation for Book Model

This demonstrates how to create a `Book` instance using Django's ORM in the Django shell.

## Django Shell Command

```python
from bookshelf.models import Book

Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
