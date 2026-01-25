# Custom User Model
AUTH_USER_MODEL = 'bookshelf.CustomUser'

# Media settings for profile_photo
import os
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Security Best Practices
DEBUG = False  # Never True in production

SECURE_BROWSER_XSS_FILTER = True  # Enables browser XSS protection
X_FRAME_OPTIONS = 'DENY'  # Prevents clickjacking
SECURE_CONTENT_TYPE_NOSNIFF = True  # Prevents MIME sniffing
CSRF_COOKIE_SECURE = True  # CSRF cookie over HTTPS only
SESSION_COOKIE_SECURE = True  # Session cookie over HTTPS only

# Content Security Policy (CSP) - Install django-csp via pip if needed
INSTALLED_APPS = [... , 'csp']
MIDDLEWARE = [... , 'csp.middleware.CSPMiddleware']
CSP_DEFAULT_SRC = ("'self'",)  # Restrict sources to same origin
CSP_STYLE_SRC = ("'self'", "'unsafe-inline'")  # Allow inline styles (adjust as needed)
CSP_SCRIPT_SRC = ("'self'",)
CSP_IMG_SRC = ("'self'", "data:")
