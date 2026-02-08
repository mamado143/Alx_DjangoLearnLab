from django.shortcuts import render
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView

# 1. Function-Based View: List all books
def list_books(request):
    books = Book.objects.all()  # Fetch all book instances
    context = {'books': books}  # Create a context dictionary
    return render(request, 'relationship_app/list_books.html', context)

# 2. Class-Based View: Show library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
