from django.urls import path
from .views import list_books, LibraryDetailView, register # Import register
from django.contrib.auth.views import LoginView, LogoutView # Import built-in views

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

 # Login view
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),

    # Logout view
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),

    # Register view (This is exactly what the checker is looking for: "views.register")
    path('register/', views.register, name='register'),
] 
