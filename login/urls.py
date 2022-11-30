from django.urls import path

from . import views
urlpatterns=[ 
    path('logreg/',views.registerview,name='logreg')
]