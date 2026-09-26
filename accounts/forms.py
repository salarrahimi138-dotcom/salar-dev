from django import forms
from django.contrib.auth.forms import AuthenticationForm
from core.models import Skill  , Project , Certificate , LearningJourney , Post


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
        
        
class CertificateForm(forms.ModelForm):
    class Meta:
        model = Certificate
        fields = [
             "title",
             "provider" ,
             "issue_date" ,
             "image" ,
             "description" ,
             "certificate_url" ,
             "display_order"
        ]
        
        
class LearningJourneyForm(forms.ModelForm):
    class Meta:
        model = LearningJourney
        fields = [
                "title",
                "skill" ,
                "route_title" ,
                "provider" ,
                "status",
                "explanation" ,
                "display_order" 
        ]
        
        
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields =[ 
            "title" ,
            "category" ,
            "tags" ,
            "image" ,
            "slug" ,
            "content" ,
            "status"
        ]