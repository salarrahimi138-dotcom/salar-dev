# Salar.dev

## Personal Developer Portfolio

Salar.dev is a personal developer portfolio website built as the final project for CS50 Web Programming with Python and JavaScript.

The goal of this project is to create a professional platform to showcase my programming projects, skills, learning journey, certificates, and technical achievements.

---

# Distinctiveness and Complexity

Salar.dev is a personal portfolio platform and is different from previous CS50W projects such as Wiki, Commerce, Mail, and Network.

Unlike a simple CRUD application, this project focuses on creating a complete developer profile system with project management, technology relationships, categories, and future content management features.

The project uses Django as the backend framework and will include JavaScript features and responsive frontend design.

---

# Technologies Used

- Python
- Django
- HTML
- CSS
- JavaScript
- SQLite (development database)

---

# Project Progress

## Day 1 - Project Setup

Completed:

- Created Django project structure.
- Created the main application (`core`).
- Configured project settings.
- Created the first homepage view.
- Created base template structure.
- Initialized Git repository.

---

## Day 2 - Frontend Structure

Completed:

- Created template folders.
- Connected Django views with templates.
- Created homepage page.
- Added static file structure.
- Prepared the foundation for future frontend development.

---

## Day 3 - Projects System

Completed:

### Database Models

Created the following models:

## Category

Used to organize projects into different groups.

Fields:

- name


## Technology

Stores technologies used in projects.

Fields:

- name


## Project

Stores portfolio projects.

Fields:

- category
- title
- short description
- description
- technologies
- GitHub URL
- Demo URL
- Image
- Featured status
- Created date
- Updated date


### Relationships

Implemented:

- One Category can contain multiple Projects.
- One Project can have multiple Technologies.

Using:

- ForeignKey
- ManyToManyField


### Admin Panel

Configured Django Admin to manage projects.

Added:

- Project title display
- Category display
- Featured status
- Creation date


### Project Display

Created a projects page that displays:

- Project title
- Description
- Category
- Technologies
- GitHub link
- Demo link


---

# Current Status

The project foundation and project management system are completed.

Next steps:

- Create project detail pages.
- Improve frontend design.
- Add authentication and dashboard.
- Add learning journey section.
- Add blog/notes system.
- Make the website fully responsive.
- Deploy the final project.

---

# Installation

Coming soon.

---

# Author

Salar

CS50 Web Programming with Python and JavaScript