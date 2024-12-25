from django.db import models
from root.models import Category
# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=220)
    desc = models.TextField()
    categorys = models.ManyToManyField(Category)

    def __str__(self) :
        return self.name

class Comment(models.Model):
    service = models.ForeignKey(Service,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    message = models.TextField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.service.name