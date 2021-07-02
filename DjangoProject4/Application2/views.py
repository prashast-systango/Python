from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def function2(request):
    return HttpResponse('<h1>Application 2 here</h1>')