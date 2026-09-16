from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Technology(models.Model):
    name=models.CharField(max_length=50)
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