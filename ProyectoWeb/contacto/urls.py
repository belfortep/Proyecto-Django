from django.urls import path

from . import views



#enlazar urls del proyecto al de la aplicacion

urlpatterns = [

    path('', views.contacto, name="Contacto"),

]
