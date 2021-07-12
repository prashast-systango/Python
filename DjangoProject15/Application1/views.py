from django.shortcuts import render
from .forms import ModelRegistration
from django.contrib import messages
# Create your views here.

def regi(request):
    if request.method == 'POST':
        formObj = ModelRegistration(request.POST)
        if formObj.is_valid():
            formObj.save()
            # can write like this also
            # messages.add_message(request, messages.SUCCESS, "Your account has been created !!!")
            messages.info(request, "Your account has been created !!!")
    else:
        formObj = ModelRegistration()
    return render(request, 'Application1/UserRegistration.html', {'form': formObj})
        
