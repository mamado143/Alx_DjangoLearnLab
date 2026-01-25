from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("Additional Fields", {"fields": ("date_of_birth", "profile_photo")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional Fields", {"fields": ("date_of_birth", "profile_photo")}),
    )
    list_display = ("email", "first_name", "last_name", "is_staff", "date_of_birth")
    search_fields = ("email", "first_name", "last_name")
    ordering = ("email",)

admin.site.register(CustomUser, CustomUserAdmin)
