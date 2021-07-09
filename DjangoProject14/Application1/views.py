from django.shortcuts import render
from .forms import StudentRegistration
# Create your views here.

def showFormData(request):
    if request.method == 'POST':
        formObj = StudentRegistration(request.POST)
        if formObj.is_valid(): #(is_valid) method will only run if the complete form is validated
            print("ye post hai",formObj)
            print(formObj.cleaned_data) # this will return cleaned data in dictionary  
            print("Name :", formObj.cleaned_data['name']) # this will return the value of specified field
            print("Email :", formObj.cleaned_data['email'])
            
            # this is not good, because the form can be filled multiple 
            formObj = StudentRegistration() # this will make the fields empty after we press submit
    else:
        formObj = StudentRegistration(auto_id = True, label_suffix = '-')
        print(formObj)
    return render(request, 'Application1/UserRegistration.html', {'form' : formObj})