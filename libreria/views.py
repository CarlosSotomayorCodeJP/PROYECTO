from django.shortcuts import render
from django.http import HttpResponse
from .models import Libro
from .forms import Libroform

# Create your views here.
def inicio(request):
    #return HttpResponse('<h1>INICIO</h1>')
    return render(request, 'index.html')
def contacto(request):
    return render(request, 'contacto.html')
def acerca(request):
    return render(request, 'acerca.html')
def libros(request):
    libros = Libro.objects.all()
    
    return render(request, 'libros/index.html', {'libros': libros})

def crear(request):
    form= Libroform()
    return render(request, 'libros/crear.html', {'form': form} )
