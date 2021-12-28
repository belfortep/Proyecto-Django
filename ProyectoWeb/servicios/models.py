from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class Servicio(models.Model):
    
    titulo=models.CharField(max_length=50)
    contenido=models.CharField(max_length=50)
    imagen=models.ImageField(upload_to='servicios')#upload_to="nombre de una carpeta". Lleva las imagenes a guardarse en la carpeta que indique antes en el archivo settings.py, pero a una subcarpeta de esta con el nombre que le di aca.
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='servicio' 
        verbose_name_plural='servicios'

    def __str__(self):
        return self.titulo