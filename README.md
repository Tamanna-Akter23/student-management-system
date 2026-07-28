# Student Management System

A responsive Django project using three databases:

- Students: MySQL
- Courses: PostgreSQL
- Student Notes: MongoDB

## Features

- Secure login and logout
- Protected dashboard and CRUD pages
- Student, course, and note CRUD
- Search on all record pages
- Pagination
- Success and error messages
- Responsive Bootstrap interface
- Dashboard totals and recent records
- Docker startup wait checks

## Start the project

```powershell
docker compose up --build
```

## Create the first login account

Open a second terminal in the project folder and run:

```powershell
docker compose exec web python manage.py createsuperuser
```

Enter a username, email, and password. Then sign in at:

```text
http://127.0.0.1:8000/accounts/login/
```

## Stop the project

```powershell
docker compose down
```

Do not add `-v` unless you intentionally want to delete all database data.

## Django Administration as a Primary Interface

Staff and superusers can manage the complete system at `/admin/`:

- Students stored in MySQL
- Courses stored in PostgreSQL
- Student Notes stored in MongoDB
- User accounts, permissions and groups

Create an administrator account with:

```bash
docker compose exec web python manage.py createsuperuser
```

The public Bootstrap interface and the Django admin interface both manage the same records.
