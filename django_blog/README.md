📘 Django Blog Project

A simple blog application built with Django.
This project supports post creation, editing, deletion, comments, tagging, authentication, and search functionality.

🚀 Features

User registration & authentication

Create, update, delete blog posts

Comment system

Tagging system

Search functionality

Admin panel

Media file support

📂 Project Structure
django_blog/
├── blog/                 # Blog app
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   ├── templates/
│   └── migrations/
│
├── django_blog/          # Project configuration
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── manage.py
└── README.md
⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone <your-repo-url>
cd django_blog
2️⃣ Create Virtual Environment
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
3️⃣ Install Dependencies
pip install django

(Optional: create requirements.txt)

pip freeze > requirements.txt
4️⃣ Apply Migrations
python manage.py makemigrations
python manage.py migrate
5️⃣ Create Superuser
python manage.py createsuperuser
6️⃣ Run Development Server
python manage.py runserver

Visit:

Blog: http://127.0.0.1:8000/

Admin Panel: http://127.0.0.1:8000/admin/

🛠️ Configuration
Add App to settings.py
INSTALLED_APPS = [
    ...
    'blog',
]
Static & Media Settings
STATIC_URL = '/static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
🧪 Running Tests
python manage.py test
📦 Future Improvements


REST API with Django REST Framework

Like system

Follow system

Notifications

Deployment (Docker, AWS, etc.)

Production-ready security settings

👤 Author

Mohamed Dahir Mohamoud
Mobile Software Engineer

📄 License

This project is for educational purposes.
