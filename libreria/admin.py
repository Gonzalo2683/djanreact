from django.contrib import admin
from .models import Editor, Libro, Autor
# Register your models here.

class AutorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'email')
    search_fields = ('nombre', 'apellido')

class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'editor', 'publicacion_fecha')
    list_filter = ('publicacion_fecha',)
    date_hierarchy = 'publicacion_fecha'

    fields = ('titulo', 'publicacion_fecha', 'editor', 'autores',)
    filter_horizontal = ('autores',)
    raw_id_fields = ('editor',)


admin.site.register(Editor)
admin.site.register(Autor, AutorAdmin)
admin.site.register(Libro, LibroAdmin)

















