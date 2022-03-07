from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class Softskill(models.Model):
    name = CharField(max_length= 30)
    description = CharField(max_length= 500)

    def create(json):
        try:
            print("Data",json)
            softskill = Softskill.objects.create(
                name = json['name'],
                description = json['description'],
            )
            print(softskill)
            softskill.save()
            print('softskill', softskill, softskill.name)
            return 200, 'Softskill registered'
        except Exception as e:
            return 400, str(e)


    def getjson(self):
        res = {
            'name' : self.name,
            'description' : self.description
        }
        return res


    def getSoftskill(param):
        response = Softskill.objects.filter(name = param)
        print(response)
        res =[]
        for i in response:
            res.append(i.getjson())
        print(res)
        return 200, res


    def getAllSoftskill():
        response = Softskill.objects.all()
        print(response)
        res =[]
        for i in response:
            res.append(i.getjson())
        print(res)
        return 200, res