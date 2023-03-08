from django.urls import path
from . import views


urlpatterns = [
    path('', views.index_america, name='index_america'),
    path('brazil', views.brazil, name='brazil'),
    path('argentina', views.argentina, name='argentina'),
   
]



