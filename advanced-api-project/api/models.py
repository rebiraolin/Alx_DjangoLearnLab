from django.db import models

# Create your models here.
class Author(models.Model):
    """
    Represents an author.

    Fields:
    - name: The name of the author (CharField with max_length=100).
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        """
        String representation of the Author model.
        Returns the author's name.
        """
        return self.name

class Book(models.Model):
    """
    Represents a book.

    Fields:
    - author: A ForeignKey to the Author model, establishing a many-to-one relationship.
              When an Author is deleted, all their associated Books will also be deleted (CASCADE).
              Django automatically creates a reverse relationship from Author to Book,
              accessible via 'author_instance.book_set.all()'.
    - title: The title of the book (CharField with max_length=100).
    - publication_year: The year the book was published (IntegerField).
    """
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        """
        String representation of the Book model.
        Returns the book's title and author.
        """
        return f"{self.title} by {self.author.name}"