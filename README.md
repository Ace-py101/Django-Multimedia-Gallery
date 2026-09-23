# Multimedia Gallery

A simple Django multimedia gallery application built with Python, Django,
and PostgreSQL.

## Features

- Django administration for managing multimedia
- PostgreSQL database
- Image uploads
- Video uploads
- Audio uploads
- Public multimedia gallery
- Individual media detail pages
- Static CSS styling
- Media file serving during development
- Basic automated tests

## Technologies

- Python
- Django
- PostgreSQL
- HTML
- CSS
- Pillow
- psycopg

## Project Structure

```text
assignment-5/
│
├── audio/
├── images/
├── videos/
│
├── media_gallery/
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   ├── admin.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── multimedia_project/
│   ├── settings.py
│   └── urls.py
│
├── .gitignore
├── manage.py
└── README.md