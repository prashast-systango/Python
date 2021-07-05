from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def func1(request):
    username = {
        'name' : "Prashast",
        'age' : 22,
        }
    return render(request, 'Application1/func1.html', username)