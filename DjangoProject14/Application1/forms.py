from django import forms
from django.forms.widgets import PasswordInput, Widget

class StudentRegistration(forms.Form):
    name = forms.CharField(label='Student Name' ,label_suffix =':')
    email = forms.EmailField(help_text = 'Limit 20 character')
    password = forms.CharField(widget = PasswordInput) # (more widgets : HiddenInput, TextArea, FileInput, checkbox)
    