from django.contrib import admin

from .models import Atleta, Prueba

# Register your models here.


class AtletaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido']


admin.site.register(Atleta, AtletaAdmin)
admin.site.register(Prueba)
