from django.shortcuts import render
from .models import Student
# Create your views here.

def home(request):
    student_data = Student.objects.all()
    # student_data = Student.objects.filter(city__exact ='Indore') # Case sensetive
    # student_data = Student.objects.filter(city__iexact ='indore') # Case in-sensetive
    # student_data = Student.objects.filter(name__contains ='s') # returns a query set for the condition
    # student_data = Student.objects.filter(id__in =[1,4,6]) # will return all the fields with ids = 1,4,6
    # student_data = Student.objects.filter(marks__in =[85]) # will return all the fields with marks = 85
    # student_data = Student.objects.filter(marks__gt =80) # will return all the fields with marks greater than 80 (marks>80)
    # student_data = Student.objects.filter(marks__gte =80) # will return all the fields with marks greater than equla to 80 (marks >= 80)
    # student_data = Student.objects.filter(marks__lt =80) # will return all the fields with marks less than 80 (marks < 80)
    # student_data = Student.objects.filter(marks__lte =80) # will return all the fields with marks less than equla to 80 (marks <= 80)
    # student_data = Student.objects.filter(pass_date__range =('2021-04-01', '2021-04-07')) # will return all the fields within the range
    
### NOTE : We can also use multiple lookups at once
# student_data = Student.objects.filter(admdatetime__year__lt =2021)


#### More field lookups(__startswith, __istartswith, __endswith, __iendswith, __date, __time, __month, __day, __week_day, __quarter, __hour, __minute, __second)



    print("DATA :", student_data)
    print()
    print("SQL Query :",student_data.query)

    return render(request, 'Application1/home.html', {'students' : student_data})