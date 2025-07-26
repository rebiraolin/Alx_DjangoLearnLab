from django.db import models
from django.conf import settings

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100) #

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100) #
    author = models.ForeignKey(Author, on_delete=models.CASCADE) #
    publication_year = models.IntegerField(default=2000) # Added as it's used in library_detail.html for Task 1

    class Meta:
        permissions = [
            ("can_add_book", "Can add book"),
            ("can_change_book", "Can change book"),
            ("can_delete_book", "Can delete book"),
        ]

    def __str__(self):
        return f"{self.title} by {self.author.name}"


class Library(models.Model):
    name = models.CharField(max_length=100) #
    books = models.ManyToManyField(Book) #

    def __str__(self):
        return self.name


class Librarian(models.Model):
    name = models.CharField(max_length=100) # Added as it's common for a person model
    library = models.OneToOneField(Library, on_delete=models.CASCADE) #

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    ROLES = (
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL , on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLES, default='Member')

    def __str__(self):
        return f"{self.user.username} - {self.role}"