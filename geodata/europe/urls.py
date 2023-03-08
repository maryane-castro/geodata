from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('france', views.france, name='france'),
    path('spain', views.spain, name='spain'),
    path('portugal', views.portugal, name='portugal'),
   
]