from django.db import models

# Create your models here.
class moviemodel(models.Model):
    Mid=models.BigAutoField(primary_key=True)
    mname= models.CharField(max_length=50)
    mdesc= models.TextField()
    mdate=models.DateTimeField(auto_now=True)
    mpic=models.ImageField(upload_to='media/img/')

