# Blog Application

A feature-rich blog application built with Django that allows users to read, share, and comment on blog posts. The application includes user authentication, post management, tagging, and search functionality.

## Features

- **Blog Posts**
  - Create, read, update, and delete blog posts
  - Draft and publish functionality
  - Rich text content support
  - Post tagging and categorization
  - Post sharing via email
  - Related posts suggestions

- **Comments System**
  - Comment on blog posts
  - Comment moderation
  - Nested comments support

- **User Authentication**
  - User registration and login
  - User profiles
  - Password reset functionality

- **Search & Filtering**
  - Full-text search
  - Tag-based filtering
  - Date-based archiving
  - Pagination

- **SEO Friendly**
  - Clean URLs with slugs
  - Sitemap generation
  - RSS/Atom feeds

## Technology Stack

- **Backend**: Django 4.2+
- **Database**: SQLite (can be configured for PostgreSQL)
- **Frontend**: HTML5, CSS3, JavaScript
- **Additional Packages**:
  - django-taggit for tagging
  - django-sitemaps for sitemap generation
  - django-feeds for RSS/Atom feeds

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd blog-application
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the admin panel**
   - Visit `http://127.0.0.1:8000/admin/`
   - Log in with your superuser credentials

## Project Structure

```
blog-application/
├── blog/                    # Main application directory
│   ├── migrations/          # Database migrations
│   ├── static/              # Static files (CSS, JS, images)
│   ├── templates/           # HTML templates
│   ├── __init__.py
│   ├── admin.py            # Admin site configuration
│   ├── apps.py             # Application configuration
│   ├── feeds.py            # RSS/Atom feeds
│   ├── forms.py            # Form definitions
│   ├── models.py           # Database models
│   ├── sitemaps.py         # Sitemap configuration
│   ├── tests.py            # Test cases
│   ├── urls.py             # URL routing
│   └── views.py            # View functions
├── mysite/                 # Project configuration
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py         # Django settings
│   ├── urls.py            # Main URL configuration
│   └── wsgi.py
├── .gitignore
├── db.sqlite3             # SQLite database (not in version control)
├── manage.py              # Django management script
└── requirements.txt       # Python dependencies
```

## Configuration

1. **Database Configuration**
   The application uses SQLite by default. To use PostgreSQL, update the `DATABASES` setting in `mysite/settings.py`:

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'blogdb',
           'USER': 'your_username',
           'PASSWORD': 'your_password',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```

2. **Email Configuration**
   Update email settings in `mysite/settings.py` to enable email functionality:

   ```python
   EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
   EMAIL_HOST = 'smtp.gmail.com'
   EMAIL_PORT = 587
   EMAIL_USE_TLS = True
   EMAIL_HOST_USER = 'your-email@gmail.com'
   EMAIL_HOST_PASSWORD = 'your-email-password'
   ```

## Usage

### Creating Blog Posts
1. Log in to the admin panel
2. Navigate to "Posts"
3. Click "Add Post"
4. Fill in the post details and save

### Managing Comments
- Comments can be moderated through the admin panel
- Toggle comment visibility using the "Active" checkbox

### Searching Content
- Use the search bar to find posts by keywords
- Click on tags to filter posts by category
- Browse posts by date using the archive links

## API Endpoints

The application provides the following API endpoints:

- `GET /api/posts/` - List all published posts
- `GET /api/posts/<slug>/` - Get a specific post
- `GET /api/posts/<slug>/comments/` - Get comments for a post
- `POST /api/posts/<slug>/comments/` - Add a new comment

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Django Documentation
- Django Girls Tutorial
- Real Python Django Tutorials
