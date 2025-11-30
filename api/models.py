from django.db import models

# Create your models here.
from django.db import models

# Author represents a writer who can have multiple books.
# One-to-many: Author -> Book via Book.author ForeignKey.
class Author(models.Model):
    name = models.CharField(max_length=255)  # Author's full name

    def __str__(self):
        return self.name

# Book represents a single published work by an Author.
# Links to Author with a ForeignKey; related_name='books' enables reverse lookup.
class Book(models.Model):
    title = models.CharField(max_length=255)  # Book title
    publication_year = models.IntegerField()  # Year of publication (YYYY)
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='books'  # Allows author.books.all() in queries/serializers
    )

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
