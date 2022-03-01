from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class Softskill(models.Model):
    name = CharField(max_length= 30)
    description = CharField(max_length= 500)

    def create(json):
        try:
            softskill = Softskill.objects.create(
                name = json['name'],
                description = json['description'],
            )
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


    def getSoftskill(softskill):
        response = Softskill.objects.get(name = softskill.name)
        print(response.getjson())
        return 200, response.getjson()