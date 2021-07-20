from django.shortcuts import render
from .models import ExamCenter, Student
# Create your views here.

def home(request):
    exam_data = ExamCenter.objects.all()
    student_data = Student.objects.all()
    return render(request, 'School/home.html', {'students':student_data, 'centers':exam_data})