from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Comentarios(models.Model):
    
    mensaje=models.TextField()
    autor=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='miComentario'
        verbose_name_plural='misComentarios'
