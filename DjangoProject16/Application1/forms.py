from django import forms
from .models import User

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User

        # fields = ['name','email','password']
        fields = '__all__' # takes all the fields of model class in specified sequence