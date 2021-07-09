from django.shortcuts import render
from .forms import StudentRegistration
# Create your views here.

def showFormData(request):
    formObj = StudentRegistration()
    return render(request, 'Application1/UserRegistration.html', {'form' : formObj})