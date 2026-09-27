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

# Day 11 — Dashboard Content Management System (Continued)

## Project Management CRUD

Completed full CRUD functionality for Projects inside the custom dashboard management system.

The Project management section now allows the administrator to manage portfolio projects directly from the private dashboard without using Django Admin.

Implemented:

* Project management dashboard page
* Create project functionality
* Update project functionality
* Delete project functionality
* Project data management through custom forms
* Image upload support
* Project relationship management

---

## Project Form

Created a custom `ProjectForm` using Django ModelForm.

Managed project fields:

* `title`
* `category`
* `slug`
* `short_description`
* `description`
* `technologies`
* `github_url`
* `demo_url`
* `image`
* `featured`

The form is connected directly to the Project model and validates submitted project information before saving.

---

## Create Project

Implemented project creation from the dashboard.

Features:

* Add new portfolio projects
* Select project category
* Select multiple technologies
* Upload project images
* Add GitHub and demo links
* Mark projects as featured

Implemented using:

```python
ProjectForm()
```

and POST request handling.

---

## Update Project

Added project editing functionality.

Features:

* Load existing project information
* Modify project details
* Update database records
* Preserve project relationships

Implemented using:

```python
ProjectForm(instance=project)
```

---

## Delete Project

Added secure project deletion functionality.

Features:

* Confirmation page before deletion
* POST-based deletion
* Remove selected projects from database
* Redirect back to project management page

Implemented using:

```python
project.delete()
```

---

## Image Upload Handling

Added support for uploading project images through dashboard forms.

Implemented:

* `request.FILES` handling in views
* `multipart/form-data` form encoding
* ImageField support through Pillow

Example:

```python
form = ProjectForm(request.POST, request.FILES)
```

---

## Project CRUD Testing

The complete Project CRUD workflow was tested successfully.

Verified:

* Creating new projects ✅
* Displaying projects in dashboard ✅
* Updating project information ✅
* Deleting projects successfully ✅

The management flow now works as:

```
Dashboard
   |
   |
Projects Management
   |
   |
Create / Update / Delete
   |
   |
Database Update
```

---

# Current Project Progress After Day 11

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
* Projects CRUD management

---

# Remaining Day 11 Tasks

Next development steps:

* Add CRUD management for Certificates
* Add CRUD management for Learning Journey
* Add CRUD management for Blog Posts
* Improve dashboard navigation
* Implement JavaScript interactive features
* Create professional UI/CSS design
* Perform security review
* Prepare deployment configuration



# Day 11 — Dashboard Content Management System (Completed)

Completed the full custom portfolio management dashboard.

The dashboard was expanded into a complete content management system that allows the administrator to manage all major portfolio sections directly from the website without relying on Django Admin.

Implemented:

* Custom dashboard management interface
* Admin-only access control
* CRUD operations for portfolio content
* Database management through Django Forms
* Image upload support
* Content organization system

---

# Dashboard Management Sections

Created management systems for:

* Projects
* Skills
* Certificates
* Learning Journey
* Blog Posts

Each section has:

* List page
* Create page
* Update page
* Delete confirmation page

---

# Certificate Management CRUD

Completed full CRUD functionality for Certificates.

The certificate management section allows the administrator to manage professional achievements directly from the dashboard.

Implemented:

* Certificate management dashboard page
* Create certificate functionality
* Update certificate functionality
* Delete certificate functionality
* Certificate image upload support
* External certificate link support

---

## Certificate Form

Created a custom `CertificateForm` using Django ModelForm.

Managed certificate fields:

* `title`
* `provider`
* `issue_date`
* `image`
* `description`
* `certificate_url`
* `display_order`

The form validates and saves certificate information directly to the database.

---

## Certificate CRUD Workflow

Implemented:

### Create Certificate

Features:

* Add new certificates
* Upload certificate images
* Add verification links
* Organize certificate display order

---

### Update Certificate

Features:

* Edit existing certificate information
* Update certificate details
* Preserve database records

Implemented using:

```python
CertificateForm(instance=certificate)
```python
CertificateForm(instance=certificate)
```

---

### Delete Certificate

Added secure certificate deletion functionality.

Features:

* Confirmation page before deletion
* POST-based deletion request
* Remove selected certificates from database
* Redirect back to certificate management page

Implemented using:

```python
certificate.delete()
```

---

# Learning Journey Management CRUD

Completed full CRUD functionality for Learning Journey.

The learning journey management section allows the administrator to manage educational progress and learning milestones from the custom dashboard.

Implemented:

* Learning Journey management page
* Create learning item functionality
* Update learning item functionality
* Delete learning item functionality
* Skill relationship management
* Learning status management

---

## Learning Journey Form

Created a custom `LearningJourneyForm` using Django ModelForm.

Managed fields:

* `title`
* `skill`
* `route_title`
* `provider`
* `status`
* `explanation`
* `display_order`

The form validates and saves learning progress information directly into the database.

---

## Learning Journey CRUD Workflow

Implemented:

### Create Learning Journey

Features:

* Add new learning milestones
* Select related skills
* Define learning provider
* Set learning status
* Control display order

---

### Update Learning Journey

Features:

* Edit existing learning progress
* Update learning information
* Modify status and ordering

Implemented using:

```python
LearningJourneyForm(instance=learning)
```

---

### Delete Learning Journey

Features:

* Confirmation before deletion
* Secure POST-based deletion
* Remove selected learning records

Implemented using:

```python
learning.delete()
```

---

# Blog Post Management CRUD

Completed full CRUD functionality for Blog Posts.

The blog management section allows the administrator to manage technical articles and notes directly from the dashboard.

Implemented:

* Blog post management page
* Create blog posts
* Update blog posts
* Delete blog posts
* Category management
* Tag management
* Image upload support
* Draft and published status control

---

## Blog Post Form

Created a custom `PostForm` using Django ModelForm.

Managed fields:

* `title`
* `category`
* `tags`
* `image`
* `slug`
* `content`
* `status`

The form allows the administrator to create and manage technical articles from the private dashboard.

---

## Blog CRUD Workflow

Implemented:

### Create Post

Features:

* Create new articles
* Select blog category
* Add multiple tags
* Upload article images
* Save draft or publish articles

---

### Update Post

Features:

* Edit existing articles
* Update content
* Modify categories and tags
* Change publication status

Implemented using:

```python
PostForm(instance=post)
```

---

### Delete Post

Features:

* Confirmation page before deletion
* Secure deletion process
* Remove selected blog posts

Implemented using:

```python
post.delete()
```

---

# Dashboard Navigation Improvements

Improved dashboard structure to provide easier access to management sections.

Added management links for:

* Projects
* Skills
* Certificates
* Learning Journey
* Blog Posts

The dashboard now works as a complete portfolio content management system.

---

# Final Dashboard Architecture

Current management workflow:

```
User Login
    |
    |
