from django.db import models

from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Technology(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
class SkillCategory(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
class Project(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True , blank=True)
    short_description = models.TextField(max_length=300)
    description = models.TextField()
    technologies = models.ManyToManyField(Technology)
    github_url = models.URLField(blank=True)
    demo_url = models.URLField(blank=True)
    image = models.ImageField(blank=True)
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    
    
class Skill(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(SkillCategory , on_delete=models.CASCADE)
    proficiency = models.PositiveIntegerField()
    def __str__(self):
        return self.name


class LearningJourney(models.Model):
    title = models.CharField(max_length=50)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    route_title = models.TextField(max_length=200)
    provider = models.CharField(max_length=50)
    STATUS_CHOICES = [
        ("completed", "Completed"),
        ("progress", "In Progress"),
        ("planned", "Planned"),
    ]
    status = models.CharField(max_length=20 , choices=STATUS_CHOICES , default="planned")
    explanation = models.TextField(max_length=500 , blank=True)
    display_order = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.title

class Certificate(models.Model):
     title = models.CharField(max_length=50)
     provider = models.CharField(max_length=50)
     issue_date = models.DateField()
     image = models.ImageField(blank=True)
     description = models.TextField(max_length=200)
     certificate_url = models.URLField(blank=True)
     display_order = models.PositiveIntegerField(default=0)
    
     def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class BlogCategory(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
    
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    image = models.ImageField(blank=True)
    slug = models.SlugField(unique=True , blank=True)
    content = models.TextField()
    STATUS_CHOICES = [
    ("draft", "Draft"),
    ("published", "Published"),
    ("archived", "Archived"),
]
    status = models.CharField(
    max_length=20,
    choices=STATUS_CHOICES,
    default="draft"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

