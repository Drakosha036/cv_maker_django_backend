from django.db import models
from django.db.models.fields import CharField

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
            return 200, 'Softskill registered'
        except Exception as e:
            return 400, str(e)


    def getjson(self):
        res = {
            'name' : self.name,
            'description' : self.description
        }
        return res


    def getHardskill(hardskill):
        response = Hardskill.objects.get(name = hardskill.name)
        print(response.getjson())
        return 200, response.getjson()