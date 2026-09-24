from django import forms
from django.contrib.auth.forms import AuthenticationForm
from core.models import Skill


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