from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nombre=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)#para que la fecha se ponga automaticamente
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='categoria'  #nombre en modelo de BBDD, como el nombre que tengan los campos
        verbose_name_plural='categorias'

    def __str__(self):
        return self.nombre



class Post(models.Model):
    titulo=models.CharField(max_length=50)
    contenido=models.CharField(max_length=50)
    imagen=models.ImageField(upload_to='blog', null=True, blank=True)
    autor=models.ForeignKey(User, on_delete=models.CASCADE)#Relacion uno a varios. RELACIONA AL AUTOR CON SUS POST, SI SE ELIMINA A ESTE AUTOR, SE ELIMINAN TODOS SUS POSTS
    categorias=models.ManyToManyField(Categoria)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='post'  
        verbose_name_plural='posts'

    def __str__(self):
        return self.titulo