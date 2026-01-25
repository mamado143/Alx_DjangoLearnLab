# Add to MIDDLEWARE
MIDDLEWARE = [
    # Include our local CSP middleware to avoid third-party deps
    'security_middleware.CSPMiddleware',
]

# If using django-csp instead of local middleware, uncomment and add to INSTALLED_APPS
# CSP_DEFAULT_SRC = ("'self'",)
# CSP_STYLE_SRC = ("'self'", "'unsafe-inline'")
# CSP_SCRIPT_SRC = ("'self'", "'unsafe-inline'")

# SECURITY SETTINGS
# Set to True in production
DEBUG = False

# HTTPS Settings
SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 31536000  # 1 Year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Cookie Security
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Browser Security Headers
X_FRAME_OPTIONS = 'DENY'
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True

# Proxy setup (Required if behind Nginx/Apache)
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Django app registration and custom user model
INSTALLED_APPS = [
    'users',
    'users.bookshelf',
]
AUTH_USER_MODEL = 'users.CustomUser'
