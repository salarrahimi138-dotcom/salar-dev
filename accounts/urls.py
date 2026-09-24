from django.urls import path

from . import views


urlpatterns = [
    
path("login/", views.login_view, name="login"),
path("logout/", views.logout_view, name="logout"),
path("dashboard/", views.dashboard, name="dashboard"),
path("dashboard/projects/", views.dashboard_projects, name="dashboard_projects"),
path("dashboard/skills/", views.dashboard_skills, name="dashboard_skills"),
path("dashboard/certificates/",views.dashboard_certificates,name="dashboard_certificates"),
path("dashboard/learning/", views.dashboard_learning, name="dashboard_learning"),
path("dashboard/posts/", views.dashboard_posts, name="dashboard_posts"),
path("dashboard/skills/create/",views.dashboard_skill_create,name="dashboard_skill_create"),
path("dashboard/skills/<int:id>/update/",views.dashboard_skill_update,name="dashboard_skill_update"),
path("dashboard/skills/<int:id>/delete/",views.dashboard_skill_delete,name="dashboard_skill_delete"),
]