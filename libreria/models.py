from django.db import models

# Create your models here.

class Editor(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=60)
    provincia= models.CharField(max_length=30)
    pais = models.CharField(max_length=50)
    website = models.URLField()

    def __unicode__(self):
        return self.nombre


class Autor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=40)
    email = models.EmailField(blank=True, verbose_name="e-mail")

    def __unicode__(self):
        return "{} {}".format(self.nombre, self.apellido)


class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autores = models.ManyToManyField(Autor)
    editor = models.ForeignKey(Editor)
    publicacion_fecha = models.DateField(blank=True, null=True)

    def __unicode__(self):
        return self.titulo






















