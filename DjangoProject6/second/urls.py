from django.urls import path
from . import views

urlpatterns = [
    path('second/',views.second_function),
]