from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(resquest):
    return render(resquest, 'index_europe.html')

def france(request):
    return render(request, 'france.html')

def spain(request):
    return render(request, 'spain.html')

def portugal(request):
    return render(request, 'portugal.html')

