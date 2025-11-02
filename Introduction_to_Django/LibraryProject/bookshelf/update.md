# Update Book

```python
from bookshelf.models import Book
book = Book.objects.get(title="1984")
book.title = "Animal Farm"
book.save()
