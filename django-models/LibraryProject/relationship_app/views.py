from django.shortcuts import render
from .models import Book
from .models import Library
from django.contrib.auth.decorators import user_passes_test
from django.views.generic.detail import DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import BookForm


# 1. Add Book View (Requires 'can_add_book')
@permission_required('relationship_app.can_add_book')
def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        form = BookForm()
    return render(request, 'relationship_app/add_book.html', {'form': form})

# 2. Edit Book View (Requires 'can_change_book')
@permission_required('relationship_app.can_change_book')
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        form = BookForm(instance=book)
    return render(request, 'relationship_app/edit_book.html', {'form': form, 'book': book})

# 3. Delete Book View (Requires 'can_delete_book')
@permission_required('relationship_app.can_delete_book')
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect('list_books')
    return render(request, 'relationship_app/delete_book.html', {'book': book})

def list_books(request):
    books = Book.objects.all()  # Fetch all book instances
    context = {'books': books}  # Create a context dictionary
    return render(request, 'relationship_app/list_books.html', context)

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            return redirect('list_books')  # Redirect to the home page (or any page you want)
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# Helper functions to check roles
def check_admin(user):
    return user.userprofile.role == 'Admin'

def check_librarian(user):
    return user.userprofile.role == 'Librarian'

def check_member(user):
    return user.userprofile.role == 'Member'

# Admin View
@user_passes_test(check_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

# Librarian View
@user_passes_test(check_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

# Member View
@user_passes_test(check_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')
