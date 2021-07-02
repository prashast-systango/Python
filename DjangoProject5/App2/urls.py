from django.urls import path
from . import views

urlpatterns = [
    path('app2.2',views.page2),
    path('app2.1',views.page1),
]
