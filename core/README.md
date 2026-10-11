# Salar.dev — Personal Developer Hub

## Overview

Salar.dev is my final project (Capstone) for **CS50's Web Programming with Python and JavaScript**.

It is a personal developer platform built with Django. The goal of this project is to create a professional developer identity where I can introduce myself, showcase my projects, display my skills and certificates, share my learning journey, and publish technical blog posts.

Unlike a simple static portfolio website, Salar.dev is a complete full-stack web application. All content is stored dynamically using Django models and can be managed through a custom dashboard without manually editing source code.

The project has two main parts:

- **Public Website:** Visitors can explore my projects, skills, certificates, learning journey, and blog content.
- **Private Dashboard:** A custom management system where I can create, edit, and delete website content.


---

# Distinctiveness and Complexity

Salar.dev is different from previous CS50W projects because it is not an e-commerce website, social network, email client, or encyclopedia.

The idea behind this project was to build a personal developer management platform that combines a professional portfolio website with a custom content management system.

The complexity of this project comes from combining several different systems:

- A complete Django backend architecture
- Multiple related database models
- Dynamic portfolio content
- Authentication system
- User profiles
- Custom dashboard
- CRUD management system
- Responsive frontend design
- JavaScript interactions
- Modern UI components


The project includes several database models:

- Projects
- Project categories
- Technologies
- Skills
- Certificates
- Learning Journey
- Blog categories
- Blog posts
- User profiles


The dashboard allows managing website content without modifying the source code. It includes:

- Statistics overview
- Project management
- Skills management
- Certificate management
- Learning Journey management
- Blog management


Each management section supports full CRUD functionality:

- Create
- Read
- Update
- Delete


---

# Features

## Public Website

The public side includes:

- Home page
- About page
- Projects page
- Project details page
- Skills page
- Certificates page
- Learning Journey page
- Blog list
- Blog details
- Search system


## Dashboard

The custom dashboard includes:

- Content statistics
- Dynamic dashboard icons
- Project CRUD
- Skills CRUD
- Certificates CRUD
- Learning Journey CRUD
- Blog CRUD


## Authentication and Profile

The account system includes:

- Signup
- Login
- Logout
- Automatic profile creation
- Profile editing
- Profile image upload


## Additional Features

The project also includes:

- Dark/light theme
- LocalStorage theme saving
- Responsive design
- Custom loading page
- Custom animations
- Search functionality
- Custom 404, 403, and 500 error pages


---

# Technologies

## Backend

- Python
- Django
- SQLite


## Frontend

- HTML
- CSS
- JavaScript


## Resources Used

During development, I used:

- Django Documentation
- MDN Web Docs
- Technical articles
- Google searches and research
- Professional website examples


For UI inspiration:

- Uiverse.io
- 3dicons.so


---

# Design and UI Development

The design of Salar.dev was created with custom CSS.

I used:

- CSS Variables
- Flexbox
- CSS Grid
- Media Queries
- Custom animations
- Responsive layouts


The goal was to create a modern developer portfolio experience instead of a basic template website.
# Design Resources and Inspiration

During the frontend development process, I researched many modern website designs and UI patterns to improve the quality of Salar.dev.

I used **Uiverse.io** as a source of inspiration for some UI elements such as:

- Buttons
- Cards
- Animations
- Interactive components

I studied how these components were built and adapted the ideas into my own design instead of directly copying complete sections.

For dashboard icons, I used resources from **3dicons.so** to create a more modern and professional dashboard appearance.


---

# Learning Process and Research

During the development of Salar.dev, I learned many parts of web development through independent research, practice, and problem solving.

Instead of only following tutorials, I tried to understand each feature by building it, facing problems, searching for solutions, and improving the implementation.

Whenever I faced a challenge, I used Google searches, documentation, technical articles, and examples from other developers to understand the concepts and find better solutions.

For frontend development, especially CSS, I improved my skills by researching professional website designs, studying modern CSS techniques, and practicing:

- Layout design
- Responsive design
- Animations
- Components
- Theme systems
- Modern UI patterns


For Django development, I learned by:

- Reading Django documentation
- Studying examples
- Understanding models, views, templates, and forms
- Testing different approaches
- Debugging problems during development


This process helped me move from simply writing code by following instructions to independently designing, developing, debugging, and improving a complete full-stack application.


---

# Development Journey

The development of Salar.dev was completed step by step.

## Phase 1 — Project Planning and Django Setup

At the beginning, I planned the structure of the application and created the Django project.

Tasks completed:

- Django project setup
- Application structure design
- Database planning
- Static and media configuration


## Phase 2 — Database and Backend Development

I designed the database structure and created the required Django models.

Implemented models for:

- Projects
- Categories
- Technologies
- Skills
- Certificates
- Learning Journey
- Blog system
- User profiles


I also created the required relationships between models and prepared the backend structure.


## Phase 3 — Public Website Development

I created the main portfolio pages:

- Home
- About
- Projects
- Skills
- Certificates
- Learning Journey
- Blog


The pages were built dynamically using Django templates and database data.


## Phase 4 — Custom Dashboard Development

A custom dashboard was developed to manage the website content.

Features added:

- Dashboard statistics
- Management cards
- CRUD operations
- Content editing system


This allows the website owner to update content without changing the source code.


## Phase 5 — Authentication and Profile System

The authentication system was implemented.

Added:

- Signup
- Login
- Logout
- Profile model
- Profile image upload
- Profile editing page


Users can manage their personal information through the profile section.


## Phase 6 — Frontend Polish and User Experience

The final stage focused on improving the user interface.

Implemented:

- Responsive design
- Dark/light theme
- Animations
- Loading screen
- Search improvements
- Error pages
- UI improvements
- Mobile compatibility


The final result is a complete personal developer platform with both backend management and a modern frontend experience.


---

# File Structure

The main structure of the project:
# Files and Their Purpose

Important files and folders:

- `manage.py`
  - Django command-line utility used to manage the project.

- `requirements.txt`
  - Contains all Python packages required to run the project.

- `settings.py`
  - Contains Django configuration including:
    - Installed applications
    - Database settings
    - Static files
    - Media files
    - Authentication settings

- `urls.py`
  - Handles the main URL routing of the project.

- `models.py`
  - Contains all database models including:
    - Projects
    - Skills
    - Certificates
    - Learning Journey
    - Blog
    - Profile

- `views.py`
  - Contains the application logic for:
    - Public pages
    - Dashboard
    - Authentication
    - Profile system
    - Search system

- `forms.py`
  - Contains Django forms for:
    - Signup
    - Profile editing
    - CRUD operations

- `templates/`
  - Contains all HTML templates.

Important templates:

- `base.html`
  - Main layout shared between all pages.

- `components/navbar.html`
  - Website navigation.

- Dashboard templates
  - Management interface.

- Account templates
  - Login, signup, and profile pages.

- Error templates
  - 404, 403, and 500 pages.


- `static/css/`
  - Contains all custom styles:
    - Layout
    - Components
    - Animations
    - Responsive design
    - Theme system


- `static/js/`
  - Contains JavaScript features:
    - Theme switching
    - UI interactions
    - Animations


- `static/images/`
  - Contains website images and dashboard icons.


- `media/`
  - Stores uploaded user profile images.



---

# How to Run the Project

1. Clone the repository:
