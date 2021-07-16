from django.shortcuts import render, HttpResponse
from Application1 import signals
# Create your views here.

def home(request):
    signals.notification.send(sender=None, request=request, user= ['Prashast', 'Sitlani'])
    return HttpResponse("This is homepage")