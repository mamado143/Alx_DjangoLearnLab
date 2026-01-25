from django.utils.deprecation import MiddlewareMixin

class CSPMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        # Minimal, safe default policy
        response["Content-Security-Policy"] = "default-src 'self'"
        return response