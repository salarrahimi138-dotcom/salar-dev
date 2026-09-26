from django.urls import path

from . import views


urlpatterns = [
    
path("login/", views.login_view, name="login"),
path("logout/", views.logout_view, name="logout"),
path("dashboard/", views.dashboard, name="dashboard"),
path("dashboard/projects/", views.dashboard_projects, name="dashboard_projects"),
path("dashboard/skills/", views.dashboard_skills, name="dashboard_skills"),
path("dashboard/certificates/",views.dashboard_certificates,name="dashboard_certificates"),
path("dashboard/learning/", views.dashboard_learning, name="dashboard_learningjourneys"),
path("dashboard/posts/", views.dashboard_posts, name="dashboard_posts"),
path("dashboard/skills/create/",views.dashboard_skill_create,name="dashboard_skill_create"),
path("dashboard/skills/<int:id>/update/",views.dashboard_skill_update,name="dashboard_skill_update"),
path("dashboard/skills/<int:id>/delete/",views.dashboard_skill_delete,name="dashboard_skill_delete"),
path("dashboard/projects/create/",views.dashboard_project_create,name="dashboard_project_create"),
path("dashboard/projects/<int:id>/update/",views.dashboard_project_update,name="dashboard_project_update"),
path("dashboard/projects/<int:id>/delete/",views.dashboard_project_delete,name="dashboard_project_delete"),
path("dashboard/certificates/create/",views.dashboard_certificate_create,name="dashboard_certificate_create"),
path("dashboard/certificates/<int:id>/update/",views.dashboard_certificate_update,name="dashboard_certificate_update"),
path("dashboard/certificates/<int:id>/delete/",views.dashboard_certificate_delete,name="dashboard_certificate_delete"),
path("dashboard/learning/create/",views.dashboard_learningjourney_create,name="dashboard_learningjourney_create"),
path("dashboard/learning/<int:id>/update/",views.dashboard_learningjourney_update,name="dashboard_learningjourney_update"),
path("dashboard/learning/<int:id>/delete/",views.dashboard_learningjourney_delete,name="dashboard_learningjourney_delete"),
path("dashboard/posts/create/",views.dashboard_post_create,name="dashboard_post_create"),
path("dashboard/posts/<int:id>/update/",views.dashboard_post_update,name="dashboard_post_update"),
path("dashboard/posts/<int:id>/delete/",views.dashboard_post_delete,name="dashboard_post_delete"),
]