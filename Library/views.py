from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request, 'pages/index.html')

def we(request):
    return render(request, 'pages/we.html')

def libros(request):
    return render(request, 'libros/index.html')