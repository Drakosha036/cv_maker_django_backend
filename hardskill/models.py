from django.db import models
from django.db.models.fields import CharField
from django.http import response

# Create your models here.

class Hardskill(models.Model):
    name = CharField(max_length= 30)
    description = CharField(max_length= 500)

    def create(json):
        try:
            hardskill = Hardskill.objects.create(
                name = json['name'],
                description = json['description'],
            )
            hardskill.save()
            print('hardskill', hardskill, hardskill.name)
            return 200, 'Hardskill registered'
        except Exception as e:
            return 400, str(e)


    def getjson(self):
        res = {
            'name' : self.name,
            'description' : self.description
        }
        return res


    def getHardskill(param):
        response = Hardskill.objects.filter(name = param)
        print(response)
        res =[]
        for i in response:
            res.append(i.getjson())
        print(res)
        return 200, res

    def getAllHardskill():
        response = Hardskill.objects.all()
        print(response)
        res =[]
        for i in response:
            res.append(i.getjson())
        print(res)
        return 200, res