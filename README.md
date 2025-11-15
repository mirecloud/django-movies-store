# Django Movie Store

A Django-based web application for managing and displaying a movie catalog with image galleries and pricing information.

## Project Overview

Django Movie Store is a full-featured content management system built with Django 5.0. The application provides functionality for browsing movies, managing inventory, and handling media assets through an intuitive admin interface.

## Technology Stack

- **Backend**: Django 5.0
- **Database**: SQLite3
- **Image Processing**: Pillow 12.0.0
- **Query Formatting**: SQLParse 0.5.3
- **Python Version**: 3.12+

## Project Structure

```
django-movies-store/
├── moviesstore/                 # Main Django project directory
│   ├── manage.py               # Django management command-line utility
│   ├── db.sqlite3              # SQLite database
│   ├── media/                  # User-uploaded files and media assets
│   │   └── movie_images/       # Movie cover images
│   ├── moviesstore/            # Project configuration package
│   │   ├── settings.py         # Project settings and configuration
│   │   ├── urls.py             # URL routing configuration
│   │   ├── asgi.py             # ASGI configuration for async servers
│   │   └── wsgi.py             # WSGI configuration for production servers
│   ├── home/                   # Home app (landing pages)
│   │   ├── models.py           # Data models
│   │   ├── views.py            # View logic
│   │   ├── urls.py             # App-level URL configuration
│   │   ├── admin.py            # Admin interface registration
│   │   ├── migrations/         # Database migration files
│   │   └── templates/home/     # HTML templates
│   ├── movies/                 # Movies app (core functionality)
│   │   ├── models.py           # Movie model definition
│   │   ├── views.py            # Movie view logic
│   │   ├── urls.py             # App-level URL configuration
│   │   ├── admin.py            # Admin interface registration
│   │   ├── migrations/         # Database migration files
│   │   └── templates/movies/   # Movie templates
│   └── moviesstore/            # Project templates (base templates)
│       ├── static/             # Static files (CSS, images)
│       │   ├── css/            # Stylesheets
│       │   └── img/            # Static images
│       └── templates/          # Base project templates
└── django-movie/               # Python virtual environment
```

## Installation and Setup

### Prerequisites

- Python 3.12 or higher
- pip (Python package installer)

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/mirecloud/django-movies-store.git
   cd django-movies-store
   ```

2. **Create and activate virtual environment**
   ```bash
   python3.12 -m venv django-movie
   source django-movie/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Navigate to project directory**
   ```bash
   cd moviesstore
   ```

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create superuser account**
   ```bash
   python manage.py createsuperuser
   ```

## Running the Development Server

```bash
cd moviesstore
python manage.py runserver
```

The application will be accessible at `http://127.0.0.1:8000/`

## Key Features

### Movies Application
- Movie listing and detail views
- Movie image gallery management
- Price tracking
- Comprehensive descriptions
- Admin interface for content management

### Home Application
- Landing page
- About page
- Navigation structure

### Media Management
- Automatic media file serving in development
- Image upload and storage
- Static file management

## Database Models

### Movie Model
```python
class Movie(models.Model):
    id          # Auto-generated primary key
    name        # Movie title (max 255 characters)
    price       # Numeric price value
    description # Detailed movie information
    image       # Movie cover image
```

## Configuration

### Media Files Configuration
- `MEDIA_URL`: `/media/`
- `MEDIA_ROOT`: `BASE_DIR/media`

Media files are automatically served in development mode. Ensure the URL routing in `urls.py` includes media file serving for development environments.

### Static Files Configuration
- `STATIC_URL`: `/static/`
- `STATICFILES_DIRS`: Contains `moviesstore/static/`

## Admin Interface

Access the Django admin panel at `/admin/` using your superuser credentials. From here you can:
- Add, edit, or delete movies
- Manage user accounts and permissions
- View system information
- Monitor application activity

## URL Routing

- `/` - Home page
- `/about/` - About page
- `/movies/` - Movie listing
- `/admin/` - Admin interface

## Development Notes

- The project uses SQLite for development. For production, consider PostgreSQL or MySQL.
- DEBUG mode is currently enabled. Disable for production deployment.
- SECRET_KEY should be stored securely in environment variables for production.
- ALLOWED_HOSTS should be configured appropriately for production environments.

## File Upload Requirements

Images uploaded to the movies app are automatically stored in `media/movie_images/`. Ensure this directory exists and has appropriate permissions.

## Production Deployment Checklist

- [ ] Set `DEBUG = False` in settings.py
- [ ] Configure `ALLOWED_HOSTS` with actual domain names
- [ ] Move `SECRET_KEY` to environment variables
- [ ] Switch to production-grade database
- [ ] Configure proper static file serving
- [ ] Set up HTTPS
- [ ] Configure email backend
- [ ] Use a production WSGI server (Gunicorn, uWSGI)

## License

This project is maintained by mirecloud.

## Support

For issues or questions, please refer to the Django documentation at https://docs.djangoproject.com/
