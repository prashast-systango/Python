from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def second_function(request):
    return render(request ,'Second/two.html')