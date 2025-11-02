# Delete Book

```python
from bookshelf.models import Book
book = Book.objects.get(title="Animal Farm")
book.delete()
