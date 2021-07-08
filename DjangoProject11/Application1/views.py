from django.shortcuts import render
from Application1.models import Student
# Create your views here.
def studentInfo(request):
    stud = Student.objects.all()
    return render(request, 'Application1/Student_Details.html', {'stu' : stud})