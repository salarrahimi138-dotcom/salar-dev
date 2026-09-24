from django.contrib.auth.decorators import login_required
from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.auth import login
from django.contrib.auth import logout
from .forms import LoginForm , SkillForm
from core.models import Project , Skill , Certificate , Post ,LearningJourney
from django.contrib.auth.decorators import user_passes_test

def is_admin(user):
    return user.is_staff

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
@user_passes_test(is_admin)
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


@login_required
@user_passes_test(is_admin)
def dashboard_projects(request):
    projects = Project.objects.all()
    return render(request , "accounts/dashboard_projects.html" , {
        "projects":projects
    })
    
@login_required
@user_passes_test(is_admin)
def dashboard_skills(request):
    skills = Skill.objects.all()
    return render(request , "accounts/dashboard_skills.html" , {
        "skills":skills
    })
    
@login_required
@user_passes_test(is_admin)
def dashboard_certificates(request):
    certificates = Certificate.objects.all().order_by("display_order")
    return render(request, "accounts/dashboard_certificates.html", {
        "certificates": certificates
    })
    
    
@login_required
@user_passes_test(is_admin)
def dashboard_learning(request):
    learning_journeys = LearningJourney.objects.all().order_by("display_order")
    return render(request, "accounts/dashboard_learning.html", {
        "learning_journeys": learning_journeys
    })
    
    
@login_required
@user_passes_test(is_admin)
def dashboard_posts(request):
    posts = Post.objects.all().order_by("-created_at")
    return render(request, "accounts/dashboard_posts.html", {
        "posts": posts
    })
    
    
@login_required
@user_passes_test(is_admin)
def dashboard_skill_create(request):

    if request.method == "POST":
        form = SkillForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("dashboard_skills")

    else:
        form = SkillForm()

    return render(request, "accounts/dashboard_skill_create.html", {
        "form": form
    })
    
@login_required
@user_passes_test(is_admin)
def dashboard_skill_update(request, id):
    skill = get_object_or_404(Skill, id=id)
    if request.method == "POST":
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            return redirect("dashboard_skills")
    else:
        form = SkillForm(instance=skill)
    return render(request, "accounts/dashboard_skill_update.html", {
    "form": form
    })
    
    
@login_required
@user_passes_test(is_admin)
def dashboard_skill_delete(request, id):
    skill = get_object_or_404(Skill, id=id)
    if request.method == "POST":
        skill.delete()
        return redirect("dashboard_skills")
    return render(request, "accounts/dashboard_skill_delete.html", {
    "skill": skill
})