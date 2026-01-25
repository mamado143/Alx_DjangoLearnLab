Security Measures:
- DEBUG=False for prod.
- Headers for XSS, clickjacking prevention.
- CSRF in all forms.
- CSP to mitigate XSS.
- ORM for SQL injection prevention.
Tests: Manual input validation, header checks via browser dev tools.

Deployment for HTTPS:
- Use Nginx/Apache with SSL.
Nginx Example:
server {
    listen 80;
    server_name example.com;
    return 301 https://$server_name$request_uri;
}
server {
    listen 443 ssl;
    server_name example.com;
    ssl_certificate /path/to/fullchain.pem;
    ssl_certificate_key /path/to/privkey.pem;
    # Proxy to Django
    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header X-Forwarded-Proto https;
    }
}
- Obtain certs via Let's Encrypt.

Security Review:
- HTTPS: Enforces encrypted traffic via redirects and HSTS (prevents downgrade attacks).
- Cookies: Secure flags ensure HTTPS-only transmission.
- Headers: Protect against XSS, clickjacking, MIME issues.
Improvements: Regular cert renewal, monitor for vulnerabilities.
Contributions: Enhances data privacy, prevents MITM attacks.
