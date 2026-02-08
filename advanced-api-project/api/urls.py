from django.urls import path
from .views import (
    BookListView, BookCreateView,
    BookDetailView, BookUpdateView, BookDeleteView
)

urlpatterns = [
    # List and Create share the same URL (DRF dispatches by HTTP method)
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/', BookCreateView.as_view(), name='book-create'),

    # Detail, Update, Delete share the same URL (dispatched by method)
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/<int:pk>/', BookUpdateView.as_view(), name='book-update'),
    path('books/<int:pk>/', BookDeleteView.as_view(), name='book-delete'),
]f
