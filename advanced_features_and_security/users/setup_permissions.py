import os
import sys
from pathlib import Path
import django

# Ensure project root is on sys.path so 'users' and 'bookshelf' are importable
BASE_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = BASE_DIR.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

# Point Django to the correct settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')

django.setup()

from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from users.bookshelf.models import Book

def setup_groups():
    # Define Groups
    editors, _ = Group.objects.get_or_create(name='Editors')
    viewers, _ = Group.objects.get_or_create(name='Viewers')
    admins, _ = Group.objects.get_or_create(name='Admins')

    # Get Permissions
    ct = ContentType.objects.get_for_model(Book)
    can_view = Permission.objects.get(codename='can_view', content_type=ct)
    can_create = Permission.objects.get(codename='can_create', content_type=ct)
    can_edit = Permission.objects.get(codename='can_edit', content_type=ct)
    can_delete = Permission.objects.get(codename='can_delete', content_type=ct)

    # Assign Permissions
    viewers.permissions.add(can_view)
    editors.permissions.add(can_create, can_edit)
    admins.permissions.add(can_create, can_edit, can_delete, can_view)

    print("Groups and permissions setup successfully.")

if __name__ == "__main__":
    setup_groups()
