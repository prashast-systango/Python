from django.shortcuts import render
from .models import Student
# Create your views here.

def home(request):
    # student_data = Student.objects.get()


    student_data = Student.objects.all() # This returns a QuerySet, with all the data in student table
 
    # student_data = Student.objects.filter(roll_no=10700) # This returns a QuerySet for specified condition
 
    # student_data = Student.objects.exclude(roll_no=10700) # This returns a QuerySet with all the fields excluding the fields with specified condition

    # student_data = Student.objects.order_by('name') # returns a QuerySet in Ascending order according to specified field

    # student_data = Student.objects.order_by('-name') # returns a QuerySet in Descending order according to specified field

    # student_data = Student.objects.order_by('?') # returns a QuerySet in Random order

    # student_data = Student.objects.values() # returns a QuerySet, which holds a list of dictionaries for each field

    # student_data = Student.objects.values('name', 'city') # returns a QuerySet, which holds a list of dictionaries for specified columns

    # student_data = Student.objects.values_list(named=True) # returns a QuerySet, which holds a list of tuples for each field

    # using('alias')(This can be used when you are using more than one database)
    # student_data = Student.objects.using('default') # returns a QuerySet, which is an alias of the specified database

    
    #### Some more methods used in multiple tables(union, intersection, difference)(these methods are used with the above methods)
    #(eg: table1.objects.values_list().union(table2.objects.values_list()) )

    #### Operators which return QuerySet( AND(&), OR(|) )
    #(eg: table1.objects.filter(id = 11) & table2.objects.filter(roll_no = 10701) )


    print("SQL Query :", student_data.query) # This gives the SQL Query, which is running behind
    return render(request, 'Application1/home.html', {'students':student_data})