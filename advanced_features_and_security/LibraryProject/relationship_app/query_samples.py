from models import Book, Author, Librarian, Library

def book_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        print(f"Books by {author_name}")
        for book in books:
            print(f"- {book}")
    except Author.DoesNotExist:
        print(f"No author found with the name {author_name}")


def books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        print(f"Books in {library_name} library: ")
        for book in books:
            print(f"- {book}")
    except Library.DoesNotExist:
        print(f"No library with the name {library_name}")


def librarian_from_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarians = Librarian.objects.get(library=library)
        print(f"Librarians for {library_name} library:")
        for librarian in librarians:
            print(f"- {librarian}")
    except library.DoesNotExist:
        print(f"No libraray found with the name: {library_name}")
