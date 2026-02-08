import os
import django

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings") 
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        # Filter books by the author instance
        books = Book.objects.filter(author=author)
        for book in books:
            print(book.title)
    except Author.DoesNotExist:
        print(f"Author {author_name} not found")

# 2. List all books in a library
def get_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        # Access the ManyToMany field
        books = library.books.all()
        for book in books:
            print(book.title)
    except Library.DoesNotExist:
        print(f"Library {library_name} not found")

# 3. Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        # Access the OneToOne field (Librarian is associated with Library)
        librarian = Librarian.objects.get(library=library)
        print(librarian.name)
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        print(f"Librarian for {library_name} not found")

# Example usage (Optional - for your testing)
# get_books_by_author("Orwell")
