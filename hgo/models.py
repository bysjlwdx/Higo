from django.db import models

# Create your models here.
class  Stu(models.Model):
    name= models.CharField(max_length=50)
    gender= models.CharField(max_length=2)
    age= models.IntegerField()
    address= models.CharField(max_length=50)