from django import forms
from django.forms import fields
from .models import User

class ModelRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'password']