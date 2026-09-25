from django import forms
from django.contrib.auth.forms import AuthenticationForm
from core.models import Skill  , Project


class LoginForm(AuthenticationForm):
    pass


class SkillForm(forms.ModelForm):

    class Meta:
        model = Skill
        fields = [
            "name",
            "category",
            "proficiency",
        ]
        
        
class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = [
                 
                "title",
                "category" ,
                "slug" , 
                "short_description" ,
                "description" ,
                "technologies" ,
                "github_url" , 
                "demo_url" ,
                "image" ,
                "featured"
        ]