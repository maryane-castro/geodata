from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('brazil', views.brazil, name='brazil'),
    path('argentina', views.argentina, name='argentina'),
   
]



