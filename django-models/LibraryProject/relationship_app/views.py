from django.views.generic.detail import DetailView
from .models import Library  # literal import required

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  # literal path required
    context_object_name = 'library'  # literal name required
