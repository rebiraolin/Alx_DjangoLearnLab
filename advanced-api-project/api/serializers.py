from rest_framework import serializers
from .models import Book, Author
from datetime import date

class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model.

    This serializer handles the serialization and deserialization of Book objects.
    It includes custom validation to ensure that the publication year is not in the future.
    """
    class Meta:
        model = Book
        fields = "__all__"  # Includes all fields from the Book model

    def validate_publication_year(self, value):
        """
        Custom validation for the 'publication_year' field.

        Ensures that the provided publication year is not in the future.
        Raises a ValidationError if the year is greater than the current year.
        """
        current_year = date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Author model.

    This serializer includes the author's name and a nested representation of their books.
    The 'book_set' field leverages Django's reverse relationship from the Book model
    (where Book has a ForeignKey to Author). 'many=True' indicates that an author can
    have multiple books, and 'read_only=True' means that books cannot be created or
    updated directly through this nested serializer when creating/updating an author.
    """
    book_set = BookSerializer(many=True, read_only=True) # Nested serializer for related books

    class Meta:
        model = Author
        fields = ["name", "book_set"] # Includes the author's name and their associated books