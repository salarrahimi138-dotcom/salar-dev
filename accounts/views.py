from django.contrib.auth.decorators import login_required
from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.auth import login
from django.contrib.auth import logout
from .forms import LoginForm , SkillForm , ProjectForm , CertificateForm , LearningJourneyForm , PostForm
from core.models import Project , Skill , Certificate , Post ,LearningJourney , DashboardIcon
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
    icons = DashboardIcon.objects.all().order_by("display_order")
    learning_count = LearningJourney.objects.count()
    return render(request , "accounts/dashboard.html" , {
        "project_count":project_count , 
        "skill_count":skill_count , 
        "certificate_count":certificate_count ,
        "post_count":post_count,
        "icons": icons,
        "learning_count": learning_count,
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
    
@login_required
@user_passes_test(is_admin)
def dashboard_project_create(request):

    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect("dashboard_projects")

    else:
        form = ProjectForm()

    return render(request, "accounts/dashboard_project_create.html", {
        "form": form
    })
    
@login_required
@user_passes_test(is_admin)
def dashboard_project_update(request, id):
    project = get_object_or_404(Project, id=id)
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect("dashboard_projects")
    else:
        form = ProjectForm(instance=project)
    return render(request, "accounts/dashboard_project_update.html", {
    "form": form
    })
    
    
@login_required
@user_passes_test(is_admin)
def dashboard_project_delete(request, id):
    project = get_object_or_404(Project, id=id)
    if request.method == "POST":
        project.delete()
        return redirect("dashboard_projects")
    return render(request, "accounts/dashboard_project_delete.html", {
    "project": project
})
    
    
@login_required
@user_passes_test(is_admin)
def dashboard_certificate_create(request):

    if request.method == "POST":
        form = CertificateForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect("dashboard_certificates")

    else:
        form = CertificateForm()

    return render(request, "accounts/dashboard_certificate_create.html", {
        "form": form
    })
    
@login_required
@user_passes_test(is_admin)
def dashboard_certificate_update(request, id):
    certificate = get_object_or_404(Certificate, id=id)
    if request.method == "POST":
        form = CertificateForm(request.POST, request.FILES, instance=certificate)
        if form.is_valid():
            form.save()
            return redirect("dashboard_certificates")
    else:
        form = CertificateForm(instance=certificate)
    return render(request, "accounts/dashboard_certificate_update.html", {
    "form": form
    })
    
    
@login_required
@user_passes_test(is_admin)
def dashboard_certificate_delete(request, id):
    certificate = get_object_or_404(Certificate, id=id)
    if request.method == "POST":
        certificate.delete()
        return redirect("dashboard_certificates")
    return render(request, "accounts/dashboard_certificate_delete.html", {
    "certificate": certificate
})
    
    
    
    
@login_required
@user_passes_test(is_admin)
def dashboard_learningjourney_create(request):

    if request.method == "POST":
        form = LearningJourneyForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("dashboard_learningjourneys")

    else:
        form = LearningJourneyForm()

    return render(request, "accounts/dashboard_learningjourney_create.html", {
        "form": form
    })
    
@login_required
@user_passes_test(is_admin)
def dashboard_learningjourney_update(request, id):
    learningjourney = get_object_or_404(LearningJourney, id=id)
    if request.method == "POST":
        form = LearningJourneyForm(request.POST , instance=learningjourney)
        if form.is_valid():
            form.save()
            return redirect("dashboard_learningjourneys")
    else:
        form = LearningJourneyForm(instance=learningjourney)
    return render(request, "accounts/dashboard_learningjourney_update.html", {
    "form": form
    })
    
    
@login_required
@user_passes_test(is_admin)
def dashboard_learningjourney_delete(request, id):
    learningjourney = get_object_or_404(LearningJourney, id=id)
    if request.method == "POST":
        learningjourney.delete()
        return redirect("dashboard_learningjourneys")
    return render(request, "accounts/dashboard_learningjourney_delete.html", {
    "learningjourney": learningjourney
})
    
@login_required
@user_passes_test(is_admin)
def dashboard_post_create(request):

    if request.method == "POST":
        form = PostForm(request.POST , request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            form.save_m2m()
            return redirect("dashboard_posts")
    else:
        form = PostForm()
    return render(request, "accounts/dashboard_post_create.html", {
        "form": form
    })
    
@login_required
@user_passes_test(is_admin)
def dashboard_post_update(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == "POST":
        form = PostForm(request.POST , request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect("dashboard_posts")
    else:
        form = PostForm(instance=post)
    return render(request, "accounts/dashboard_post_update.html", {
    "form": form
    })
    
    
@login_required
@user_passes_test(is_admin)
def dashboard_post_delete(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == "POST":
        post.delete()
        return redirect("dashboard_posts")
    return render(request, "accounts/dashboard_post_delete.html", {
        "post": post
    })