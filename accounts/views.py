from django.contrib.auth.decorators import login_required
from django.shortcuts import render , redirect
from django.contrib.auth import login
from django.contrib.auth import logout
from .forms import LoginForm
from core.models import Project , Skill , Certificate , Post


def login_view(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
            
    return render(request, "accounts/login.html" ,{"form":form})

def logout_view(request):
    logout(request)
    return redirect("home")

@login_required
def dashboard(request):
    project_count = Project.objects.count()
    skill_count = Skill.objects.count()
    certificate_count = Certificate.objects.count()
    post_count = Post.objects.count()
    return render(request , "accounts/dashboard.html" , {
        "project_count":project_count , 
        "skill_count":skill_count , 
        "certificate_count":certificate_count ,
        "post_count":post_count
    })
