from django.shortcuts import render
from django.views.decorators.cache import cache_page

# Create your views here.
# Cached view function
@cache_page(40)
def home(request):
    return render(request, 'Application1/course.html')

# URL cached view fuction
def contact(request):
    return render(request, 'Application1/contact.html')


