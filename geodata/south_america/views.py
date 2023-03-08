from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.




def index_america(resquest):
    return render(resquest, 'index_america.html')


def brazil(request):
    return render(request, 'brazil.html')


def argentina(request):
    return render(request, 'argentina.html')