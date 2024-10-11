from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name=('inicio') ),
    path('contacto', views.contacto, name='contacto'),
    path('acerca', views.acerca, name='acerca'),
    path("libros", views.libros, name="libros.index"),
    path("libros/crear", views.crear, name="libros.crear"),
    path("libros/editar/<int:id>", views.editar, name="libros.editar"),
    path('salir',views.salir, name='exit'),
    path('regsitro', views.regsitro, name='regsitro'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)