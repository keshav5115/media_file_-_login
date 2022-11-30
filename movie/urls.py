from django.urls import path
from movie import views
urlpatterns=[
    path('create/',views.createmovie.as_view(),name='create'),
    path('update/<pk>/',views.updatemovie.as_view(),name='update'),
    path('delete/<pk>/',views.deletemovie.as_view(),name='delete'),
    path('list/',views.listmovie.as_view(),name='list'),
    path('success/',views.success_view,name='success'),
]