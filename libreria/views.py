from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Libro
from .forms import Libroform
from django.contrib import messages
# Create your views here.

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
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

@login_required
def crear(request):
    form= Libroform(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        messages.info(request, 'Creado con exito!!!')
        return redirect('libros.index')
    return render(request, 'libros/crear.html', {'form': form} )
@login_required
def editar(request, id):
    libro=Libro.objects.get(id=id)
    form=Libroform(request.POST or None, request.FILES or None, instance=libro)
    if form.is_valid() and request.POST:
        form.save()
        messages.success(request, 'Modificado con exito!!!')
        return redirect('libros.index')
    return render(request, 'libros/editar.html', {'form': form} )
def salir(request):
    logout(request)
    return redirect('inicio')

