from django.utils import timezone

from django.db import models
from django.conf import settings

# Create your models here.


class Post(models.Model):
    STATUS_ENTRADA = (
        ('borrador', 'Borrador'),
        ('publicado', 'Publicado'),
    )
    autor = models.ForeignKey(settings.AUTH_USER_MODEL)
    titulo = models.CharField(max_length=145)
    contenido = models.TextField()
    creado = models.DateTimeField(default=timezone.now)
    publicado = models.DateTimeField(blank=True, null=True)

    status = models.CharField(max_length=10, choices=STATUS_ENTRADA, default='borrador')

    def __unicode__(self):
        return self.titulo


class Cometario(models.Model):
    post = models.ForeignKey(Post, related_name='comentarios')
    nombre = models.CharField(max_length=80)
    email = models.EmailField()
    mensaje = models.TextField()
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    activo = models.BooleanField(default=True)

    def __unicode__(self):
        return 'Comentario por {} en {}'.format(self.nombre, self.post)


class AutorCelebre(models.Model):
    nombre = models.CharField(max_length=60)
    nacimiento = models.DateTimeField()
    bio = models.TextField()

    def __unicode__(self):
        return self.nombre


class FraseCelebre(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL)
    autor_celebre = models.ForeignKey(AutorCelebre)
    frase = models.TextField()
    creado = models.DateField(auto_now_add=False, auto_now=False)
    activo = models.BooleanField(default=False)

    def __unicode__(self):
        return self.autor_celebre.nombre



