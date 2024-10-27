from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Libro
from .forms import CustomUserCreationForm, Libroform
from django.contrib import messages
from django.contrib.auth import authenticate, login

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
@login_required
def eliminar(request, id):
    libro = Libro.objects.get(id = id)
    libro.delete()
    messages.warning(request, 'Eliminado con exito')
    return redirect('libros.index')
def salir(request):
    logout(request)
    return redirect('inicio')
def registro(request):
    data = {'form': CustomUserCreationForm()}
    if request.method == 'POST':
        usuario_creation_form= CustomUserCreationForm(data=request.POST)
        if usuario_creation_form.is_valid() :
            usuario_creation_form.save()
            usuario = authenticate(username=usuario_creation_form.cleaned_data['username'] , password=usuario_creation_form.cleaned_data['password1'])
            login(request, usuario)
            messages.warning(request, 'Cuenta creada con exito!!!')
            return redirect('inicio')
        else:
            data['form'] = usuario_creation_form
    return render(request, 'registration/registro.html', data)


