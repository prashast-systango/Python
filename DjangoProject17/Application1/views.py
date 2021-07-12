from django.shortcuts import render
from .forms import TeacherRegistration, StudentRegistration
# Create your views here.

def student_form(request):
    if request.method == 'POST':
        formObj = StudentRegistration(request.POST)
        if formObj.is_valid():
            formObj.save()
    else:
        formObj = StudentRegistration()
    return render(request, 'Application1/student.html', {'form':formObj})    


def teacher_form(request):
    if request.method == 'POST':
        formObj = TeacherRegistration(request.POST)
        if formObj.is_valid():
            formObj.save()
    else:
        formObj = TeacherRegistration()
    return render(request, 'Application1/teacher.html', {'form':formObj})