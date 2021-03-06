
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.db.models.fields import BooleanField, CharField
from rest_framework.permissions import IsAdminUser
# Create your models here.



class Users(User):
    birthdate = CharField(max_length= 30)
    IsAdminUser = BooleanField(default= False)
    photo = CharField(max_length= 30)
    address = CharField(max_length= 30)

    def create(json):
        print(json['email'])
        try:
            user = Users.objects.create_user(username = json['email'] ,
                        first_name = json['first_name'], 
                        last_name = json['last_name'] ,
                        email = json['email'] ,
                        password = json['password'] ,
                        IsAdminUser = True,
                        )
            user.save()
            print('user', user, user.password)
            return 200,'User registered'
        except Exception as e:
            return 400,str(e)

    def login(username, password):
        print(username," ",password)
        u = authenticate(username=username, password=password)
        print(u)
        return u

    def getProfil(user):
        response = Users.objects.get(username = user.username)
        print(response.getjson())
        return 200, response.getjson()

    def getjson(self):
        res = {
            'username' : self.username,
            'firstname' : self.first_name,
            'lastname': self.last_name,
            'isAdmin' : self.IsAdminUser
        }
        return res