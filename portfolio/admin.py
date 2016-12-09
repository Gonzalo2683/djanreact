from django.contrib import admin
from .models import Categoria, Proyecto

# Register your models here.


class ProyectoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'categoria', 'fecha_realizacion', 'actualizado' , 'activo']


class CateAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'actualizado']


admin.site.register(Categoria, CateAdmin)
admin.site.register(Proyecto, ProyectoAdmin)
