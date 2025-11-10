# 🏢 OEMS (Office Employee Management System)

## 📘 Overview

**OEMS** is a Django-based Office Employee Management System designed to efficiently manage employees, departments, and roles.  
It includes **user authentication**, **CRUD operations**, **filtering**, and a **responsive UI** built with Bootstrap.  
The project integrates with **MySQL** for robust database handling and supports easy deployment to cloud platforms like **PythonAnywhere** or **Render**.

---

## ✨ Features

- ✅ **Employee Management** – Add, update, delete, and view employee records  
- 🔍 **Filtering System** – Filter employees by name, department, or role  
- 👥 **User Authentication** – Signup, login, logout, and forgot password functionality  
- 🧩 **Department & Role Management** – Organized and linked through models  
- 💾 **Database Integration** – MySQL (recommended) or SQLite (for testing)  
- 💻 **Responsive UI** – Clean design using Bootstrap and custom CSS  
- ⚙️ **Modular Structure** – Easy to extend with additional apps or features  

---

## 🗂️ Project Structure

```
office_emp/          # Main project folder (settings, URLs, WSGI)
testapp/             # Core app with models, forms, views, and templates
templates/           # HTML templates (login, signup, dashboard, etc.)
static/              # CSS, JS, images
requirements.txt     # Python dependencies
README.md            # Documentation
.gitignore           # Ignored files and directories
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

```bash
git clone https://github.com/sidhu3/OEMS.git
cd office_emp
```

### 2️⃣ Create and activate a virtual environment (recommended)

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/macOS
source venv/bin/activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure the database (MySQL recommended)

Update your `office_emp/settings.py` file:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'oems_db',
        'USER': 'yourusername',
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

Then, set your environment variable for MySQL password:

#### Windows (PowerShell)
```powershell
setx DB_PASSWORD "your_mysql_password"
```

#### Linux/macOS
```bash
export DB_PASSWORD="your_mysql_password"
```

---

### 5️⃣ Apply migrations

```bash
python manage.py migrate
```

### 6️⃣ Create an admin user (optional)

```bash
python manage.py createsuperuser
```

### 7️⃣ Run the development server

```bash
python manage.py runserver
```

Then open your browser at 👉 [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 🧠 Usage

- Go to **Signup** to create a user account.  
- **Login** and navigate to the dashboard.  
- Add, edit, or delete employees.  
- Use **Filter Employees** to search by name, department, or role.  
- Access the **Forgot Password** page to reset credentials.  
- Admins can also manage data from the Django admin panel.

---

## 📄 Notes

- Sensitive data like passwords should be stored in **environment variables**.  
- The SQLite database (`db.sqlite3`) is ignored in Git.  
- For production, prefer **MySQL** or **PostgreSQL**.  
- Deployment tested on **PythonAnywhere** and **Render**.  

---

## 🧾 License

This project is developed for **educational and academic purposes** as part of a college project.
