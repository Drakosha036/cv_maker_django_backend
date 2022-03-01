from django.urls import path
from  . import views

urlpatterns = [
    path('register', views.register),
    path(r'getSoftskill', views.getSoftskill), #pourquoi r?
]