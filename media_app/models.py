from django.db import models

# Create your models here.
class Register(models.Model):
    name=models.CharField(max_length=30)
    phone=models.PositiveBigIntegerField()
    email=models.EmailField()
    sal=models.IntegerField()
    li=[['male','male'],['female','female']]
    gender=models.CharField(max_length=20,choices=li)
    date=models.DateField(auto_now=True)
    photo=models.ImageField(upload_to='img')
    resume=models.FileField(upload_to='resume')
