from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def func1(request):
    message = {
        'msg1' : "Here's a red rose for you",
        'msg2' : "Here's a yellow rose for you"
        }
    return render(request, 'Application1/App1.1.html', message)

def func2(request):
    message = {
        'msg1' : "Here's a red rose for you",
        'msg2' : "Here's a yellow rose for you"
        }
    return render(request, 'Application1/App1.2.html', message)    