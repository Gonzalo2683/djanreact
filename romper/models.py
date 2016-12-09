from django.db import models

# Create your models here.


class Prueba(models.Model):
    nombre = models.CharField(max_length=120)
    tipo = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nombre


class Atleta(models.Model):
    nombre = models.CharField(max_length=120)
    apellido = models.CharField(max_length=120)

    pruebas = models.ManyToManyField(Prueba)

    def __unicode__(self):
        return self.nombre