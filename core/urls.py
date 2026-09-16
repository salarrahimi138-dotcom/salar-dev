from django.urls import path

from .import views

urlpatterns=[
    
    path("" , views.home , name="home") , 
    
    path("projects" , views.projects , name="projects"),
    
    path("projects/<slug:slug>" , views.projects_view , name="projects_view")
]