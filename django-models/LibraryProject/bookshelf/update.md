# Update Book

```python
from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.title = "Animal Farm"
book.save()
