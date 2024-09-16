from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Libro
from .forms import libroForm
# Create your views here.


def index(request):
    return render(request, 'pages/inicio.html')

def we(request):
    return render(request, 'pages/we.html')

def libros(request):
    libros = Libro.objects.all()
    return render(request, 'libros/index.html', {'libros':libros})

def crear(request):
    formulario = libroForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('libros/')
    return render(request, 'libros/crear.html', {'formulario': formulario})

def editar(request, id):
    libro_ed = Libro.objects.get(id=id)
    formulario = libroForm(request.POST or None, request.FILES or None, instance=libro_ed)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('libros/')
    return render(request, 'libros/editar.html', {'formulario': formulario})


def eliminar(request, id):
    libroe = libros.objects.get(id=id)
    libroe.delete()
    return redirect('libros')
