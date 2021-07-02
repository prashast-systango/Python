"""DjangoProject3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from MultipleURL import views

# # we can create multiple URLs for one function, by passing different routes for one function
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.function_With_Multiple_URLs), # URL 1
    path('url2/', views.function_With_Multiple_URLs), # URL 2
    path('url3/', views.function_With_Multiple_URLs), #URL 3
    path('url4/', views.function_With_Multiple_URLs), #URL 4
    path('url5/', views.function_With_Multiple_URLs), #URL 5
]
