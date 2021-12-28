from django.shortcuts import render, redirect

from .models import Comentarios
from .forms import FormularioComentarios
from django.contrib.auth.models import User






def comentarios(request):
    comentarios=Comentarios.objects.all()
    
    if request.method=='POST':

        formulario_comentarios=FormularioComentarios(request.POST)

        if formulario_comentarios.is_valid():
            
            comentario= Comentarios()#el modelo

            comentario.mensaje=formulario_comentarios.cleaned_data['mensaje']
            comentario.autor=request.user.username
            comentario.save()
            
            
            
            return redirect('/comentarios')
            
        
    else:
        formulario_comentarios = FormularioComentarios()
        


    return render(request, 'comentarios/comentarios.html', {"comentarios" : comentarios, "form" : formulario_comentarios})

def eliminar_comentario(request, comentario_id):

    comentario=Comentarios.objects.get(id=comentario_id)

    comentario.delete()

    return redirect('/comentarios')
