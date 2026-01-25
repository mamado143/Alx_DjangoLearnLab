# Advanced Features and Security – Implementation Notes

- Custom user model: `users.CustomUser` (fields: `date_of_birth`, `profile_photo`).
- Admin integration: `users/admin.py` registers `CustomUser` with extra fields.
- Settings: `LibraryProject/LibraryProject/settings.py` sets `AUTH_USER_MODEL` and includes security settings (HSTS, SSL redirect, secure cookies, X-Frame-Options, no-sniff, XSS filter, CSP via `security_middleware`).
- Permissions: `LibraryProject/bookshelf/models.py` defines `can_view`, `can_create`, `can_edit`, `can_delete`.
- Views: `LibraryProject/bookshelf/views.py` uses `@permission_required` for those permissions.
- CSRF: templates include `{% csrf_token %}` (see form_example.html under app templates).
- Groups setup: run `users/setup_permissions.py` to create Viewers/Editors/Admins and assign permissions.
- HTTPS: see `nginx.conf` for sample reverse proxy with SSL.
