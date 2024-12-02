from django.db import models

# Create your models here.
class Proyecto(models.Model):
    nombre = models.CharField(max_length=255, default=True)
    rut = models.CharField(max_length=255, default=True)  # Campo para los RUT
    integrantes = models.CharField(max_length=255, default=True)  # Campo para los nombres de los integrantes

    def __str__(self):
        return self.nombre