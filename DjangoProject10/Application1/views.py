from django.shortcuts import render

# Create your views here.
def function1(request):
    return render(request, 'Application1/one.html')

def function2(request):
    return render(request, 'Application1/one.html')