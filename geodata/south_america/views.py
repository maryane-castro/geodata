from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.




def index(resquest):
    return render(resquest, 'index_america.html')
