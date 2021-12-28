from django.urls import path

from . import views

app_name='misComentarios'

urlpatterns = [

    path('', views.comentarios, name="Coment"), 
    path('eliminar/<int:comentario_id>/', views.eliminar_comentario, name='eliminar'),
    
    

]