AUTH_USER_MODEL = 'bookshelf.CustomUser'

# Also recommended when using custom user + image field
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
DEBUG = False

SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'
SECURE_CONTENT_TYPE_NOSNIFF = True
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
# HTTPS and Secure Redirects
SECURE_SSL_REDIRECT = True  # Redirect HTTP to HTTPS
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')  # For proxies

SECURE_HSTS_SECONDS = 31536000  # 1 year HSTS
SECURE_HSTS_INCLUDE_SUBDOMAINS = True  # Include subdomains
SECURE_HSTS_PRELOAD = True  # Allow HSTS preload list

# Secure Cookies (already in Task 2, but repeated for completeness)
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
# For profile_photo ImageField
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
# ... other settings ...

AUTH_USER_MODEL = 'bookshelf.CustomUser'
# ... rest of file ...
# Secure Headers (from Task 2)
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'
