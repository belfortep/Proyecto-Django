from django.contrib import admin
from .models import Comentarios

# Register your models here.

class ComentariosAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')


admin.site.register(Comentarios, ComentariosAdmin)
