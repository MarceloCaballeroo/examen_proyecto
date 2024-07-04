from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Usuarios(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    password = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    comuna = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Region(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Comuna(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre