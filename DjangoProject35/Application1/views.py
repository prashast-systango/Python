from django.shortcuts import render
from .models import Student
from django.db.models import Avg, Sum, Min, Max, Count
# Create your views here.

def home(request):
    student_data = Student.objects.all()
    average = student_data.aggregate(Avg('marks'))
    total = student_data.aggregate(Sum('marks'))
    minimum = student_data.aggregate(Min('marks'))
    maximum = student_data.aggregate(Max('marks'))
    count = student_data.aggregate(Count('marks'))

    context = {'students':student_data, 'average':average, 'total':total, 'minimum':minimum, 'maximum':maximum, 'count':count}

    print(average)
    print("DATA :", student_data)
    print()
    print("SQL Query :",student_data.query)

    return render(request, 'Application1/home.html', context)