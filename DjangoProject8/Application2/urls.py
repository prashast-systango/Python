from django.urls import path
from . import views

urlpatterns = [
    path('func3/',views.func3),
    path('func4/',views.func4), 
]