from django.shortcuts import render , get_object_or_404

from .models import Project ,Category ,Skill , LearningJourney , Certificate , Post

from django.db.models import Q

from django.core.exceptions import PermissionDenied

def home(request): 
    
    projects = Project.objects.filter(featured=True)
    skills = Skill.objects.all()[:6]
    learning = LearningJourney.objects.all().order_by("display_order")[:4]
    return render(request , "core/home.html" , {"projects":projects , "skills": skills , "learning": learning })


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

def search(request):
    query = request.GET.get("q")
    projects = []
    posts = []
    skills = []
    learning = []
    certificates = []
    if  query :
        projects = Project.objects.filter(
            Q(title__icontains=query) | 
            Q(short_description__icontains=query) | 
            Q(description__icontains=query) |
            Q(technologies__name__icontains=query)).distinct()
        posts = Post.objects.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(tags__name__icontains=query),
            status="published").distinct()
        skills = Skill.objects.filter(
            Q(name__icontains=query) |
            Q(category__name__icontains=query)).distinct()
        learning = LearningJourney.objects.filter(
            Q(title__icontains=query) |
            Q(route_title__icontains=query) |
            Q(provider__icontains=query) |
            Q(explanation__icontains=query) |
            Q(skill__name__icontains=query)).distinct()
        certificates = Certificate.objects.filter(
            Q(title__icontains=query) |
            Q(provider__icontains=query) |
               Q(description__icontains=query)).distinct()

            
    return render(request , "core/search_results.html" , {
        "query" : query ,
        "projects": projects,
        "posts": posts,
        "skills": skills,
        "learning": learning,
        "certificates": certificates,})
    
def test_403(request):
    raise PermissionDenied


def test_500(request):
    x = 1 / 0