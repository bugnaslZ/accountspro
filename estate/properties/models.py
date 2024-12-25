from django.db import models
from root.models import Agent
# Create your models here.
class Property_type(models.Model):
    type = models.CharField(max_length=220)

    def __str__(self):
        return self.type

class Status(models.Model):
    status = models.CharField(max_length=200)

    def __str__(self):
        return self.status

class Properties(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField()
    agent = models.ForeignKey(Agent,on_delete=models.CASCADE)
    property_id = models.CharField(max_length=5)
    type = models.ForeignKey(Property_type,on_delete=models.CASCADE)
    status = models.ForeignKey(Status,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Commentt(models.Model):
    name = models.CharField(max_length=200)
    comment = models.TextField()

    def __str__(self):
        return self.name