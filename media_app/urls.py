from django.urls import path
from . import views

app_name='media_app'

urlpatterns=[ 
    path('register/',views.Registerview,name='register'),
    path('read/',views.getview,name='read/'),
]