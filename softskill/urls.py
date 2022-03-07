from django.urls import path
from  . import views

urlpatterns = [
    path('register', views.register),
    path(r'getAllSoftskill', views.getAllSoftskill),
    path(r'getSoftskill', views.getSoftskill), #r = expression reguliere, facultative
]