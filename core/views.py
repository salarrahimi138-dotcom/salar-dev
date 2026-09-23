from django.shortcuts import render , get_object_or_404

from .models import Project ,Category ,Skill , LearningJourney , Certificate , Post

from django.db.models import Q

def home(request): 
    
    projects=Project.objects.filter(
      featured=True
    )
    return render(request , "core/home.html" , {"projects":projects})


def projects(request):
    q = request.GET.get("q")
    category = request.GET.get("category")
    projects= Project.objects.all()
    if category:
        projects = projects.filter(
        category__name__iexact=category
    )
    
    categories = Category.objects.all()
    if q:
        projects = projects.filter(
        Q(title__icontains=q) |
        Q(short_description__icontains=q) |
        Q(description__icontains=q)
    )
    return render(request , "core/projects.html" , {
        "projects": projects ,
        "categories":categories})


def projects_view( request , slug):
    project=get_object_or_404(Project , slug=slug)
    return render(request , "core/projects_view.html" , {"project":project} )


def about(request):
    return render(request , "core/about.html")

def view_skill(request):
      skills = Skill.objects.all().order_by("name")
      return render(request ,"core/skills.html" , {"skills":skills})
  
  
def learning(request):
    learning = LearningJourney.objects.all().order_by("display_order")
    return render(request , "core/learning.html" , {"learning":learning})


def certificates(request):
    certificates = Certificate.objects.all().order_by("display_order")
    return render(request , "core/certificates.html" , {"certificates":certificates})
def blog(request):
    
    posts =  Post.objects.filter(
        status="published"
    ).order_by("-created_at")
    return render(request , "core/blog.html" , {
        "posts":posts ,
        
    })
    
def blog_detail(request , slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request , "core/blog_detail.html" ,{ "post":post} )