from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inicio(request):
    #return HttpResponse('<h1>INICIO</h1>')
    return render(request, 'index.html')
def nosotros(request):
    return render(request, 'nosotros.html')
def acerca(request):
    return render(request, 'acerca.html')