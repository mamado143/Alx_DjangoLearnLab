# Social Media API

A Django REST API for social media functionality, including user management (`accounts` app) and authentication using **DRF Token Authentication**.

---

## 🗂 Project Structure
social_media_api/
├── manage.py
├── db.sqlite3
├── requirements.txt
├── social_media_api/
│ ├── init.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
└── accounts/
├── init.py
├── admin.py
├── apps.py
├── models.py
├── views.py
├── serializers.py
├── urls.py
├── tests.py
└── migrations/


---

## ⚡ Features

- Custom user model (`accounts.CustomUser`)
- User registration & authentication
- Token-based authentication via **DRF**
- User profile management
- Media support (profile pictures)

---

## 📦 Requirements

- Python 3.9+
- Django 4.2+
- Django REST Framework
- (Optional) Other packages listed in `requirements.txt`

Install dependencies:

```bash
pip install -r requirements.txt
🚀 Setup

Clone the repository

git clone <your-repo-url>
cd social_media_api

Apply migrations

python manage.py makemigrations
python manage.py migrate

Create superuser (optional)

python manage.py createsuperuser

Run the development server

python manage.py runserver

The API will be available at: http://127.0.0.1:8000/

🔗 API Endpoints

/api/accounts/register/ – User registration

/api/accounts/login/ – User login (returns token)

/api/accounts/profile/ – Retrieve/update profile

(Add other endpoints from accounts/urls.py here)

🛠 Project Configuration

Custom User Model: AUTH_USER_MODEL = 'accounts.CustomUser'

Authentication: TokenAuthentication

Media files: Stored in /media/, URL at /media/

📝 Notes

Make sure accounts app is in INSTALLED_APPS in settings.py.

Use the same Python environment where Django is installed.

Run python manage.py runserver from the project root (manage.py location).

📄 License

MIT License © 2026
