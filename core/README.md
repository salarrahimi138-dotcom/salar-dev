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

The project is being developed incrementally, with each feature implemented, tested, and committed before moving to the next stage.

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
* Created the base template structure.
* Prepared the foundation for future frontend development.

---

# Day 3 — Projects Backend

Completed:

## Database Models

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

---

## Database Relationships

Implemented:

* One Category can contain multiple Projects.
* One Project can use multiple Technologies.

Using:

* `ForeignKey`
* `ManyToManyField`

---

## Project Slugs

Added a unique slug field to projects to create clean and readable project detail URLs.

Example:

```text
/projects/salar-dev/


# Day 4 — Projects Frontend and Filtering

Completed:

## Projects Frontend

Created the projects list page and connected it with the database.

The projects page displays:

* Project title
* Short description
* Category
* Technologies
* GitHub link
* Demo link

---

## Project Detail Page

Created individual project pages using project slugs.

The detail page displays:

* Project title
* Image
* Short description
* Full description
* Category
* Technologies
* GitHub link
* Demo link

---

## Search and Filtering

Implemented project search and category filtering.

Features:

* Search projects by title, short description, and description
* Case-insensitive search
* Persian text search support
* Filter projects by category
* Combine search and category filters

Search and filtering are implemented using Django ORM and `Q` objects.


# Day 5 — Home and About Pages

Completed:

## About Page

Created the About page and connected it to the website structure.

Implemented:

* About view
* About URL route
* About template
* Base template inheritance

---

## Dynamic Homepage

Converted the homepage from a static page into a dynamic page.

Implemented:

* Loading featured projects from the database
* Displaying projects dynamically on the homepage
* Connecting Django views with templates

---

## Featured Projects Section

Added a featured projects section to the homepage.

Displayed information:

* Project title
* Project link
* Short description
* Category
* Technologies

Featured projects are loaded dynamically using Django ORM.