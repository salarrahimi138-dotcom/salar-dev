from django.urls import path

from .import views

urlpatterns=[
    
    path("" , views.home , name="home") , 
    
    path("projects/" , views.projects , name="projects"),
    
    path("projects/<slug:slug>/" , views.projects_view , name="projects_view") ,
    
    path("about/" , views.about , name="about"),
    
    path("skills/" ,views.view_skill , name="skills" ),
    
    path("learning/" , views.learning , name="learning"),
    
    path("certificates/" , views.certificates, name="certificate") ,
    
    path("blog/" , views.blog , name="blog"),
    
    path("blog/<slug:slug>/", views.blog_detail, name="blog_detail"),
    
    path("search/", views.search, name="search"),
    
    path("test-403/", views.test_403, name="test_403"),
    path("test-500/", views.test_500, name="test_500"),
]