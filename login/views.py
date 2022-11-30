from django.shortcuts import render
from django.http import HttpResponse
from .models import Register
from .forms import registerform
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate
# Create your views here.

def registerview(request):
    form=registerform()
    if request.method == 'POST':
        form=registerform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('data has been stored')
    return render(request,'logregister.html',{'form':form})

def loginview(request):
    form=AuthenticationForm()
    if request.method == 'POST':
        form=AuthenticationForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(username,password)
            if user is not None:
                login(request,user)
            return HttpResponse('successfully login')
    return render(request,'login.html',{'form':form})