Protected Dashboard
    |
    |
Content Management Sections
    |
    |
CRUD Operations
    |
    |
Database Update
    |
    |
Website Content Update
```

---

# Day 11 Final Project Status

After completing Day 11, Salar.dev includes:

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
* Projects CRUD
* Skills CRUD
* Certificates CRUD
* Learning Journey CRUD
* Blog Posts CRUD
* Image upload management

---

# Day 12 — Professional UI / CSS Design Phase

Started the professional frontend design phase of Salar.dev.

The goal of this phase is to transform the functional portfolio application into a modern, polished, and professional developer portfolio experience.

The focus of Day 12 is building a reusable design system and creating the foundation for a consistent user interface across all website pages.

---

# Design System Foundation

Completed the initial CSS architecture for the project.

Implemented:

* Global color system
* Typography system
* Spacing foundation
* Container system
* Global reset styles
* Reusable UI components
* Animation and transition system

---

# CSS Variables System

Created a centralized design token system using CSS variables.

Implemented variables for:

* Background colors
* Surface colors
* Card colors
* Border colors
* Text colors
* Primary brand colors
* Border radius
* Shadows
* Transitions
* Container width

Example categories:

```css
--color-bg
--color-surface
--color-card
--color-primary
--radius
--shadow
--transition
```

This allows future design changes to be managed from one central location.

---

# Global Layout Foundation

Implemented the main layout structure.

Completed:

* Global box sizing reset
* Body styling
* Container system
* Responsive width foundation
* Default typography rules
* Image behavior
* Link styling
* List reset

---

# Typography System

Created a consistent typography hierarchy.

Implemented styles for:

* Main headings
* Section headings
* Card titles
* Paragraph text
* Muted descriptions

Configured:

* Font weights
* Font sizes
* Line heights
* Text colors

---

# Button Component System

Created reusable button components.

Implemented:

## Primary Button

Features:

* Main action style
* Brand color background
* Hover animation
* Shadow effect

## Secondary Button

Features:

* Transparent design
* Border style
* Hover interaction

## Button States

Added:

* Hover state
* Active state
* Smooth transitions

---

# Icon System

Created reusable icon components.

Implemented:

## Icon Button

Features:

* Circular icon container
* Hover animation
* Border system
* Background interaction

---

## 3D Icon Wrapper

Created a reusable wrapper for 3D-style icons.

Implemented:

* Card background
* Rounded corners
* Shadow system
* Hover elevation effect

Used for future:

* Skills section
* Tools section
* Feature cards

---

# Card Component System

Created reusable card architecture for portfolio sections.

Implemented:

* Base card component
* Card image section
* Card content section
* Card header
* Card title
* Card subtitle
* Card footer

Features:

* Border system
* Shadow system
* Hover animation
* Image zoom effect

---

# Specialized Portfolio Cards

Created specific card styles for portfolio content.

Implemented:

## Project Card

Features:

* Project title styling
* Hover interaction
* Image animation

## Skill Card

Features:

* Centered layout
* Icon support
* Skill presentation structure

## Certificate Card

Features:

* Certificate image layout
* Provider information
* Date display
* External link styling

## Blog Card

Features:

* Article metadata
* Category display
* Date styling
* Content preview structure

## Learning Journey Card

Features:

* Learning status badge
* Provider information
* Educational timeline structure

---

# Tag and Badge System

Created reusable tag components.

Implemented:

* Default tags
* Primary tags
* Outline tags
* Category badges
* Status indicators

Features:

* Rounded pill design
* Hover effects
* Consistent color system

---

# Glass Card Component

Implemented modern glass-style UI components.

Features:

* Transparent background
* Blur effect
* Border system
* Shadow depth
* Hover animation

Used for future modern sections and dashboard improvements.

---

# Current Day 12 Progress

Completed:

* Design token system
* Global CSS foundation
* Button system
* Icon system
* 3D icon wrapper
* Card system
* Tag system
* Portfolio component foundation

---

# Next Day 12 Tasks

Continue professional UI development:

* Header and navigation system
* Hero section design
* Footer design
* Responsive layouts
* Mobile navigation
* Page section styling
* Final UI consistency improvements

The goal is to create a complete professional frontend design system for Salar.dev before final testing and deployment.
