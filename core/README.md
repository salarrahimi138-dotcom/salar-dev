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

---

# Day 6 — Skills and Learning Journey

Completed:

## Skills System

Created a structured skill management system for the developer portfolio.

Implemented:

* Skill categories
* Individual skills
* Skill proficiency levels
* Dynamic skill display from the database

---

## Database Models

Created the following models:

### SkillCategory

Used to organize skills into different groups.

Examples:

* Backend
* Frontend
* Database
* Tools

Fields:

* `name`

---

### Skill

Stores technical skills and their proficiency levels.

Fields:

* `name`
* `category`
* `proficiency`

Database relationship:

* One SkillCategory can contain multiple Skills.
* Each Skill belongs to one SkillCategory.

Using:

* `ForeignKey`

---

## Skills Admin Management

Added Skills and Skill Categories to Django Admin.

Implemented:

* Creating skill categories
* Adding skills
* Managing proficiency levels
* Managing portfolio skills through Django Admin

---

## Skills Page

Created a dynamic skills page.

Route:


# Day 7 — Learning Journey and Certificates System

Completed:

## Learning Journey System

Created a structured system to display the developer learning path and educational progress.

Implemented:

* Learning journey database model
* Learning progress status management
* Dynamic learning journey page
* Django Admin management

---

## Database Model

Created:

### LearningJourney

Used to store educational progress and learning milestones.

Fields:

* `title`
* `skill`
* `route_title`
* `provider`
* `status`
* `explanation`
* `display_order`

---

## Learning Journey Features

Implemented:

* Display learning courses and milestones dynamically
* Show related skills
* Display course provider
* Display learning status:

  * Completed
  * In Progress
  * Planned

Learning items are ordered using:

```python
display_order
```

---

# Day 8 — Certificates System and Portfolio Expansion

Completed:

## Certificates Management System

Added a complete certificate management section to the developer portfolio.

Implemented:

* Certificate database model
* Certificate management through Django Admin
* Dynamic certificate display page
* Certificate images support
* External certificate links support

---

## Database Model

Created:

### Certificate

Used to store professional certificates and achievements.

Fields:

* `title`
* `provider`
* `issue_date`
* `image`
* `description`
* `certificate_url`
* `display_order`

---

## Certificate Features

Implemented:

* Display certificate title
* Display certificate provider
* Display issue date
* Display certificate description
* Support certificate image upload
* Support external certificate verification links

---

## Django Admin Improvements

Updated Django Admin to manage:

* Projects
* Skills
* Learning Journey
* Certificates

The admin panel now works as a content management system for updating portfolio information without modifying code.

---

## Template Integration

Created dynamic templates for:

* Learning Journey page
* Certificates page

Connected templates with Django views and database queries.

---

## Current Project Structure

The portfolio currently includes:

* Home page
* About page
* Projects section
* Project search and filtering
* Skills section
* Learning Journey section
* Certificates section

---

## Upcoming Development

Future steps:

* Connect all website sections through navigation links
* Improve website security and increase application safety
* Add authentication and private dashboard
* Add content management improvements
* Implement JavaScript interactive features
* Add responsive professional UI design
* Deploy the application online

---

## Security Improvements (Planned)

Security enhancements will include:

* Authentication protection
* Permission management
* Secure form handling
* Input validation
* Protection against common web vulnerabilities
* Production security configuration

---

# Day 9 — Blog / Notes System

Completed:

## Blog Content Management System

Created a dynamic blog and notes system for sharing development experiences, learning progress, and technical articles.

Implemented:

* Blog post database model
* Blog categories
* Tag management system
* Post status management
* Dynamic blog list page
* Blog detail pages using slugs
* Django Admin content management

---

## Database Models

Created:

### BlogCategory

Used to organize blog posts into different topics.

Examples:

* Django
* Python
* Cyber Security
* Web Development

Fields:

* `name`

---

### Tag

Used to add multiple labels to blog posts.

Examples:

* Django
* Python
* CS50
* Programming

Fields:

* `name`

Database relationship:

* One post can contain multiple tags.
* One tag can be used by multiple posts.

Using:

* `ManyToManyField`

---

### Post

Stores blog article information.

Fields:

* `title`
* `author`
* `category`
* `tags`
* `image`
* `slug`
* `content`
* `status`
* `created_at`
* `updated_at`

Database relationships:

* Each post belongs to one blog category.
* Each post can have multiple tags.
* Each post has an author.

Using:

* `ForeignKey`
* `ManyToManyField`

---

## Blog Features

Implemented:

* Display published blog posts dynamically
* Create clean blog URLs using slugs
* Blog list page
* Individual blog detail pages
* Display article author
* Display categories
* Display tags
* Support article images
* Show creation and update dates

---

## Blog Filtering and Status Management

Implemented post status management:

Available statuses:

* Draft
* Published
* Archived

Only published articles are displayed on the public blog page.

