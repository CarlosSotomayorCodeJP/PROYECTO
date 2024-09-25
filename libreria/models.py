from django.db import models

# Create your models here.
class Libro(models.Model):
    id=models.AutoField(primary_key=True)
    titulo=models.CharField(max_length=255, verbose_name='Título')
    imagen=models.ImageField(upload_to='imagenes/', verbose_name='Imagen', null=True)
    descrip=models.TextField(null=True, verbose_name='Descripción')

