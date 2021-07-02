from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def page1(request):
    return HttpResponse('''<h1>Application 2</h1>
    <h2>page1</h2>''')

def page2(request):
    return HttpResponse('''<h1>Application 2</h1>
    <h2>page2</h2>''')