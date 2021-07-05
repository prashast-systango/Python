from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def first_function(request):
    return render(request ,'one.html')
