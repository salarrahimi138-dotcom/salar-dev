from django.shortcuts import render

from .models import Project

def home(request):
    return render(request , "core/home.html")


def projects(request):
    projects= Project.objects.all()
    return render(request , "core/projects.html" , {"projects": projects})