# OEMS (Office Employee Management System)

## Description

OEMS is a simple Django-based Office Employee Management System that allows you to manage employees, departments, and roles efficiently. The system includes CRUD operations, user authentication, filtering, and integrates with MySQL for robust database management.

## Features

* Add, view, update, and delete employees
* Filter employees by name, department, or role
* User signup, login, and logout
* MySQL database integration
* Simple and responsive UI design
* Employee data management with departments and roles

## Project Structure

```
office_emp/          # Project settings and configurations
testapp/             # Django app containing models, views, templates
templates/           # HTML templates
static/              # CSS, JS, images
db.sqlite3           # Local SQLite database (ignored in Git)
requirements.txt     # Project dependencies
README.md            # Project documentation
```

## Setup Instructions

1. **Clone the repository:**

```bash
git clone <your-github-repo-url>
cd office_emp
```

2. **Create and activate a virtual environment (optional but recommended):**

```bash
python -m venv venv
# Activate on Windows:
venv\Scripts\activate
# Activate on Linux/macOS:
source venv/bin/activate
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

4. **Configure MySQL database:**

* Make sure you have MySQL installed locally.
* Create a database `oems_db`.
* Update `office_emp/settings.py` to use environment variable for password:

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

5. **Set environment variable for MySQL password:**

* **Windows (PowerShell):**

```powershell
setx DB_PASSWORD "your_mysql_password"
```

* **Linux/macOS:**

```bash
export DB_PASSWORD="your_mysql_password"
```

6. **Run migrations:**

```bash
python manage.py migrate
```

7. **Create superuser (optional, for admin access):**

```bash
python manage.py createsuperuser
```

8. **Run the development server:**

```bash
python manage.py runserver
```

* Open your browser at `http://127.0.0.1:8000/` to access the application.

## Usage

* Navigate to **Add Employee** to add new employees.
* Use **View All Employees** to see the list of employees.
* Filter employees by name, department, or role.
* Admin users can manage departments, roles, and employees via the Django admin panel.

## Notes

* Do **not commit `settings.py`** with your database password.
* SQLite database (`db.sqlite3`) is ignored in GitHub; use MySQL for production.
* Use environment variables to manage sensitive credentials.

## License

This project is for educational purposes only (college project).
