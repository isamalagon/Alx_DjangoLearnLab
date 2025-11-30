from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer

# List all authors with nested books.
class AuthorList(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

# List and create books (with validation).
class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
