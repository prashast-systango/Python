from django.urls import path
from . import views

urlpatterns = [
    path('app1.2',views.page2),
    path('app1.1',views.page1),
]
