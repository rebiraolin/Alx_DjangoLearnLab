from bookshelf.models import Book
>>> book = Book.objects.get(title="1984")
>>> book.title = "Nineteen Eighty-Four" 
>>> book.save()
>>> updated_book = Book.objects.get(id=book.id)
>>> print(updated_book.title)
Nineteen Eighty-Four
>>>