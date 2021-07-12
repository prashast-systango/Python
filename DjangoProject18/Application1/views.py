from django.shortcuts import render
# from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
# Create your views here.

def sign_up(request):
    if request.method == 'POST':
        formObj = SignUpForm(request.POST)
        if formObj.is_valid():
            formObj.save()
    else:
        formObj = SignUpForm()
    return render(request, 'Application1/signup.html', {'form':formObj})