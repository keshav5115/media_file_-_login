from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView,UpdateView,ListView,DeleteView,DetailView
# Create your views here.
from movie.models import moviemodel
from movie.forms import movieform
class createmovie(CreateView):
    model=moviemodel
    fields='__all__'
    template_name='cmovie.html'
    success_url='/movie/success'

class updatemovie(UpdateView):
    model=moviemodel
    fields='__all__'
    template_name='cmovie.html'
    success_url='/movie/success'

class deletemovie(DeleteView):
    model=moviemodel
    fields='__all__'
    template_name='cmovie.html'
    success_url='/movie/success'

class listmovie(ListView):
    model=moviemodel
    fields='__all__'
    template_name='cmovie.html'
    context_object_name='form'
    success_url='/movie/success'

def success_view(request):
    return HttpResponse("success")