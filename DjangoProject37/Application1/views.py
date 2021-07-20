from django.shortcuts import render
from .models import Student, Teacher, Constructor
# Create your views here.

def home(request):
    student_data = Student.objects.all()
    teacher_data = Teacher.objects.all()
    constructor_data = Constructor.objects.all()
    return render(request,'Application1/home.html',
    {'students':student_data, 'teachers':teacher_data, 'constructors':constructor_data})