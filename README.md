# 📝 Django Blog Project

This Django project is a **simple blog and user authentication system** built with **Django 5.2**. 
It allows users to register, log in, and manage blog posts with full CRUD (Create, Read, Update, Delete) functionality. 
The project includes two main apps — **`blog`** and **`users`** — and uses **Crispy Forms with Bootstrap 4** for clean, responsive UI components.

---


## Preview

![Screenshot of the blog project](screenshot.PNG)

---


## 🚀 Features

- 🧑‍💻 User registration, login, logout, and profile management  
- 📰 Blog post management with create, edit, delete, and detail views  
- 🔐 Authentication protection for creating and managing posts  
- 🧱 Uses Django’s class-based and function-based views  
- 🎨 Styled with **Bootstrap 4** via `crispy_forms`  
- 🧩 SQLite as the default database  
- ⚙️ Organized project structure following Django best practices  

---

## 🛠️ Tech Stack

- **Backend:** Django 5.2, Python 3  
- **Frontend:** Bootstrap 4 (via Django Crispy Forms)  
- **Database:** SQLite  
- **Authentication:** Django built-in auth system  

---

## ⚙️ Setup Instructions

### 1. Clone the repository
```bash
git clone <repository-url>
cd <project-folder>
```

### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate   # On Windows use: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run migrations
```bash
python manage.py migrate
```

### 5. Create a superuser (optional)
```bash
python manage.py createsuperuser
```

### 6. Run the development server
```bash
python manage.py runserver
```

Then visit `http://127.0.0.1:8000/` in your browser.

---

## 📸 Preview

![Screenshot of the blog project](screenshot.PNG)

---

## 📂 Project Structure

```
myproject/
│
├── blog/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/blog/
│
├── users/
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── templates/users/
│
├── myproject/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
└── manage.py
```

---

## 📜 License

This project is open-source and free to use for educational and personal purposes.
