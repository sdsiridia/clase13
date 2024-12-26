'''modelo de un autor'''
from django.db import models


# Modelo para Autores
class Autor(models.Model):
    '''campos de un autor'''
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    f_nac = models.DateField()
    nacionalidad = models.CharField(max_length=100)
    biografia = models.TextField()
    email = models.EmailField()
    telefono = models.CharField(max_length=20, blank=True, null=True)
    sitio_web = models.URLField(blank=True, null=True)
    premios = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
