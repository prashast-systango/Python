from django.urls import path
from . import views
urlpatterns = [
    path('yellow/', views.yellow),
    path('red/', views.red),
    path('blue/', views.blue),
    path('black/', views.black),
]
