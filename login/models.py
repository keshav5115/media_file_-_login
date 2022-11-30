from django.db import models

from django.contrib.auth.models import User


# Create your models here.

class Register(User):
    phone=models.PositiveBigIntegerField()
    list=[['male','male'],['female','female']]
    gender=models.CharField(max_length=20,choices=list)

