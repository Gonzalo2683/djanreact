from django.db import models

# Create your models here.


class ActiveProyectoManager(models.Manager):
    def get_queryset(self):
        return super(ActiveProyectoManager, self).get_queryset().filter(activo=True)


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    actualizado = models.DateField(auto_now=True)

    def __unicode__(self):
        return self.nombre


class Proyecto(models.Model):
    titulo = models.CharField(max_length=140)
    categoria = models.ForeignKey(Categoria)
    fecha_realizacion = models.DateField()
    actualizado = models.DateTimeField(auto_now=True)
    activo = models.BooleanField(default=False)

    objects = models.Manager()
    publicados = ActiveProyectoManager()

    def __unicode__(self):
        return self.titulo

