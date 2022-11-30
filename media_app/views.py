from django.shortcuts import render
from django.http import HttpResponse

from media_app.forms import Registerform
from media_app.models import Register
# Create your views here.

def Registerview(request):
    form=Registerform()
    if request.method =='POST' and request.FILES:
        form=Registerform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return  HttpResponse('data created')
    return render(request,'register.html',{'form':form})

def getview(request):
    data=Register.objects.all()
    return render(request,'read.html',{'data':data})