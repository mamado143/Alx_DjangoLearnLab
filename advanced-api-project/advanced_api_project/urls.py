from django.contrib import admin
from django.urls import path

# Import your views directly here
from api.views import BookListCreateView, BookRetrieveUpdateDestroyView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # API endpoints directly in project urls (no include needed)
    path('api/books/', BookListCreateView.as_view(), name='book-list'),
    path('api/books/<int:pk>/', BookRetrieveUpdateDestroyView.as_view(), name='book-detail'),
]
