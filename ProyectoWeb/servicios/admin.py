from django.contrib import admin
from .models import Servicio    #como estan al mismo nivel, pongo el .nombreArchivo

# Register your models here.

class ServicioAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(Servicio, ServicioAdmin)

