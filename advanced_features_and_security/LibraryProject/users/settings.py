INSTALLED_APPS = [
    # ... other apps ...
    'users.bookshelf',
    'users',  # Add this
]

AUTH_USER_MODEL = 'users.CustomUser'
