# accounts/urls.py

from django.urls import path
from .views import (                # ← Add this import line!
    RegisterView,
    LoginView,
    ProfileView,
    follow_user,                    # ← This is the missing one
    unfollow_user,                  # ← Add this too if you have unfollow
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    
    # Follow/unfollow endpoints (these were causing the NameError)
    path('follow/<int:user_id>/', follow_user, name='follow_user'),     # ✅ follow
    path('unfollow/<int:user_id>/', unfollow_user, name='unfollow_user'),  # ✅ unfollow
    ]
