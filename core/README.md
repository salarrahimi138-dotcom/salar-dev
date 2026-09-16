# Salar.dev

## Personal Developer Portfolio

Salar.dev is a personal developer portfolio website built as the final project for **CS50 Web Programming with Python and JavaScript**.

The project is designed to provide a central place to showcase my programming projects, technical skills, learning journey, certificates, and other professional achievements.

The website is being developed with **Django** as the backend framework, with HTML, CSS, and JavaScript used for the frontend.

---

# Distinctiveness and Complexity

Salar.dev is a personal developer portfolio platform and is distinct from the previous CS50W projects such as Wiki, Commerce, Mail, and Network.

Rather than focusing on a single application feature, the project is designed as a complete personal developer hub.

The project includes a structured database for managing portfolio projects, categories, and technologies, as well as dynamic project search and filtering.

The application uses Django models and relationships to organize project information and Django views and templates to dynamically display the content.

Future development will expand the platform with additional sections such as authentication, content management, learning journey, blog/notes, JavaScript functionality, responsive design, and deployment.

---

# Technologies Used

* Python
* Django 6.1.1
* HTML
* CSS
* JavaScript
* SQLite
* Git / GitHub

### Python Packages

* Django
* Pillow

Pillow is used to support image fields for portfolio projects.

---

# Project Structure

The project currently uses the following main Django components:

* `config` — Main Django project configuration
* `core` — Main application containing models, views, URLs, and templates
* `templates` — Django HTML templates
* `static` — Static files for future frontend styling and JavaScript
* `media` — Uploaded project images

---

# Project Progress

## Day 1 — Project Setup

Completed:

* Created the Django project.
* Created the main application (`core`).
* Configured the Django project.
* Created the initial homepage view.
* Created the template structure.
* Initialized the Git repository.
* Verified the project with Django system checks.

---

## Day 2 — Template and Static Structure

Completed:

* Created Django template directories.
* Connected views with templates.
* Created the homepage.
* Added the static file structure.
* Prepared the foundation for future frontend development.

---

## Day 3 — Projects Backend

Completed:

### Database Models

Created the following models:

### Category

Used to organize projects into different groups.

Fields:

* `name`

### Technology

Stores the technologies used in projects.

Fields:

* `name`

### Project

Stores portfolio project information.

Fields:

* `category`
* `title`
* `slug`
* `short_description`
* `description`
* `technologies`
* `github_url`
* `demo_url`
* `image`
* `featured`
* `created_at`
* `updated_at`

### Database Relationships

Implemented:

* One Category can contain multiple Projects.
* One Project can use multiple Technologies.

Using:

* `ForeignKey`
* `ManyToManyField`

### Project Slugs

Added a unique slug field to projects to create clean and readable project detail URLs.

Example:

```text
/projects/salar-dev/
```

### Django Admin

Configured the Django Admin panel for project management.

The Project admin includes:

* Project title
* Category
* Featured status
* Creation date

This allows portfolio content to be managed through Django's built-in administration system.

---

# Day 4 — Projects Frontend and Filtering

Completed:

### Projects List

Created a dedicated projects page displaying:

* Project title
* Short description
* Category
* Technologies
* GitHub link
* Demo link

### Project Detail Page

Created individual project pages using the project's unique slug.

The detail page displays:

* Project title
* Project image
* Short description
* Full description
* Category
* Technologies
* GitHub link
* Demo link

Optional fields such as the image, GitHub URL, and Demo URL are displayed only when they exist.

### Search

Implemented project search using Django QuerySets and `Q` objects.

Users can search projects by:

* Title
* Short description
* Full description

The search uses case-insensitive matching.

Search functionality was tested successfully, including Persian text.

### Category Filter

Implemented dynamic category filtering.

Categories are loaded directly from the database and users can filter projects by category.

The category filter uses:

```python
category__name__iexact
```

which allows case-insensitive category matching.

### Combined Filtering

Search and category filtering can be used together.

For example:

```text
/projects/?category=Python%20Projects&q=Python
```

The filters are applied to the same QuerySet, allowing users to narrow down project results.

### Empty Search Results

The application correctly handles searches that do not match any project.

---

# Current Status

The core Projects system is currently implemented and tested.

Completed functionality:

* Django project setup
* Core application
* Template structure
* Static structure
* Project database models
* Category model
* Technology model
* Project model
* Database relationships
* Django Admin management
* Project slugs
* Project list page
* Project detail page
* Project search
* Persian search support
* Category filtering
* Combined search and category filtering
* Empty search result handling

The project is currently being developed incrementally as part of the CS50W Capstone process.

---

# Planned Features

The following features are planned for the next development stages:

* About Me section
* Skills section
* Learning Journey
* Certificates section
* Blog / Notes
* Tools section
* Authentication
* Private dashboard
* Content management
* JavaScript-based dynamic features
* Responsive frontend design
* Advanced styling and UI improvements
* Automated testing
* GitHub integration
* Deployment

---

# Installation

Installation and deployment instructions will be added after the development phase is completed.

For development, the project uses a Python virtual environment and Django.

---

# Development

The project is being developed incrementally, with each major stage tested before moving to the next stage.

The development process includes:

1. Backend development
2. Database design
3. Django views and URLs
4. Template development
5. Feature testing
6. JavaScript functionality
7. Frontend styling
8. Responsive design
9. Final testing
10. Deployment

---

# Future Goals

The long-term goal of Salar.dev is to become a complete personal developer hub where projects, technical skills, certificates, learning progress, notes, and other professional work can be organized in one place.

The current version focuses on building a strong and maintainable foundation before adding more advanced features.

---

# Author

**Salar**

Computer Engineering Student

CS50 Web Programming with Python and JavaScript
