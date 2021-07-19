from django.shortcuts import render
from .models import Student
from django.db.models import Avg, Sum, Min, Max, Count
# Create your views here.

# we can limit QuerySet in djangousing slicing
def home(request):
    # student_data = Student.objects.all()[:5]
    # student_data = Student.objects.all()[2:]
    student_data = Student.objects.all()[::2]
    
    print("DATA :", student_data)
    print()
    # print("SQL Query :",student_data.query)

    return render(request, 'Application1/home.html',{'students': student_data})