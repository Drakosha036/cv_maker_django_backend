from django.urls import path
from  . import views

urlpatterns = [
    path('login', views.login),
    path(r'helloworld', views.helloworld),
    path(r'getProfil', views.getProfil),
    path(r'register', views.register),
    
]