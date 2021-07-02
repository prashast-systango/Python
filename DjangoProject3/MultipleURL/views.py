from django.shortcuts import render
from django.http import HttpResponse, request
# Create your views here.

def function_With_Multiple_URLs(request):
    return HttpResponse('Hello this URL is also mine')