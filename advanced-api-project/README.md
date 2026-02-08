# Advanced API Project

A comprehensive Django REST Framework API for managing a library of books and authors. This project demonstrates advanced features including serialization, authentication, dynamic filtering, searching, ordering, and unit testing.

## 📋 Table of Contents
- [Features](#features)
- [Installation](#installation)
- [API Endpoints](#api-endpoints)
- [Filtering & Searching](#filtering--searching)
- [Testing](#testing)

---

## 🚀 Features

* **CRUD Operations:** Full Create, Read, Update, and Delete functionality for Books.
* **Authentication & Permissions:**
    * Read-only access for unauthenticated users.
    * Create, Update, and Delete access restricted to authenticated users.
* **Advanced Querying:**
    * **Filtering:** Filter books by title, author, or publication year.
    * **Searching:** specific text search on book titles and author names.
    * **Ordering:** Sort results by publication year or title.
* **Data Validation:** Custom validation ensures books cannot be created with a publication year in the future.

---

## 🛠️ Installation

1.  **Clone the repository:**
    ```bash
    git clone <your-repo-url>
    cd advanced_api_project
    ```

2.  **Create and Activate a Virtual Environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install Dependencies:**
    ```bash
    pip install django djangorestframework django-filter
    ```

4.  **Apply Migrations:**
    ```bash
    python manage.py migrate
    ```

5.  **Create a Superuser (Optional):**
    ```bash
    python manage.py createsuperuser
    ```

6.  **Run the Server:**
    ```bash
    python manage.py runserver
    ```

---

## 🔗 API Endpoints

All endpoints are prefixed with `/api/`.

| Method | Endpoint | Description | Permission |
| :--- | :--- | :--- | :--- |
| `GET` | `books/` |