Implemented using Django ORM filtering:


Post.objects.filter(status="published")



# Day 10 — Authentication and Private Dashboard System

Completed:

## User Authentication System

Implemented a complete authentication foundation for the portfolio management area.

Added:

* User login system
* User logout system
* Protected dashboard access
* Authentication-based navigation

Implemented using Django authentication features:

* Django built-in User model
* Authentication views
* Login form handling
* Session-based user authentication

---

## Login System

Created a custom login page for administrators.

Features:

* Username and password authentication
* Login form validation
* Redirect users after successful login
* Display login page using Django templates

Implemented:

* `LoginForm`
* Login view
* Login template

---

## Logout System

Added logout functionality.

Features:

* Secure user logout
* Session termination
* Redirect user back to homepage after logout

---

## Private Dashboard

Created a protected dashboard page for managing portfolio information.

Dashboard access is restricted using:

```python
@login_required
```

Only authenticated users can access the dashboard.

---

## Dashboard Statistics

Implemented dynamic statistics display from the database.

Dashboard currently displays:

* Total projects count
* Total skills count
* Total certificates count
* Total blog posts count

Data is retrieved dynamically using Django ORM:

```python
Project.objects.count()
Skill.objects.count()
Certificate.objects.count()
Post.objects.count()
```

---

## Dashboard Template

Created a dashboard interface connected with the base template.

Implemented:

* Template inheritance
* Dynamic data rendering
* Display current logged-in username
* Portfolio statistics section

Displayed information:

* Projects
* Skills
* Certificates
* Posts
* Logged-in user information

---

## Authentication Structure

Current authentication flow:

```
User
 |
 |-- Login Page
 |
 |-- Authentication
 |
 |-- Dashboard
 |
 |-- Portfolio Management Area
```

---

## Current Project Progress After Day 10

The portfolio now includes:

* Home page
* About page
* Projects system
* Project search and filtering
* Skills system
* Learning Journey system
* Certificates system
* Blog system
* Authentication system
* Private dashboard
* Portfolio statistics dashboard

---

## Upcoming Development

Next steps:

* Create management pages for portfolio content
* Add dashboard links to different management sections
* Connect all website pages through navigation
* Add professional UI design and CSS improvements
* Implement JavaScript interactive features
* Improve security and permissions
* Prepare deployment configuration

---

# Day 11 — Dashboard Content Management System

Completed:

## Custom Portfolio Management Dashboard

Expanded the private dashboard into a custom content management area for managing portfolio data.

The goal of this system is to allow the administrator to manage website content directly from the portfolio dashboard instead of relying only on Django Admin.

Implemented:

* Dashboard management sections
* Custom management pages
* Admin-only access control
* CRUD foundation for portfolio content

---

## Dashboard Management Sections

Created management pages for:

* Projects
* Skills
* Certificates
* Learning Journey
* Blog Posts

Each section has its own dashboard route and displays related database content dynamically.

---

## Permission Management

Added permission protection for dashboard management pages.

Implemented using:

```python
@login_required
@user_passes_test(is_admin)
```

Only authenticated staff users can access the management area.

This prevents unauthorized users from modifying portfolio content.

---

# Skills Management CRUD

Completed full CRUD functionality for Skills.

Implemented:

## Skill List

Created a dashboard page to display all skills.

Displayed information:

* Skill name
* Skill category
* Proficiency level
* Edit action
* Delete action

---

## Create Skill

Added a custom skill creation form.

Features:

* Create new skills from dashboard
* Validate submitted data
* Save skills directly to database
* Redirect back to skill management page

Implemented using:

* Django Forms
* ModelForm
* POST request handling

---

## Update Skill

Added skill editing functionality.

Features:

* Load existing skill data
* Display current values in form
* Update database records
* Save changes through dashboard

Implemented using:

```python
SkillForm(instance=skill)
```

---

## Delete Skill

Added skill deletion functionality.

Features:

* Confirmation page before deletion
* Secure POST-based deletion
* Remove selected skill from database
* Redirect back to skill list

Implemented using:

```python
skill.delete()
```

---

## Current Dashboard Flow

The current management flow:

```
Login
  |
  |
Dashboard
  |
  |
Management Sections
  |
  |
Create / Update / Delete Content
  |
  |
Database Update
```

---

## Current Project Progress After Day 11

The portfolio now includes:

* Home page
* About page
* Projects system
* Project search and filtering
* Skills system
* Learning Journey system
* Certificates system
* Blog system
* Authentication system
* Private dashboard
* Dashboard statistics
* Custom content management system
* Skills CRUD management

---

## Next Development Steps

Next steps:

* Complete CRUD management for Projects
* Add CRUD management for Certificates
* Add CRUD management for Learning Journey
* Add CRUD management for Blog Posts
* Improve dashboard navigation
* Implement JavaScript features
* Add professional UI design and responsive layout
* Final security review and deployment preparation

