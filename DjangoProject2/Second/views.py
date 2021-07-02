from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Home-Page</h1>")

def learnDjango(request):
    return HttpResponse("Hello")

def math(request):
    return HttpResponse(5+5)

def math1(request):
    a = 10+10
    return HttpResponse(a)

def var(request):
    a ='<h1>Prashast</h1>'
    return HttpResponse(f'Hello I am {a}')

