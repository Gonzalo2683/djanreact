from django.contrib import admin
from .models import Post, Cometario, FraseCelebre, AutorCelebre

# Register your models here.
admin.site.register(Post)
admin.site.register(Cometario)
admin.site.register(AutorCelebre)
admin.site.register(FraseCelebre)