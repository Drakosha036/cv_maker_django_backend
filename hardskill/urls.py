from django.urls import path
from  . import views

urlpatterns = [
    path('register', views.register),
    path(r'getHardskill', views.getHardskill), #r = expression reguliere, facultative
    path(r'getAllHardskill', views.getAllHardskill),
]