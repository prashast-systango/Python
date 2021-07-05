from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def func3(request):
    message = {
        'msg3' : "Here's a blue rose for you",
        'msg4' : "Here's a black rose for you"
        }
    return render(request, 'Application2/App2.1.html', message)

def func4(request):
    message = {
        'msg3' : "Here's a blue rose for you",
        'msg4' : "Here's a black rose for you"
        }
    return render(request, 'Application2/App2.2.html', message)