from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

# BookSerializer: serializes all Book fields and validates publication_year.
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    # Custom validation to ensure the year is not in the future.
    def validate_publication_year(self, value):
        current_year = datetime.utcnow().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        if value < 0:
            raise serializers.ValidationError("Publication year must be a positive year.")
        return value

# AuthorSerializer: includes the author's name and a nested list of their books.
# Uses BookSerializer with many=True to serialize the reverse relation (Author -> books).
class AuthorSerializer(serializers.ModelSerializer):
    # Nest related books using the 'books' related_name from Book.author ForeignKey.
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
